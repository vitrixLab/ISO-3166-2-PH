from pathlib import Path

from server.rag import Document, load_markdown_documents, retrieve


def test_retrieve_returns_provenance() -> None:
    documents = [
        Document(
            id="data/SOURCES.md",
            text="Philippine Statistics Authority PSGC current source",
            status="current",
            source="data/SOURCES.md",
        ),
        Document(
            id="legacy.html",
            text="Philippine Statistics Authority PSGC current source",
            status="legacy",
            source="legacy.html",
        ),
    ]
    matches = retrieve("PSGC source", documents, limit=1)
    assert matches[0].source == "data/SOURCES.md"
    assert matches[0].status == "current"


def test_markdown_loader_excludes_html_by_construction(tmp_path: Path) -> None:
    (tmp_path / "current.md").write_text("current information", encoding="utf-8")
    (tmp_path / "legacy.html").write_text("legacy information", encoding="utf-8")
    documents = load_markdown_documents(tmp_path)
    assert [doc.id for doc in documents] == ["current.md"]
