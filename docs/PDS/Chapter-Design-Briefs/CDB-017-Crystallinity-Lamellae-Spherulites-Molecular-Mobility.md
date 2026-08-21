# CDB-017 — Chapter Design Brief: Crystallinity, Lamellae, Spherulites and Molecular Mobility

**PDS Baseline:** 1.0  
**Working Chapter:** 017  
**Status:** Draft — Author Approval Required  
**Date:** 2026-08-21  
**Architecture source:** `BOOK_STRUCTURE.md`  
**Historical scope sources:** `docs/HISTORICAL-KNOWLEDGE-SCOPE-RECOVERY.md`, `docs/MASTER-KNOWLEDGE-SCOPE-MAP.md`  
**Upstream prerequisites:** Chapter 014 — Atomic Structure, Chemical Bonding and Carbon Chemistry; Chapter 015 — From Monomer to Polymer; Chapter 016 — Polymer Chain Architecture

## 1. Chapter purpose

Develop the controlled engineering treatment of **polymer morphology** that sits between chain architecture and bulk thermomechanical, transport, fracture and joining behaviour.

The chapter must preserve the historical depth of two explicit legacy chapters:

- historical Chapter 8 — **Crystallinity**;
- historical Chapter 9 — **Amorphous Regions and Molecular Mobility**.

The redevelopment shall not mark those historical topics as complete merely because crystallinity, amorphous regions or tie molecules are mentioned elsewhere.

Chapter 016 established that chain architecture constrains what structures may form but does not uniquely determine the solid-state morphology. Chapter 017 shall therefore develop the next controlled reasoning chain:

`chain architecture + thermal / deformation / processing history → crystallization and morphology → measured morphological state → downstream property hypothesis → direct property / product verification → engineering decision`

Chapter 017 owns **morphological structure and morphology-characterization logic at engineering-use depth**. It does not own full thermal-transition theory, full viscoelastic constitutive behaviour, fracture/SCG qualification, detailed laboratory SOPs, joining qualification or pipe design.

The chapter must prevent two opposite engineering errors:

1. treating a semicrystalline polymer as a simple two-box mixture of “crystal” and “amorphous” material with no hierarchy, interfaces or connectivity;
2. treating one scalar crystallinity value as sufficient proof of stiffness, toughness, permeability, SCG resistance, weldability or service suitability.

## 2. Primary audience

Practicing mechanical, process, piping, materials, reliability, QA/inspection, procurement and owner/EPC engineers who work with thermoplastic piping but may not have formal polymer-physics, polymer-crystallization or morphology-characterization training.

Secondary readers include polymer-processing engineers, joining specialists, laboratory personnel, resin/pipe manufacturers and advanced technical students.

## 3. Engineering problem addressed

Two specimens made from the same polymer family — and even from the same nominal resin — can differ materially in solid-state morphology because of architecture and processing history.

Relevant variables can include:

- crystalline versus amorphous fraction;
- crystal polymorph where applicable;
- crystallite size / perfection;
- lamellar thickness and organization;
- lamellar stacks and larger superstructures;
- spherulitic organization where applicable;
- amorphous-domain state;
- interlamellar amorphous material;
- tie molecules connecting different crystals;
- chain folds, loops and connecting segments;
- orientation / texture;
- thermal history, cooling rate and annealing;
- deformation / flow / shear history;
- secondary crystallization or morphological reorganization;
- spatial gradients through a molded, extruded or welded product.

Those features may influence engineering behaviour, but they do not bypass the need to measure the relevant downstream property or to qualify the actual pipe, fitting, joint or system.

The governing engineering question is:

> **How should a piping engineer describe and verify polymer morphology — crystalline domains, lamellae, spherulites, amorphous regions, tie molecules and molecular mobility — and how should that morphology be converted into bounded engineering hypotheses without turning morphology into a direct design rule?**

## 4. Reader outcomes

After completing the chapter, the reader should be able to:

1. Distinguish amorphous, crystalline, partially crystalline / semicrystalline and polycrystalline descriptions without using them as loose synonyms.
2. Explain why real engineering thermoplastics can contain crystalline and amorphous domains simultaneously.
3. Distinguish polymer crystal, crystallite, lamellar crystal, lamellar stack and spherulitic organization.
4. Explain chain stems, folding and the connection between chain architecture and crystal formation without implying that every polymer adopts one universal morphology.
5. Explain what an amorphous domain is and why amorphous material in a semicrystalline polymer is not merely “unused space.”
6. Define a tie molecule and explain why tie-molecule population/connectivity is important conceptually while remaining difficult to infer from one routine QC test.
7. Distinguish morphology from molecular architecture, thermal transitions, rheology, fracture behaviour and product qualification.
8. Explain the concept of degree of crystallinity, including mass- and volume-fraction descriptions and the limitations of the ideal two-phase model.
9. Explain why crystallinity values obtained by calorimetry, X-ray methods, density and spectroscopy can differ and should not be treated as automatically interchangeable.
10. Explain what conventional DSC can and cannot establish about melting/crystallization and morphology.
11. Explain how cooling rate, annealing, orientation, shear and processing history can create morphology hypotheses that require direct verification.
12. Explain how morphological heterogeneity can exist through pipe wall, fitting, weld, molded section or aged region.
13. Explain why molecular mobility depends on local environment and morphology but detailed glass-transition and viscoelastic treatment belongs to Chapters 018–019.
14. Translate a supplier or failure-analysis statement such as “higher crystallinity,” “larger spherulites,” “more tie molecules” or “different cooling history” into a controlled evidence request.
15. Route detailed thermal transitions to Chapter 018; viscoelasticity/rheology to Chapter 019; fracture/SCG/fatigue/degradation to Chapter 020; material-family-specific morphology to Chapters 021 onward; detailed laboratory execution to Part V; and fusion/joining consequences to Part VII.

## 5. Controlled terminology

Canonical terminology shall be aligned first to current IUPAC terminology and the 2011 IUPAC Recommendations on crystalline polymers.

Controlled terms shall include, where relevant:

- amorphous state / amorphous domain;
- crystalline polymer;
- polymer crystal;
- polymer crystallite;
- degree of crystallinity;
- mass fraction of crystallinity;
- volume fraction of crystallinity;
- partially crystalline / semicrystalline material where used in engineering practice, with terminology mapping made explicit;
- lamellar crystal / lamella;
- lamellar stack where scientifically supported;
- stem / chain-fold concepts at controlled depth;
- dominant and subsidiary lamellae where useful;
- spherulite;
- polycrystalline polymer;
- tie molecule;
- primary and secondary crystallization where source-supported;
- crystallization / recrystallization / reorganization only with clear process meaning;
- orientation / texture where morphology requires it;
- amorphous molecular mobility as a local structural/dynamic concept, without pre-empting the Chapter 018 glass-transition treatment.

Do not use `crystalline polymer` to imply a perfectly crystalline bulk material.

Do not use `degree of crystallinity` without stating the measurement basis and model assumptions.

Do not use `tie molecule density` as a routine directly measured quantity unless the retained source and method actually establish it.

## 6. Standards and evidence framework

### 6.1 Authoritative terminology path

The initial controlling terminology path shall include:

1. **IUPAC Compendium of Chemical Terminology (Gold Book), 5th ed., online v5.0.0 (2025)** — current terminology layer. Load-bearing terms include crystalline polymer, polymer crystal, polymer crystallite, degree of crystallinity, amorphous domain, spherulite and tie molecule.
2. **Meille et al., Definitions of terms relating to crystalline polymers (IUPAC Recommendations 2011), Pure and Applied Chemistry 83(10), 1831–1871, DOI `10.1351/PAC-REC-10-11-13`** — primary controlled source for polymer crystalline structure, morphology and crystallization terminology.
3. Current IUPAC/Purple Book polymer terminology where the Gold Book entry routes to a foundational term not reproduced in the 2011 Recommendation.

### 6.2 ISO characterization path

The initial ISO path shall include only methods whose public scope has been verified and shall not be represented as universal morphology acceptance standards.

1. **ISO 472:2013 + Amd 1:2018 — Plastics — Vocabulary** — plastics vocabulary cross-check only; publication lifecycle recheck remains required because the edition is in revision lifecycle.
2. **ISO 11357-1:2023 — Plastics — Differential scanning calorimetry (DSC) — Part 1: General principles** — current general DSC framework, Published, stage 60.60 at the 2026-08-21 checkpoint.
3. **ISO 11357-3:2025 — Plastics — Differential scanning calorimetry (DSC) — Part 3: Determination of temperature and enthalpy of melting and crystallization** — current conventional-DSC route for crystalline or partially crystalline plastics, Published, stage 60.60 at the current checkpoint.
4. **ISO 11357-7:2022 — Plastics — Differential scanning calorimetry (DSC) — Part 7: Determination of crystallization kinetics** — current isothermal/non-isothermal crystallization-kinetics route for partially crystalline polymers in stated molten-polymer scope, Published, stage 60.60 at the current checkpoint.
5. **ISO 23976:2021 — Plastics — Fast differential scanning calorimetry (FSC) — Chip calorimetry** — may be cited only where scan-rate / rapid-cooling morphology context materially improves the engineering explanation; detailed method execution remains in Part V.
6. **ISO 1183-1:2025 — Plastics — Methods for determining the density of non-cellular plastics — Part 1** — current density measurement route, Published, stage 60.60. Density may reflect physical structure/composition but is not a direct universal crystallinity measurement.
7. **ISO 6721-1:2019 — Plastics — Determination of dynamic mechanical properties — Part 1: General principles** — downstream dynamic-mechanical/mobility context only. Detailed DMA and linear-viscoelastic interpretation belong to Chapter 019 and Part V.

No generic X-ray-diffraction, SAXS/WAXS or microscopy standard shall be invented merely to fill a standards list. If a specific method standard is required during Engineering Development, its identity, edition, scope and lifecycle shall be directly verified first.

### 6.3 Measurement triangulation rule

The chapter shall explicitly distinguish:

- **calorimetric evidence** — enthalpy/transition response under a specified thermal program;
- **diffraction/scattering evidence** — structural order / periodicity / orientation within method resolution;
- **density evidence** — bulk physical density influenced by morphology and composition;
- **spectroscopic evidence** — method-specific structural signatures;
- **microscopy evidence** — directly imaged morphology at method-dependent spatial scale;
- **dynamic-mechanical / spectroscopic mobility evidence** — local or bulk dynamic response that is not itself a complete morphology map.

A result from one route shall not be silently converted into another route's quantity.

### 6.4 Primary-literature gate

General morphology definitions and measurement principles may use IUPAC/ISO plus established academic references.

Any retained statement of the form:

`specified morphology feature / processing history → specified mechanical / fracture / transport / fusion / ageing effect`

requires directly reviewed primary evidence and an explicit transferability statement.

Examples involving PE, PP, PVDF, PE-X or named piping compounds shall not be admitted merely because the trend is common industry knowledge.

## 7. Quantitative treatment

Chapter 017 shall use equations only when they clarify what a morphology quantity means and what assumptions support it.

### 7.1 Quantities/equations authorized for Technical Outline evaluation

At minimum evaluate:

1. IUPAC degree-of-crystallinity mass fraction `w_c` and volume fraction `ψ_c`.
2. The IUPAC relation connecting mass and volume fraction through sample and crystalline-phase density:

   `w_c = ψ_c ρ_c / ρ`

   only with definitions and two-phase-model assumptions stated.
3. A conventional DSC-based crystallinity calculation of the form `X_c ∝ ΔH_m / ΔH_m^0` only if:
   - the reference enthalpy basis is explicitly material-specific and sourced;
   - filler/reinforcement/additive corrections are controlled where relevant;
   - cold crystallization / multiple melting / reorganization effects are dispositioned;
   - the result is not presented as method-independent absolute truth.
4. Crystallization-kinetics equations such as Avrami-type treatment only if the Engineering Development gate demonstrates clear piping-engineering value and all model assumptions are stated. They are not mandatory.
5. Lamellar-thickness / melting-temperature relations such as Gibbs–Thomson only if directly needed for an engineering explanation and if Chapter 018 ownership is not violated. They are not mandatory.

### 7.2 Quantitative controls

Every retained equation shall state:

- quantity definition;
- units / dimensionless status;
- measurement basis;
- physical model;
- assumptions;
- reference-state data required;
- sensitivity to processing/thermal history where relevant;
- what the quantity does **not** establish about pipe performance.

No equation may convert crystallinity, lamellar thickness, spherulite size, density, tie-molecule hypothesis or DSC enthalpy directly into pressure rating, SCG life, weld strength, permeability limit, design stress or service lifetime.

## 8. Required engineering assets

### 8.1 Figures

Develop original figures for:

1. **FIG-017-001 — Morphology hierarchy from chain to engineering product** — chain architecture → crystal/amorphous domains → lamellae → superstructure → product-scale morphology gradient.
2. **FIG-017-002 — Semicrystalline polymer morphology map** — crystallites/lamellae, amorphous regions, folds/loops and tie molecules without implying one universal morphology.
3. **FIG-017-003 — Lamellar organization and spherulitic growth concept** — show scale hierarchy and explicitly label it as conceptual, not universal.
4. **FIG-017-004 — Processing history → morphology hypothesis** — cooling rate, annealing, orientation/shear and geometry/thickness as hypothesis generators requiring measurement.
5. **FIG-017-005 — Why crystallinity is method-dependent** — DSC / diffraction / density / spectroscopy / microscopy observe different aspects and can legitimately disagree.
6. **FIG-017-006 — Morphology evidence chain** — morphology claim → measurement route → corroboration → downstream property test → product qualification → engineering decision.

### 8.2 Tables

At minimum develop:

- **TAB-017-001 — Morphology terminology / scale / meaning / common misuse**.
- **TAB-017-002 — Morphology characterization route / directly observed quantity / inference / principal limitations**.
- **TAB-017-003 — Processing-history variable / plausible morphology response / required verification**.
- **TAB-017-004 — Morphology feature → plausible downstream hypothesis → required property/product evidence**.
- **TAB-017-005 — Downstream chapter ownership crosswalk**.

### 8.3 Worked interpretation examples

**EX-017-001 — Same resin, different cooling history:** two specimens from the same nominal resin receive different thermal histories. The exercise shall show which morphology differences may be hypothesized and which measurements are required before any property conclusion.

**EX-017-002 — Two crystallinity values disagree:** compare a hypothetical DSC-derived value and an X-ray/density-derived value and explain why disagreement does not automatically mean one method is wrong.

**EX-017-003 — “Higher crystallinity” supplier claim:** convert the statement into a controlled evidence request including method, specimen history, calculation/reference basis, spatial location and downstream property verification.

### 8.4 Workflow

`Identify morphology claim → define the controlled morphology quantity/feature → record specimen/process history → select direct measurement route(s) → distinguish direct observation from model/inference → triangulate if load-bearing → state downstream property hypothesis → verify property/product → engineering decision boundary`

### 8.5 Checklist

**Before using morphology information in a piping decision.**

## 9. Investigation roadmap

### Investigation 1 — Why does morphology matter after chain architecture is known?

Bridge Chapter 016 to Chapter 017. Establish that architecture defines possibilities, while solid-state morphology is created through crystallization and processing history and must be measured.

Key boundary:

`chain architecture → crystallization / packing possibilities`

not

`chain architecture → guaranteed morphology`.

### Investigation 2 — What do amorphous, crystalline, semicrystalline and polycrystalline mean in polymers?

Build the controlled terminology layer using IUPAC. Explain why the ideal two-phase model is useful but incomplete as a literal picture of every real material.

Primary assets: `TAB-017-001` and part of `FIG-017-001`.

### Investigation 3 — How do polymer chains form crystals, stems, folds and lamellae?

Develop chain packing, stems, folded-chain concepts, crystallites and lamellae at engineering-use depth.

Do not turn the chapter into crystallography or reproduce detailed crystal-unit-cell data for every polymer family.

Primary assets: `FIG-017-002`, `FIG-017-003`.

### Investigation 4 — What are spherulites and larger morphological superstructures?

Explain spherulitic organization where applicable, dominant/subsidiary lamellae as useful terminology, orientation/texture and why not every semicrystalline product has one textbook spherulitic morphology.

Connect morphology scale to extrusion, molding and section-thickness history without yet making performance claims.

### Investigation 5 — What happens in the amorphous regions, and what are tie molecules?

Preserve the historical “Amorphous Regions and Molecular Mobility” depth.

Explain amorphous domains, interlamellar material, loops/connecting chains, tie molecules and connectivity concepts. Distinguish tie molecules from entanglements and covalent crosslinks already controlled in Chapter 016.

Do not claim that a routine density, DSC or MFR measurement uniquely determines tie-molecule population.

### Investigation 6 — What is “degree of crystallinity,” and why is it not one method-independent truth?

Develop mass/volume crystallinity concepts, the ideal two-phase assumption and method dependence.

Compare conceptual evidence from DSC, X-ray diffraction/scattering, density, spectroscopy and microscopy. Explain why different techniques can produce different crystallinity estimates.

Primary assets: `FIG-017-005`, `TAB-017-002`, `EX-017-002`.

### Investigation 7 — How does processing and thermal history create morphology?

Treat cooling rate, annealing, reheating, orientation, shear/flow, wall thickness and time history as morphology-hypothesis inputs.

Use ISO 11357-3/-7 only for their method scope. Detailed crystallization kinetics and DSC procedure remain bounded.

Primary assets: `FIG-017-004`, `TAB-017-003`, `EX-017-001`.

### Investigation 8 — What does molecular mobility mean inside a semicrystalline morphology?

Explain why amorphous-chain mobility can be constrained by crystalline domains, interfaces, tie chains and local environment.

Establish the handoff boundaries:

- Chapter 017 owns morphology-dependent mobility concepts;
- Chapter 018 owns `T_g`, `T_m`, thermal transitions and thermophysical behaviour;
- Chapter 019 owns time/frequency-dependent viscoelastic and rheological response.

No full DMA, WLF or time-temperature-superposition treatment belongs here.

### Investigation 9 — How can morphology influence engineering behaviour without becoming a design rule?

Primary-literature evidence gate for retained morphology→behaviour cases.

Candidate downstream questions include:

- modulus / yield / toughness balance;
- craze/crack initiation or SCG resistance;
- diffusion/permeation / free-volume pathways;
- environmental ageing or reorganization;
- fusion/interdiffusion and heat-affected morphology;
- property gradients through pipe wall or fitting section.

Every retained case shall record:

`material/system | morphology variable | processing history | morphology measurement | downstream measurement | confounders | supported conclusion | unsupported conclusion | transferability`.

No universal directional rule such as `higher crystallinity = better pipe` is authorized.

### Investigation 10 — What morphology information should the engineer request, and where must inference stop?

Close the chapter with the final engineering workflow, checklist and supplier/failure-analysis evidence request.

Primary assets:

- `FIG-017-006`;
- `TAB-017-004`;
- `TAB-017-005`;
- `EX-017-003`;
- `WF-017-001`;
- `CL-017-001`.

Final handoff:

`morphological state → thermal transitions / mobility → time-dependent behaviour / fracture / transport / joining evidence`

with those downstream domains kept under their own chapters.

## 10. Required evidence gates before or during Engineering Development

1. **Terminology gate** — current Gold Book + IUPAC 2011 crystalline-polymer Recommendation.
2. **Crystallinity-quantity gate** — mass/volume fraction definitions, two-phase-model assumptions and method-dependence review.
3. **DSC scope gate** — ISO 11357-1:2023, ISO 11357-3:2025 and ISO 11357-7:2022 current scope/lifecycle confirmation.
4. **Density-method gate** — ISO 1183-1:2025 role and limitation; density shall not be treated as unique morphology identification.
5. **Measurement-triangulation gate** — direct observation versus inference for DSC, diffraction/scattering, microscopy, density and spectroscopy.
6. **Tie-molecule / amorphous-connectivity gate** — no named quantitative claim without direct source/method review.
7. **Processing-history gate** — no universal cooling-rate / annealing / orientation → morphology rule without defined system evidence.
8. **Primary morphology→behaviour literature gate** — mandatory for every named case in Investigation 9.
9. **Quantitative equation/units gate** — required before any crystallinity or kinetics equation becomes canonical.
10. **Downstream-ownership gate** — ensure Chapter 017 does not absorb Chapters 018–020, detailed laboratory methods or joining qualification.

## 11. Explicit exclusions

Chapter 017 shall not become:

- a crystallography textbook;
- a complete crystal-unit-cell database for all piping polymers;
- a detailed DSC, WAXS/SAXS, microscopy or density-testing SOP;
- a full glass-transition chapter;
- a full crystallization-kinetics modeling chapter unless the Technical Outline proves the engineering need;
- a DMA/viscoelasticity chapter;
- a fracture-mechanics / SCG qualification chapter;
- a welding/fusion qualification chapter;
- a material-family ranking chapter;
- a direct pressure-design or lifetime-calculation chapter.

## 12. Definition-of-Ready conditions

Engineering Development shall not begin until all are true:

1. Author explicitly approves this CDB or an amended version.
2. CDB status is synchronized from Draft to Approved.
3. Technical Outline defines the exact Investigation sequence, equations, assets and ownership boundaries.
4. Standards/Evidence Plan establishes controlled source IDs and current lifecycle/status checkpoints.
5. Initial terminology / crystallinity / DSC method-scope gates are reviewed sufficiently to support Investigation 1–3 authoring.
6. Primary-literature gate rules for Investigation 9 are explicit.
7. Chapter 016 canonical baseline remains on `main` and Chapter 017 branch is synchronized to that baseline.
8. No unresolved architecture conflict exists with Chapters 018–020 or Part V.
9. Definition-of-Ready review record is written and PASS.

## 13. Acceptance criteria for chapter closure

Chapter 017 can reach Human Approval only when:

- Investigations 1–10 are canonically integrated exactly once;
- historical Crystallinity and Amorphous Regions/Molecular Mobility scope is demonstrably represented at intended depth;
- morphology terminology is IUPAC-controlled;
- all retained equations have passed equation/units/assumption review;
- crystallinity values are always tied to method/model basis;
- DSC, density, diffraction/scattering, microscopy and spectroscopy are not treated as automatically interchangeable;
- every named morphology→behaviour case has passed direct-primary-evidence review;
- no morphology metric is converted directly into piping acceptance or design value;
- controlled figures/tables/examples/workflow/checklist are complete;
- downstream ownership to Chapters 018–020, Part V and Part VII is preserved;
- final full-file Technical Review passes;
- final claim-level Standards/Evidence Review passes with publication holds recorded where necessary;
- final Editorial / Style Review + continuous Desk Test passes;
- explicit Human Approval is recorded before merge.

## 14. Current disposition

**DRAFT CDB — AUTHOR REVIEW REQUIRED. ENGINEERING DEVELOPMENT NOT AUTHORIZED.**

This branch/PR shall contain the CDB only. It shall not create the Chapter 017 manuscript directory, Technical Outline, Standards/Evidence Plan or Engineering Development content before explicit author approval of the CDB.
