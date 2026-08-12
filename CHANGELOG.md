# PPE-BoK Changelog

## 1.1 — Architecture Recovery and Repository Hygiene — 2026-08-12

### Architecture and scope

- Recovered and documented the working full-book architecture in `BOOK_STRUCTURE.md`.
- Confirmed the governing rule that knowledge scope determines chapter count; final numbering and Part boundaries remain unfrozen.
- Preserved the historical knowledge inventory in `docs/MASTER-KNOWLEDGE-SCOPE-MAP.md` and `docs/HISTORICAL-KNOWLEDGE-SCOPE-RECOVERY.md`.

### Repository hygiene

- Added `archive/` as the controlled home for superseded and legacy material.
- Migrated Chapter 009 from the retired `Book/` structure into the canonical `/chapters` namespace without changing its current `main` technical content.
- Archived the retired `Book/` structure for provenance.
- Archived the superseded `docs/PPE-BoK_LLM_WIKI.md`, which predates and conflicts with PDS 1.0.
- Retired the duplicate `/standards` namespace; the active central standards index remains `references/Standards-Register.md`.
- Preserved superseded authoring templates under `archive/legacy-templates/` before replacing the active templates with PDS-aligned versions.
- Added `docs/REPOSITORY-METADATA-AUDIT-2026-08-12.md` to record the cleanup basis and dispositions.

### Documentation synchronization

- Updated repository navigation, manuscript inventory, production sequence and governance wording to reflect the recovered continuation beyond Chapter 013.
- Updated the central Standards Register from standards already documented in Chapter 009–013 source registers; no new normative claims are introduced by the metadata cleanup.
- Generalized formal EDR/RDP/review templates from Chapter-13-pilot wording to normal PDS 1.0 production use.

### Current production sequence

1. Resolve the Chapter 013 redevelopment branch / pull-request state.
2. Complete authoritative Standards Validation and remaining publication gates for Chapter 013.
3. Create the controlled CDB for Working Chapter 014.
4. Continue book development according to `BOOK_STRUCTURE.md`, while maintaining the topic-depth coverage map.

---

## 1.0 — PDS Production Baseline

### Added

- PPE-BoK Development System governance and production controls.
- Approved repository architecture: `/chapters`, `/docs`, `/templates`, `/assets`, `/references`, `/governance`.
- Central Standards Register.
- Engineering asset ID convention: `EQ`, `FIG`, `TAB`, `WF`, `EX`, `DT`, `CL` + chapter and sequence numbers.
- Human Approval Gate before technical content becomes repository baseline.
- Definitions of Ready and Done.
- Configuration-management and versioning rules using `1.0`, `1.1`, `1.2`, `2.0`.

### Historical production sequence at Baseline 1.0

1. Finalize and validate Chapter 13 as the PDS pilot.
2. After pilot acceptance, redevelop the then-current book sequentially from Chapter 001 through Chapter 013.
3. No chapter revision becomes official before joint review, explicit author approval, merge and baseline.

This sequence is retained here as historical baseline context. The active production sequence is governed by the current `BOOK_STRUCTURE.md` and the 1.1 repository-hygiene update above.

### Standards control

Standards-derived content is revalidated directly against authoritative source documents after authoring is complete and before publication approval.
