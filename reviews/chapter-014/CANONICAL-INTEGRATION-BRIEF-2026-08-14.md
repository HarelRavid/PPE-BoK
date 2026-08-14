# Chapter 014 — Canonical Integration Brief

**Date:** 2026-08-14  
**Repository:** `HarelRavid/PPE-BoK`  
**Target branch:** `chapter-014-engineering-development`  
**Target PR:** #12  
**Change class:** controlled mechanical manuscript integration  
**Technical judgement required during execution:** **NONE — follow this brief exactly**

## 1. Purpose

Integrate the already authored and reviewed Investigation 9 and Investigation 10 temporary files into the canonical Chapter 014 manuscript without adding, removing or materially rewriting approved technical content.

The integration must also apply the bounded findings already approved by:

- `reviews/chapter-014/INVESTIGATION-009-AUTHORING-REVIEW-2026-08-14.md`;
- `reviews/chapter-014/INVESTIGATION-010-AND-CHAPTER-CLOSURE-REVIEW-2026-08-14.md`;
- `reviews/chapter-014/PRE-INTEGRATION-TECHNICAL-REVIEW-2026-08-14.md`;
- `reviews/chapter-014/STANDARDS-AND-EVIDENCE-VALIDATION-2026-08-14.md`;
- `reviews/chapter-014/PRE-INTEGRATION-EDITORIAL-STYLE-REVIEW-2026-08-14.md`.

This brief exists because the current connected GitHub write interface supports whole-file replacement but not safe partial patching of a large canonical manuscript. The hold is mechanical, not technical.

## 2. Authoritative input files

Use the branch versions of exactly these files:

1. `chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/chapter.md`
2. `chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/investigation-009-authoring.md`
3. `chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/investigation-010-authoring.md`
4. `chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/technical-outline.md`
5. `chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/review.md`
6. `chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/references.md`
7. `docs/PDS/Chapter-Design-Briefs/CDB-014-Atomic-Structure-Chemical-Bonding-Carbon-Chemistry.md`

Do not use old chat text, old branch snapshots or generated reconstructions if the branch file is available.

## 3. Pre-execution safety checks

Before editing:

1. `git status --short` must be clean.
2. Current branch must be exactly `chapter-014-engineering-development`.
3. Fetch remote refs.
4. Record current branch HEAD SHA in the execution report.
5. Do not switch to or modify `main`.
6. Confirm both temporary authoring files exist.
7. Confirm canonical `chapter.md` currently contains exactly one Investigation 9 placeholder and one Investigation 10 placeholder.
8. Confirm the branch does not currently contain `.github/workflows/chapter014-canonical-integration.yml`.

If any of these checks fail, STOP and report the mismatch. Do not improvise.

## 4. Canonical integration boundary

The canonical `chapter.md` currently contains completed Investigations 1–8 followed by development placeholders for Investigations 9–10.

The integration shall:

1. retain the existing canonical Chapter 014 content from the beginning of `chapter.md` through the end of Investigation 8;
2. remove the old Investigation 9 and 10 placeholder/development-hold content;
3. insert the approved Investigation 9 authoring candidate;
4. insert the approved Investigation 10 / chapter-closure authoring candidate;
5. normalize heading levels so both read as normal Investigations within `chapter.md`;
6. add/synchronize the final Chapter 014 engineering-asset register and publication hold points;
7. remove the two temporary authoring files only after successful verification.

No new technical example or claim may be introduced.

## 5. Mandatory technical findings to apply

### TR-014-01 — Claim Class vs evidence Level disambiguation

In Investigation 1, replace the three statement classes:

- `Level 1 — Chemistry fact`
- `Level 2 — Mechanism hypothesis`
- `Level 3 — Engineering conclusion`

with:

- **Claim Class A — Chemistry fact**
- **Claim Class B — Mechanism hypothesis**
- **Claim Class C — Engineering conclusion**

Change:

> `Never jump directly from Level 1 to Level 3.`

to:

> `Never jump directly from Claim Class A to Claim Class C.`

Also update nearby prose referring to `make Level 1 accurate and Level 2 useful` / `reach Level 3` to use Claim Classes A/B/C.

Reserve `Level 1–6` exclusively for the final Investigation 10 PPE-BoK evidence ladder.

### TR-014-02 — FIG-014-002 terminology

Preserve asset ID `FIG-014-002` but rename it everywhere in active Chapter 014 files to:

> **Primary Bonding and Noncovalent Interaction Map**

Do not use `Primary and secondary bonding map` as the controlled title.

### TR-014-03 / E10-01 — evidence ladder is non-normative

Immediately before the Investigation 10 six-level evidence ladder, add:

> **PPE-BoK framework:** The following levels are a PPE-BoK reasoning framework for controlling evidence transfer; they are not a normative classification defined by a single standard.

Keep this adjacent to the ladder.

### TR-014-04 — Investigation 9 transferability controls

Apply all three:

1. processing history is an input/confounder, not itself a molecular feature;
2. in Case B, do not imply free volume was independently measured in every membrane; use wording such as `density / packing / morphology / free-volume interpretation` where the evidence supports it;
3. distinguish `same polymer family / nominal chemistry` from `identical material state`.

Do not broaden the evidence set beyond Cases A–C and S014-009 through S014-012.

## 6. Controlled asset-identity corrections

### 6.1 TAB-014-002 duplicate

Investigation 6 currently contains an early teaching table labeled `TAB-014-002`.

The final controlled `TAB-014-002` belongs to Investigation 9.

Therefore:

- retain the Investigation 6 table content;
- remove the controlled asset number from the Investigation 6 heading;
- title it as a **preliminary teaching table**;
- ensure exactly one final `TAB-014-002` remains, in Investigation 9.

### 6.2 WF-014-001 duplicate/provisional version

Investigation 9 contains a first/provisional `WF-014-001` sequence.

Investigation 10 owns the final controlled `WF-014-001`.

Therefore:

- do not keep two assets named `WF-014-001`;
- retain the Investigation 9 reasoning sequence as an unnumbered workflow checkpoint/evidence-chain summary;
- retain the final controlled `WF-014-001 — Chemical structure to engineering decision boundary` in Investigation 10.

### 6.3 FIG-014-006 development vs final specification

Investigation 9 may retain evidence-chain design requirements for `FIG-014-006`, but Investigation 10 contains the final scientific specification.

Make the distinction explicit so the reader does not see two separate final figures with the same ID.

## 7. Investigation 9 integration rules

Integrate the approved candidate without changing its evidence scope.

It must retain:

- the structure→hypothesis→measurement→confounder→transferability→qualification logic;
- `TAB-014-002`;
- Cases A–C only;
- `TAB-014-003`;
- `EX-014-002`;
- evidence-chain / FIG-014-006 development requirements;
- verification questions;
- common mistakes / Failure Lens;
- final engineering decision / handoff to Investigation 10.

Explicitly prohibited during integration:

- adding another polymer case;
- adding a new numerical property value;
- ranking commercial materials;
- turning membrane/coupon data into pipe-wall design data;
- removing transferability limitations for PA6 / fluoropolymer membrane / PFA processing studies.

## 8. Investigation 10 integration rules

Integrate the approved candidate and preserve:

- chemistry as mechanism/evidence filter rather than product certificate;
- the six-level PPE-BoK evidence ladder;
- the stop-rule;
- final `FIG-014-006` two-track scientific-reasoning / engineering-qualification specification;
- final `WF-014-001`;
- `CL-014-001`;
- `TAB-014-004`;
- first-principles + qualification complementarity;
- final Desk Test;
- engineering decision;
- chapter closure and handoff to Working Chapter 015.

Do not present the six-level ladder as an ISO/IUPAC/industry-standard taxonomy.

## 9. Final canonical asset register

At the end of `chapter.md`, synchronize at minimum:

| ID | Controlled disposition after integration |
|---|---|
| FIG-014-001 | Atom-to-material hierarchy — scientific placeholder / final graphic pending |
| FIG-014-002 | Primary Bonding and Noncovalent Interaction Map — scientific specification complete / graphic pending |
| FIG-014-003 | Carbon hybridization and geometry — scientific specification complete / graphic pending |
| FIG-014-004 | Sigma and pi bonding in ethene — scientific specification complete / graphic pending |
| FIG-014-005 | Ethene to polyethylene bridge — scientific specification complete / graphic pending |
| FIG-014-006 | Molecular feature to engineering evidence chain — final scientific specification integrated / graphic pending |
| TAB-014-001 | Integrated |
| TAB-014-002 | Integrated once, in Investigation 9 |
| TAB-014-003 | Integrated |
| TAB-014-004 | Integrated |
| EX-014-001 | Integrated |
| EX-014-002 | Integrated |
| WF-014-001 | Final version integrated once, in Investigation 10 |
| CL-014-001 | Integrated |

Final graphic production is not part of this integration task.

## 10. Publication hold section

Retain/add a clear closing hold section stating that Engineering Development completion does not imply publication readiness.

At minimum retain holds for:

- final full-file Technical Review;
- final claim-level Standards/Evidence validation;
- ISO 472 / ISO 1043-1 lifecycle recheck before publication freeze;
- exact IUPAC term/version capture;
- Investigation 8 nomenclature recheck;
- Investigation 9 primary-study claim/citation adjacency audit;
- final Editorial / Style Review;
- continuous-manuscript Desk Test;
- final publishing figures;
- Human Approval Gate;
- synchronization with current `main` and controlled merge.

## 11. Supporting-file synchronization

### `technical-outline.md`

Update the disposition so it no longer says Investigation 1 may now be authored.

Record:

- Investigations 1–10 authored;
- Investigation 9 evidence gate PASS;
- Investigation 9 authoring review PASS;
- Investigation 10 / chapter closure review PASS;
- pre-integration Technical Review CONDITIONAL PASS;
- TR-014-01 through TR-014-04 applied;
- canonical integration complete;
- next gate = final full-file Technical Review.

### `review.md`

Add an integration checkpoint recording:

- approved Investigation 9/10 candidates integrated;
- TR-014-01 through TR-014-04 applied;
- final full-file Technical Review is next;
- Standards/Evidence publication pass, final Editorial/Style, Human Approval and merge remain open.

### CDB

Only synchronize the controlled FIG-014-002 title if needed.

**Do not change CDB scope or reopen the approved Design Brief.**

### `references.md`

Do not add technical sources unless required to correct an existing factual error. No new evidence is required for this mechanical integration.

## 12. Delete temporary authoring files

Delete only after canonical integration and assertions pass:

- `chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/investigation-009-authoring.md`
- `chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/investigation-010-authoring.md`

The review records remain permanently for provenance.

## 13. Mandatory validation assertions

Before commit, verify all of the following:

1. `git diff --check` passes.
2. Exactly one `# Investigation 9 —` exists in canonical `chapter.md`.
3. Exactly one `# Investigation 10 —` exists.
4. No Investigation 9/10 `Authoring state: BLOCKED` / planned placeholder remains.
5. `Claim Class A — Chemistry fact` exists.
6. `Never jump directly from Claim Class A to Claim Class C` exists.
7. The six-level ladder contains the explicit `PPE-BoK framework` non-normative note.
8. The Investigation 6 table is not numbered `TAB-014-002`.
9. Exactly one final `TAB-014-002` exists in Investigation 9.
10. Exactly one final `WF-014-001` exists in Investigation 10.
11. `FIG-014-002` controlled title is `Primary Bonding and Noncovalent Interaction Map`.
12. Both temporary authoring files are deleted.
13. No new material-specific case or numerical piping acceptance value has been introduced.
14. Chapters 000–013 are untouched.
15. No standards PDFs or copyrighted source files are added.

If any assertion fails, do not commit until the integration is corrected using only the approved content/findings.

## 14. Required diff review

Before push, inspect:

```text
git status --short
git diff --check
git diff --stat
git diff -- chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/chapter.md
git diff -- chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/technical-outline.md
git diff -- chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/review.md
git diff -- docs/PDS/Chapter-Design-Briefs/CDB-014-Atomic-Structure-Chemical-Bonding-Carbon-Chemistry.md
```

Confirm that no unrelated file is modified.

## 15. Commit / stop rule

Use one atomic commit with a title equivalent to:

`Integrate Chapter 014 Investigations 9-10 canonically`

Push only to:

`chapter-014-engineering-development`

Do **not**:

- mark PR #12 Ready;
- merge PR #12;
- modify `main`;
- start Chapter 015;
- declare Technical Review PASS;
- declare publication Standards/Evidence PASS;
- declare Design Freeze.

STOP after push and report:

- starting HEAD;
- resulting HEAD;
- changed files;
- insertions/deletions;
- assertion results;
- any deviation from this brief.

The next activity after a clean integration is the **final full-file Chapter 014 Technical Review**.
