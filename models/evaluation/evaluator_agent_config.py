import json
from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class EvaluatorAgentConfig:
    """Holds configuration details parsed from EvaluatorAgent.md."""

    tests: List[str]
    code_source_glob: str
    question_source_glob: str
    rubric_paths_by_test: Dict[str, str]
    output_root: str

    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON-serializable representation of the configuration."""
        return {
            "tests": list(self.tests),
            "code_source_glob": self.code_source_glob,
            "question_source_glob": self.question_source_glob,
            "rubric_paths_by_test": dict(self.rubric_paths_by_test),
            "output_root": self.output_root,
        }

    def __str__(self) -> str:
        """Return a JSON string representation of the configuration."""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=True)
