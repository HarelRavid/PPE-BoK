# Chapter 015 — Investigation 2 Authoring Review

**Date:** 2026-08-15  
**Investigation:** 2 — What Does “Polymerization” Actually Mean, and How Should the Reactions Be Classified?  
**Candidate:** `chapters/chapter-015-from-monomer-to-polymer/investigation-002-authoring.md`  
**Disposition:** **PASS — AUTHORIZE INVESTIGATION 3**

## 1. Review basis

The terminology gate was re-run against the current authoritative source set rather than relying only on the Chapter 015 planning snapshot.

Primary controlling source identified during this review:

- **S015-008** — Farrell et al., _Basic classification and definitions of polymerization reactions (IUPAC recommendations 2025)_, Pure and Applied Chemistry 98(7) (2026), 1105–1117, DOI `10.1515/pac-2025-0490`, first published 2026-05-12.

Supporting controlled sources:

- IUPAC Gold Book `P04740` — polymerization;
- Gold Book `M04017` — monomer;
- Gold Book `C00958` — chain polymerization / condensative chain polymerization;
- Gold Book `P04720` — polyaddition;
- Gold Book `P04722` — polycondensation;
- S015-003 — IUPAC Recommendations 2008 on kinetics/thermodynamics/mechanisms;
- S015-004 — IUPAC Terminology for Chain Polymerization, Recommendations 2021 / published 2022.

## 2. Important controlled correction found

**Finding T015-02-01 — planning terminology hierarchy superseded by a newer IUPAC Recommendation.**

The approved CDB / original Technical Outline treated `step-growth` mainly as explanatory language and used polyaddition/polycondensation as the formal non-chain categories.

The 2026 published IUPAC Recommendation now formally establishes:

- **step polymerization**;
  - additive step polymerization = polyaddition;
  - condensative step polymerization = polycondensation;
- **chain polymerization**;
  - additive chain polymerization;
  - condensative chain polymerization.

Disposition: **CORRECTED BEFORE INVESTIGATION 2 AUTHORING.**

The correction is recorded in `TERMINOLOGY-CLASSIFICATION-UPDATE-2026-08-15.md` and `references-addendum-2026-08-15.md`. The approved CDB baseline on `main` was not silently rewritten; final integration must absorb this controlled update into the canonical CDB, Technical Outline and Evidence Plan.

## 3. Technical review

PASS.

The candidate correctly:

- distinguishes mechanism class from additive/condensative reaction character;
- defines step polymerization around reactions among monomer/oligomer/polymer molecules of any length;
- defines chain polymerization around chain-reaction propagation at active/reactive sites on growing polymer chains;
- preserves the IUPAC control that `chain` refers to a chain reaction, not merely a polymer chain;
- uses condensative chain polymerization to falsify the shortcut `small-molecule elimination = step polymerization`;
- uses additive step polymerization/polyaddition to falsify the shortcut `no by-product = chain polymerization`;
- does not convert classification into architecture/property prediction.

No scientific rewrite is required before downstream development.

## 4. Evidence review

PASS for terminology/classification layer.

No named commercial resin, catalyst technology, reactor route or piping-performance trend is introduced. Therefore no Class-C primary material/process evidence is required for the retained Investigation 2 teaching cases.

The four cases in EX-015-002 are abstract mechanism descriptions, not claims about a named material.

## 5. Asset review

### FIG-015-001

PASS as scientific specification.

Required hierarchy is now:

`polymerization → step polymerization / chain polymerization → additive / condensative qualifiers`.

No performance ranking may be added to the figure.

### TAB-015-001

PASS as controlled terminology/common-misuse table.

### EX-015-002

PASS as a classification exercise. It demonstrates all four cells of the mechanism × reaction-character map without introducing material-property claims.

## 6. Editorial / teaching review

PASS.

The Investigation follows the chapter's engineering sequence:

`engineering question → terminology/physics → classification → figure/table → interpretation example → failure lens → verification method → engineering decision`.

The distinction between an overall reaction equation and a growth mechanism is explicit and useful for supplier-data and failure-analysis contexts.

## 7. Mandatory closure actions for end-of-chapter integration

1. Integrate `investigation-002-authoring.md` into canonical `chapter.md` after Investigation 1.
2. Add S015-008 to canonical `references.md`.
3. Update the canonical terminology matrix.
4. Update `technical-outline.md` terminology control so `step polymerization` is formal rather than merely explanatory.
5. Apply the same bounded terminology correction to CDB-015 as an explicit post-approval authoritative-source update.
6. Delete the temporary Investigation 2 candidate and evidence addendum after canonical integration.
7. Final full-file review must search for stale `step-growth only explanatory` wording.

## 8. Gate decision

**INVESTIGATION 2 — PASS.**

Investigation 3 is authorized:

> **How Does Chain Polymerization Build a Macromolecule?**

Investigation 3 shall use the current IUPAC chain-polymerization terminology and cover active/reactive site, chain carrier where needed, initiation, propagation, termination and chain transfer, while explicitly preserving that termination and chain transfer are not mandatory in every chain polymerization.