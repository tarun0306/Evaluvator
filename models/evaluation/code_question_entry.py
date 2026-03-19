import json
from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class CodeQuestionEntry:
    """Represents a single question entry and its code lines from code JSON."""

    question_key: str
    question_title: str
    code_lines: List[str]

    @staticmethod
    def from_serialized_entry(
        serialized_entry: Dict[str, Any]
    ) -> "CodeQuestionEntry":
        """Create a CodeQuestionEntry from a serialized JSON entry."""
        question_key = ""
        for key_name in serialized_entry:
            if key_name.startswith("question_"):
                question_key = key_name
                break
        if not question_key:
            raise ValueError("Missing question key in code JSON entry.")
        question_title_value = str(serialized_entry.get(question_key, ""))
        code_value = serialized_entry.get("code", [])
        code_lines = [str(line) for line in code_value] if isinstance(code_value, list) else []
        return CodeQuestionEntry(
            question_key=question_key,
            question_title=question_title_value,
            code_lines=code_lines,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON-serializable representation of the entry."""
        return {
            "question_key": self.question_key,
            "question_title": self.question_title,
            "code": list(self.code_lines),
        }

    def __str__(self) -> str:
        """Return a JSON string representation of the entry."""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=True)
