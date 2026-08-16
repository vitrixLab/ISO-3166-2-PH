from pathlib import Path

from server.rag import Document, load_markdown_documents, retrieve


def test_retrieve_returns_provenance():
    documents = [
        Document("data/SOURCES.md", "Philippine Statistics Authority PSGC current source", "current", "data/SOURCES.md"),
        Document("legacy.html", "Philippine Statistics Authority PSGC current source", "legacy", "legacy.html"),
    ]
    matches = retrieve("PSGC source", documents, 1)
    assert matches[0].source == "data/SOURCES.md"
    assert matches[0].status == "current"


def test_markdown_loader_excludes_html_by_construction(tmp_path: Path):
    (tmp_path / "current.md").write_text("current information", encoding="utf-8")
    (tmp_path / "legacy.html").write_text("legacy information", encoding="utf-8")
    assert [doc.id for doc in load_markdown_documents(tmp_path)] == ["current.md"]
