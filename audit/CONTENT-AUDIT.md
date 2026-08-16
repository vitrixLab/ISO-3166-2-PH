# Repository Content Audit

Date: 2026-08-16

## Purpose

Separate current, authoritative project information from historical, placeholder, or legacy material before repository content is used as a RAG knowledge source.

## Findings

### Current / retain

- `index.html` — current project landing page.
- `license` — repository license artifact; retain as legal metadata.
- `MIT-License.html` — human-readable license page; keep out of geographic factual retrieval.

### Historical / contextual

- `Comprehensive-Study.html` — project background and historical discussion; useful for context, not current geographic authority.
- `dbm.2012.17.pdf` — legacy/historical reference; preserve with publication metadata and `historical` status.
- `sda-prototype.html` and `geomap.html` — prototype/legacy UI; do not use as authoritative geographic data.

### Obsolete / template

- `README.md` is HTML content stored under a Markdown filename and still contains placeholder links.
- `Getting-Started.html` contains placeholder tools, repository commands, and configuration instructions unrelated to the current repository.
- `Contribution-Guidelines.html` is generic boilerplate and lacks data provenance and validation requirements.
- Legacy jQuery Mobile assets and prototype scripts should not be indexed as factual project knowledge.

## Retrieval statuses

- `current` — eligible for normal factual retrieval.
- `historical` — retrievable for historical/prior-state questions.
- `template` — excluded from retrieval.
- `legacy` — excluded from normal factual retrieval.
- `legal` — retained for licensing/compliance questions, excluded from geographic fact retrieval.

## Geographic data policy

The repository does not yet contain a canonical, verified ISO 3166-2:PH dataset. Current subdivision codes must not be inferred from prose pages or legacy files. The structured geographic layer must contain explicit provenance, source date, verification time, and status.

PSGC is a current Philippine geographic source, but PSGC and ISO 3166-2 are separate identifier systems and must not be conflated.
