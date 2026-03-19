from pathlib import Path

from classes.services.evaluation.code_json_loader_service import CodeJsonLoaderService
from classes.services.evaluation.evaluation_report_writer_service import (
    EvaluationReportWriterService,
)
from classes.services.evaluation.evaluation_service import EvaluationService
from classes.services.evaluation.question_document_loader_service import (
    QuestionDocumentLoaderService,
)
from classes.services.evaluation.rubric_loader_service import RubricLoaderService
from classes.utils.configuration.evaluator_agent_config_loader import (
    EvaluatorAgentConfigLoader,
)


class EvaluateCodeJsonCommand:
    """Command runner for evaluating code JSON submissions."""

    def __init__(self, repository_root: Path) -> None:
        """Initialize the command with the repository root path."""
        self._repository_root = repository_root

    def run(self) -> None:
        """Execute the evaluation workflow defined in EvaluatorAgent.md."""
        configuration_loader = EvaluatorAgentConfigLoader(
            self._repository_root / "EvaluatorAgent.md"
        )
        configuration = configuration_loader.load()
        code_loader = CodeJsonLoaderService()
        submissions = code_loader.load_submissions(
            self._repository_root, configuration.code_source_glob
        )
        question_loader = QuestionDocumentLoaderService()
        question_titles_by_test = question_loader.load_question_titles_by_test(
            self._repository_root, configuration.question_source_glob
        )
        rubric_loader = RubricLoaderService()
        rubric_definitions_by_test = rubric_loader.load_rubric_definitions(
            self._repository_root, configuration.rubric_paths_by_test
        )
        evaluation_service = EvaluationService()
        reports = evaluation_service.evaluate_submissions(
            submissions,
            question_titles_by_test,
            rubric_definitions_by_test,
        )
        writer_service = EvaluationReportWriterService()
        writer_service.write_reports(reports, Path(configuration.output_root))


if __name__ == "__main__":
    EvaluateCodeJsonCommand(Path(__file__).resolve().parents[3]).run()
