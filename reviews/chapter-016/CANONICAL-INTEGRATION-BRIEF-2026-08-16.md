# Chapter 016 — Canonical Integration Brief

**Date:** 2026-08-16  
**Chapter:** 016 — Polymer Chain Architecture: Molar Mass, Distribution, Branching and Crosslinking  
**Disposition:** **MECHANICAL INTEGRATION AUTHORIZED — NO SCIENTIFIC REWRITE**

## 1. Purpose

Integrate the reviewed Investigation 2–10 authoring candidates into the canonical Chapter 016 manuscript and evidence register in one controlled mechanical step.

This brief is the authoritative integration contract. The implementation engineer shall not research, rewrite, improve or expand the scientific content.

## 2. Authoritative inputs

Canonical files:

- `chapters/chapter-016-polymer-chain-architecture/chapter.md` — canonical Investigation 1 plus a provisional earlier Investigation 2 insertion;
- `chapters/chapter-016-polymer-chain-architecture/references.md` — S016-001..012 plus final pre-integration gate/status metadata;
- `chapters/chapter-016-polymer-chain-architecture/technical-outline.md`;
- `chapters/chapter-016-polymer-chain-architecture/review.md`.

Controlled candidates:

- `investigation-002-authoring.md` through `investigation-010-authoring.md`;
- `references-addendum-2026-08-16.md` containing S016-013 through S016-016 canonical source-entry candidates.

**Investigation 2 configuration rule:** `investigation-002-authoring.md` is the reviewed authoritative integration candidate. The provisional Investigation 2 already present in `chapter.md` must be **replaced**, not appended or duplicated. Canonical Investigation 1 remains the preserved manuscript base.

Review controls:

- `PRE-INTEGRATION-TECHNICAL-REVIEW-2026-08-16.md`;
- `STANDARDS-AND-EVIDENCE-VALIDATION-2026-08-16.md`;
- `PRE-INTEGRATION-EDITORIAL-STYLE-DESK-REVIEW-2026-08-16.md`;
- Investigation 2–10 gate/review records.

One-shot tool:

- `tools/chapter016_canonical_integrate.py`.

## 3. Required integration actions

1. Preserve canonical Investigation 1 unchanged except for bounded frontmatter status normalization.
2. Remove the provisional canonical Investigation 2 section by cutting the manuscript at the first top-level `# Investigation 2 —` heading; then insert the reviewed `investigation-002-authoring.md` candidate exactly once.
3. Insert reviewed Investigations 3–10 in numerical order, exactly once each.
4. Preserve candidate technical wording and evidence boundaries.
5. Insert S016-013 through S016-016 into canonical `references.md` before the Investigation-specific evidence plan.
6. Preserve the canonical primary-evidence register stating **PASS FOR S016-013 THROUGH S016-016 ONLY**; new named cases remain gated.
7. Change the evidence-register disposition from `S016-013..016 PENDING MECHANICAL ABSORPTION` to `S016-013..016 INTEGRATED; FINAL CLAIM-LEVEL REVIEW PENDING`.
8. Normalize canonical manuscript frontmatter: equations PASS, units PASS, examples PASS; final terminology/standards/editorial review remains pending/active until post-integration review.
9. Update `review.md` to Engineering Development COMPLETE, canonical integration COMPLETE, final integrated reviews PENDING and Human Approval PENDING.
10. Retain `technical-outline.md` as the synchronized development outline; no scientific rewrite is needed.
11. Delete temporary Investigation 2–10 candidates and the evidence addendum only after successful validation.
12. Delete `tools/chapter016_canonical_integrate.py` after validation and before the atomic integration commit.

## 4. Technical findings that must remain closed

Apply/preserve TR016-01 through TR016-08:

- exact candidate integration, with candidate Investigation 2 replacing the provisional canonical Investigation 2;
- S016-013..016 absorption;
- current metadata;
- controlled molar-mass notation;
- unqualified `chain length` ambiguity control;
- unique formal asset ownership;
- bounded S016-013..016 evidence cases only;
- temporary artifact cleanup.

## 5. Editorial findings that must remain closed

Apply/preserve ED016-01 through ED016-07:

- current-state metadata;
- `molar mass / MMD / M_m ≡ M_w / Đ_M` convention;
- acronym clarity is a **post-integration continuous-file review check**, not authorization for mechanical prose rewriting;
- one final formal asset label per ID;
- evidence limitations adjacent to S016-013..016 cases;
- no duplicated generic warnings caused only by file seams;
- Chapter 017 handoff remains `architecture → crystallization/packing possibilities`, not guaranteed morphology.

Mechanical integration shall not paraphrase evidence cases merely to shorten them.

## 6. Required post-integration invariants

### 6.1 Investigation structure

Canonical `chapter.md` must contain exactly one top-level heading for each Investigation 1–10. The final Investigation 2 text must originate from `investigation-002-authoring.md`, not the provisional pre-integration section.

### 6.2 Source register

Canonical `references.md` must contain exactly one source heading each for S016-013, S016-014, S016-015 and S016-016 and must retain the bounded Investigation 9 gate.

### 6.3 Formal assets

Canonical `chapter.md` must contain exactly one formal heading/specification for:

- FIG-016-001 through FIG-016-006;
- TAB-016-001 through TAB-016-005;
- EX-016-001 through EX-016-003;
- WF-016-001;
- CL-016-001.

### 6.4 Evidence controls

The integrated manuscript must retain:

- `molar mass` as controlled dimensional wording;
- `relative molecular mass` as dimensionless;
- `M_m ≡ M_w` controlled symbol relationship;
- `Đ_M` terminology;
- `chain length` ambiguity warning;
- conventional/universal SEC versus SEC-LS boundaries;
- ISO 18177 material/scope limits;
- ISO 10147 gel-content limits;
- entanglement versus covalent-crosslink distinction;
- S016-013..016 `supported / unsupported / transferability` case boundaries.

### 6.5 No downstream shortcut

No integration change may create a direct acceptance rule from molar mass/MMD/dispersity, SCB/LCB, gel content, entanglement, MFR/MVR or density to pressure rating, lifetime, SCG qualification, permeability acceptance, fusion qualification or service suitability.

### 6.6 Configuration scope

- Chapters 000–015 must be untouched.
- Chapter 017 must not be created or modified.
- CDB-016 technical scope must not be changed.
- No new source/case may be introduced.

## 7. Temporary artifacts to remove

Only after successful integration validation:

- `chapters/chapter-016-polymer-chain-architecture/investigation-002-authoring.md` through `investigation-010-authoring.md`;
- `chapters/chapter-016-polymer-chain-architecture/references-addendum-2026-08-16.md`;
- `tools/chapter016_canonical_integrate.py`.

Review/provenance records remain in `reviews/chapter-016/`.

## 8. Git control

The integration implementation shall:

- begin from the exact remote branch head specified in the execution prompt;
- use no rebase/reset/amend/force-push;
- create one atomic integration commit after all assertions pass;
- push normally if credentials are available;
- otherwise export the exact single commit as Git bundle + format-patch and stop.

## 9. Precondition control

The exact expected remote branch SHA is **not hard-coded in this brief**. The Lead Engineer shall supply the fresh SHA in the Claude execution prompt immediately before execution. If the remote branch has moved from that supplied SHA, STOP rather than integrating on an unreviewed state.

No further pre-integration technical/content edits are authorized after the fresh SHA is supplied. If the branch moves, the integration must be re-authorized against the new head.

## 10. Post-integration gates

Mechanical integration does not close the chapter.

After integration, the Lead Engineer must independently perform:

1. Final Full-File Technical Review;
2. Final Claim-Level Standards/Evidence Review;
3. Final Editorial / Style Review + continuous Desk Test;
4. branch/main synchronization check;
5. explicit Human Approval Gate.

Do not merge PR #17 or start Chapter 017 during this mechanical task.
