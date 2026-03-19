from pathlib import Path
from tempfile import TemporaryDirectory

from classes.utils.configuration.evaluator_agent_config_loader import (
    EvaluatorAgentConfigLoader,
)
from tests.base_timeout_test_case import BaseTimeoutTestCase


class EvaluatorAgentConfigLoaderTests(BaseTimeoutTestCase):
    """Tests for EvaluatorAgentConfigLoader."""

    def test_load_configuration_values(self) -> None:
        """Load configuration values from a markdown file."""
        markdown_text = """# EvaluatorAgent

## Scope
- Tests: Test_1, Test_2
- Code source: `*/_code_json/*.json`
- Question source: `Test_Questions/*.docx`
- Rubric source:
  - Test_1: `Test_1/_rubric.json`
  - Test_2: `Test_2/rubric_Test_2.json`
"""
        with TemporaryDirectory() as temporary_directory:
            markdown_path = Path(temporary_directory) / "EvaluatorAgent.md"
            markdown_path.write_text(markdown_text, encoding="utf-8")
            loader = EvaluatorAgentConfigLoader(markdown_path)
            configuration = loader.load()

        self.assertEqual(configuration.tests, ["Test_1", "Test_2"])
        self.assertEqual(configuration.code_source_glob, "*/_code_json/*.json")
        self.assertEqual(configuration.question_source_glob, "Test_Questions/*.docx")
        self.assertEqual(
            configuration.rubric_paths_by_test,
            {
                "Test_1": "Test_1/_rubric.json",
                "Test_2": "Test_2/rubric_Test_2.json",
            },
        )
