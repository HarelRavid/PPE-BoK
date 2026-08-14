# PPE-BoK Changelog

## 1.2 — Chapter 13 Controlled Integration — 2026-08-14

### Chapter 13 baseline

- Closed historical PR #2 without merge and retained it as development provenance only.
- Integrated Chapter 013 — Polyethylene through clean PR #8 on the current repository baseline.
- The Chapter 13 integration contains only the controlled manuscript, chapter references/review record and the dedicated review package; Chapters 000–012 were not rewritten by the integration.
- Chapter 13 is now the active **standards-validation candidate** on `main`, not a publication-frozen chapter.

### Review state

- Engineering redevelopment / Investigations 1–10: complete for the approved CDB scope.
- Technical Review: PASS.
- Physics / equations / units / worked examples: PASS.
- Academic/Evidence Review: PASS for the current core non-normative claim set with explicit transferability limits.
- Editorial/Style Review: CONDITIONAL PASS; no structural rewrite required.
- Public authoritative ISO identity / edition-lifecycle / scope navigation: rechecked 2026-08-14.
- Authoritative full-text Standards Validation: OPEN.
- Design Freeze: BLOCKED until the applicable standards holds and bounded publication actions close.

### Standards source-access hold

- Issue #9 tracks the five controlled full-text Standards Validation holds (`SVH-013-01` through `SVH-013-05`).
- Secondary literature, project reports and withdrawn editions do not close current normative holds.
- Chapter 13 will return to final Standards Validation and Design Freeze when lawful current authoritative source text is available.

### Current production sequence

1. Keep Chapter 13 full-text Standards Validation work controlled under Issue #9.
2. Synchronize repository metadata to the merged Chapter 13 baseline.
3. Prepare the controlled CDB for Working Chapter 014.
4. Do not begin Chapter 014 Engineering Development until its CDB satisfies the Definition of Ready and receives explicit author approval.
5. Continue book development according to `BOOK_STRUCTURE.md` without treating the external Chapter 13 source-access hold as publication closure.

---

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

### Current production sequence at 1.1

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

This sequence is retained here as historical baseline context. The active production sequence is governed by the current `BOOK_STRUCTURE.md` and the latest changelog entry above.

### Standards control

Standards-derived content is revalidated directly against authoritative source documents after authoring is complete and before publication approval.
