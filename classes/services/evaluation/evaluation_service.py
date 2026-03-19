import re
from typing import Dict, List

from models.evaluation.code_file_submission import CodeFileSubmission
from models.evaluation.evaluation_report import (
    EvaluationReport,
    QuestionEvaluation,
    RubricItemEvaluation,
)
from models.evaluation.rubric_models import RubricDefinition, RubricItem


class EvaluationService:
    """Evaluates submissions using rubric definitions and question titles."""

    def evaluate_submissions(
        self,
        submissions: List[CodeFileSubmission],
        question_titles_by_test: Dict[str, List[str]],
        rubric_definitions_by_test: Dict[str, RubricDefinition],
    ) -> List[EvaluationReport]:
        """Evaluate all submissions and return reports."""
        reports: List[EvaluationReport] = []
        for submission in submissions:
            reports.append(
                self._evaluate_submission(
                    submission,
                    question_titles_by_test,
                    rubric_definitions_by_test,
                )
            )
        return reports

    def _evaluate_submission(
        self,
        submission: CodeFileSubmission,
        question_titles_by_test: Dict[str, List[str]],
        rubric_definitions_by_test: Dict[str, RubricDefinition],
    ) -> EvaluationReport:
        """Evaluate one submission and return a report."""
        question_titles = question_titles_by_test.get(submission.test_name, [])
        rubric_definition = rubric_definitions_by_test.get(submission.test_name)
        if rubric_definition is None:
            return EvaluationReport(
                student_identifier=submission.student_identifier,
                test_name=submission.test_name,
                total_score=0.0,
                max_score=0.0,
                questions=[],
                notes="Missing rubric definition for this test.",
            )
        questions = self._evaluate_questions(
            submission,
            question_titles,
            rubric_definition,
        )
        total_score = sum(question.score for question in questions)
        max_score = sum(question.max_score for question in questions)
        notes = "Auto-scored based on code presence for rubric items."
        return EvaluationReport(
            student_identifier=submission.student_identifier,
            test_name=submission.test_name,
            total_score=total_score,
            max_score=max_score,
            questions=questions,
            notes=notes,
        )

    def _evaluate_questions(
        self,
        submission: CodeFileSubmission,
        question_titles: List[str],
        rubric_definition: RubricDefinition,
    ) -> List[QuestionEvaluation]:
        """Evaluate each question in a submission."""
        evaluations: List[QuestionEvaluation] = []
        for index, question in enumerate(submission.questions):
            title = question_titles[index] if index < len(question_titles) else question.question_title
            rubric_items = self._select_rubric_items(rubric_definition.items, title)
            evaluations.append(
                self._evaluate_question(title, question.code_lines, rubric_items)
            )
        return evaluations

    def _evaluate_question(
        self,
        question_title: str,
        code_lines: List[str],
        rubric_items: List[RubricItem],
    ) -> QuestionEvaluation:
        """Score a single question using the rubric items."""
        code_present = bool(code_lines)
        item_evaluations: List[RubricItemEvaluation] = []
        for item in rubric_items:
            score = item.score if code_present else 0.0
            notes = "Auto-scored: code present." if code_present else "No code provided."
            item_evaluations.append(
                RubricItemEvaluation(
                    description=item.description,
                    score=score,
                    max_score=item.score,
                    notes=notes,
                )
            )
        question_score = sum(item.score for item in item_evaluations)
        max_score = sum(item.max_score for item in item_evaluations)
        feedback = "Auto-scored from code presence." if code_present else "No code provided."
        return QuestionEvaluation(
            question_title=question_title,
            score=question_score,
            max_score=max_score,
            rubric_items=item_evaluations,
            feedback=feedback,
        )

    def _select_rubric_items(
        self,
        rubric_items: List[RubricItem],
        question_title: str,
    ) -> List[RubricItem]:
        """Select rubric items that match a question title prefix."""
        prefix = self._extract_question_prefix(question_title)
        if not prefix:
            return list(rubric_items)
        matched_items = [
            item for item in rubric_items if item.identifier.upper().startswith(prefix)
        ]
        return matched_items if matched_items else list(rubric_items)

    def _extract_question_prefix(self, question_title: str) -> str:
        """Extract a leading prefix like A or 1 from the question title."""
        match = re.match(r"^([A-Za-z0-9]+)\.", question_title.strip())
        if match:
            return match.group(1).upper()
        return ""
