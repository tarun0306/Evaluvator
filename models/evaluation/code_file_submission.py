import json
from dataclasses import dataclass
from typing import Any, Dict, List

from models.evaluation.code_question_entry import CodeQuestionEntry


@dataclass(frozen=True)
class CodeFileSubmission:
    """Represents a single student's submission for a test."""

    student_identifier: str
    test_name: str
    questions: List[CodeQuestionEntry]

    @staticmethod
    def from_serialized_entries(
        student_identifier: str,
        test_name: str,
        serialized_entries: List[Dict[str, Any]],
    ) -> "CodeFileSubmission":
        """Create a CodeFileSubmission from serialized JSON entries."""
        questions = [
            CodeQuestionEntry.from_serialized_entry(entry)
            for entry in serialized_entries
        ]
        return CodeFileSubmission(
            student_identifier=student_identifier,
            test_name=test_name,
            questions=questions,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON-serializable representation of the submission."""
        return {
            "student_identifier": self.student_identifier,
            "test_name": self.test_name,
            "questions": [question.to_dict() for question in self.questions],
        }

    def __str__(self) -> str:
        """Return a JSON string representation of the submission."""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=True)
