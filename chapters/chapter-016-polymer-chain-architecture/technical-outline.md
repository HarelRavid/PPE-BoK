# Chapter 016 — Technical Outline

**Working title:** Polymer Chain Architecture: Molar Mass, Distribution, Branching and Crosslinking  
**PDS baseline:** 1.0  
**CDB:** `docs/PDS/Chapter-Design-Briefs/CDB-016-Polymer-Chain-Architecture.md`  
**CDB gate:** Approved by author on 2026-08-16; approval record controls pending frontmatter metadata sync  
**Outline status:** Definition-of-Ready implementation path  
**Date:** 2026-08-16

## 1. Chapter engineering question

> How should a piping engineer describe polymer-chain architecture, determine which architecture variables actually differ, and translate those differences into testable engineering hypotheses without over-claiming final pipe performance?

## 2. Governing reasoning chain

`polymerization provenance → architecture descriptor → controlled quantity → measurement route → architecture state → downstream hypothesis → verification → product qualification → engineering decision`

Chapter 016 owns architecture descriptors and measurement logic. Chapter 017 owns morphology; Chapter 018 thermal transitions; Chapter 019 viscoelastic/rheological behaviour; Chapter 020 fracture/SCG/fatigue/degradation; Part V owns detailed laboratory execution.

## 3. Terminology controls

1. Prefer **molar mass** for the dimensional quantity.
2. Retain `molecular weight` only in standard/source titles or clearly identified common usage.
3. Use `M_n` for number-average molar mass.
4. Use `M_m` as the preferred mass-average symbol while recognizing `M_w` as an IUPAC-accepted synonym and common industry symbol.
5. Use molar-mass dispersity `Đ_M = M_m/M_n`; explain that `polydispersity index` is discouraged by IUPAC.
6. Distinguish an average from the full molar-mass distribution.
7. Distinguish branch count, branch length, branch placement and branch distribution.
8. Distinguish short-chain branching from long-chain branching.
9. Distinguish branch point, crosslink, covalent network, physical network and entanglement.
10. Do not describe gel content as a complete crosslink-density or topology measurement.
11. Do not describe MFR/MVR as a direct MWD measurement.

## 4. Quantitative treatment

### 4.1 Required definitions/equations

The following are authorized for development, subject to source verification and units/assumptions review:

- number-average molar mass, `M_n`;
- mass-average molar mass, `M_m ≡ M_w`;
- molar-mass dispersity, `Đ_M = M_m/M_n`;
- number-average degree of polymerization where useful;
- bounded repeat-unit relation between degree of polymerization and molar mass only when composition/end-group assumptions are explicit.

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

Engineering-development treatment shall explain:

- separation by hydrodynamic size;
- relative calibration using polymer standards;
- universal-calibration context where applicable;
- SEC-light-scattering route using absolute molar-mass information;
- high-temperature SEC relevance for difficult-to-dissolve polyolefin systems;
- composition, branching, dissolution and calibration as interpretation controls.

Detailed apparatus, specimen preparation and operating procedure belong to Part V.

### 5.2 Branching

Architecture claims shall distinguish:

- direct branch chemistry/sequence characterization;
- indirect thermal/rheological inference;
- method scope and calibration;
- material-system limits.

ISO 18177:2025 may be used only for its stated semicrystalline ethylene/1-olefin scope.

### 5.3 Crosslinking / network

ISO 10147:2011 may establish the PE-X gel-content method and its intended assessment context. `Gel content` is not to be equated with complete network topology or a universal crosslink-density value.

### 5.4 Melt flow

ISO 1133-1/-2 may establish what MFR/MVR measure under specified temperature/load/history controls and why those results are useful for QC. The chapter shall explicitly block `MFR → unique M_n/M_m/MWD` inference.

## 6. Investigation sequence

### Investigation 1 — Why does chain architecture matter after polymerization is finished?
Purpose: bridge Chapter 015 provenance to architecture as a measurable material state. No named architecture→property trend yet.

### Investigation 2 — What are chain length, degree of polymerization and molar mass?
Purpose: control dimensional and population terminology; distinguish molar mass from relative molecular mass/molecular-weight language.

### Investigation 3 — Why does a polymer have multiple molar-mass averages?
Purpose: develop `M_n`, `M_m/M_w`, distribution shape and dispersity.
Assets: FIG-016-001, FIG-016-002, TAB-016-001, EX-016-001.

### Investigation 4 — What does SEC/GPC actually measure, and what are its limits?
Purpose: explain measurement logic and calibration without becoming a lab SOP.
Asset: TAB-016-002.

### Investigation 5 — What is branching, and why is “more branching” incomplete?
Purpose: branch point, count, length, placement and topology.

### Investigation 6 — How do short-chain and long-chain branching differ?
Purpose: separate branching classes and measurement/evidence limits; introduce ISO 18177 only within scope.
Assets: FIG-016-003, FIG-016-004, TAB-016-003.

### Investigation 7 — What are crosslinks and polymer networks?
Purpose: crosslink, network, gel fraction and PE-X evidence limits.

### Investigation 8 — Where do entanglements fit, and why are they not crosslinks?
Purpose: establish temporary/topological connectivity without taking Chapter 019 rheology ownership.
Asset: FIG-016-005.

### Investigation 9 — How can architecture influence engineering behaviour without becoming a design rule?
Purpose: primary-literature evidence gate for bounded architecture→behaviour cases. Candidate domains: morphology, rheology, diffusion/permeation, creep, SCG and fusion/interdiffusion.

Every retained case must record:
`system | architecture variable | measurement | downstream measurement | confounders | supported conclusion | unsupported conclusion | transferability`.

### Investigation 10 — What architecture information should the engineer request, and where must inference stop?
Purpose: close workflow, supplier evidence request, checklist, failure lens and Chapter 017 handoff.
Assets: TAB-016-004, TAB-016-005, FIG-016-006, WF-016-001, CL-016-001, EX-016-002, EX-016-003.

## 7. Required asset register

| ID | Asset | Owner | Control |
|---|---|---:|---|
| FIG-016-001 | Why one molar-mass number is not enough | 3 | conceptual population/distribution |
| FIG-016-002 | Molar-mass averages on one distribution | 3 | no universal distribution shape |
| FIG-016-003 | Linear / SCB / LCB / network topology | 6 | topology only |
| FIG-016-004 | Branch count / length / distribution | 6 | prevent scalar “more branching” shortcut |
| FIG-016-005 | Branch point / crosslink / entanglement / network | 8 | permanence/connectivity map |
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

1. Investigation 2 terminology gate — IUPAC molar-mass/relative-mass language.
2. Investigation 3 quantitative gate — equations/symbols/units verified.
3. Investigation 4 method-scope gate — ISO 16014 series verified.
4. Investigation 6 branching gate — ISO 18177 scope and any named PE/PP branching claim verified.
5. Investigation 7 network gate — IUPAC network/crosslink terminology + ISO 10147 scope verified.
6. Investigation 9 primary-literature gate — each architecture→behaviour case independently reviewed.
7. Pre-integration Technical Review.
8. Final full-file Technical Review.
9. Final claim-level Standards/Evidence Review.
10. Editorial/Style + continuous Desk Test.
11. Human Approval before merge.

## 9. Explicit exclusions

Chapter 016 shall not become:

- a detailed SEC operating procedure;
- a DSC branching-analysis SOP;
- a PE-X material-family chapter;
- a rheology/creep chapter;
- a crystallinity/morphology chapter;
- a fracture/SCG chapter;
- a pipe-design or joining-qualification chapter.

## 10. Definition-of-Ready disposition

Together with the approved CDB, active Evidence Plan, canonical scaffold and DoR audit, this outline provides the sequential engineering-development path required to begin Investigation 1 once the DoR audit passes.
