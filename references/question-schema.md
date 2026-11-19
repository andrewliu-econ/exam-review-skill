# Question Bank Schema

Use JSON Lines (`.jsonl`): one UTF-8 JSON object per line. The bank is an index and evidence layer, not a replacement for the original paper.

## Required fields

| Field | Type | Meaning |
|---|---|---|
| `id` | string | Stable unique ID, for example `2024-calc-03`. |
| `year` | integer | Exam year. Use the academic year in which the exam was held. |
| `section` | string | Paper section such as `名词解释`, `计算题`, or `论述题`. |
| `number` | string or integer | Original question number. |
| `topic` | non-empty array of strings | Canonical topics; reuse spellings across the bank. |
| `question` | string | Verbatim question when possible, otherwise a clearly marked paraphrase. |
| `source` | string | File, page, and question locator. |
| `status` | string | `solved`, `draft`, or `unresolved`. |

## Recommended fields

| Field | Type | Meaning |
|---|---|---|
| `subtopic` | array of strings | Narrower concepts within the main topics. |
| `marks` | number | Mark allocation when known. |
| `answer` | string | Final answer and key steps. Required when status is `solved`. |
| `scoring_points` | array of strings | What earns marks. |
| `common_errors` | array of strings | Frequent mistakes or traps. |
| `confidence` | string | `high`, `medium`, or `low`. |
| `question_type` | string | `definition`, `calculation`, `proof`, `short_answer`, `essay`, or `unknown`. |
| `synthetic` | boolean | `true` only for generated practice questions. |
| `notes` | string | Extraction issues, ambiguities, or follow-up work. |

## Minimal example

```json
{"id":"2024-calc-03","year":2024,"section":"计算题","number":"3","topic":["简单回归","假设检验"],"question":"给定回归结果，检验斜率是否显著。","source":"2024年真题.pdf p.2 Q3","status":"solved","answer":"t=...，在5%水平拒绝原假设。","confidence":"high"}
```

## Evidence discipline

- A source locator must be specific enough for another person to find the original item.
- If the original wording is unavailable, write `paraphrase:` at the start of `question` and explain why in `notes`.
- If a source combines multiple independently scored subparts, create one record per subpart and preserve the original numbering in `number`.
- Never use `synthetic: true` to disguise an uncertain recollection of a real question. Use `unresolved` instead.
- Keep copyrighted scans outside the public repository. Store only permitted metadata and original analysis.