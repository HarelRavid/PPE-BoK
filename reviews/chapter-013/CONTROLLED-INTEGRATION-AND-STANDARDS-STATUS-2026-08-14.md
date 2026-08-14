# Chapter 13 — Controlled Integration and Standards Status

**Record date:** 2026-08-14  
**Chapter:** 013 — Polyethylene (PE)  
**PDS baseline:** 1.0  
**Change class:** B — controlled integration / review-state documentation; no new technical conclusion is created by this record.

## 1. Why this record exists

The historical Chapter 13 development PR (#2) accumulated 79 commits and expanded beyond the Chapter 13 scope, including substantial rewrites to Chapters 000–012. After repository hygiene was baselined, direct merge of that PR would therefore import unrelated technical changes and conflict with the PDS Human Approval Gate.

The approved recovery strategy is to create a clean branch from current `main` and transfer only the mature consolidated Chapter 13 manuscript plus the minimum active evidence required to understand its review state.

## 2. Clean-integration scope

Included in the active Chapter 13 candidate:

- `chapters/chapter-013-polyethylene/chapter.md` — consolidated manuscript from the historical redevelopment branch;
- `chapters/chapter-013-polyethylene/references.md` — current source/evidence register and standards holds;
- `chapters/chapter-013-polyethylene/review.md` — consolidated PDS review record;
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

- engineering redevelopment: complete for the approved scope;
- Investigations 1–10: integrated;
- Technical Review: pass based on historical review evidence;
- equations / units / worked-example arithmetic: pass based on historical review evidence;
- standards architecture and current public ISO edition/scope status: rechecked 2026-08-14;
- authoritative clause/table/equation validation: open controlled holds;
- academic evidence normalization: open;
- editorial review: open;
- Design Freeze: not permitted.

## 4. Current official standards status — public-source check

The 2026-08-14 official ISO public-source check confirms the following current published framework relevant to Chapter 13:

- ISO 9080:2012 remains the published/confirmed long-term hydrostatic statistical-extrapolation standard.
- ISO 12162:2009 remains the published/confirmed thermoplastics classification/designation/design-stress-method standard.
- ISO 4427-1:2019 and ISO 4427-2:2019 remain the current published water/pressure-drainage PE standards path; ISO 4427-2 has Amendment 1:2023 and replacement work is in development.
- ISO 4437-1:2024 remains the current published gas-system Part 1 and is expected to be replaced by an Edition 3 FDIS; the published standard exposes MOP up to 10 bar at 20 °C reference and an operating range of −20 °C to 40 °C, with 20–40 °C derating routed to ISO 4437-5.
- ISO 4437-5:2024 remains the current published fitness-for-purpose standard for assembled PE gas systems and their joints.
- ISO 21307:2017 with Amendment 1:2020 remains the current PE butt-fusion procedure standard.
- ISO 13479:2022 and ISO 18488:2025 remain current published SCG-related test-method references for the different test concepts used in the chapter.

This status check does not substitute for the current full normative text where exact clauses/tables/equations/acceptance rules are required.

## 5. Full-text standards blocker

A search of the available repository, current conversation files and user Library did **not** locate lawful full current copies of the key normative editions needed to close the remaining clause-level holds.

Older ISO 9080:2003 and ISO 12162:1995 material exists in historical project context, but both editions are withdrawn and are retained only as conceptual/provenance evidence.

Project literature reviews and secondary technical reports contain numerical interpretations of some standards. They are not used to close normative claims.

Therefore the remaining full-text standards items are recorded as a **source-access hold**, not silently guessed or marked complete.

## 6. Historical PR #2 disposition

PR #2 is superseded as an integration vehicle because its diff is no longer limited to Chapter 13 and it is materially diverged from current `main`.

It remains valuable as development provenance. Once the clean Chapter 13 integration PR is opened, PR #2 should be closed with a supersession note rather than merged.

## 7. Next controlled gate

The clean Chapter 13 PR should receive author review as a technical-content integration PR.

After approval and merge, Chapter 13 will become the active **standards-validation candidate** on `main`, while the full-text ISO holds continue to block final Design Freeze. Those holds can be closed later when the applicable current normative texts are lawfully available.
