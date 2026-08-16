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
    docs: list[Document] = []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root).as_posix()
        status = "current" if relative.startswith(("audit/", "data/")) else "historical"
        docs.append(Document(relative, path.read_text(encoding="utf-8"), status, relative))
    return docs

def retrieve(query: str, documents: Iterable[Document], limit: int = 5) -> list[Match]:
    query_terms = _tokens(query)
    if not query_terms:
        return []
    matches: list[Match] = []
    for document in documents:
        overlap = query_terms & _tokens(document.text)
        if overlap:
            score = len(overlap) / max(len(query_terms), 1)
            matches.append(Match(document.id, score, document.text, document.status, document.source))
    matches.sort(key=lambda item: (-item.score, item.id))
    return matches[:max(1, limit)]
