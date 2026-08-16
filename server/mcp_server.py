from __future__ import annotations

import json
from pathlib import Path

from mcp.server.mcpserver import MCPServer

from .rag import Document, load_markdown_documents, retrieve

ROOT = Path(__file__).resolve().parents[1]
mcp = MCPServer("ISO-3166-2-PH RAG")

def _documents() -> list[Document]:
    return load_markdown_documents(ROOT)

@mcp.tool()
def search_project_knowledge(query: str, limit: int = 5) -> dict:
    """Retrieve reviewed project knowledge with provenance metadata."""
    matches = retrieve(query, _documents(), limit)
    return {"query": query, "matches": [{"id": m.id, "score": round(m.score, 4), "status": m.status, "source": m.source, "text": m.text[:4000]} for m in matches]}

@mcp.tool()
def get_data_policy() -> str:
    """Return the current data freshness and provenance policy."""
    return (ROOT / "data" / "SOURCES.md").read_text(encoding="utf-8")

@mcp.tool()
def get_mapping_schema() -> dict:
    """Return the canonical ISO 3166-2:PH mapping schema."""
    return json.loads((ROOT / "data" / "schema.json").read_text(encoding="utf-8"))

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
