from classes.services.evaluation.evaluation_service import EvaluationService
from models.evaluation.code_file_submission import CodeFileSubmission
from models.evaluation.code_question_entry import CodeQuestionEntry
from models.evaluation.rubric_models import RubricDefinition, RubricItem
from tests.base_timeout_test_case import BaseTimeoutTestCase


class EvaluationServiceTests(BaseTimeoutTestCase):
    """Tests for EvaluationService scoring behavior."""

    def test_scores_full_credit_when_code_present(self) -> None:
        """Assign full credit when code lines are present."""
        submission = CodeFileSubmission(
            student_identifier="student",
            test_name="Test_1",
            questions=[
                CodeQuestionEntry(
                    question_key="question_1",
                    question_title="A. Selection Statement",
                    code_lines=["Console.WriteLine(\"Hello\");"],
                )
            ],
        )
        rubric_definition = RubricDefinition(
            test_name="Test_1",
            items=[
                RubricItem(identifier="A1", score=10.0, description="Step A1"),
                RubricItem(identifier="A2", score=5.0, description="Step A2"),
            ],
        )
        service = EvaluationService()
        reports = service.evaluate_submissions(
            submissions=[submission],
            question_titles_by_test={"Test_1": ["A. Selection Statement"]},
            rubric_definitions_by_test={"Test_1": rubric_definition},
        )
        report = reports[0]
        self.assertEqual(report.total_score, 15.0)
        self.assertEqual(report.max_score, 15.0)

    def test_scores_zero_when_code_missing(self) -> None:
        """Assign zero credit when no code lines exist."""
        submission = CodeFileSubmission(
            student_identifier="student",
            test_name="Test_1",
            questions=[
                CodeQuestionEntry(
                    question_key="question_1",
                    question_title="A. Selection Statement",
                    code_lines=[],
                )
            ],
        )
        rubric_definition = RubricDefinition(
            test_name="Test_1",
            items=[
                RubricItem(identifier="A1", score=10.0, description="Step A1"),
            ],
        )
        service = EvaluationService()
        reports = service.evaluate_submissions(
            submissions=[submission],
            question_titles_by_test={"Test_1": ["A. Selection Statement"]},
            rubric_definitions_by_test={"Test_1": rubric_definition},
        )
        report = reports[0]
        self.assertEqual(report.total_score, 0.0)
        self.assertEqual(report.max_score, 10.0)
