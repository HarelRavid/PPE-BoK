# Chapter 011 — Book-Wide Review Package

**Chapter:** 011 — Engineering Characteristics of Common Plastic Piping Materials  
**Review framework:** `docs/BOOK-WIDE-REVIEW-PLAN.md`  
**Branch:** `chapter-013-redevelopment`  
**Status:** REVIEW COMPLETE — REVISION APPROVAL PENDING  
**Disposition:** AUGMENT / FAMILY-COMPARISON AND BOUNDARY REFINEMENT

## 1. Review basis

Reviewed sources:

- `chapters/chapter-011-common-plastic-piping-materials/chapter.md`;
- existing Chapter 011 technical review;
- `chapters/chapter-011-common-plastic-piping-materials/references.md`;
- approved Chapter 010 Rev 1.0 for upstream material-system selection methodology;
- Chapter 012 architecture for downstream long-term pressure classification / MRS / SDR / pressure-rating boundary;
- approved Chapter 009 Rev 1.0 for polymer-fundamentals boundary;
- `docs/BOOK-WIDE-REVIEW-PLAN.md` for review criteria.

No external source was used to introduce new technical or normative claims in this review. Existing material-family and standards statements are evaluated against the chapter's own source register and current manuscript architecture.

---

## 2. Gate A — File and evidence inventory

### Present

- `chapter.md` — research-based qualitative family comparison;
- `references.md` — standards and source register;
- `review.md` — prior technical review, expanded here into the book-wide review package.

### Evidence maturity

The source package already identifies:

- ISO 15494 for covered industrial PE/PP families;
- ISO 15493 for ABS, PVC-U and PVC-C;
- ISO 10931 for PVDF;
- ISO/TR 10358 for chemical-resistance screening;
- ISO 9080 / ISO 12162 for long-term classification context;
- ISO 14692 for GRP/composite context;
- PE100+ Association and polymer-piping textbook sources.

Controlled evidence actions remain before final lock:

- purchased-standard clause-by-clause review;
- ISO 15494 edition-status recheck;
- independent technical sources for each major family;
- deeper evidence for specialty fluoropolymers;
- glossary harmonization for GRP / FRP / RTRP;
- joining-specialist and chemical-engineering review.

**Gate A result: PASS WITH CONTROLLED FAMILY-EVIDENCE HOLDS.**

---

## 3. Gate B — Architecture and scope review

### 3.1 What the chapter already does well

The chapter correctly establishes that:

- material families should not be ranked on one property;
- family names do not define complete piping systems;
- PE, PP, PVC-U/PVC-C, ABS, PVDF, specialty fluoropolymers, lined systems, and composites occupy different engineering roles;
- stiffness, ductility, thermal movement, pressure-temperature behaviour, chemistry, joining, installation, inspection, repair, availability, and cost all matter;
- family-level chemical statements are screening guidance only;
- lined piping is not equivalent to solid-wall thermoplastic piping;
- composite piping requires separate design logic;
- PE100-RC and PE100+ are not interchangeable strength classifications;
- no universal numerical temperature or pressure limits are presented.

This is the correct role for Chapter 011.

### 3.2 Boundary with Chapter 010

Chapter 010 now owns the canonical selection process:

`readiness → candidate systems → hard gates → evidence/uncertainty → comparison → verification → approval`

Chapter 011 should therefore **not repeat a second selection workflow**.

Its job is to provide family-level engineering characteristics used to generate, screen, and challenge candidate systems.

The current Sections 11.10–11.12 partly duplicate Chapter 010 and should be reframed around **how to use family-level information**, not how to approve a final material selection.

### 3.3 Boundary with Chapter 009

Chapter 009 owns polymer physics and data interpretation.

Chapter 011 should use those concepts as background but avoid re-teaching viscoelasticity, morphology, creep theory, or detailed degradation science.

### 3.4 Boundary with Chapter 012

Chapter 012 owns detailed:

- ISO 9080 long-term hydrostatic-strength methodology;
- MRS;
- design coefficient;
- design stress;
- SDR;
- pressure rating.

Chapter 011 should only identify family-specific pressure-performance tendencies qualitatively and direct the reader to product/system data and Chapter 012 for the quantitative chain.

### 3.5 Missing or underdeveloped chapter functions

The main missing or underdeveloped functions are:

1. a single canonical **family-characteristics comparison framework** used consistently across all material sections;
2. explicit distinction between **family-level tendency**, **grade/compound-specific behaviour**, **qualified product data**, and **project system suitability**;
3. a warning that comparative words such as “higher,” “lower,” “better,” or “broader” are only valid within the stated basis and should not become rankings;
4. stronger separation between **candidate-generation guidance** and **final material-selection approval**;
5. consistent treatment of each family across the same domains: structure/behaviour, pressure-temperature, chemistry, mechanics, joining, installation, inspection/repair, special cautions;
6. explicit evidence-status / verification-needs field for qualitative family claims;
7. clearer treatment of **joining method as family characteristic**, not as proof of joint suitability;
8. clearer treatment of **high-purity, fire, electrostatic/conductive, permeation, and regulatory requirements** as project-specific overlays rather than family-wide properties;
9. more explicit warning that **specialty fluoropolymer** claims remain less mature and require product-specific evidence;
10. stronger distinction among **solid-wall thermoplastic, lined, and fibre-reinforced composite** systems;
11. more explicit **repairability and life-cycle supportability** comparison across families;
12. the family comparison table should be reframed as a **screening/characteristics map**, not a quasi-selection table;
13. no canonical figure showing family-level trade-off dimensions;
14. no reader outcomes;
15. final selection sequence/checklist duplicates Chapter 010;
16. handoff to Chapter 012 and later family-specific chapters should be explicit.

**Gate B result: PASS — TARGETED FAMILY-COMPARISON REFINEMENT REQUIRED.**

---

## 4. Gate C — Technical / methodological review

### 4.1 Strong content to retain

The following should remain substantially intact:

- PE family overview and cautions;
- PP-H / PP-B / PP-R distinctions;
- PVC-U / PVC-C distinction;
- ABS positioning;
- PVDF engineering strengths and cautions;
- specialty fluoropolymer / lined-system discussion;
- GRP / FRP / RTRP separation from thermoplastics;
- qualitative comparison table;
- warnings against material-family rankings and generic compatibility charts.

### 4.2 Add one canonical family-characteristics framework

Recommended common comparison domains for each family:

1. **Typical engineering role / where commonly encountered**;
2. **Characteristic mechanical behaviour** — stiffness, ductility, impact, movement;
3. **Pressure-temperature character** — qualitative only;
4. **Chemical / permeation / purity character**;
5. **Joining and fabrication routes**;
6. **Installation and support implications**;
7. **Inspection / repair / life-cycle considerations**;
8. **Critical cautions and evidence limits**.

This will make the material sections more comparable without creating a ranking.

### 4.3 Family tendency is not product qualification

The chapter should explicitly use a four-level interpretation rule:

> **family tendency → compound/grade evidence → qualified product/system evidence → project suitability**

A statement such as “PP is stiffer than PE” may be directionally useful at family level but cannot replace the exact product data required for support or stress calculations.

Likewise, “PVDF has broad chemical resistance” is not a chemical-compatibility approval for a particular grade, fluid, concentration, temperature, and life requirement.

### 4.4 Comparative language needs a defined scope

Words such as:

- higher temperature capability;
- lower permeability;
- better impact performance;
- greater stiffness;
- broader chemical resistance

can be valid as qualitative family guidance, but should be framed as **typical trends**, not universal facts across every grade, test method, and operating condition.

### 4.5 PE / PP / PVC / PVDF content should stop before quantitative design

The chapter should avoid duplicating later chapters by introducing:

- generic allowable temperature values;
- generic pressure derating factors;
- support spans;
- design stresses;
- exact chemical ratings.

The existing draft already largely follows this rule and should continue to do so.

### 4.6 Joining descriptions should remain non-qualifying

Family-level joining summaries are useful, but should state explicitly:

- a family may support a joining route;
- the actual pipe/fitting/compound/system must be qualified for that route;
- equipment, procedure, operator, environment, and inspection still control joint quality.

This avoids the mistaken inference that “PE can be butt fused” means every PE product and project configuration can be joined interchangeably.

### 4.7 Specialty fluoropolymers require a stronger evidence caution

The existing reference register correctly states that PTFE, PFA, and ECTFE treatment is qualitative.

The revised chapter should keep those sections intentionally high-level and add a visible caution that:

- product form matters;
- solid-wall, liner, tubing, sheet, and specialty fabricated systems are not equivalent;
- product-specific standards and supplier data are required before project use.

### 4.8 Lined systems and composites need a construction-class distinction

The current text correctly warns against equivalence.

The revision should sharpen the three-way distinction:

- **solid-wall homogeneous thermoplastic**;
- **lined system** — chemically resistant liner + structural carrier/shell;
- **fibre-reinforced composite** — load-carrying reinforcement + resin matrix.

Each class has different:

- load path;
- joining;
- failure modes;
- inspection;
- repair;
- design standards.

### 4.9 Life-cycle comparison should be more explicit

Family comparison should include not only initial performance but also:

- repair practicality;
- long-term product availability;
- inspection meaning;
- damage tolerance;
- specialist equipment requirements;
- field modification capability.

This supports Chapter 010 without duplicating its approval workflow.

**Gate C result: PASS WITH FAMILY-COMPARISON AND INTERPRETATION AUGMENTATION.**

---

## 5. Gate D — Standards / evidence review

### 5.1 Existing strengths

The chapter already uses a sound standards-neutral qualitative approach:

- major family/system standards are identified;
- chemical tables are framed as screening tools;
- no universal numerical service limits are invented;
- PE100+ is not treated as an ISO strength class;
- composite standards are kept separate from thermoplastic standards.

### 5.2 Controlled evidence holds remain

Before final lock:

- review purchased standards and amendments clause by clause;
- recheck ISO 15494 status;
- add independent technical sources for each major family;
- complete deeper specialty-fluoropolymer standards mapping;
- harmonize composite terminology;
- perform joining-specialist and chemical-engineering review.

### 5.3 Rev 1.0 should not increase normative detail

The correct action is not to add more standard clauses to Chapter 011.

Detailed normative requirements belong in:

- family-specific later chapters;
- Chapter 012 for pressure-classification logic;
- joining chapters;
- application-specific design chapters.

**Gate D result: PASS WITH CONTROLLED EVIDENCE HOLDS.**

---

## 6. Gate E — Editorial and academic review

### Strengths

- readable and practical;
- strong vendor-neutral tone;
- good balance between engineering usefulness and caution;
- useful family-by-family structure;
- no false numerical precision;
- strong lined/composite distinction.

### Editorial / structure gaps

1. No reader outcomes.
2. Family sections do not all use the same comparison framework.
3. Selection sequence/checklist duplicate Chapter 010.
4. Comparative terms need stronger “typical trend” framing.
5. No canonical family-characteristics figure.
6. Qualitative table could more clearly identify its role as screening/context only.
7. Specialty fluoropolymer evidence maturity should be more visible.
8. Final visual/punctuation polish remains deferred to the book-wide cleanup pass.

**Gate E result: PASS — TARGETED AUGMENTATION / DE-DUPLICATION.**

---

## 7. Gate F — Gap Register

| Gap ID | Severity | Finding | Required disposition |
|---|---|---|---|
| GAP-011-01 | High | No canonical comparison framework across material families | Add common family-characteristics domains |
| GAP-011-02 | High | Family tendency / grade / product / system suitability hierarchy not explicit | Add four-level interpretation rule |
| GAP-011-03 | Medium | Comparative words can be over-read as universal ranking | Add typical-trend / basis caution |
| GAP-011-04 | High | Final selection sequence duplicates Chapter 010 | Replace with family-screening-use guidance |
| GAP-011-05 | Medium | Family sections use inconsistent comparison emphasis | Normalize section structure without flattening useful differences |
| GAP-011-06 | Medium | Qualitative evidence maturity not visible per family | Add evidence/verification caution field or closing note |
| GAP-011-07 | Medium | Joining-route descriptions can be over-read as qualification | Add family-route ≠ product/joint qualification rule |
| GAP-011-08 | Medium | High-purity/fire/electrostatic/regulatory overlays are under-framed | Explicitly treat them as application-specific overlays |
| GAP-011-09 | High | Specialty fluoropolymer evidence is less mature | Add visible product-specific evidence caution |
| GAP-011-10 | High | Solid-wall / lined / composite construction distinction should be sharper | Add explicit three-class comparison |
| GAP-011-11 | Medium | Life-cycle repair/supportability comparison is underdeveloped | Add repairability / supportability dimension |
| GAP-011-12 | Medium | Current comparison table can look quasi-prescriptive | Reframe as family-characteristics screening map |
| GAP-011-13 | Medium | No canonical family-level visual | Add `FIG-011-001 — Material Family Engineering Landscape` placeholder |
| GAP-011-14 | Low | No reader outcomes | Add concise outcomes |
| GAP-011-15 | Medium | Engineering checklist overlaps Chapter 010 | Replace with Family Data Use Checklist |
| GAP-011-16 | Low | Handoff to Chapters 010/012 and later family chapters weak | Add explicit ownership boundaries |

---

## 8. Disposition

# AUGMENT / FAMILY-COMPARISON AND BOUNDARY REFINEMENT

The chapter is technically useful and should **not** be rewritten from scratch.

The major revision is to make Chapter 011 the book's canonical **family-characteristics reference layer**:

`family tendency → grade/compound evidence → qualified product/system evidence → project suitability`

It should help engineers generate and challenge candidates without becoming a duplicate of Chapter 010's selection method or Chapter 012's pressure-design framework.

---

## 9. Proposed Chapter 011 Rev 1.0 scope

Recommended revision package:

1. Retain the current material families and most family-specific engineering content.
2. Add concise reader outcomes.
3. Add a canonical family-comparison framework covering mechanical behaviour, pressure-temperature character, chemistry/permeation/purity, joining, installation/support, inspection/repair, and evidence cautions.
4. Add explicit `family tendency → compound/grade → qualified product/system → project suitability` hierarchy.
5. Add a typical-trend caution around comparative terms.
6. Reframe current family sections to use consistent domains without forcing artificial symmetry.
7. Keep PE100/PE100-RC/PE100+ treatment concise and hand detailed pressure implications to Chapter 012.
8. Add explicit `family joining route ≠ qualified project joint` rule.
9. Treat high-purity, fire, electrostatic/conductive, and regulatory requirements as application-specific overlays.
10. Strengthen specialty-fluoropolymer evidence caution and product-form distinctions.
11. Add explicit three-way construction distinction: solid-wall thermoplastic / lined system / fibre-reinforced composite.
12. Strengthen life-cycle repairability and long-term supportability comparison.
13. Reframe the family comparison table as `TAB-011-001 — Material Family Characteristics Map` and state clearly that it is not a selection specification.
14. Add `FIG-011-001 — Material Family Engineering Landscape` conceptual placeholder.
15. Replace the current selection sequence/checklist with a **Family Data Use Checklist** that supports Chapter 010 rather than duplicating it.
16. Add explicit handoff: Chapter 010 owns selection/approval; Chapter 011 owns family-level characteristics; Chapter 012 owns pressure classification and rating.
17. Preserve all existing final-lock evidence actions rather than treating the prose revision as evidence closure.

---

## 10. Approval gate

No substantive change has been made to `chapter.md` in this book-wide review.

If the revision scope above is approved, prepare **Chapter 011 Rev 1.0** as a complete proposed replacement, present the integrated text for review, and only after explicit approval commit the revised manuscript before proceeding to Chapter 012.
