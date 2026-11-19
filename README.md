# Exam Review Skill

一个用于期末/考研复习的 Codex Skill：把历年真题、课堂笔记和评分要求整理成**有来源依据**的考点地图、答案卡、错题诊断和复习计划。

> 这个仓库只发布 Skill、模板和原创示例，不包含历年真题扫描件或课程讲义。

## 它能做什么

- 按年份、题型、考点整理题库；
- 统计考点频率与题型分布；
- 为每道题生成“答案 + 推导 + 得分点 + 常见错误”；
- 把高频考点、先修关系和你的薄弱项合成为优先级；
- 生成冲刺计划、模拟卷和评分标准；
- 对来源不清、扫描模糊或尚未解决的问题明确标注 `unresolved`。

## 安装

推荐使用 Codex Skills 目录：

```bash
git clone https://github.com/andrewliu-econ/exam-review-skill.git
mkdir -p ~/.codex/skills
cp -R exam-review-skill ~/.codex/skills/exam-review
```

Windows PowerShell：

```powershell
git clone https://github.com/andrewliu-econ/exam-review-skill.git
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\exam-review-skill" "$HOME\.codex\skills\exam-review"
```

重新打开 Codex 后，可以这样调用：

```text
Use $exam-review to analyze these past papers and build a 7-day review plan.
```

或中文：

```text
用 $exam-review 分析这些真题和笔记，整理高频考点、答案模板和 7 天复习计划。
```

## 快速开始

```bash
python scripts/exam_bank.py validate examples/econometrics-bank.jsonl
python scripts/exam_bank.py report examples/econometrics-bank.jsonl
```

输出一份 Markdown 报告：

```bash
python scripts/exam_bank.py report my-bank.jsonl -o report.md
```

## 题库格式

题库使用 JSONL，一行一道题。完整字段见 [`references/question-schema.md`](references/question-schema.md)。

最小示例：

```json
{"id":"2024-calc-03","year":2024,"section":"计算题","number":"3","topic":["简单回归","假设检验"],"question":"给定回归结果，检验斜率是否显著。","source":"2024年真题.pdf p.2 Q3","status":"solved","answer":"t=...，在5%水平拒绝原假设。","confidence":"high"}
```

## 设计原则

- **来源可追踪**：每道真题都有文件、页码和题号。
- **答案可复核**：数值、单位、符号和假设都要检查。
- **不会编题**：合成练习题必须标记 `synthetic: true`。
- **不泄露隐私**：公开前移除姓名、学号、签名和私人批注。
- **不替代考试诚信**：用于复习、练习和答案理解，不用于现场作弊。

## 适用场景

- 大学课程期末复习；
- 考研专业课真题整理；
- 需要按考点频率安排复习顺序；
- 需要把笔记转成答案模板和自测题；
- 需要为学习小组制作公开、合规的复习资料。

华中科技大学 853 计量经济学的复习轮廓见 [`references/hust-853-econometrics.md`](references/hust-853-econometrics.md)。该文件只提供考点清单，不声称任何具体题目出现于真实试卷。

## 测试

```bash
python -m unittest discover -s tests -v
python scripts/exam_bank.py validate examples/econometrics-bank.jsonl
```

## License

MIT