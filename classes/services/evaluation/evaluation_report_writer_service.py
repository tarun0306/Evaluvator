import json
from pathlib import Path
from typing import List

from models.evaluation.evaluation_report import EvaluationReport


class EvaluationReportWriterService:
    """Writes evaluation reports to JSON files."""

    def write_reports(self, reports: List[EvaluationReport], output_root: Path) -> None:
        """Write each report to the output folder."""
        output_root.mkdir(parents=True, exist_ok=True)
        for report in reports:
            test_directory = output_root / report.test_name
            test_directory.mkdir(parents=True, exist_ok=True)
            report_path = test_directory / f"{report.student_identifier}.json"
            report_path.write_text(
                json.dumps(report.to_dict(), indent=2, ensure_ascii=True),
                encoding="utf-8",
            )
