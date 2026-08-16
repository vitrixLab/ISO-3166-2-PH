from pathlib import Path

from server.rag import Document, load_markdown_documents, retrieve


def test_retrieve_defaults_to_current_only():
    documents = [
        Document("current.md", "Philippine Statistics Authority PSGC source", "current", "current.md"),
        Document("history.md", "Philippine Statistics Authority PSGC source", "historical", "history.md"),
    ]
    matches = retrieve("PSGC source", documents, 5)
    assert [match.id for match in matches] == ["current.md"]


def test_historical_context_is_opt_in():
    documents = [
        Document("current.md", "PSGC region", "current", "current.md"),
        Document("history.md", "PSGC region", "historical", "history.md"),
    ]
    matches = retrieve("PSGC region", documents, 5, allowed_statuses=("current", "historical"))
    assert {match.status for match in matches} == {"current", "historical"}


def test_retrieve_returns_provenance():
    documents = [Document("data/SOURCES.md", "PSGC source", "current", "data/SOURCES.md")]
    matches = retrieve("PSGC source", documents, 1)
    assert matches[0].source == "data/SOURCES.md"
    assert matches[0].status == "current"


def test_markdown_loader_excludes_html_by_construction(tmp_path: Path):
    (tmp_path / "current.md").write_text("current information", encoding="utf-8")
    (tmp_path / "legacy.html").write_text("legacy information", encoding="utf-8")
    assert [doc.id for doc in load_markdown_documents(tmp_path)] == ["current.md"]
