# PPE-BoK Repository Metadata Audit — 2026-08-12

**Audit type:** Repository hygiene / non-content documentation review  
**Change class:** B — Structural / documentation synchronization  
**Technical chapter content changed by this audit:** No  
**Baseline reviewed:** `main` after the recovered working architecture was merged into `BOOK_STRUCTURE.md`

## 1. Objective

Review the repository material that is not pure book narrative and ensure that active files agree on:

- the current source-of-truth hierarchy;
- canonical chapter locations;
- the recovered book architecture;
- PDS 1.0 workflow and review gates;
- current continuation beyond Chapter 013;
- standards-register ownership;
- archive boundaries.

Superseded material is preserved under `archive/` rather than deleted.

## 2. Classification used

Each reviewed item was classified as one of:

- **CURRENT — KEEP**: active and consistent with the current baseline.
- **UPDATE**: still required, but contains stale status, navigation or pilot-era wording.
- **ARCHIVE**: historically useful but no longer canonical.
- **MIGRATE**: valid material stored in a retired location and therefore moved to its canonical active location while preserving the legacy snapshot.
- **DEFERRED TECHNICAL GATE**: outside the metadata-cleanup scope because it requires technical/standards review.

## 3. Major findings

### 3.1 Legacy `Book/` structure remained active

`Book/Part_02_Process_Definition_and_Requirements/Chapter_009_Polymer_Fundamentals/` contained the only Chapter 009 source on `main`, even though repository governance defines `/chapters` as the canonical chapter location.

**Disposition:** MIGRATE.

- Preserve the exact current-`main` Chapter 009 source under `chapters/chapter-009-polymer-fundamentals/`.
- Preserve the retired `Book/` snapshot under `archive/legacy-book/`.
- Remove the active `Book/` namespace.

No technical rewriting is performed as part of this move.

### 3.2 `docs/PPE-BoK_LLM_WIKI.md` conflicts with PDS 1.0

The legacy LLM Wiki declares itself the master operating guide and contains rules that conflict with the released PDS, including language policy, chapter-file naming, status vocabulary and review/file conventions.

**Disposition:** ARCHIVE under `archive/legacy-governance/`.

The current governing set is `docs/PDS/` + `governance/` + `BOOK_STRUCTURE.md`.

### 3.3 `/standards` duplicated the central standards function

The active architecture identifies `references/Standards-Register.md` as the central standards register. The separate `standards/` directory contained only a legacy README defining a second standards-index location.

**Disposition:** ARCHIVE under `archive/legacy-structure/standards/` and remove the active `/standards` namespace.

### 3.4 Repository status documents stopped at the Chapter 13 pilot

The following active files contained obsolete production-sequence/status wording:

- `README.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `chapters/README.md`
- `governance/Architecture-Specification.md`
- `governance/Configuration-Management.md`
- `docs/PDS/README.md`
- `docs/PDS/Engineering-Development-Manual.md`

Common stale assumptions included:

- Chapter 13 described only as a future pilot/validation step;
- redevelopment described as ending at Chapter 013;
- `/reviews` and `/archive` missing from active repository structure;
- legacy directories allowed to remain indefinitely;
- Chapter 009 shown in the manuscript index although it was not physically stored under `/chapters`;
- Chapter 013 absent from the chapter index.

**Disposition:** UPDATE.

### 3.5 Authoring templates predate the released PDS

The active files under `templates/` used the earlier Hebrew/LLM-Wiki structure, including retired status fields, `Knowledge Objects`, and evidence conventions that do not match PDS 1.0.

**Disposition:** UPDATE, with the previous templates preserved under `archive/legacy-templates/`.

Current templates are aligned to:

- CDB-first development;
- professional engineering English publication chapters unless explicitly overridden;
- chapter → Investigation → Engineering Asset architecture;
- PDS equation/asset metadata;
- final Standards Validation after authoring;
- PDS evidence and review gates.

### 3.6 Formal review templates still contained pilot-only wording

`reviews/templates/` is valid and useful, but several files still stated that they were pilot artifacts or used pilot-only lessons-learned language.

**Disposition:** UPDATE pilot-only wording while preserving the review architecture validated by Chapter 013.

Chapter-013-specific review records remain unchanged because they are historical evidence of the pilot.

### 3.7 Central Standards Register was incomplete

`references/Standards-Register.md` contained only standards mapped to Chapter 013, although Chapters 009–012 already contain standards in their controlled source registers.

**Disposition:** UPDATE using only standards already documented in repository chapter references. No new normative claims or unverified editions are invented.

## 4. Active documents verified and retained

The following documents remain relevant and are not archived merely because they are not chapter prose:

- `BOOK_STRUCTURE.md` — active working architecture.
- `docs/MASTER-KNOWLEDGE-SCOPE-MAP.md` — atomic recovered knowledge-scope control.
- `docs/HISTORICAL-KNOWLEDGE-SCOPE-RECOVERY.md` — historical recovery evidence and unresolved historical holds.
- `docs/PDS/Engineering-Doctrine.md` — current PDS doctrine.
- `docs/PDS/Quality-and-Validation-Manual.md` — current validation gates.
- `docs/PDS/Style-Guide.md` — current publication/style rules.
- `governance/Definition-of-Ready.md` — current chapter entry gate.
- `governance/Definition-of-Done.md` — current chapter completion gate.
- `governance/README.md` — governance index.
- `assets/README.md` — engineering-asset ID control.
- `docs/PDS/Chapter-Design-Briefs/CDB-013-Polyethylene.md` — controlled Chapter 013 pilot/reference CDB.
- `reviews/chapter-013/*` — controlled historical review evidence for the Chapter 013 pilot.
- chapter-specific `references.md` and `review.md` files — retained as chapter evidence/support records.

## 5. Items deliberately not changed by this audit

### Chapter 013 technical content and PR

Chapter 013 has substantial completed redevelopment work on `chapter-013-redevelopment`, but its content/standards-validation/merge status is a separate controlled technical task. This metadata audit does not silently merge or rewrite it.

### Final chapter numbering

Working Chapters 014+ remain provisional under `BOOK_STRUCTURE.md`. Final TOC, Part names and numbering remain unfrozen until the required coverage and editorial reviews are complete.

### Historical recovery holds

Unrecovered historical titles/numbers remain controlled holds. They are not filled by guesswork during cleanup.

## 6. Repository source-of-truth after cleanup

The active navigation hierarchy is:

1. `README.md` — repository orientation and current status.
2. `BOOK_STRUCTURE.md` — working book architecture and continuation map.
3. `chapters/README.md` — canonical manuscript inventory/status.
4. `docs/PDS/` + `governance/` — development and configuration controls.
5. `references/Standards-Register.md` — central standards index.
6. `reviews/` — engineering-review evidence and review templates.
7. `templates/` — active authoring/support templates.
8. `archive/` — superseded material retained for provenance only.

## 7. Next controlled task after this audit

After repository hygiene is merged:

1. resolve the Chapter 013 redevelopment PR/state;
2. complete authoritative Standards Validation for Chapter 013;
3. complete remaining Chapter 013 publication gates;
4. create CDB-014 under PDS 1.0;
5. begin Working Chapter 014 according to `BOOK_STRUCTURE.md`.
