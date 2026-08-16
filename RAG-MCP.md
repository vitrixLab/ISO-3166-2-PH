# RAG + MCP Architecture

This repository now has a provenance-aware baseline for retrieval-augmented generation (RAG) and a Model Context Protocol (MCP) server.

## Design goals

1. Keep authoritative geographic data separate from historical and template content.
2. Require explicit provenance and verification metadata for ISO 3166-2:PH mappings.
3. Expose retrieval through MCP tools without coupling clients to storage internals.
4. Keep the first retriever dependency-free so the data and trust model can be tested before adopting a vector database.

## MCP interface

The server exposes:

- `search_project_knowledge(query, limit)` — provenance-aware retrieval over reviewed Markdown knowledge.
- `get_data_policy()` — current source/provenance policy.
- `get_mapping_schema()` — canonical mapping-record schema.
- `iso3166ph://policy` — policy resource.
- `iso3166ph://schema` — schema resource.

The implementation targets the current MCP Python SDK v2 line (`mcp>=2,<3`). The official SDK supports MCP tools/resources/prompts and stdio, Streamable HTTP, and SSE transports.

## RAG trust model

Current factual retrieval is based on reviewed Markdown content and the structured data/provenance layer. HTML prototypes, template instructions, and legacy assets are not indexed by the baseline loader.

The lexical retriever in `server/rag.py` is deliberately a baseline. A production deployment can replace it with embeddings and a vector store while retaining the same provenance contract.

## Data freshness

Current Philippine geographic entity information should be refreshed from the latest PSA PSGC release. ISO 3166-2 mappings require independent verification; PSGC and ISO identifiers must never be conflated.
