# Chapter 13 — Controlled Integration and Standards Status

**Record date:** 2026-08-14  
**Chapter:** 013 — Polyethylene (PE)  
**PDS baseline:** 1.0  
**Change class:** B — controlled integration / review-state documentation; no new technical conclusion is created by this record.

## 1. Why this record exists

The historical Chapter 13 development PR (#2) accumulated 79 commits and expanded beyond the Chapter 13 scope, including substantial rewrites to Chapters 000–012. After repository hygiene was baselined, direct merge of that PR would therefore import unrelated technical changes and conflict with the PDS Human Approval Gate.

The controlled recovery strategy is to use a clean branch from current `main` and transfer only the mature consolidated Chapter 13 manuscript plus the active evidence required to understand its review state.

## 2. Clean-integration scope

Included in the active Chapter 13 candidate:

- `chapters/chapter-013-polyethylene/chapter.md` — consolidated manuscript from the historical redevelopment branch;
- `chapters/chapter-013-polyethylene/references.md` — current source/evidence register and standards holds;
- `chapters/chapter-013-polyethylene/review.md` — consolidated PDS review record;
- `reviews/chapter-013/ACADEMIC-EVIDENCE-REVIEW-2026-08-14.md` — primary-research claim review;
- `reviews/chapter-013/EDITORIAL-STYLE-REVIEW-2026-08-14.md` — editorial/style/navigation review;
- this integration/status record.

Not imported from the historical branch:

- unrelated Chapter 000–012 rewrites;
- intermediate `Batch-*` authoring files;
- intermediate `Integration-Pass-*` files;
- temporary pre-review artifacts;
- empty book-wide placeholder documents;
- duplicate working files that do not need to remain in the active repository.

Those materials remain available through Git history and the historical PR for provenance.

## 3. Current maturity statement

Chapter 13 has reached the following controlled state:

- engineering redevelopment: **complete for the approved CDB scope**;
- Investigations 1–10: **integrated**;
- Technical Review: **PASS** based on historical review evidence;
- equations / units / worked-example arithmetic: **PASS** based on historical review evidence;
- standards architecture and current public ISO edition/scope status: **PASS / rechecked 2026-08-14**;
- authoritative clause/table/equation validation: **OPEN — controlled full-text holds**;
- Academic/Evidence Review: **PASS for the current core claim set**;
- Editorial/Style Review: **CONDITIONAL PASS — no structural rewrite required**;
- final claim-level citation placement / metadata synchronization: **OPEN bounded editorial actions**;
- Publishing visual completion: **OPEN where final figures are required**;
- Design Freeze: **not permitted while the authoritative standards holds remain open**.

## 4. Current official standards status — public-source check

The 2026-08-14 official ISO public-source check confirms the following current published framework relevant to Chapter 13:

- ISO 9080:2012 remains the published/confirmed long-term hydrostatic statistical-extrapolation standard.
- ISO 12162:2009 remains the published/confirmed thermoplastics classification/designation/design-stress-method standard.
- ISO 4427-1:2019 and ISO 4427-2:2019 remain the current published water/pressure-drainage PE standards path; ISO 4427-2 has Amendment 1:2023 and replacement work is in development.
- ISO 4437-1:2024 remains the current published gas-system Part 1 while replacement work is in development; its public scope establishes the gas-system application envelope and routes elevated-temperature treatment to the applicable system framework.
- ISO 4437-5:2024 remains the current published fitness-for-purpose standard for assembled PE gas systems and their joints.
- ISO 21307:2017 with Amendment 1:2020 remains the current PE butt-fusion procedure standard.
- ISO 13479:2022 and ISO 18488:2025 remain current published SCG-related test-method references for different test concepts used in the chapter.

This status check does not substitute for the current full normative text where exact clauses, tables, equations, coefficients, marking requirements or acceptance rules are required.

## 5. Academic / Evidence Review closure

The Chapter 13 core non-normative material/mechanism claim set was reviewed against directly checked primary research on 2026-08-14.

The evidence package supports, with explicit transferability limits:

- morphology / branching / tie-molecule influence on SCG;
- amorphous-phase mobility and craze-fibril mechanisms;
- time- and temperature-dependent HDPE creep response;
- long-term plasticity-controlled PE100 behaviour;
- ductile/creep-controlled to SCG failure transition;
- notch/local-defect relevance;
- cyclic crack-growth / SCG interaction under tested HDPE pipe conditions.

The review is recorded in `ACADEMIC-EVIDENCE-REVIEW-2026-08-14.md`. Academic literature remains supporting evidence and does not replace the governing ISO framework.

## 6. Editorial / Style Review closure

The consolidated manuscript was reviewed against the active PDS 1.0 Style Guide.

**Result:** no structural rewrite is required. Investigation hierarchy, navigation, asset IDs, worked examples, cross-references, tone, uncertainty language and authoring-stage visual placeholders are suitable for controlled integration.

Bounded open editorial actions remain:

- final claim-level academic citation placement;
- front-matter status/date synchronization;
- final publishing visual production where required;
- source-dependent terminology (`σ_LCL`, lower prediction/confidence wording and final pressure terminology) after full-text Standards Validation.

The review is recorded in `EDITORIAL-STYLE-REVIEW-2026-08-14.md`.

## 7. Full-text standards blocker

A search of the available repository, current conversation files and user Library did **not** locate lawful full current copies of the key normative editions needed to close the remaining clause-level holds.

Older ISO 9080:2003 and ISO 12162:1995 material exists in historical project context, but both editions are withdrawn and are retained only as conceptual/provenance evidence.

Project literature reviews and secondary technical reports contain numerical interpretations of some standards. They are not used to close normative claims.

Therefore the remaining full-text standards items are recorded as a **source-access hold**, not silently guessed or marked complete.

The active hold IDs are maintained in `chapters/chapter-013-polyethylene/references.md` as `SVH-013-01` through `SVH-013-05`.

## 8. Historical PR #2 disposition

PR #2 has been **closed without merge** and explicitly superseded as an integration vehicle by clean PR #8.

It remains valuable as development provenance. Its Chapter 13 manuscript was preserved through the consolidated source blob carried into the clean integration branch; its unrelated Chapter 000–012 rewrites are not imported.

## 9. Current controlled gate

PR #8 is the sole active Chapter 13 integration path.

It shall remain a Draft technical-content PR until author review/approval. Approval and merge would make Chapter 13 the active **standards-validation candidate** on `main`; it would **not** label the chapter publication-ready and would **not** close the full-text ISO holds.

Final Design Freeze remains a later gate after the authoritative standards holds and bounded publication actions are closed.