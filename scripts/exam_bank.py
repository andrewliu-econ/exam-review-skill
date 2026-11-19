#!/usr/bin/env python3
"""Validate and summarize an exam-question JSONL bank."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


REQUIRED_FIELDS = {
    "id": str,
    "year": int,
    "section": str,
    "number": (str, int),
    "topic": list,
    "question": str,
    "source": str,
    "status": str,
}
VALID_STATUS = {"solved", "draft", "unresolved"}
VALID_CONFIDENCE = {"high", "medium", "low"}


def load_bank(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"line {line_number}: invalid JSON: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"line {line_number}: each line must contain a JSON object")
            value["_line"] = line_number
            records.append(value)
    if not records:
        raise ValueError("the bank contains no question records")
    return records


def validate_records(records: Iterable[dict[str, Any]]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    ids: set[str] = set()

    for record in records:
        label = f"line {record.get('_line', '?')}"
        for field, expected_type in REQUIRED_FIELDS.items():
            if field not in record:
                errors.append(f"{label}: missing required field '{field}'")
                continue
            if not isinstance(record[field], expected_type):
                errors.append(
                    f"{label}: field '{field}' has type {type(record[field]).__name__}, "
                    f"expected {getattr(expected_type, '__name__', expected_type)}"
                )

        record_id = record.get("id")
        if isinstance(record_id, str) and record_id.strip():
            if record_id in ids:
                errors.append(f"{label}: duplicate id '{record_id}'")
            ids.add(record_id)

        topics = record.get("topic")
        if isinstance(topics, list):
            if not topics:
                errors.append(f"{label}: 'topic' must not be empty")
            if any(not isinstance(topic, str) or not topic.strip() for topic in topics):
                errors.append(f"{label}: every topic must be a non-empty string")

        status = record.get("status")
        if isinstance(status, str) and status not in VALID_STATUS:
            errors.append(f"{label}: invalid status '{status}'")

        confidence = record.get("confidence")
        if confidence is not None and confidence not in VALID_CONFIDENCE:
            errors.append(f"{label}: invalid confidence '{confidence}'")

        if status == "solved":
            answer = record.get("answer")
            if not isinstance(answer, str) or not answer.strip():
                errors.append(f"{label}: solved questions require a non-empty answer")
        if status == "unresolved" and not record.get("notes"):
            warnings.append(f"{label}: unresolved item should explain the blocker in 'notes'")
        if record.get("synthetic") is True and status == "solved":
            if not isinstance(record.get("answer"), str) or not record["answer"].strip():
                warnings.append(f"{label}: synthetic solved item has no answer")

    return errors, warnings


def _topic_years(records: list[dict[str, Any]]) -> dict[str, set[int]]:
    result: dict[str, set[int]] = defaultdict(set)
    for record in records:
        year = record.get("year")
        if not isinstance(year, int):
            continue
        for topic in record.get("topic", []):
            if isinstance(topic, str) and topic.strip():
                result[topic].add(year)
    return result


def build_report(records: list[dict[str, Any]], source_name: str) -> str:
    years = sorted({record["year"] for record in records if isinstance(record.get("year"), int)})
    statuses = Counter(record.get("status", "unknown") for record in records)
    sections = Counter(record.get("section", "unknown") for record in records)
    topic_counts = Counter(
        topic
        for record in records
        for topic in record.get("topic", [])
        if isinstance(topic, str) and topic.strip()
    )
    topic_years = _topic_years(records)

    lines = [
        "# Exam Bank Report",
        "",
        f"Source: `{source_name}`",
        f"Questions: {len(records)}",
        f"Years: {', '.join(map(str, years)) if years else 'unknown'}",
        "",
        "## Status",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    for status in ("solved", "draft", "unresolved", "unknown"):
        if statuses[status]:
            lines.append(f"| {status} | {statuses[status]} |")

    lines.extend(["", "## Question sections", "", "| Section | Count |", "|---|---:|"])
    for section, count in sections.most_common():
        lines.append(f"| {section} | {count} |")

    lines.extend(["", "## Topic frequency", "", "| Topic | Questions | Years |", "|---|---:|---|"])
    for topic, count in topic_counts.most_common():
        year_text = ", ".join(str(year) for year in sorted(topic_years.get(topic, set())))
        lines.append(f"| {topic} | {count} | {year_text or '-'} |")

    return "\n".join(lines) + "\n"


def command_validate(path: Path) -> int:
    records = load_bank(path)
    errors, warnings = validate_records(records)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Validation failed: {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"Validation passed: {len(records)} question(s), {len(warnings)} warning(s)")
    return 0


def command_report(path: Path, output: Path | None) -> int:
    records = load_bank(path)
    report = build_report(records, path.name)
    if output:
        output.write_text(report, encoding="utf-8")
        print(f"Wrote {output}")
    else:
        print(report, end="")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="validate required fields and values")
    validate_parser.add_argument("bank", type=Path)

    report_parser = subparsers.add_parser("report", help="summarize coverage and topic frequency")
    report_parser.add_argument("bank", type=Path)
    report_parser.add_argument("-o", "--output", type=Path)

    args = parser.parse_args()
    try:
        if args.command == "validate":
            return command_validate(args.bank)
        return command_report(args.bank, args.output)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())