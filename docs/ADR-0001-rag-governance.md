# ADR-0001: Tiered RAG Governance

## Status
Accepted for the initial implementation.

## Decision

Use a hybrid governance model:

1. Apply hard exclusions during ingestion for content that must never enter the trusted corpus (for example, malformed inputs or explicitly prohibited sources).
2. Preserve historical, unverified, and deprecated material with provenance where retention is useful for auditability.
3. Apply softer trust filtering at query time, with `current` as the default and `historical` as an explicit opt-in.
4. Keep policy logic independent from the MCP transport so the same policy can be used by batch jobs, HTTP APIs, tests, or another MCP implementation.
5. Automate freshness detection in production from source metadata and schedule re-verification rather than treating `SOURCES.md` as a manual per-document registry.

## Rationale

A pure default-deny index maximizes precision but can lose legitimate historical context and creates unnecessary reclassification work. A pure confidence-ranked index risks stale facts appearing as current answers. The hybrid model preserves recall without weakening the default current-state trust boundary.

## Retrieval evaluation

Governance correctness and retrieval relevance are measured separately. The lexical retriever is a testable baseline, not a production-quality semantic-search claim. A labeled query set will be used to benchmark embeddings/vector storage before replacing the baseline.

## Failure mode

MCP is not the sole governance dependency. Retrieval and policy remain importable independently so an MCP outage does not make the underlying knowledge layer unusable.
