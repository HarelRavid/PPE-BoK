# CDB-016 — Chapter Design Brief: Polymer Chain Architecture — Molar Mass, Distribution, Branching and Crosslinking

**PDS Baseline:** 1.0  
**Working Chapter:** 016  
**Status:** Draft — Author Approval Required  
**Date:** 2026-08-16  
**Architecture source:** `BOOK_STRUCTURE.md`  
**Upstream prerequisites:** Chapter 014 — Atomic Structure, Chemical Bonding and Carbon Chemistry; Chapter 015 — From Monomer to Polymer

## 1. Chapter purpose

Develop the engineering treatment of polymer-chain architecture that sits between polymerization history and bulk morphology/property behaviour.

Chapter 015 established how polymerization mechanism, catalyst environment and process history can create different architecture hypotheses. Chapter 016 shall define what that architecture actually means at molecular level, how it is described and measured, and what a piping engineer may or may not infer from descriptors such as molar mass, molar-mass distribution, branching, crosslinking, network formation and melt-flow data.

The chapter shall make one principle explicit throughout:

`polymerization provenance → chain architecture → characterization → morphology / mobility → engineering behaviour → product qualification`

Chapter 016 owns **chain architecture and its measurement logic**. It does not own detailed morphology, viscoelasticity, fracture mechanics, SCG/RCP, diffusion/permeation, joining qualification or pipe design.

The chapter must prevent two opposite engineering errors:

1. reducing a polymer to one scalar “molecular weight” or one MFR value;
2. treating chain-architecture descriptors as direct proof of piping performance.

## 2. Primary audience

Practicing mechanical, process, piping, materials, reliability, QA/inspection, procurement and owner/EPC engineers who work with thermoplastic piping but may not have formal polymer-physics or polymer-characterization training.

Secondary readers include polymer-processing engineers, joining specialists, laboratory personnel, resin/pipe manufacturers and advanced technical students.

## 3. Engineering problem addressed

Two polymers can share the same chemical family and nominal monomer basis while differing materially in:

- chain length distribution;
- number-average and mass-average molar mass;
- distribution shape and dispersity;
- short-chain branching;
- long-chain branching;
- branch placement and topology;
- comonomer/sequence architecture where relevant;
- crosslink density / gel fraction / network formation;
- entanglement state and effective molecular connectivity.

Those differences can change what the material is capable of doing, but they do not bypass the need to measure morphology, rheology, mechanical response and product qualification.

The governing engineering question is:

> **How should a piping engineer describe polymer-chain architecture, determine which architecture variables actually differ, and translate those differences into testable engineering hypotheses without over-claiming final pipe performance?**

## 4. Reader outcomes

After completing the chapter, the reader should be able to:

1. Distinguish chain length, degree of polymerization, molar mass and molecular weight terminology.
2. Explain why a non-uniform polymer does not have one unique molar mass.
3. Distinguish number-average molar mass (`Mn`), mass-average/weight-average molar mass (`Mm` / `Mw`), higher averages and the full molar-mass distribution.
4. Use dispersity (`Đ`) correctly and explain why the older expression `polydispersity index` is discouraged in controlled terminology.
5. Explain why two materials can have similar average molar mass yet different distribution shape and therefore require different interpretation.
6. Explain the conceptual basis and limitations of size-exclusion chromatography (SEC/GPC), including relative calibration versus SEC coupled to light scattering, without turning the chapter into a laboratory SOP.
7. Distinguish linear, branched and network architectures.
8. Distinguish short-chain branching from long-chain branching and explain why branch count, branch length and branch distribution are different descriptors.
9. Explain why branching cannot be inferred reliably from family name, catalyst label, density or one rheological number alone.
10. Distinguish branch points, crosslinks, covalent networks, physical networks and entanglements.
11. Explain why gel content is a measurement related to insoluble/network fraction and is not automatically equivalent to a complete crosslink-density description.
12. Explain why MFR/MVR are useful QC/rheological indicators but are not direct substitutes for a molar-mass distribution measurement.
13. Build an evidence request that separates architecture characterization from morphology/property/product qualification.
14. Route detailed crystallinity/morphology questions to Chapter 017; thermal transitions to Chapter 018; creep/rheology to Chapter 019; fracture/SCG/fatigue/degradation to Chapter 020; and laboratory execution to Part V.

## 5. Controlled terminology

Canonical prose shall prefer **molar mass** for the dimensional physical quantity.

Industry and standard titles may retain **molecular weight** where that wording is established. Original titles and quotations shall not be silently rewritten.

Controlled terms shall include, where relevant:

- degree of polymerization;
- molar-mass average;
- number-average molar mass (`Mn`);
- mass-average molar mass (`Mm`, with `Mw` retained as familiar synonym/symbol where appropriate);
- z-average molar mass where engineering-useful;
- molar-mass distribution;
- molar-mass dispersity / dispersity (`Đ`);
- linear polymer / linear chain;
- branch point;
- branched polymer;
- short-chain branching;
- long-chain branching;
- crosslink;
- crosslinking;
- network / covalent network;
- network polymer;
- physical network;
- entanglement only with a clear distinction from permanent covalent connectivity.

The expression **polydispersity index (PDI)** may be mentioned as familiar historical/industrial language but shall not be the preferred controlled term for `Mw/Mn`.

## 6. Standards and evidence framework

Chapter 016 requires a stronger measurement-evidence layer than Chapter 015 because the chapter describes quantities that are routinely measured and compared.

### 6.1 Authoritative terminology path

The initial controlling terminology path shall include:

1. **IUPAC Compendium of Chemical Terminology (Gold Book), 5th ed., online v5.0.0 (2025)** — current controlled term source. Relevant entries include degree of polymerization, molar-mass average, number-average molar mass, mass-average molar mass, molar-mass dispersity/dispersity, branched polymer, crosslink, crosslinking, network, network polymer and physical network.
2. **Definitions of terms relating to individual macromolecules, macromolecular assemblies, polymer solutions, and amorphous bulk polymers — IUPAC Recommendations 2014, published 2015** — primary terminology source for molar-mass averages, distributions and related polymer quantities; DOI `10.1515/pac-2013-0201`.
3. **Dispersity in polymer science — IUPAC Recommendations 2009** — terminology basis for `Đ` and the discouragement of `polydispersity index`; DOI `10.1351/PAC-REC-08-05-02`.
4. **Glossary of Basic Terms in Polymer Science — IUPAC Recommendations 1996** — foundational polymer architecture terminology including branches, crosslinks and networks.
5. **Definitions of terms relating to the structure and processing of sols, gels, networks, and inorganic-organic hybrid materials — IUPAC Recommendations 2007** — network / physical-network / crosslinking terminology where required.

### 6.2 ISO vocabulary and characterization path

The initial standards path shall include:

1. **ISO 472:2013 + Amendment 1:2018 — Plastics — Vocabulary** — plastics terminology cross-check only. Lifecycle hold: current publication remains published but at stage `90.92 — International Standard to be revised`.
2. **ISO 16014-1:2019 through ISO 16014-5:2019** — SEC family for average molecular weight/molar-mass distribution characterization. Parts are current and were confirmed in 2024. Chapter 016 may use them to establish what the methods are intended to determine and the distinction between relative calibration routes and SEC-LS; detailed test execution belongs to Part V.
3. **ISO 18177:2025 — Plastics — Test method for estimation of the short chain branching distribution of semicrystalline ethylene 1-olefin copolymers — DSC** — current branch-distribution measurement route for its stated material scope. Use only within scope; do not generalize it to every polymer or every branching architecture.
4. **ISO 10147:2011 — Pipes and fittings made of crosslinked polyethylene (PE-X) — Estimation of the degree of crosslinking by determination of the gel content** — piping-specific crosslinking measurement route; current/confirmed. The chapter shall distinguish `gel content` from a universal, complete measure of network topology or crosslink density.
5. **ISO 1133-1:2022 / ISO 1133-2:2011** — MFR/MVR characterization context. These standards may support the distinction between a melt-flow QC metric and direct architecture measurement. The chapter shall not convert MFR/MVR into a unique molar mass or distribution.

### 6.3 Primary-literature gate

General definitions and measurement principles may use IUPAC/ISO plus established academic references.

Any retained statement of the form:

`specified architecture feature → specified mechanical / transport / fracture / fusion effect`

requires directly reviewed primary evidence and an explicit transferability statement.

Named PE/PP/PE-X examples shall not be admitted merely because the trend is common knowledge in the plastics industry.

## 7. Quantitative treatment

Chapter 016 is quantitatively important, but equations must clarify architecture rather than imitate a polymer-characterization textbook.

### 7.1 Equations authorized for Technical Outline evaluation

At minimum evaluate inclusion of:

1. Number-average molar mass, `Mn`.
2. Mass-average molar mass, `Mm ≡ Mw`.
3. Molar-mass dispersity, `ĐM = Mm/Mn` (or controlled equivalent notation consistent with the current IUPAC source).
4. Number-average degree of polymerization where useful.
5. A bounded relation between degree of polymerization and molar mass only when assumptions about repeat-unit composition/end groups are explicit.

### 7.2 Quantitative controls

Every retained equation shall state:

- quantity definition;
- symbol and units;
- weighting basis;
- assumptions;
- what measurement can obtain it;
- what it does **not** establish about pipe performance.

Do not introduce an equation that converts `Mn`, `Mw`, `Đ`, branch content, gel fraction, MFR or MVR directly into pressure rating, SCG life, weld strength, permeability or service lifetime.

## 8. Required engineering assets

### 8.1 Figures

Develop original figures for:

1. **FIG-016-001 — Why one “molecular weight” number is not enough** — a population of polymer chains with different lengths and the concept of a distribution.
2. **FIG-016-002 — Molar-mass averages on one distribution** — conceptual placement/weighting of `Mn`, `Mw/Mm` and higher averages without implying a universal distribution shape.
3. **FIG-016-003 — Linear, short-chain-branched, long-chain-branched and network topologies** — explicit distinction between topology categories.
4. **FIG-016-004 — Branch count, branch length and branch distribution are different variables** — prevent “more branching” from being treated as one scalar concept.
5. **FIG-016-005 — Branch point vs crosslink vs entanglement vs physical/covalent network** — permanence/connectivity map.
6. **FIG-016-006 — Architecture evidence chain** — `architecture descriptor → measurement → morphology/property hypothesis → downstream verification → product qualification`.

### 8.2 Tables

At minimum develop:

- **TAB-016-001 — Chain-architecture quantities: term / symbol / units / meaning / common misuse**.
- **TAB-016-002 — Architecture measurement route / quantity observed / directness / principal limitation**.
- **TAB-016-003 — Branching descriptor / what it means / what it does not mean**.
- **TAB-016-004 — Architecture feature → plausible downstream hypothesis → required verification**.
- **TAB-016-005 — Downstream chapter ownership crosswalk**.

### 8.3 Worked interpretation examples

**EX-016-001 — Same `Mw`, different distribution:** construct two simplified chain populations that share a similar mass-average value but differ in `Mn`, `Đ` and distribution shape; show why one average is insufficient.

**EX-016-002 — “High molecular weight” supplier claim:** convert an imprecise supplier statement into a controlled request for `Mn`, `Mw/Mm`, distribution method/calibration, branch information and product qualification evidence.

**EX-016-003 — MFR is not molecular architecture:** compare what an MFR/MVR result can legitimately support versus what requires SEC, branching characterization or rheological/morphological evidence.

### 8.4 Workflow

`Identify architecture claim → define the controlled quantity → identify measurement method and calibration basis → separate direct measurement from inference → state downstream property hypothesis → obtain morphology/property/product evidence → engineering decision boundary`

### 8.5 Checklist

**Before using chain-architecture information in a piping decision**.

## 9. Investigation roadmap

### Investigation 1 — Why does chain architecture matter after polymerization is finished?

Bridge Chapter 015 provenance to Chapter 016 architecture. Establish that architecture is a material state requiring characterization, not a catalyst/process label.

### Investigation 2 — What are chain length, degree of polymerization and molar mass?

Control the dimensional and population concepts. Explain why `molecular weight` and `molar mass` are often mixed in industry and how this book will handle them.

### Investigation 3 — Why does a polymer have multiple molar-mass averages?

Develop `Mn`, `Mw/Mm`, higher averages as needed, distribution functions and dispersity. Show why averages weight the population differently.

Primary assets: `FIG-016-001`, `FIG-016-002`, `TAB-016-001`, `EX-016-001`.

### Investigation 4 — What does SEC/GPC actually measure, and what are its limits?

Explain separation by hydrodynamic size at engineering-use depth; relative calibration versus absolute/light-scattering routes; high-temperature SEC relevance for polyolefins; calibration/composition/branching limitations. Detailed laboratory procedure remains in Part V.

Primary asset: `TAB-016-002`.

### Investigation 5 — What is branching, and why is “more branching” an incomplete statement?

Define branch point and branched chain. Distinguish branch count, branch length, branch placement and topology.

### Investigation 6 — How do short-chain and long-chain branching differ as architecture variables?

Explain short-chain versus long-chain branching as controlled architecture descriptors. Use PE/ethylene-1-olefin systems as the primary piping-relevant example only where direct evidence supports the statement. Introduce ISO 18177:2025 only within its stated scope.

Primary assets: `FIG-016-003`, `FIG-016-004`, `TAB-016-003`.

### Investigation 7 — What are crosslinks and polymer networks?

Distinguish branch point, crosslink, crosslinking, covalent network, physical network and network polymer. Explain PE-X as a piping-relevant example without turning the chapter into the PE-X material-family chapter.

Introduce gel-content logic and ISO 10147:2011 evidence limits.

### Investigation 8 — Where do entanglements fit, and why are they not the same as crosslinks?

Explain topological/physical connectivity at the minimum depth needed for later melt, creep and fracture reasoning. Preserve Chapter 019 ownership of full viscoelastic/rheological treatment.

Primary asset: `FIG-016-005`.

### Investigation 9 — How can architecture influence engineering behaviour without becoming a design rule?

Primary-literature evidence gate for retained architecture→behaviour cases.

Candidate downstream hypotheses include:

- crystallization/morphology sensitivity;
- stiffness/toughness balance;
- melt/rheological behaviour;
- diffusion/permeation;
- creep;
- slow-crack-growth resistance;
- fusion/interdiffusion behaviour.

Every retained case shall state:

`material/system | architecture variable | measurement | downstream quantity measured | confounders | supported conclusion | unsupported conclusion | transferability`.

No universal ranking such as `higher Mw = better pipe`, `broader MWD = better processing`, `more branching = tougher`, or `more crosslinking = stronger` is authorized without bounded evidence.

### Investigation 10 — What architecture information should an engineer request, and where must inference stop?

Close the chapter with the evidence workflow, supplier-data request, checklist, failure lens and handoff to Chapter 017.

Primary assets: `TAB-016-004`, `TAB-016-005`, `FIG-016-006`, `WF-016-001`, `CL-016-001`, `EX-016-002`, `EX-016-003`.

## 10. Primary-evidence gate policy

### Stable terminology / measurement layer

May use current IUPAC terminology and current ISO method scope/status plus established academic references.

### Material-specific architecture layer

Direct primary evidence is required when the manuscript asserts a specific architecture difference for a named resin/catalyst/process/material.

### Architecture-to-property layer

Direct primary evidence is mandatory for a retained named claim linking architecture to:

- crystallinity/morphology;
- modulus/toughness;
- creep;
- SCG/RCP/fatigue;
- diffusion/permeation;
- melt strength/rheology;
- joining/fusion;
- long-term pressure behaviour.

The chapter shall record whether the source measured architecture directly or inferred it from another property.

## 11. Evidence-boundary rules

1. Polymerization route is not measured architecture.
2. One average molar mass is not a molar-mass distribution.
3. `Mw/Mn` or `Đ` does not uniquely define distribution shape.
4. MFR/MVR is not a direct molar-mass distribution measurement.
5. Density is not a direct branching-distribution measurement.
6. Gel content is not automatically a complete crosslink-density or network-topology measurement.
7. Branching is not one scalar variable.
8. Entanglement is not automatically a permanent covalent crosslink.
9. Measured chain architecture is not measured morphology.
10. Measured architecture/morphology is not product qualification.
11. Product qualification is not application/system suitability.

## 12. Common errors the chapter must explicitly address

- Saying “the molecular weight” as though a non-uniform polymer has one unique value.
- Using `Mn`, `Mw` and MFR interchangeably.
- Calling `Mw/Mn` a complete description of MWD.
- Using `PDI` as the preferred controlled term without explaining current `Đ` terminology.
- Assuming SEC calibration is universally absolute.
- Ignoring branching/composition effects on hydrodynamic separation/calibration.
- Equating short-chain branching with long-chain branching.
- Treating branch count, length and distribution as the same parameter.
- Inferring branch distribution directly from density.
- Equating crosslink, branch point and entanglement.
- Equating gel fraction with a complete network architecture.
- Inferring pipe performance directly from `high molecular weight`, `bimodal`, `broad MWD`, `long-chain branched`, `crosslinked` or `high gel content` labels.
- Re-teaching morphology, creep or fracture mechanics that belong to Chapters 017–020.

## 13. Out of scope / controlled cross-reference

Chapter 016 shall introduce but not duplicate full treatments of:

- crystallinity, lamellae, spherulites, amorphous regions and tie molecules — Chapter 017;
- Tg, Tm and thermophysical behaviour — Chapter 018;
- rheology, viscoelasticity, creep, relaxation and time-temperature superposition — Chapter 019;
- fracture, SCG, RCP, fatigue, ESC and ageing — Chapter 020;
- polymer family qualification — Chapters 021 onward;
- detailed SEC/DSC/rheometry laboratory procedures, uncertainty budgets and instrument qualification — Part V;
- joining process physics/qualification — Part VII;
- pressure/mechanical design — Part VIII;
- detailed PE-X product standards and application design beyond the architecture example.

Chapter 015 remains the provenance/mechanism prerequisite and shall not be retaught except where a concise causal bridge is needed.

## 14. Technical style and depth rules

1. Start each Investigation from an engineering question.
2. Prefer population/distribution diagrams over chemistry-heavy derivations where possible.
3. Every quantitative architecture descriptor shall carry a definition and evidence limit.
4. Use `molar mass` in canonical explanatory prose; retain `molecular weight` where required by original standard/source titles or familiar industry language, with the distinction explained once.
5. Keep `architecture → measurement → hypothesis → downstream verification` visible throughout.
6. Use PE/PP as primary piping-relevant examples but do not turn the chapter into a PE or PP family chapter.
7. Use PE-X only to demonstrate network/crosslink concepts and measurement boundaries.
8. Do not infer morphology from architecture without measurement/evidence.
9. Do not infer pipe performance from architecture labels without direct evidence and product qualification.
10. Stop before Chapter 017 morphology and Chapters 019–020 property/failure mechanics.

## 15. Success / acceptance criteria

The CDB is ready for author approval when:

- chain architecture is clearly separated from polymerization provenance;
- molar-mass terminology is controlled;
- `Mn`, `Mw/Mm`, distribution and `Đ` are differentiated;
- SEC/GPC evidence limits are explicit;
- linear/branched/network architectures are separated;
- short-chain and long-chain branching are differentiated;
- branch point/crosslink/network/entanglement concepts are separated;
- MFR/MVR and gel content are bounded as indirect/specific measurements rather than universal architecture substitutes;
- architecture→property claims are gated behind direct primary evidence;
- Chapter 017–020 ownership boundaries are explicit;
- required figures/tables/examples/workflow/checklist are defined;
- no chain-architecture descriptor is allowed to become a piping acceptance criterion by unsupported inference.

The completed chapter will satisfy its Definition of Done only when:

- authoritative terminology is traceable to current IUPAC sources;
- standards identity/status/scope for ISO 16014, ISO 18177, ISO 10147 and any retained additional test standards are validated;
- all retained equations are independently checked;
- all named architecture→property cases pass direct primary-evidence review;
- Technical Review, Standards/Evidence Validation, Editorial/Style Review, Desk Test and Human Approval are complete;
- the final manuscript is placed under the canonical `chapters/` directory before merge to `main`.

## 16. Definition-of-Ready disposition

**Current disposition: DRAFT CDB — AUTHOR APPROVAL REQUIRED.**

After author approval, produce the detailed Technical Outline and active Standards/Evidence Plan, perform Definition-of-Ready verification, and only then begin sequential Engineering Development.
