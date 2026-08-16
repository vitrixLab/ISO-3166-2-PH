# Data Sources and Provenance

## Current geographic source

- Publisher: Philippine Statistics Authority (PSA)
- Dataset: Philippine Standard Geographic Code (PSGC)
- Current page: https://psa.gov.ph/classification/psgc/regions
- Verification note: PSA currently reports 18 regions as of 31 July 2025 and lists 2026 PSGC updates, including the 13 July 2026 second-quarter release.
- Use: current Philippine geographic entity names and PSGC identifiers.
- Restriction: PSGC is not the same identifier system as ISO 3166-2.

## ISO 3166-2 mapping

ISO 3166-2:PH mappings must be maintained as a versioned, provenance-bearing artifact. Do not infer ISO codes from PSGC codes.

Required fields for each verified mapping:

- `iso_3166_2`
- `name`
- `subdivision_type`
- `parent_iso_3166_2`
- `psgc_code` when an explicit verified mapping exists
- `valid_from`
- `valid_to`
- `source`
- `source_published_at`
- `verified_at`
- `status`

## Historical sources

Historical project studies and the repository's 2012-era PDF may be retained for contextual retrieval, but must be tagged `historical` and must not override newer authoritative sources.

## Conflict rule

For current-state questions, prefer the newest verified authoritative source. Preserve conflicting older records with provenance rather than silently deleting them.
