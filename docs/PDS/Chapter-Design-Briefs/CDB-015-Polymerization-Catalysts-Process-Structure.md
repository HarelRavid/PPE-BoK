# CDB-015 — Chapter Design Brief: From Monomer to Polymer — Polymerization, Catalysts and Process–Structure Relationships

**PDS Baseline:** 1.0  
**Working Chapter:** 015  
**Status:** Approved — Engineering Development Authorized after Definition-of-Ready verification  
**Date:** 2026-08-15  
**Author approval:** 2026-08-15  
**Architecture source:** `BOOK_STRUCTURE.md`  
**Upstream prerequisite:** Chapter 014 — Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers

## 1. Chapter purpose

Develop the polymer-formation bridge between the first-principles molecular chemistry established in Chapter 014 and the real chain architecture developed in Chapter 016.

The chapter shall explain how monomers become macromolecules, why different polymerization mechanisms and catalyst systems can generate different molecular outcomes, and why process history must be treated as part of the material's engineering provenance rather than as irrelevant manufacturing background.

The chapter is not intended to become a reaction-engineering textbook, a catalyst-design monograph or a polymer-manufacturing operating manual. Every mechanism, catalyst concept and process variable shall be included only where it helps a piping engineer understand why nominally similar polymer families or grades may emerge with different architecture and therefore require different downstream characterization, qualification and engineering treatment.

The core engineering chain is:

`monomer / feed → polymerization mechanism → active species / catalyst environment → process conditions → chain-building history → molecular-architecture output → characterization / qualification → piping behaviour`

Chapter 015 owns the chain-building history. Chapter 016 owns the detailed engineering treatment of molecular weight, molecular-weight distribution, branching and crosslinking. Chapter 017 owns morphology. Chapters 018–020 own thermal, viscoelastic and fracture/degradation consequences.

## 2. Primary audience

Practicing mechanical, process, piping, materials, reliability, inspection and owner/EPC engineers who use thermoplastic piping but may not have formal polymer-reaction-engineering training.

Secondary readers include polymer-processing engineers, joining specialists, QA/inspection personnel, manufacturers, procurement engineers and advanced technical students who need to interpret how polymerization route and manufacturing provenance affect the material delivered to a piping project.

## 3. Engineering problem addressed

Two materials may share the same broad polymer family name — or even the same nominal monomer basis — and still differ substantially because the polymer chains were created through different mechanisms, catalyst environments, comonomer strategies and process histories.

The chapter shall answer:

> **How does the route from monomer to polymer create the molecular-architecture possibilities that later control real engineering behaviour, and what can a piping engineer legitimately infer from catalyst/process information before material-specific evidence is required?**

The chapter must prevent two opposite errors:

1. treating polymerization history as irrelevant because the finished product has a family/grade label;
2. treating knowledge of a catalyst or process route as sufficient to predict final pipe performance without characterization and qualification.

## 4. Reader outcomes

After completing the chapter, the reader should be able to:

1. Distinguish monomer, polymerization, chain polymerization, polyaddition and polycondensation using controlled modern terminology.
2. Explain why the older classroom split `addition polymerization versus condensation polymerization` is insufficient as a formal classification and can hide different growth mechanisms.
3. Explain the difference between chain-growth-style behaviour and growth by reactions between molecules of multiple degrees of polymerization without oversimplifying IUPAC terminology.
4. Describe initiation, propagation, termination and chain transfer at the minimum depth needed to understand chain polymerization.
5. Explain radical polymerization as one chain-polymerization route and identify which process variables can alter the chain-building history.
6. Explain coordination polymerization at engineering-use depth, including the distinction between heterogeneous coordination catalysis and homogeneous/metallocene systems.
7. Understand why the industrial term `Ziegler–Natta polymerization` requires controlled use and why current IUPAC terminology prefers the underlying coordination-polymerization description.
8. Explain how catalyst-site environment, monomer/comonomer availability, chain transfer and process conditions can plausibly influence chain length, comonomer placement, stereoregularity and branching tendency without prematurely teaching Chapter 016 as finished material architecture.
9. Explain why temperature, pressure, feed composition, catalyst/initiator system, hydrogen/chain-transfer environment, residence history and reactor/process conditions may become part of the causal provenance of a polymer grade.
10. Use PE and PP as the main controlled industrial examples and use selected other polymer families only where they clarify a distinct polymerization class.
11. Distinguish polymerization-mechanism evidence from commercial-grade qualification and piping-product acceptance.
12. Route the next engineering question to Chapter 016, 017, 018, 019, 020 or the applicable material-family/testing/design chapter.

## 5. Controlled scientific / process inputs

Chapter 015 shall address, where relevant and evidence-supported:

- monomer identity and functionality;
- unsaturation / reactive functional groups;
- monomer and comonomer composition;
- polymerization classification;
- active species / chain carrier;
- initiator, catalyst precursor, catalyst, cocatalyst / activator terminology where applicable;
- radical, ionic and coordination mechanism categories only to useful engineering depth;
- heterogeneous versus homogeneous coordination catalysis;
- catalyst-site environment / site distribution as a hypothesis source;
- polymerization temperature;
- pressure where relevant to monomer state/concentration/process;
- monomer / comonomer concentration and feed ratio;
- chain-transfer environment;
- hydrogen as a controlled polyolefin chain-transfer/process variable only where directly supported;
- residence / reaction history;
- conversion only where it changes the engineering interpretation;
- reactor/process history only to the depth required to explain material provenance;
- polymerization kinetics concepts only where they clarify mechanism or chain-building outcomes.

These are process/mechanism descriptors. They are not product acceptance values.

## 6. Standards and evidence framework

No pressure-piping design standard governs the fundamental reaction mechanisms taught in this chapter. The standards/evidence layer is therefore primarily terminology, nomenclature, direct polymerization science and material-specific primary evidence.

The initial authoritative path shall include:

1. **IUPAC Compendium of Chemical Terminology (Gold Book), 5th ed., online v5.0.0 (2025)** — controlled definitions for polymerization and relevant reaction/mechanism terminology. Version/date shall be captured at final validation because the online compendium is maintained continuously.
2. **IUPAC Purple Book — Compendium of Polymer Terminology and Nomenclature, Recommendations 2008, 2nd ed. published 2009** — polymer terminology/nomenclature framework.
3. **Glossary of Basic Terms in Polymer Science, IUPAC Recommendations 1996, Pure and Applied Chemistry 68, 2287–2311** — source for the classical controlled terms including polymerization, chain polymerization, polyaddition and polycondensation.
4. **Glossary of terms related to kinetics, thermodynamics, and mechanisms of polymerization, IUPAC Recommendations 2008, Pure and Applied Chemistry 80, 2163–2193** — mechanism/kinetics terminology where required.
5. **Terminology for chain polymerization, IUPAC Recommendations 2021, published in Pure and Applied Chemistry 94 (2022), 1093–1147** — current terminology path for coordination polymerization, catalyst precursor/activator language, heterogeneous/homogeneous coordination polymerization and metallocene polymerization.
6. **ISO 472 and ISO 1043-1** only where plastics terminology or polymer abbreviations need controlled cross-reference; neither is to be treated as polymerization-design authority.
7. **Directly reviewed primary literature** for every retained claim that links a named catalyst/process route to a real material-specific architecture/property tendency.

### 6.1 Terminology-control rule

Formal chapter language shall prefer the mechanism-based IUPAC categories rather than the oversimplified historical pair `addition polymerization / condensation polymerization`.

The chapter may introduce **step-growth** as a widely used explanatory concept, but when formal classification is required it shall map the actual process to the appropriate controlled terminology such as `polyaddition` or `polycondensation` rather than silently treating `step-growth polymerization` as a universal normative category.

`Ziegler–Natta` may be retained as established industrial/historical language, but the chapter shall explain that current IUPAC coordination-polymerization terminology distinguishes the underlying heterogeneous coordination-catalysis concept and deprecates reliance on named-reaction terminology as the technical definition.

### 6.2 Evidence boundary

A catalyst/process description may support a **mechanism or architecture hypothesis**.

It does not by itself establish:

- molecular-weight distribution;
- branching distribution;
- comonomer distribution;
- density;
- crystallinity;
- modulus;
- toughness;
- SCG resistance;
- permeability;
- fusion behaviour;
- pressure rating;
- long-term lifetime;
- chemical-service suitability.

Those require characterization, compound/product qualification and downstream engineering evidence.

## 7. Core scientific relationships / quantitative treatment

Chapter 015 is mechanism-led but may include bounded quantitative relationships where they materially improve engineering understanding.

Candidates for Technical Outline evaluation include:

1. Basic rate concepts for chain polymerization only if they help explain why reaction conditions affect chain-building history.
2. Simple degree-of-polymerization / conversion relationships for idealized step-growth systems only if assumptions and limitations are explicit and Chapter 016 ownership is preserved.
3. Qualitative or bounded kinetic-chain relationships for radical polymerization only if symbols, assumptions and validity limits are controlled.
4. Process-variable relationships such as chain-transfer effects only when supported by authoritative mechanism sources and material-specific evidence.

No equation quota is required.

No equation may be used to infer a commercial piping-grade property directly from polymerization chemistry.

## 8. Required engineering assets

### 8.1 Figures

Develop original figures for:

1. **FIG-015-001 — Polymerization classification map** — controlled map of polymerization → chain polymerization / polyaddition / polycondensation, with a warning showing why the historical `addition vs condensation` split is incomplete.
2. **FIG-015-002 — Chain-polymerization lifecycle** — `initiation → propagation → termination / chain transfer`, clearly showing that not every chain polymerization contains every possible event in the same way.
3. **FIG-015-003 — Radical polymerization mechanism at engineering-use depth** — active radical, monomer addition, chain growth, termination / transfer concepts without unnecessary reaction-detail overload.
4. **FIG-015-004 — Coordination-polymerization catalyst environment map** — heterogeneous coordination catalysis / commonly termed Ziegler–Natta versus homogeneous coordination catalysis / metallocene route, with terminology warnings.
5. **FIG-015-005 — Same monomer, different chain-building histories** — conceptual ethene/propene example showing how catalyst/process history can lead to different architecture hypotheses without claiming final grade properties.
6. **FIG-015-006 — Process provenance to engineering evidence chain** — `feed + catalyst/mechanism + process history → chain-building outcome → characterization → compound/product qualification → piping decision`.

### 8.2 Tables

At minimum develop:

- **TAB-015-001 — Polymerization terminology: controlled term / useful meaning / common misuse**.
- **TAB-015-002 — Polymerization route / active-species concept / engineering-relevant outputs / evidence limits**.
- **TAB-015-003 — Catalyst/process variable → plausible chain-building effect → required characterization**.
- **TAB-015-004 — Controlled polymer-family examples and their polymerization route** without becoming a commercial-material ranking table.
- **TAB-015-005 — Downstream chapter ownership crosswalk**.

### 8.3 Worked interpretation examples

Use mechanism/evidence interpretation examples rather than plant operating calculations.

**EX-015-001 — Ethene is the same monomer; why can the resulting polyethylene differ?** Compare two controlled catalyst/process histories and identify what can be hypothesized versus what must be measured.

**EX-015-002 — Why “addition polymer” is not enough information** Classify several simplified polymerization descriptions using current controlled terminology and show which engineering questions remain unanswered.

**EX-015-003 — Process-history evidence request** Given a supplier claim that a catalyst/process route produces “better” pipe performance, build the minimum characterization/qualification evidence request rather than accepting the mechanism claim directly.

### 8.4 Workflow

`Monomer/feed → classify polymerization mechanism → identify active species/catalyst environment → identify process variables → state architecture hypothesis → define characterization → verify grade/product qualification → engineering decision boundary`

### 8.5 Checklist

**Before inferring material behaviour from polymerization route or catalyst history**.

## 9. Investigation roadmap

### Investigation 1 — Why should a piping engineer care how the polymer was made?
Establish polymerization history as material provenance and connect Chapter 014 chemistry to Chapter 016 architecture.

### Investigation 2 — What does “polymerization” actually mean, and how should the reactions be classified?
Control monomer/polymerization terminology, chain polymerization, polyaddition, polycondensation and the limits of `addition/condensation` classroom language.

### Investigation 3 — How does chain polymerization build a macromolecule?
Initiation, propagation, termination and chain transfer at engineering-use depth. Distinguish kinetic chain from polymer chain where required.

### Investigation 4 — How does radical polymerization work, and what process variables matter?
Radical active species, initiator context, propagation, termination/transfer and process-variable hypotheses. No commercial-grade property claims without direct evidence.

### Investigation 5 — How does growth by reactions between molecules of different chain lengths differ from chain polymerization?
Polyaddition/polycondensation concepts, functional-group conversion, stoichiometric sensitivity where relevant, and the bridge to material architecture without turning the chapter into a polymer-synthesis textbook.

### Investigation 6 — What is coordination polymerization?
Monomer coordination, chain carrier, catalyst precursor/activator concepts and the minimum organometallic context needed for polyolefins.

### Investigation 7 — What does “Ziegler–Natta” mean in modern engineering language?
Heterogeneous coordination catalysis, multi-site/heterogeneous environment as a bounded architecture hypothesis, industrial terminology versus controlled IUPAC terminology, and evidence limits.

### Investigation 8 — What changes with homogeneous / metallocene coordination polymerization?
Single-/defined-site concepts only where scientifically justified, stereoregularity/comonomer-placement hypotheses, and direct comparison with heterogeneous catalyst environments without creating a superiority ranking.

### Investigation 9 — How do process variables become molecular-architecture hypotheses?
Temperature, monomer/comonomer feed, pressure/concentration context, chain transfer, hydrogen where appropriate, residence/reaction history and process configuration. Every named-material/process claim requires direct evidence and confounder control.

### Investigation 10 — What may the engineer infer from polymerization provenance, and where must the inference stop?
Formalize the process-provenance evidence workflow, transferability limits, supplier-data questions, downstream chapter routing and the Chapter 016 handoff.

## 10. Primary-evidence gate policy

### Stable mechanism layer
May use authoritative IUPAC recommendations and established academic references for definitions/classification, general reaction-mechanism concepts, initiation/propagation/termination/transfer vocabulary, coordination-polymerization terminology and general catalyst/active-species concepts.

### Material/process-specific layer
Requires directly reviewed primary evidence whenever a retained claim asserts that a named material, catalyst family or process variable produced a specific architecture/property trend.

Each retained case shall record exact feed/material/catalyst system, process variable or catalyst distinction, measured molecular/structural output, measured engineering property if discussed, confounders, supported conclusion, unsupported conclusion and transferability to piping compounds/products.

No commercial catalyst/grade ranking is authorized by default.

## 11. Common errors the chapter must explicitly address

- Teaching `addition polymerization versus condensation polymerization` as a complete modern classification.
- Confusing `chain polymerization` with merely “making a polymer chain.”
- Treating initiation, propagation, termination and chain transfer as mandatory identical steps for every polymerization route.
- Assuming a double bond alone determines the industrial polymerization mechanism.
- Treating `Ziegler–Natta` as a complete catalyst specification.
- Treating every homogeneous coordination catalyst as a metallocene.
- Treating every metallocene-like ligand environment as identical in polymerization behaviour.
- Equating catalyst family with one fixed molecular-weight distribution, branching pattern or comonomer distribution.
- Ignoring process temperature, feed, hydrogen/transfer environment, residence history or reactor configuration.
- Treating processing/manufacturing history as irrelevant after a grade name exists.
- Converting a catalyst/process mechanism directly into pipe strength, SCG, permeability, fusion or lifetime claims.
- Duplicating Chapter 016 architecture, Chapter 017 morphology or later property/qualification chapters.

## 12. Out of scope / controlled cross-reference

Chapter 015 shall introduce but not duplicate full treatments of:

- molecular weight, MWD, branching, crosslinking and detailed chain architecture — Chapter 016;
- crystallinity, lamellae, spherulites, amorphous regions and tie molecules — Chapter 017;
- Tg, Tm and thermophysical behaviour — Chapter 018;
- viscoelasticity, creep and time–temperature superposition — Chapter 019;
- fracture, SCG, RCP, fatigue, ESC and ageing — Chapter 020;
- detailed industrial reactor design, heat/mass-transfer design and polymer-plant operations;
- catalyst synthesis or organometallic chemistry beyond the minimum required for polymerization understanding;
- detailed commercial resin manufacturing recipes or proprietary catalyst formulations;
- detailed polymer compounding / extrusion processing after polymerization;
- material-family qualification and selection — Chapters 021 onward;
- laboratory methods — Part V;
- joining process qualification — Part VII;
- pressure/mechanical design — Part VIII.

Chapter 014 remains the molecular-chemistry prerequisite. Chapter 015 shall not reteach orbitals, hybridization or the ethene bonding model except as a concise bridge into reaction mechanism.

## 13. Technical style and depth rules

1. Begin each Investigation from an engineering question, not a polymer-chemistry syllabus.
2. Use reaction diagrams only where they clarify a mechanism or evidence boundary.
3. Every mechanism drawing shall distinguish conceptual simplification from a full mechanistic scheme.
4. Prefer current IUPAC terminology and explicitly label historical/industrial language when it differs.
5. Keep `mechanism → architecture hypothesis → characterization → qualification` visible throughout.
6. Use PE/PP as primary industrial examples because of their piping relevance, but do not turn the chapter into a PE/PP material-family chapter.
7. Use other polymers only when they demonstrate a genuinely different polymerization class or prevent a misconception.
8. Material/process-specific quantitative claims require direct evidence and transferability limits.
9. Do not infer a final property merely from catalyst family, reactor type or polymerization route.
10. Stop before detailed Chapter 016 architecture treatment; the chapter should explain **how architecture is created**, not fully explain **what architecture does**.

## 14. Success / acceptance criteria

The CDB is approved because:

- the monomer→polymer engineering purpose is clear;
- current polymerization terminology is controlled;
- the historical `addition/condensation` simplification is explicitly bounded;
- radical and coordination polymerization receive engineering-use treatment;
- heterogeneous coordination / Ziegler–Natta and homogeneous/metallocene treatment is defined without false equivalence;
- process-history variables are included as causal provenance without becoming reactor design;
- the Chapter 014→015→016 handoff is explicit;
- primary-evidence gates are defined for catalyst/process-specific claims;
- required figures, tables, examples, workflow and checklist are defined;
- no catalyst/process description is allowed to become a piping acceptance criterion by inference;
- chapter scope can be developed without freezing final book numbering.

The completed chapter will satisfy its Definition of Done only when:

- authoritative terminology claims are traceable to current IUPAC/ISO sources as applicable;
- polymerization-classification language is scientifically controlled;
- radical/coordination mechanism diagrams are scientifically reviewed;
- material/process-specific cases pass direct primary-evidence review;
- every process→architecture bridge states evidence and transferability limits;
- Chapter 016/017 ownership boundaries remain intact;
- Technical Review, Standards/Evidence Validation, Editorial/Style Review, Desk Test and final Human Approval are complete;
- the final chapter manuscript is placed under the canonical `chapters/` directory before merge to `main`.

## 15. Definition-of-Ready disposition

**Current disposition: CDB APPROVED — detailed Technical Outline and active Standards/Evidence Plan required before Engineering Development starts.**

This CDB defines the chapter purpose, scope, audience, inputs, standards/evidence path, investigation roadmap, engineering assets, exclusions and acceptance criteria required by `governance/Definition-of-Ready.md`.

Author approval was recorded on 2026-08-15. The next controlled step is to produce the detailed Technical Outline and active Standards/Evidence Plan, verify the Definition of Ready is complete, and only then begin sequential Investigation authoring.
