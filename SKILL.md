---
name: exam-review
description: Build evidence-grounded exam review packs from past papers, lecture notes, and rubrics, including topic-frequency maps, model answers, weak-point diagnosis, and prioritized study plans. Use when course-exam preparation requires analysis of supplied source material; do not use to fabricate answers for unseen exams or to assist with cheating.
metadata:
  short-description: Turn exam sources into a prioritized review pack
---

# Exam Review

## Outcome

Turn supplied exam material into a review pack that helps the learner decide what to study, understand why an answer earns marks, and practise under realistic constraints. Preserve the relationship between every claim, the source that supports it, and the reasoning that connects them.

## Non-negotiables

- **Stay source-grounded.** Distinguish what appears in the supplied papers or notes from your own derivation, convention, or inference. If the source is incomplete or illegible, say so instead of silently filling the gap.
- **Do not invent exam content.** Never present a reconstructed, remembered, or synthetic question as an authentic past-paper question. Label paraphrases and practice questions clearly.
- **Verify before polishing.** Recompute numerical answers, check units and signs, and confirm that notation is used consistently. A clean layout is not a substitute for a correct derivation.
- **Optimize for marks, not volume.** Put the scoring point, required condition, and common trap next to each answer. Omit background that would not earn credit.
- **Protect private and copyrighted material.** Remove names, student IDs, signatures, and private annotations. Do not publish past papers, scans, or lecture slides unless the user confirms the right to redistribute them.
- **Make uncertainty actionable.** Use `high`, `medium`, or `low` confidence and state what would resolve a low-confidence item.

Write the final response in the user's language unless they request otherwise.

## Workflow

### 1. Inventory the sources

Identify the exam board or course, years, paper sections, answer keys, syllabus, lecture notes, and the learner's deadline. Build a source ledger with one row per artifact: filename, year, page count, quality, and what it can support.

If no source is provided, ask for the minimum needed: one paper or syllabus plus the target date. If the request is only for a study plan, a syllabus or topic list is sufficient.

### 2. Extract and normalize questions

Record each question with a stable ID, year, section, number, topic, source locator, question text, marks, answer status, and confidence. Use the schema in `references/question-schema.md` and validate a machine-readable bank with `scripts/exam_bank.py`.

Rules for extraction:

- Preserve formulas, subscripts, conditions, and wording that changes the task. Paraphrase only when necessary and mark it as a paraphrase.
- Keep the original section and question number so the learner can cross-check the paper.
- Split compound questions only when subparts are assessed separately.
- Do not merge questions merely because they share a topic.
- Mark an item `unresolved` when the source is unclear, the answer key is missing, or a derivation cannot be completed.

### 3. Diagnose the exam

Produce an exam map rather than a raw list:

- question types and mark allocation;
- topic and subtopic frequency across years;
- recurrent wording, assumptions, and calculation templates;
- topics that appear together;
- recent changes in emphasis;
- high-frequency topics that the learner has not mastered.

Do not rank topics by frequency alone. Combine exam evidence, the learner's stated weak areas, prerequisite dependencies, and the cost of learning the topic.

### 4. Build the review pack

Use the smallest deliverable that answers the request. Typical modes are:

- **Rapid cram:** one-page exam map, top 8-12 answer templates, and a timed drill list.
- **Full review:** topic map, worked answers, common errors, and a day-by-day plan.
- **Answer drafting:** question-by-question answer cards with scoring points and source evidence.
- **Mock exam:** a clearly labeled synthetic paper built only from the syllabus and the learner's authorized materials, followed by a rubric.

For answer cards, use:

```text
Question:
Source:
Topic / marks:
Short answer:
Derivation or key steps:
Scoring points:
Common error:
Confidence:
```

For a study plan, state the learner's available hours, the sequence, the output for each session, and the review checkpoint. Do not create an unrealistically dense plan.

### 5. Run the quality gate

Before delivery, check:

- Every authentic question has a source locator.
- Every numerical result has been recomputed.
- Every formula has defined symbols and assumptions.
- Every answer distinguishes definition, mechanism, consequence, test, and remedy when those are relevant.
- Every low-confidence item is visibly labeled.
- Every synthetic question is labeled synthetic.
- The plan fits the stated time and names a measurable output for each block.

## Supporting Resources

- Read `references/review-playbook.md` for answer structures, cramming modes, and common scoring patterns.
- Read `references/question-schema.md` before creating a JSONL question bank.
- Read `references/hust-853-econometrics.md` when the course is HUST 853 Econometrics or a closely equivalent econometrics exam.
- Run `python scripts/exam_bank.py validate <bank.jsonl>` to check a bank.
- Run `python scripts/exam_bank.py report <bank.jsonl>` to generate topic and coverage statistics.
- Use `examples/econometrics-bank.jsonl` as a schema example, not as evidence about any real exam.