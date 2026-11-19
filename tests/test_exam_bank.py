from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "exam_bank.py"
SPEC = importlib.util.spec_from_file_location("exam_bank", MODULE_PATH)
assert SPEC and SPEC.loader
exam_bank = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(exam_bank)


def valid_record() -> dict:
    return {
        "_line": 1,
        "id": "2024-calc-01",
        "year": 2024,
        "section": "计算题",
        "number": "1",
        "topic": ["简单回归"],
        "question": "检验斜率是否显著。",
        "source": "paper p.1 Q1",
        "status": "solved",
        "answer": "t=4，拒绝原假设。",
        "confidence": "high",
    }


class ValidationTests(unittest.TestCase):
    def test_valid_record_passes(self) -> None:
        errors, warnings = exam_bank.validate_records([valid_record()])
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_duplicate_id_fails(self) -> None:
        first = valid_record()
        second = valid_record()
        second["_line"] = 2
        errors, _ = exam_bank.validate_records([first, second])
        self.assertTrue(any("duplicate id" in error for error in errors))

    def test_solved_requires_answer(self) -> None:
        record = valid_record()
        record.pop("answer")
        errors, _ = exam_bank.validate_records([record])
        self.assertTrue(any("require a non-empty answer" in error for error in errors))

    def test_report_counts_topics(self) -> None:
        records = [valid_record()]
        report = exam_bank.build_report(records, "sample.jsonl")
        self.assertIn("Questions: 1", report)
        self.assertIn("简单回归", report)


if __name__ == "__main__":
    unittest.main()