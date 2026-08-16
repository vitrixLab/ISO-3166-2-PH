from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


@dataclass(frozen=True)
class Document:
    id: str
    text: str
    status: str
    source: str


@dataclass(frozen=True)
class Match:
    id: str
    score: float
    text: str
    status: str
    source: str


_WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9:_./-]+")


def _tokens(text: str) -> set[str]:
    return {token.lower() for token in _WORD.findall(text)}


def load_markdown_documents(root: Path) -> list[Document]:
    """Load only current-oriented markdown sources; legacy/template pages are excluded."""
    docs: list[Document] = []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root).as_posix()
        if relative.startswith("audit/"):
            status = "current"
        elif relative.startswith("data/"):
            status = "current"
        else:
            # README and project docs are contextual until individually reviewed.
            status = "historical"
        docs.append(
            Document(
                id=relative,
                text=path.read_text(encoding="utf-8"),
                status=status,
                source=relative,
            )
        )
    return docs


def retrieve(query: str, documents: Iterable[Document], limit: int = 5) -> list[Match]:
    """Small dependency-free baseline retriever.

    It intentionally does lexical retrieval first. A production deployment can replace this
    implementation with an embedding/vector store without changing the MCP interface.
    """
    query_terms = _tokens(query)
    if not query_terms:
        return []

    matches: list[Match] = []
    for doc in documents:
        doc_terms = _tokens(doc.text)
        overlap = query_terms & doc_terms
        if not overlap:
            continue
        score = len(overlap) / max(len(query_terms), 1)
        matches.append(Match(doc.id, score, doc.text, doc.status, doc.source))

    matches.sort(key=lambda item: (-item.score, item.id))
    return matches[: max(1, limit)]
