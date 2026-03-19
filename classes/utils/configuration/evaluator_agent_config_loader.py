import re
from pathlib import Path
from typing import Dict, List

from models.evaluation.evaluator_agent_config import EvaluatorAgentConfig


class EvaluatorAgentConfigLoader:
    """Loads EvaluatorAgent.md and extracts configuration values."""

    def __init__(self, markdown_path: Path) -> None:
        """Initialize the loader with the markdown path."""
        self._markdown_path = markdown_path

    def load(self) -> EvaluatorAgentConfig:
        """Parse the markdown file and return an EvaluatorAgentConfig."""
        markdown_lines = self._markdown_path.read_text(encoding="utf-8").splitlines()
        tests = self._extract_tests(markdown_lines)
        code_source = self._extract_code_source(markdown_lines)
        question_source = self._extract_question_source(markdown_lines)
        rubric_paths = self._extract_rubric_paths(markdown_lines)
        output_root = str(self._markdown_path.parent / "_evaluation_json")
        return EvaluatorAgentConfig(
            tests=tests,
            code_source_glob=code_source,
            question_source_glob=question_source,
            rubric_paths_by_test=rubric_paths,
            output_root=output_root,
        )

    def _extract_tests(self, markdown_lines: List[str]) -> List[str]:
        """Extract the test list from the markdown content."""
        for line in markdown_lines:
            if line.strip().startswith("- Tests:"):
                value = line.split(":", 1)[1]
                return [item.strip() for item in value.split(",") if item.strip()]
        raise ValueError("Tests list not found in EvaluatorAgent.md.")

    def _extract_code_source(self, markdown_lines: List[str]) -> str:
        """Extract the code source glob from the markdown content."""
        return self._extract_inline_code(markdown_lines, "- Code source:")

    def _extract_question_source(self, markdown_lines: List[str]) -> str:
        """Extract the question source glob from the markdown content."""
        return self._extract_inline_code(markdown_lines, "- Question source:")

    def _extract_rubric_paths(self, markdown_lines: List[str]) -> Dict[str, str]:
        """Extract rubric paths by test from the markdown content."""
        rubric_paths: Dict[str, str] = {}
        in_rubric_section = False
        for line in markdown_lines:
            stripped_line = line.strip()
            if stripped_line == "- Rubric source:":
                in_rubric_section = True
                continue
            if in_rubric_section and stripped_line.startswith("-"):
                match = re.match(r"-\s*(.+?):\s*`(.+?)`", stripped_line)
                if match:
                    rubric_paths[match.group(1).strip()] = match.group(2).strip()
                continue
            if in_rubric_section and stripped_line.startswith("##"):
                break
        if not rubric_paths:
            raise ValueError("Rubric paths not found in EvaluatorAgent.md.")
        return rubric_paths

    def _extract_inline_code(self, markdown_lines: List[str], prefix: str) -> str:
        """Extract inline code content following a prefix."""
        for line in markdown_lines:
            if line.strip().startswith(prefix):
                match = re.search(r"`(.+?)`", line)
                if match:
                    return match.group(1).strip()
        raise ValueError(f"Missing configuration line: {prefix}")
