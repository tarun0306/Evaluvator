import json
from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class RubricItemEvaluation:
    """Captures a score and feedback for a rubric item."""

    description: str
    score: float
    max_score: float
    notes: str

    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON-serializable representation of the evaluation."""
        return {
            "description": self.description,
            "score": self.score,
            "max_score": self.max_score,
            "notes": self.notes,
        }

    def __str__(self) -> str:
        """Return a JSON string representation of the evaluation."""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=True)


@dataclass(frozen=True)
class QuestionEvaluation:
    """Captures scoring details for a single question."""

    question_title: str
    score: float
    max_score: float
    rubric_items: List[RubricItemEvaluation]
    feedback: str

    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON-serializable representation of the question evaluation."""
        return {
            "question_title": self.question_title,
            "score": self.score,
            "max_score": self.max_score,
            "rubric_items": [item.to_dict() for item in self.rubric_items],
            "feedback": self.feedback,
        }

    def __str__(self) -> str:
        """Return a JSON string representation of the question evaluation."""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=True)


@dataclass(frozen=True)
class EvaluationReport:
    """Represents the evaluation report for one submission."""

    student_identifier: str
    test_name: str
    total_score: float
    max_score: float
    questions: List[QuestionEvaluation]
    notes: str

    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON-serializable representation of the report."""
        return {
            "student_id": self.student_identifier,
            "test": self.test_name,
            "total_score": self.total_score,
            "max_score": self.max_score,
            "questions": [question.to_dict() for question in self.questions],
            "notes": self.notes,
        }

    def __str__(self) -> str:
        """Return a JSON string representation of the report."""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=True)
