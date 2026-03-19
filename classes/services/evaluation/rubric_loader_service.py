import json
from pathlib import Path
from typing import Dict, List

from models.evaluation.rubric_models import RubricDefinition, RubricItem


class RubricLoaderService:
    """Loads rubric definitions from JSON files."""

    def load_rubric_definitions(
        self,
        repository_root: Path,
        rubric_paths_by_test: Dict[str, str],
    ) -> Dict[str, RubricDefinition]:
        """Return rubric definitions keyed by test name."""
        definitions: Dict[str, RubricDefinition] = {}
        for test_name, rubric_path in rubric_paths_by_test.items():
            absolute_path = repository_root / rubric_path
            definitions[test_name] = self._load_rubric_for_test(test_name, absolute_path)
        return definitions

    def _load_rubric_for_test(
        self,
        test_name: str,
        rubric_path: Path,
    ) -> RubricDefinition:
        """Load rubric items from a JSON file."""
        rows = self._read_rows(rubric_path)
        items: List[RubricItem] = []
        for row in rows:
            identifier_key = self._find_identifier_key(row)
            if not identifier_key:
                continue
            identifier_value = str(row.get(identifier_key, "")).strip()
            if not identifier_value or identifier_value.lower() == "total":
                continue
            description = str(row.get("Description", "")).strip()
            score_value = self._parse_score(row.get("Score"))
            items.append(
                RubricItem(
                    identifier=identifier_value,
                    score=score_value,
                    description=description,
                )
            )
        return RubricDefinition(test_name=test_name, items=items)

    def _parse_score(self, score_value: object) -> float:
        """Parse rubric score values safely."""
        if score_value is None:
            return 0.0
        try:
            return float(score_value)
        except (TypeError, ValueError):
            return 0.0

    def _read_rows(self, rubric_path: Path) -> List[Dict[str, object]]:
        """Read rubric JSON rows from disk."""
        with rubric_path.open("r", encoding="utf-8") as file_handle:
            data = json.load(file_handle)
        if not isinstance(data, list):
            raise ValueError(f"Expected list in rubric JSON: {rubric_path}")
        return data

    def _find_identifier_key(self, row: Dict[str, object]) -> str:
        """Identify the column that holds the rubric identifier."""
        for key_name in row.keys():
            if key_name not in {"Score", "Description"}:
                return key_name
        return ""
