# RAG + MCP Architecture

The repository now has a provenance-aware baseline for retrieval-augmented generation (RAG) and a Model Context Protocol (MCP) server.

## Trust model

- Current and structured data are eligible for normal factual retrieval.
- Historical material is available for historical questions only.
- Template and legacy content is excluded from the baseline Markdown index.
- ISO 3166-2 mappings require explicit verification and provenance.
- PSGC identifiers are never converted into ISO identifiers by inference.

## MCP interface

- `search_project_knowledge(query, limit)` — provenance-aware retrieval.
- `get_data_policy()` — current source and freshness policy.
- `get_mapping_schema()` — canonical mapping schema.
- `iso3166ph://policy` — policy resource.
- `iso3166ph://schema` — schema resource.

The implementation targets the current MCP Python SDK v2 line (`mcp>=2,<3`). The official SDK supports tools/resources/prompts and standard MCP transports.

## Next production step

Replace the dependency-free lexical retriever in `server/rag.py` with embeddings/vector storage after the verified ISO dataset is populated. Keep the provenance fields and retrieval-status contract unchanged.
