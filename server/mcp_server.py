from __future__ import annotations

import json
from pathlib import Path

from mcp.server.mcpserver import MCPServer

from .rag import Document, load_markdown_documents, retrieve

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_ROOT = ROOT

mcp = MCPServer("ISO-3166-2-PH RAG")


def _documents() -> list[Document]:
    return load_markdown_documents(KNOWLEDGE_ROOT)


@mcp.tool()
def search_project_knowledge(query: str, limit: int = 5) -> dict:
    """Retrieve project knowledge with provenance and retrieval status."""
    matches = retrieve(query, _documents(), limit=limit)
    return {
        "query": query,
        "matches": [
            {
                "id": match.id,
                "score": round(match.score, 4),
                "status": match.status,
                "source": match.source,
                "text": match.text[:4000],
            }
            for match in matches
        ],
    }


@mcp.tool()
def get_data_policy() -> str:
    """Return the repository's current data provenance and freshness policy."""
    path = ROOT / "data" / "SOURCES.md"
    return path.read_text(encoding="utf-8")


@mcp.tool()
def get_mapping_schema() -> dict:
    """Return the canonical schema used for ISO 3166-2:PH mapping records."""
    path = ROOT / "data" / "schema.json"
    return json.loads(path.read_text(encoding="utf-8"))


@mcp.resource("iso3166ph://policy")
def policy_resource() -> str:
    return get_data_policy()


@mcp.resource("iso3166ph://schema")
def schema_resource() -> str:
    return json.dumps(get_mapping_schema(), indent=2)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
