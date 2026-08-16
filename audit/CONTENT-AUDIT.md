# Repository Content Audit

Date: 2026-08-16

## Purpose

This audit separates current, authoritative project information from historical, placeholder, or legacy material before the repository is used as a retrieval-augmented generation (RAG) knowledge source.

## Findings

### Current / retain

- `index.html` — current project landing page.
- `license` — repository license artifact; retain as legal metadata.
- `MIT-License.html` — retain as a human-readable license page, but keep it out of geographic factual retrieval.

### Historical / contextual

- `Comprehensive-Study.html` — project background and historical discussion. Useful for context, but it must not be treated as current geographic authority.
- `dbm.2012.17.pdf` — legacy/historical reference material. Preserve with publication metadata and a historical status marker.
- `sda-prototype.html` and `geomap.html` — prototype/legacy UI material. Do not use as authoritative geographic data.

### Obsolete / template content

- `README.md` currently contains HTML rather than Markdown and still includes placeholder links such as `[link]`.
- `Getting-Started.html` contains placeholder tools, placeholder repository commands, and references to files/directories that do not exist in the current repository.
- `Contribution-Guidelines.html` is generic boilerplate and does not describe validation, provenance, or data-review requirements.
- Legacy jQuery Mobile assets and prototype scripts should not be indexed as factual project knowledge.

## Retrieval policy

The RAG layer must distinguish at least these statuses:

- `current` — eligible for normal factual retrieval.
- `historical` — retrievable only when the question explicitly asks for history or prior state.
- `template` — excluded from retrieval.
- `legacy` — excluded from normal factual retrieval.
- `legal` — retained for licensing/compliance questions, excluded from geographic fact retrieval.

## Geographic data policy

The repository currently does not contain a canonical, versioned ISO 3166-2:PH dataset. The implementation must not infer current subdivision codes from prose pages or legacy files.

The authoritative geographic layer will be maintained as structured data with explicit provenance, source date, and verification status. Philippine Standard Geographic Code (PSGC) material from the Philippine Statistics Authority is a source for current Philippine geographic entities; ISO 3166-2 mappings must be separately verified and must not be conflated with PSGC identifiers.

The PSA page currently reports 18 regions as of 31 July 2025 and lists 2026 PSGC updates, including the second-quarter 2026 update released on 13 July 2026. See `data/SOURCES.md` for provenance.
