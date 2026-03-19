import json
from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class RubricItem:
    """Represents a single rubric criterion."""

    identifier: str
    score: float
    description: str

    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON-serializable representation of the rubric item."""
        return {
            "identifier": self.identifier,
            "score": self.score,
            "description": self.description,
        }

    def __str__(self) -> str:
        """Return a JSON string representation of the rubric item."""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=True)


@dataclass(frozen=True)
class RubricDefinition:
    """Represents all rubric items for a test."""

    test_name: str
    items: List[RubricItem]

    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON-serializable representation of the rubric definition."""
        return {
            "test_name": self.test_name,
            "items": [item.to_dict() for item in self.items],
        }

    def __str__(self) -> str:
        """Return a JSON string representation of the rubric definition."""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=True)
