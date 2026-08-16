# Chapter 016 — Technical Outline

**Working title:** Polymer Chain Architecture: Molar Mass, Distribution, Branching and Crosslinking  
**PDS baseline:** 1.0  
**CDB:** `docs/PDS/Chapter-Design-Briefs/CDB-016-Polymer-Chain-Architecture.md`  
**CDB gate:** Approved by author on 2026-08-16; metadata synchronized on `main`  
**Outline status:** Engineering Development complete at controlled-authoring level — canonical integration pending  
**Date:** 2026-08-16

## 1. Chapter engineering question

> How should a piping engineer describe polymer-chain architecture, determine which architecture variables actually differ, and translate those differences into testable engineering hypotheses without over-claiming final pipe performance?

## 2. Governing reasoning chain

`polymerization provenance → architecture descriptor → controlled quantity → measurement route → architecture state → downstream hypothesis → verification → product qualification → engineering decision`

Chapter 016 owns architecture descriptors and measurement logic. Chapter 017 owns morphology; Chapter 018 thermal transitions; Chapter 019 viscoelastic/rheological behaviour; Chapter 020 fracture/SCG/fatigue/degradation; Part V owns detailed laboratory execution.

## 3. Terminology controls

1. Prefer **molar mass** for the dimensional quantity.
2. Retain `molecular weight` only in standard/source titles or clearly identified common usage.
3. Do not use unqualified `chain length` as the formal molecular-size quantity when DP, molar mass/distribution or a defined geometric quantity is intended.
4. Use `M_n` for number-average molar mass.
5. Use `M_m` as the preferred mass-average symbol while recognizing `M_w` as an IUPAC-accepted synonym and common industry symbol.
6. Use molar-mass dispersity `Đ_M = M_m/M_n`; explain that `polydispersity index` is discouraged by IUPAC.
7. Distinguish an average from the full molar-mass distribution.
8. Distinguish branch count, branch length, branch placement and branch distribution.
9. Distinguish short-chain branching from long-chain branching.
10. Distinguish branch point, covalent crosslink, physical network and entanglement when permanence/connectivity matters.
11. Do not describe gel content as a complete crosslink-density or topology measurement.
12. Do not describe MFR/MVR as a direct MWD measurement.

## 4. Quantitative treatment

### 4.1 Retained definitions/equations after Investigation gates

- bounded individual-chain bookkeeping relation `M_chain = x M_0 + M_end`, with explicit composition/end-group assumptions;
- number-average molar mass, `M_n`;
- mass-average molar mass, `M_m ≡ M_w`;
- molar-mass dispersity, `Đ_M = M_m/M_n`;
- degree-of-polymerization dispersity `Đ_X = X_m/X_n` when that quantity is explicitly intended;
- no architecture→pipe-performance equation.

### 4.2 Equation control

For every retained relation state:

- mathematical definition;
- weighting basis;
- units;
- assumptions;
- measurement route;
- what the quantity does not prove about pipe performance.

No equation may convert architecture quantities directly into pressure rating, SCG life, weld strength, permeability, service temperature or lifetime.

## 5. Measurement logic

### 5.1 SEC/GPC

Engineering-development treatment establishes:

- separation by hydrodynamic size;
- conventional relative calibration using polymer standards;
- universal-calibration context as a relative ISO 16014-2 route;
- SEC-light-scattering route using absolute molar-mass information within ISO 16014-5 method scope;
- low-temperature and high-temperature ISO 16014 routes;
- composition, branching, dissolution, detector and calibration as interpretation controls.

Detailed apparatus, specimen preparation and operating procedure belong to Part V.

### 5.2 Branching

Architecture claims distinguish:

- direct branch chemistry/sequence characterization;
- indirect thermal/rheological inference;
- method scope and calibration;
- material-system limits.

ISO 18177:2025 is used only for its stated semicrystalline ethylene/1-olefin SCB-distribution scope.

### 5.3 Crosslinking / network

ISO 10147:2011 establishes the PE-X gel-content method and assessment context. `Gel content` is not equated with complete network topology or a universal crosslink-density value.

### 5.4 Melt flow

ISO 1133-1/-2 establish MFR/MVR under specified method conditions and QC context. The chapter explicitly blocks `MFR → unique M_n/M_m/MWD/branch topology` inference.

## 6. Investigation sequence and gate status

### Investigation 1 — Why does chain architecture matter after polymerization is finished?
**PASS / canonical.** Bridge Chapter 015 provenance to architecture as a measurable material state.

### Investigation 2 — What are chain length, degree of polymerization and molar mass?
**PASS / controlled candidate.** IUPAC terminology/units gate passed.

### Investigation 3 — Why does a polymer have multiple molar-mass averages?
**PASS / controlled candidate.** Quantitative gate passed; EX-016-001 independently verified.
Assets: FIG-016-001, FIG-016-002, TAB-016-001, EX-016-001.

### Investigation 4 — What does SEC/GPC actually measure, and what are its limits?
**PASS / controlled candidate.** ISO 16014 method-scope gate passed.
Asset: TAB-016-002.

### Investigation 5 — What is branching, and why is “more branching” incomplete?
**PASS / controlled candidate.** Branch terminology/topology review passed.

### Investigation 6 — How do short-chain and long-chain branching differ?
**PASS / controlled candidate.** ISO 18177 scope gate passed.
Assets: FIG-016-003, FIG-016-004, TAB-016-003.

### Investigation 7 — What are crosslinks and polymer networks?
**PASS / controlled candidate.** IUPAC network/crosslink + ISO 10147 gate passed.

### Investigation 8 — Where do entanglements fit, and why are they not crosslinks?
**PASS / controlled candidate.** Entanglement/physical-connectivity review passed.
Asset: FIG-016-005.

### Investigation 9 — How can architecture influence engineering behaviour without becoming a design rule?
**PASS / controlled candidate.** Primary-evidence gate passed for S016-013..016 only.

Every retained case records:
`system | architecture variable | measurement | downstream measurement | confounders | supported conclusion | unsupported conclusion | transferability`.

### Investigation 10 — What architecture information should the engineer request, and where must inference stop?
**PASS / controlled candidate.** Chapter closure authoring review passed.
Assets: TAB-016-004, TAB-016-005, FIG-016-006, WF-016-001, CL-016-001, EX-016-002, EX-016-003.

## 7. Required asset register

| ID | Asset | Owner | Control |
|---|---|---:|---|
| FIG-016-001 | Why one molar-mass number is not enough | 3 | conceptual population/distribution |
| FIG-016-002 | Molar-mass averages on one distribution | 3 | no universal distribution shape |
| FIG-016-003 | Linear / SCB / LCB / network topology | 6 | topology only |
| FIG-016-004 | Branch amount / placement / distribution | 6 | prevent scalar “more branching” shortcut |
| FIG-016-005 | Branch point / covalent crosslink / entanglement / physical network | 8 | permanence/connectivity map |
| FIG-016-006 | Architecture evidence chain | 10 | final decision-boundary figure |
| TAB-016-001 | Quantities / symbols / units / misuse | 3 | IUPAC-controlled |
| TAB-016-002 | Measurement route / quantity / limitation | 4 | no method equivalence claims |
| TAB-016-003 | Branching descriptor matrix | 6 | method/scope explicit |
| TAB-016-004 | Architecture feature → hypothesis → verification | 10 | no design-rule conversion |
| TAB-016-005 | Downstream ownership crosswalk | 10 | match BOOK_STRUCTURE |
| EX-016-001 | Same `M_m`, different distribution | 3 | synthetic teaching example |
| EX-016-002 | “High molecular weight” supplier claim | 10 | evidence-request exercise |
| EX-016-003 | MFR is not architecture | 10 | method-boundary exercise |
| WF-016-001 | Architecture claim → engineering decision | 10 | final workflow |
| CL-016-001 | Before using architecture in piping decision | 10 | final checklist |

## 8. Evidence gates

Completed:

1. Investigation 2 terminology gate — PASS.
2. Investigation 3 quantitative/equation/units gate — PASS.
3. Investigation 4 ISO 16014 method-scope gate — PASS.
4. Investigation 6 ISO 18177 branching gate — PASS.
5. Investigation 7 IUPAC network/crosslink + ISO 10147 gate — PASS.
6. Investigation 9 primary-literature gate — PASS FOR S016-013..016 ONLY.
7. Pre-integration Technical Review — CONDITIONAL PASS, bounded integration findings only.
8. Pre-integration Standards/Evidence Validation — PASS.
9. Pre-integration Editorial/Style + Desk Review — CONDITIONAL PASS, no structural rewrite.

Pending after canonical integration:

10. Final full-file Technical Review.
11. Final claim-level Standards/Evidence Review.
12. Final Editorial/Style + continuous Desk Test.
13. Human Approval before merge.

## 9. Explicit exclusions

Chapter 016 shall not become:

- a detailed SEC operating procedure;
- a DSC branching-analysis SOP;
- a PE-X material-family chapter;
- a rheology/creep chapter;
- a crystallinity/morphology chapter;
- a fracture/SCG chapter;
- a pipe-design or joining-qualification chapter.

## 10. Current disposition

**ENGINEERING DEVELOPMENT COMPLETE AT CONTROLLED-AUTHORING LEVEL — CANONICAL INTEGRATION AUTHORIZED.**

The one-shot integration shall combine Investigations 2–10 with canonical Investigation 1, absorb S016-013..016 into the evidence register, apply bounded metadata/editorial normalization, validate controlled assets/source IDs, remove temporary authoring artifacts and stop before final integrated-manuscript review.