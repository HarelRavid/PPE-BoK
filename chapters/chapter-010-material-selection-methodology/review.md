# Chapter 010 — Book-Wide Review Package

**Chapter:** 010 — Engineering Methodology for Material Selection  
**Review framework:** `docs/BOOK-WIDE-REVIEW-PLAN.md`  
**Branch:** `chapter-013-redevelopment`  
**Status:** REVIEW COMPLETE — REVISION APPROVAL PENDING  
**Disposition:** AUGMENT / SELECTION-GOVERNANCE REFINEMENT

## 1. Review basis

Reviewed sources:

- `chapters/chapter-010-material-selection-methodology/chapter.md`;
- existing Chapter 010 technical review;
- `chapters/chapter-010-material-selection-methodology/references.md`;
- approved Chapter 009 Rev 1.0 for upstream polymer/material-behaviour boundary;
- `chapters/chapter-011-common-plastic-piping-materials/chapter.md` for downstream material-family boundary;
- Chapter 012 architecture for detailed long-term pressure-design boundary;
- approved Chapters 005–008 for Design Basis, service-envelope, uncertainty, and fluid-characterization inputs;
- `docs/BOOK-WIDE-REVIEW-PLAN.md` for review criteria.

No external source was used to introduce new technical or normative claims in this review. Existing standards statements are evaluated only against the chapter's own source register and current manuscript architecture.

---

## 2. Gate A — File and evidence inventory

### Present

- `chapter.md` — research-based full draft;
- `references.md` — normative/technical source register and evidence map;
- `review.md` — prior technical review, expanded here into the book-wide review package.

### Evidence maturity

The existing source package is comparatively strong and already identifies:

- ISO/TR 10358;
- ISO 15494;
- ISO 9080;
- ISO 12162;
- application/product-standard families;
- limitations of chemical-resistance screening data.

The prior technical review correctly leaves open:

- current-edition recheck before final lock;
- clause-level full-text mapping;
- jurisdiction-specific design-code treatment;
- later evidence for combined chemical-mechanical ageing.

These remain final-lock evidence actions and must not be silently treated as closed by content revision.

**Gate A result: PASS WITH CONTROLLED EVIDENCE HOLDS.**

---

## 3. Gate B — Architecture and scope review

### 3.1 What the chapter already does well

The chapter is already one of the stronger methodology chapters in the manuscript. It correctly establishes that:

- material selection is a complete-system decision rather than a resin-name decision;
- selection starts from service rather than a preferred material;
- chemical compatibility is a screening input, not complete approval;
- pressure-temperature capability must be evaluated separately from chemistry;
- credible failure mechanisms must be considered;
- installation, joining, inspection, maintenance, repair, availability, and life-cycle concerns matter;
- system components and interfaces can limit suitability;
- alternatives should be compared transparently;
- mandatory disqualifiers should not be hidden by a weighted score;
- testing may be required when the available evidence does not represent the actual service;
- changed service conditions should reopen the selection.

This is the correct canonical role for Chapter 010.

### 3.2 Boundary with Chapters 005–008

The revised upstream chapters now provide controlled inputs:

- Chapter 005 — approved Design Basis baseline;
- Chapter 006 — discrete service/design envelope cases;
- Chapter 007 — uncertainty and residual-risk discipline;
- Chapter 008 — case-specific fluid-characterization package.

Chapter 010 should consume these inputs rather than substantially re-teach their creation.

The current Sections 10.2 and 10.3 are technically sound but should be reframed as a **selection-entry readiness gate** and a check that the upstream packages are sufficiently mature.

### 3.3 Boundary with Chapter 009

Chapter 009 now owns material-science fundamentals and property interpretation.

Chapter 010 should use that understanding to screen and compare candidate systems. It should not repeat the polymer-physics explanation of creep, relaxation, morphology, or long-term classification.

### 3.4 Boundary with Chapter 011

Chapter 011 owns the engineering characteristics of common material families.

Canonical boundary:

- Chapter 010: **How should candidate piping systems be selected and verified?**
- Chapter 011: **What are the characteristic strengths, limitations, and application cautions of the major material families?**

Chapter 010 may define candidate-screening criteria but should avoid becoming another material-family comparison catalogue.

### 3.5 Boundary with Chapter 012

Chapter 012 owns detailed long-term hydrostatic strength, MRS, design stress, SDR, and pressure-rating logic.

Chapter 010 should require that the candidate system pass the applicable long-term pressure-temperature verification, but should not reproduce the calculation chain.

### 3.6 Missing or underdeveloped chapter functions

The following require targeted refinement:

1. **selection-entry readiness gate** based on controlled upstream inputs;
2. **candidate system definition** — a candidate should include material/compound, product/system basis, geometry/pressure series where relevant, joining route, components/interfaces, and qualification evidence;
3. explicit distinction between **screening, qualification, verification, and final selection approval**;
4. explicit separation of **hard gates / disqualifiers** from comparative or weighted criteria;
5. a canonical **candidate elimination log** so rejected options and reasons remain traceable;
6. an **evidence sufficiency model** for each material candidate;
7. stronger integration of Chapter 007 uncertainty discipline into candidate comparison;
8. explicit treatment of **residual uncertainty after selection**, not only before selection;
9. clearer **selection verification plan** identifying which downstream analyses/tests must close before release;
10. stronger distinction between **material-family suitability, qualified product availability, and complete system suitability**;
11. lifecycle cost / availability should be explicitly subordinate to mandatory technical and safety suitability;
12. selection outputs should be defined as a controlled decision package, not only a narrative conclusion;
13. change/reopen logic should identify which selection assumptions and evidence are invalidated;
14. no canonical workflow figure in the chapter manuscript;
15. no compact candidate decision register / matrix with evidence status and hard-gate disposition;
16. no reader outcomes / final selection-readiness check aligned with the rest of the revised book.

**Gate B result: PASS — TARGETED SELECTION-GOVERNANCE AUGMENTATION REQUIRED.**

---

## 4. Gate C — Technical / methodological review

### 4.1 Strong content to retain

The existing ten-step selection method should remain substantially intact:

- service-envelope basis;
- standards framework;
- chemical compatibility screening;
- long-term pressure-temperature capability;
- credible failure mechanisms;
- mechanical/installation demands;
- joining-system selection;
- complete component-system review;
- inspection/maintenance/repair;
- transparent alternatives comparison.

The revision should improve control and traceability around this method, not replace it.

### 4.2 Add a selection-entry readiness gate

Material selection should begin only when the inputs are mature enough for the current project stage.

Recommended readiness questions:

- Is the Design Basis active and controlled?
- Are relevant service/envelope cases identified?
- Is the fluid characterization adequate for the material decision?
- Are mandatory requirements known?
- Are unresolved assumptions/holds visible?
- Are governing standards and editions identified sufficiently for screening?

Possible outcomes:

- READY FOR SCREENING;
- CONDITIONALLY READY;
- NOT READY.

This prevents the selection chapter from re-creating upstream data governance while preserving a clear entry gate.

### 4.3 Define the candidate as a system configuration

A candidate should not be recorded simply as “PE,” “PP,” “PVDF,” or “PVC.”

A material-selection candidate should be defined at the level needed for the decision, potentially including:

- polymer family and compound/grade where known;
- product/system standard or qualified system basis;
- pipe/fitting/component availability;
- joining route;
- seal/gasket/interface materials;
- pressure-temperature basis;
- installation context;
- evidence status.

This reinforces the book-wide rule:

> material qualification ≠ product conformity ≠ system suitability.

### 4.4 Separate screening from qualification and verification

The chapter should distinguish four stages:

1. **Screening** — eliminate clearly unsuitable families/options using available evidence;
2. **Qualification** — confirm that the material/product/system has the necessary recognized qualification basis;
3. **Project verification** — demonstrate suitability for the actual Design Basis and interfaces;
4. **Selection approval** — issue the controlled decision and required conditions.

This helps prevent chemical-resistance tables or generic material data from being treated as final approval.

### 4.5 Hard gates must precede scoring

The current warning against hiding critical disqualifiers behind scores is excellent and should become a formal rule.

Examples of hard gates may include:

- mandatory regulatory/code requirement;
- unacceptable chemistry;
- inadequate pressure-temperature capability;
- unavailable compliant product/system;
- infeasible joining/inspection route;
- unacceptable failure consequence without adequate control.

Only candidates that pass the required gates should proceed to comparative optimization.

### 4.6 Evidence sufficiency should be candidate-specific

For each candidate, the engineer should know whether critical claims are supported by:

- applicable standard/product qualification;
- manufacturer data for the actual system;
- operating history;
- test evidence;
- engineering analysis;
- bounded assumption;
- unresolved hold.

A candidate may therefore be technically promising but remain **not yet verified**.

### 4.7 Uncertainty should travel with the candidate

Chapter 007 established that uncertainty should remain tied to the affected decision.

The selection chapter should therefore require recording:

- uncertain property or condition;
- decision sensitivity;
- required test/data/control;
- residual uncertainty after selection;
- monitoring or reopen trigger.

This is especially important where two candidates appear similar but one has a materially stronger evidence base.

### 4.8 Selection verification plan

The selected candidate should leave Chapter 010 with a clear list of downstream verification actions, such as:

- detailed pressure design;
- hydraulic analysis;
- mechanical/flexibility analysis;
- chemical compatibility confirmation;
- joining qualification;
- component/interface verification;
- inspection/testing requirements;
- project-specific test or trial where required.

Material selection is therefore not the end of verification. It is a controlled decision that releases a candidate system into detailed verification.

### 4.9 Cost and availability are legitimate but subordinate

Availability, contractor capability, schedule, and lifecycle cost are valid selection criteria.

They must not override mandatory safety, regulatory, chemical, pressure-temperature, or system-suitability requirements.

A technically unsuitable system cannot become acceptable because it is cheaper or locally available.

### 4.10 Selection output should be a controlled decision package

Recommended output fields include:

- selection ID / system segment;
- Design Basis revision;
- candidate systems considered;
- hard-gate results;
- comparative criteria;
- evidence status;
- rejected candidates and reasons;
- selected system;
- assumptions / holds;
- required downstream verification;
- residual uncertainty;
- owner / approver;
- reopen triggers.

**Gate C result: PASS WITH SELECTION-GOVERNANCE AND TRACEABILITY AUGMENTATION.**

---

## 5. Gate D — Standards / evidence review

### 5.1 Existing strengths

The references and current chapter already apply useful evidence discipline:

- chemical-resistance tables are screening inputs;
- product-standard compliance does not prove project suitability;
- standards editions and scopes require checking;
- generic online charts and distributor summaries are not sole authority;
- proprietary mixtures and unusual conditions may require further testing.

### 5.2 Controlled holds remain

Before final lock:

- verify current published status/edition of temporally unstable standards;
- complete clause-level full-text mapping where normative precision is required;
- add later domain-specific evidence for combined chemical-mechanical ageing and specialized mechanisms;
- update cross-references after final book numbering;
- perform independent senior engineering review.

The Rev 1.0 content revision should preserve these holds.

### 5.3 Standards detail should remain proportionate

Chapter 010 should identify the standards framework and require candidate verification against it.

Detailed normative calculations and material-family-specific acceptance rules belong in Chapters 011–012 and later specialist chapters.

**Gate D result: PASS WITH CONTROLLED EVIDENCE HOLDS.**

---

## 6. Gate E — Editorial and academic review

### Strengths

- strong engineering voice;
- clear ten-step structure;
- excellent system-level framing;
- useful examples of disqualifiers and trade-offs;
- strong testing and re-evaluation cautions;
- vendor-neutral wording.

### Editorial / structure gaps

1. No reader outcomes.
2. The chapter partly repeats upstream service-definition content rather than treating it as controlled input.
3. Screening, qualification, verification, and approval are not explicitly separated.
4. No canonical candidate-system definition.
5. No hard-gate versus comparative-criteria model.
6. No candidate elimination/evidence register.
7. No explicit final selection-readiness/release review.
8. Existing figure concepts are in `review.md` but not represented in the manuscript as canonical placeholders.
9. Final visual/punctuation polish remains deferred to the book-wide cleanup pass.

**Gate E result: PASS — TARGETED AUGMENTATION.**

---

## 7. Gate F — Gap Register

| Gap ID | Severity | Finding | Required disposition |
|---|---|---|---|
| GAP-010-01 | High | No explicit selection-entry readiness gate | Add READY / CONDITIONALLY READY / NOT READY input gate |
| GAP-010-02 | High | Candidate is not defined explicitly as a system configuration | Add canonical candidate-system definition |
| GAP-010-03 | High | Screening, qualification, verification, and approval are blended | Separate the four selection stages |
| GAP-010-04 | High | Hard disqualifiers are warned about but not formalized | Add hard-gate-before-scoring rule |
| GAP-010-05 | Medium | Rejected candidate reasoning is not captured in a canonical record | Add candidate elimination log |
| GAP-010-06 | High | Candidate evidence sufficiency/status not explicit | Add evidence-status assessment per candidate |
| GAP-010-07 | High | Chapter 007 uncertainty discipline is only partially integrated | Carry sensitivity, holds, controls, residual uncertainty into selection |
| GAP-010-08 | Medium | Residual uncertainty after final selection is underdeveloped | Add explicit residual-uncertainty disposition |
| GAP-010-09 | High | No defined selection verification plan | Add downstream verification/release actions |
| GAP-010-10 | High | Family / product / system suitability hierarchy needs stronger control | Reinforce qualification → conformity → system suitability chain |
| GAP-010-11 | Medium | Cost/availability priority hierarchy is implicit | State they cannot override mandatory suitability gates |
| GAP-010-12 | Medium | Final decision output is narrative rather than canonical controlled package | Add selection decision record fields |
| GAP-010-13 | Medium | Reopen logic does not explicitly map changed input to affected evidence/decision | Add impact-based reopen logic |
| GAP-010-14 | Medium | Workflow figures remain only proposed in prior review | Add canonical `FIG-010-001 — Material Selection and Verification Workflow` placeholder |
| GAP-010-15 | Medium | No compact selection register asset | Add `TAB-010-001 — Material Selection Decision Register` |
| GAP-010-16 | Low | No reader outcomes / release-readiness check | Add outcomes and final release review |

---

## 8. Disposition

# AUGMENT / SELECTION-GOVERNANCE REFINEMENT

The chapter is technically strong and should **not** be rewritten from scratch.

The major revision is to turn the existing ten-step methodology into the book's canonical **controlled selection process**:

`controlled inputs → readiness gate → candidate systems → hard-gate screening → evidence/uncertainty assessment → comparative evaluation → selection → verification plan → approved decision → reopen triggers`

---

## 9. Proposed Chapter 010 Rev 1.0 scope

Recommended revision package:

1. Retain the existing system-level material-selection philosophy and most of the ten-step method.
2. Add concise reader outcomes.
3. Add a **Selection Entry Readiness Gate** consuming the approved Design Basis, envelope cases, fluid package, requirements, and uncertainty/hold register.
4. Add a canonical definition of a **candidate piping system**, not merely a material family.
5. Separate **screening → qualification → project verification → selection approval**.
6. Formalize **hard gates before scoring/optimization**.
7. Add a candidate elimination log and require rejection reasons to remain traceable.
8. Add candidate-specific evidence status and uncertainty treatment.
9. Carry residual uncertainty and controls into the selected-system decision.
10. Add a **Selection Verification Plan** identifying required downstream analyses/tests before final system release.
11. Reinforce `material qualification ≠ product conformity ≠ system suitability` as a selection-control rule.
12. State explicitly that availability, schedule, and lifecycle cost cannot compensate for failure of mandatory technical/safety gates.
13. Add a canonical selection decision record with owner, approver, Design Basis revision, evidence, assumptions/holds, selected option, rejection rationale, and reopen triggers.
14. Add `FIG-010-001 — Material Selection and Verification Workflow` placeholder.
15. Add `TAB-010-001 — Material Selection Decision Register`.
16. Add a final **Selection Release Review** with GO / CONDITIONAL GO / NO-GO alignment to Chapter 002.
17. Reduce repeated upstream process-definition detail and replace it with explicit handoffs to Chapters 005–008.
18. Keep detailed material-family properties in Chapter 011 and detailed MRS/SDR/pressure design in Chapter 012.
19. Preserve all existing standards/evidence holds until final lock.

---

## 10. Approval gate

No substantive change has been made to `chapter.md` in this book-wide review.

If the revision scope above is approved, prepare **Chapter 010 Rev 1.0** as a complete proposed replacement, present the integrated text for review, and only after explicit approval commit the revised manuscript before proceeding to Chapter 011.
