# Chapter 015 — Canonical Integration Brief

**Date:** 2026-08-15  
**Branch:** `chapter-015-engineering-development`  
**Task type:** controlled mechanical integration only  
**Technical authoring status:** Investigations 1–10 complete; pre-integration review cycle complete  
**Human Approval:** NOT YET AUTHORIZED  
**PR merge:** NOT AUTHORIZED

## 1. Purpose

Integrate the reviewed Investigation 2–10 controlled candidates into the canonical Chapter 015 manuscript and absorb the controlled 2026 terminology/evidence updates into the canonical chapter support files.

This task is mechanical. It is **not** an invitation to research, rewrite, expand, simplify scientific claims, add examples, change evidence conclusions or begin Chapter 016.

## 2. Authoritative integration inputs

Read before executing:

1. `docs/PDS/Chapter-Design-Briefs/CDB-015-Polymerization-Catalysts-Process-Structure.md`
2. `chapters/chapter-015-from-monomer-to-polymer/chapter.md`
3. `chapters/chapter-015-from-monomer-to-polymer/technical-outline.md`
4. `chapters/chapter-015-from-monomer-to-polymer/references.md`
5. `chapters/chapter-015-from-monomer-to-polymer/review.md`
6. `reviews/chapter-015/PRE-INTEGRATION-TECHNICAL-REVIEW-2026-08-15.md`
7. `reviews/chapter-015/STANDARDS-AND-EVIDENCE-VALIDATION-2026-08-15.md`
8. `reviews/chapter-015/PRE-INTEGRATION-EDITORIAL-STYLE-DESK-REVIEW-2026-08-15.md`
9. `reviews/chapter-015/TERMINOLOGY-CLASSIFICATION-UPDATE-2026-08-15.md`
10. `chapters/chapter-015-from-monomer-to-polymer/references-addendum-2026-08-15.md`
11. Investigation candidate files `investigation-002-authoring.md` through `investigation-010-authoring.md`.
12. `tools/chapter015_canonical_integrate.py`.

## 3. Required repository preconditions

Before running the integration script:

- repository must be `HarelRavid/PPE-BoK`;
- branch must be exactly `chapter-015-engineering-development`;
- fetch origin first;
- local branch must contain the current remote branch without rebase/reset/history rewrite;
- working tree must be clean;
- record the pre-integration HEAD SHA;
- PR #15 must remain open, Draft and unmerged;
- do not merge `main` as part of the integration task unless explicitly instructed after the integration review; current synchronization is a separate final-closure action.

If any precondition is false, STOP and report it.

## 4. Controlled integration method

Run the one-shot script from repository root.

### Dry run

```bash
python tools/chapter015_canonical_integrate.py
```

Expected:

- `Chapter 015 canonical integration validation: PASS`;
- dry-run statement confirming no changes;
- canonical writes listed;
- temporary files listed for deletion.

If the dry run fails, STOP. Do not patch around an assertion without returning the failure for review.

### Apply

```bash
python tools/chapter015_canonical_integrate.py --apply
```

Expected:

- integration validation PASS;
- five canonical files updated:
  - `chapters/chapter-015-from-monomer-to-polymer/chapter.md`;
  - `chapters/chapter-015-from-monomer-to-polymer/references.md`;
  - `chapters/chapter-015-from-monomer-to-polymer/technical-outline.md`;
  - `chapters/chapter-015-from-monomer-to-polymer/review.md`;
  - `docs/PDS/Chapter-Design-Briefs/CDB-015-Polymerization-Catalysts-Process-Structure.md`;
- Investigation 2–10 temporary candidate files deleted;
- `references-addendum-2026-08-15.md` deleted;
- one-shot script deleted, or explicitly delete it manually if the script reports a self-delete warning.

## 5. Scientific / terminology changes that ARE authorized

Only the bounded pre-reviewed changes below are authorized during integration.

### TR015-01 / ED015-01 — 2026 IUPAC classification update

Canonical wording shall use:

- `step polymerization`;
  - additive step polymerization = polyaddition;
  - condensative step polymerization = polycondensation;
- `chain polymerization`;
  - additive chain polymerization;
  - condensative chain polymerization.

This is the already-reviewed post-CDB source update, not a new scope change.

### TR015-02 — Investigation 5 title

Canonical title:

`How Does Step Polymerization Build Macromolecules, and What Distinguishes Additive from Condensative Step Growth?`

### TR015-03 / TR015-04 — asset ownership

- one final `FIG-015-001` only; Investigations 2/5 contribute to it;
- one final `FIG-015-004` only; Investigations 6–8 contribute to it;
- final asset ownership is consolidated in Investigation 10 / chapter closure.

### TR015-05 — supporting tables

Do not create duplicate formal table IDs outside TAB-015-001..005.

### TR015-06 / ED015-02 — molar-mass language

Prefer `molar mass` in canonical prose while preserving original publication titles and familiar `MWD` language where intentionally used.

Do not perform a broad wording rewrite merely to chase terminology style if the script has not encoded it; final Editorial Review may identify any remaining bounded normalization.

### TR015-07 — `single-site`

Retain as descriptive/industrial language requiring definition/evidence; do not promote it to an IUPAC formal classification.

## 6. Changes that are NOT authorized

Do not:

- add a new catalyst/material/process case;
- add a new paper/source;
- add a Carothers equation;
- add a generic radical-polymerization rate equation;
- add numerical process-design values;
- generalize hydrogen, temperature, comonomer-feed, residence-time or support effects;
- change any S015-009..016 supported/unsupported conclusion;
- rank Ziegler–Natta versus metallocene technology;
- convert catalyst/process information into SCG/RCP/fusion/pressure/lifetime claims;
- edit Chapters 000–014;
- start Chapter 016;
- rebase/reset/amend/force-push;
- merge PR #15.

## 7. Required post-apply validation

Run at minimum:

```bash
git status --short
git diff --stat
git diff --name-status
git diff --check
```

Then verify content invariants. The script already checks many of these, but they must also be inspected from the repository state:

1. Investigation headings 1–10 exist exactly once in canonical `chapter.md`.
2. No stale `planned`, `controlled candidate`, or Investigation 9 `BLOCKED` authoring state remains in canonical manuscript.
3. `chapter.md` contains current step/chain hierarchy.
4. `references.md` contains S015-008 through S015-016.
5. CDB contains the post-approval S015-008 update.
6. Technical Outline no longer says step-growth is only explanatory/non-formal.
7. `review.md` says Engineering Development COMPLETE and final integrated reviews pending.
8. Temporary Investigation 2–10 files are gone.
9. Temporary references addendum is gone.
10. integration script is gone.
11. final canonical manuscript remains under `chapters/chapter-015-from-monomer-to-polymer/chapter.md`.
12. no Chapters 000–014 files changed.
13. no Chapter 016 file created/changed.

If `git diff --check` reports Markdown hard-break double spaces, distinguish intentional Markdown hard breaks from accidental whitespace and report them. Do not rewrite technical prose merely to make a whitespace checker silent.

## 8. Atomic commit

If all validations pass, create **one atomic integration commit** with subject:

```text
Integrate Chapter 015 canonically
```

Do not squash earlier chapter history, amend or rebase.

Push normally to:

`origin/chapter-015-engineering-development`

If authentication prevents push:

- do not recreate the commit;
- do not alter it;
- create/export a Git bundle and a format-patch for the exact integration commit;
- report exact local SHA, parent SHA, tree SHA, changed-file list and bundle/patch paths;
- STOP.

## 9. Expected post-integration gate state

After the integration commit is remote (or the exact commit is exported if push is unavailable):

- Engineering Development: COMPLETE;
- canonical integration: COMPLETE;
- final full-file Technical Review: PENDING;
- final claim-level Standards/Evidence Review: PENDING;
- final Editorial/Style + continuous Desk Test: PENDING;
- Human Approval: PENDING;
- PR #15: Draft / NOT MERGED;
- Chapter 016: NOT STARTED.

## 10. Stop rule

STOP after the integration commit/push or exact commit export.

Do not perform final technical/editorial review on behalf of the Lead Engineer and do not merge the PR.