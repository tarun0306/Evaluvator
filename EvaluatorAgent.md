# EvaluatorAgent

## Purpose
Evaluate student code in `_code_json` against the official questions in `Test_Questions` and the rubric JSON files for each test. Produce a structured evaluation with per-question scoring and feedback.

## Scope
- Tests: Test_1, Test_2, Test_3, Test_2_makeup
- Code source: `*/_code_json/*.json`
- Question source: `Test_Questions/*.docx`
- Rubric source:
  - Test_1: `Test_1/_rubric.json`
  - Test_2: `Test_2/rubric_Test_2.json`
  - Test_3: `Test_3/rubric_Test_3.json`
  - Test_2_makeup: `Test_2_makeup/rubric_Test_2_makeup.json`

## Inputs
- Code JSON: array of objects with keys `question_1`, `question_2`, ... and `code` (array of code lines). Example:
  - `{ "question_1": "A. Selection Statement", "code": ["namespace ...", "{"] }`
- Question document: the official prompt text per test (DOCX).
- Rubric JSON: rows containing question identifiers, score, and descriptions.

## Required Behavior
- Map each code JSON entry to the matching question section in the corresponding DOCX.
- Use the rubric descriptions as grading criteria. Apply only the rubric items that match the question title or identifier.
- Ignore handwritten text or artifacts in the PDFs; treat the code JSON as the canonical source of code.
- When code is missing or empty, score as zero with explicit feedback.
- Provide concise feedback tied to rubric items.

## Matching Strategy
1. Identify the test by folder name.
2. Load the test DOCX and extract question titles in order.
3. Match each `question_n` entry to the extracted question title in the same order.
4. Map rubric rows by question title, or by the leading identifier (A/B/C, 1/2/3) if present.

## Output Format
Produce one JSON report per student code file:
```
{
  "student_id": "bhagams4063",
  "test": "Test_1",
  "total_score": 85,
  "max_score": 100,
  "questions": [
    {
      "question_title": "A. Selection Statement",
      "score": 30,
      "max_score": 40,
      "rubric_items": [
        {"description": "Without using a loop, input three integers.", "score": 10, "max_score": 10, "notes": "OK"}
      ],
      "feedback": "Missing average output formatting."
    }
  ],
  "notes": "Any overall notes here."
}
```

## Evaluation Rules
- Score each rubric item independently; sum to question score.
- Total score is sum of question scores.
- If question matching is ambiguous, include a warning in `notes` and grade in order of appearance.

## Non-Goals
- Do not modify source code or rubrics.
- Do not infer missing rubric items.
