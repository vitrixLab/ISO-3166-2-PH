# RAG + MCP Architecture

This repository uses a provenance-aware RAG baseline and an MCP interface. Governance is enforced at ingestion for hard exclusions and at retrieval time for softer trust tiers.

## Trust model

- **Current** records are the default factual retrieval tier.
- **Historical** records remain indexed when useful, but are opt-in and always labeled historical.
- **Unverified/deprecated** records are retained for auditability but are not eligible for default factual answers.
- Template/legacy HTML is excluded from the baseline Markdown index by construction.
- ISO 3166-2 mappings require explicit verification and provenance; PSGC identifiers are never converted into ISO identifiers by inference.

## Governance and scaling

`data/SOURCES.md` defines source and freshness policy, but it is not the runtime database of every document. Production ingestion should extract provenance automatically from source metadata, run freshness checks, and emit a versioned manifest. Manual audit is for exceptions and policy decisions, not per-document recurring classification.

Hard exclusions belong in ingestion. Query-time filters handle softer trust choices, so historical/comparative questions can opt in without weakening the default current-state policy. Policy functions are reusable outside MCP; MCP exposes them rather than owning the governance lifecycle.

## MCP interface

- `search_project_knowledge(query, limit, include_historical)` — retrieval with explicit historical opt-in.
- `get_data_policy()` — current source and freshness policy.
- `get_mapping_schema()` — canonical mapping schema.
- `iso3166ph://policy` — policy resource.
- `iso3166ph://schema` — schema resource.

The MCP server is an API/control surface, not the sole governance authority. Retrieval remains testable independently, and the policy/data layer can be reused by another API or batch job if the MCP service is unavailable.

## Evaluation

Keep evaluation dimensions separate:

1. **Governance tests:** provenance propagation, status filtering, freshness metadata, and exclusion rules.
2. **Retrieval tests:** relevance/recall on a small labeled query set.
3. **Answer tests:** citation correctness and refusal/uncertainty behavior.

The dependency-free lexical retriever is only a baseline for these tests; it is not evidence that lexical retrieval is sufficient for production semantic search.

## Next production step

Populate `data/iso-3166-2-ph.json` with independently verified mappings, then benchmark a small embedding/vector backend against the labeled retrieval set. Preserve the provenance fields and status contract while allowing the backend to evolve.
