# Data Sources and Provenance

## Source registry

- Publisher: Philippine Statistics Authority (PSA)
- Dataset: Philippine Standard Geographic Code (PSGC)
- Current page: https://psa.gov.ph/classification/psgc/regions
- Use: current Philippine geographic entity names and PSGC identifiers.
- Restriction: PSGC is not ISO 3166-2. ISO mappings must be independently verified.

## Freshness policy

Source freshness is metadata, not a permanent label. Every ingested record should retain `source_published_at` and `verified_at`. In production, scheduled checks should detect changed source pages/files and mark affected records for re-verification rather than relying on a manual rewrite of this document.

Suggested operational states:

- `current`: verified against the newest applicable authoritative source.
- `historical`: valid for a prior period or contextual/historical use.
- `unverified`: retained for audit/review but excluded from default factual retrieval.
- `deprecated`: superseded and excluded from default retrieval.

## ISO 3166-2 mapping

Maintain mappings as versioned, provenance-bearing records. Never infer an ISO code by transforming a PSGC identifier.

Required fields:

- `iso_3166_2`
- `name`
- `subdivision_type`
- `parent_iso_3166_2`
- `psgc_code` (only when explicitly verified)
- `valid_from`
- `valid_to`
- `source`
- `source_published_at`
- `verified_at`
- `status`

## Historical sources

Historical project studies and older repository documents may be retained for contextual retrieval. They must carry `historical` status and must not override newer verified geographic sources in current-state answers.

## Retrieval policy

Default factual queries use `current` records. Historical/comparative queries may explicitly opt into `historical`. Unverified and deprecated records remain auditable but are not default retrieval candidates.

When sources conflict, prefer the newest verified authoritative source for current-state questions and preserve the conflicting record with provenance rather than silently deleting it.
