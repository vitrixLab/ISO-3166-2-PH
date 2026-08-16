# Data Sources and Provenance

## Current geographic source

- Publisher: Philippine Statistics Authority (PSA)
- Dataset: Philippine Standard Geographic Code (PSGC)
- Current page: https://psa.gov.ph/classification/psgc/regions
- Current scope: Philippine administrative/geographic entities
- Verification note: PSA currently publishes 18 regions as of 31 July 2025 and lists 2026 PSGC updates, including Q2 2026 updates released 13 July 2026.
- Use: current Philippine geographic entity names and PSGC identifiers
- Restriction: PSGC is not the same identifier system as ISO 3166-2. ISO mappings must be separately verified.

## ISO 3166-2 mapping

The project must maintain ISO 3166-2:PH mappings as a versioned, provenance-bearing artifact. Do not infer or silently translate ISO codes from PSGC codes.

Required fields for every mapping:

- `iso_3166_2`
- `name`
- `subdivision_type`
- `parent_iso_3166_2`
- `psgc_code` (when an explicit verified mapping exists)
- `valid_from`
- `valid_to`
- `source`
- `source_published_at`
- `verified_at`
- `status`

## Historical sources

Historical project studies and the 2012-era PDF in the repository may be retained for contextual retrieval, but they must be tagged `historical` and must not override newer official geographic sources.

## Retrieval rule

When sources conflict, prefer the newest verified authoritative source for current-state questions. Preserve the conflicting record with provenance instead of silently deleting it.
