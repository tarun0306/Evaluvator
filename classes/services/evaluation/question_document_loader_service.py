import re
from pathlib import Path
from typing import Dict, List

from docx import Document


class QuestionDocumentLoaderService:
    """Loads question titles from DOCX documents."""

    def load_question_titles_by_test(
        self,
        repository_root: Path,
        question_source_glob: str,
    ) -> Dict[str, List[str]]:
        """Return question titles keyed by test name."""
        titles_by_test: Dict[str, List[str]] = {}
        for document_path in repository_root.glob(question_source_glob):
            test_name = self._resolve_test_name(document_path)
            titles_by_test[test_name] = self._extract_titles_from_document(document_path)
        return titles_by_test

    def _resolve_test_name(self, document_path: Path) -> str:
        """Map a document filename to the test name."""
        lower_name = document_path.name.lower()
        if "test02_makeup" in lower_name:
            return "Test_2_makeup"
        if "test01" in lower_name:
            return "Test_1"
        if "test02" in lower_name:
            return "Test_2"
        if "test03" in lower_name:
            return "Test_3"
        raise ValueError(f"Unrecognized test document: {document_path}")

    def _extract_titles_from_document(self, document_path: Path) -> List[str]:
        """Extract question titles from a DOCX file."""
        document = Document(str(document_path))
        titles: List[str] = []
        pattern = re.compile(r"^(?:[A-Z]\.\s+|\d+\.\s+).+")
        for paragraph in document.paragraphs:
            text = paragraph.text.strip()
            if not text:
                continue
            if pattern.match(text):
                titles.append(text)
        return titles
