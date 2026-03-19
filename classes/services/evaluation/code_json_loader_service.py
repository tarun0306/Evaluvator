import json
from pathlib import Path
from typing import Any, Dict, List

from models.evaluation.code_file_submission import CodeFileSubmission


class CodeJsonLoaderService:
    """Loads code JSON files and builds submission models."""

    def load_submissions(
        self,
        repository_root: Path,
        code_source_glob: str,
    ) -> List[CodeFileSubmission]:
        """Load all code JSON files matching the configured glob."""
        submissions: List[CodeFileSubmission] = []
        for json_path in repository_root.glob(code_source_glob):
            submissions.append(self._load_submission(json_path))
        return submissions

    def _load_submission(self, json_path: Path) -> CodeFileSubmission:
        """Load a single submission from a JSON file path."""
        serialized_entries = self._read_serialized_entries(json_path)
        test_name = json_path.parents[1].name
        student_identifier = json_path.stem
        return CodeFileSubmission.from_serialized_entries(
            student_identifier=student_identifier,
            test_name=test_name,
            serialized_entries=serialized_entries,
        )

    def _read_serialized_entries(self, json_path: Path) -> List[Dict[str, Any]]:
        """Read a JSON file and return its serialized entries."""
        with json_path.open("r", encoding="utf-8") as file_handle:
            data = json.load(file_handle)
        if not isinstance(data, list):
            raise ValueError(f"Expected list in code JSON: {json_path}")
        return data
