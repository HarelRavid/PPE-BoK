# Chapter 012 — Book-Wide Review Package

**Chapter:** 012 — Long-Term Strength, MRS, Design Stress, SDR and Pressure Rating  
**Review framework:** `docs/BOOK-WIDE-REVIEW-PLAN.md`  
**Branch:** `chapter-013-redevelopment`  
**Status:** REVIEW CLOSED — REV 1.0 APPROVED AND INTEGRATED  
**Disposition:** AUGMENT / PRESSURE-DESIGN CHAIN AND TERMINOLOGY CONTROL — COMPLETED

## 1. Review basis

Reviewed sources:

- `chapters/chapter-012-long-term-strength-mrs-sdr-pressure-rating/chapter.md`;
- existing Chapter 012 technical review;
- `chapters/chapter-012-long-term-strength-mrs-sdr-pressure-rating/references.md`;
- approved Chapter 009 Rev 1.0 for polymer-fundamentals boundary;
- approved Chapter 010 Rev 1.0 for material-selection boundary;
- approved Chapter 011 Rev 1.0 for family-characteristics boundary;
- prior Chapter 013 standards-validation findings regarding ISO 9080 / ISO 12162 terminology and controlled holds;
- `docs/BOOK-WIDE-REVIEW-PLAN.md` for review criteria.

No new external source was used to introduce normative claims in this review. The chapter is assessed against its own evidence package and the manuscript architecture already established.

---

## 2. Gate A — File and evidence inventory

### Present

- `chapter.md` — substantial research-based pressure-design draft;
- `references.md` — primary standards and supporting source register;
- `review.md` — prior equation / terminology review, expanded here into the book-wide review package.

### Evidence maturity

The chapter already has a comparatively strong primary-source basis:

- ISO 9080 for long-term hydrostatic-strength extrapolation;
- ISO 12162 for thermoplastic material classification / designation / design coefficient;
- ISO 4427 and ISO 4437 application/product-standard families;
- ISO 15494 industrial-system context;
- ISO 17456 for multilayer long-term strength where relevant;
- PE100+ Association and PPI background sources.

However, the chapter contains several statements whose **exact normative terminology remains dependent on full-text verification**, especially:

- the exact lower-bound / confidence terminology and notation in ISO 9080;
- exact MRS classification / rounding / designation rules;
- exact design-coefficient requirements by application;
- exact PN / MOP / pressure-temperature terminology in product standards;
- the exact role of product-specific derating, time-at-temperature and cumulative exposure rules.

These remain controlled standards holds rather than content facts to be guessed.

**Gate A result: PASS WITH CONTROLLED CLAUSE-LEVEL STANDARDS HOLDS.**

---

## 3. Gate B — Architecture and scope review

### 3.1 What the chapter already does well

The chapter correctly establishes that:

- short-term tensile strength is not the basis of long-term pressure design;
- ISO 9080 provides a long-term statistical extrapolation framework from pipe test data;
- MRS is a classified long-term material value rather than tensile strength or allowable pressure;
- PE100 / PE80 designations should not be misread as pressure or service-life claims;
- PE100-RC and PE100+ describe different qualification / quality concepts;
- design stress is obtained through a coefficient framework rather than by using MRS directly;
- SDR is a geometric ratio, not a pressure rating;
- the hoop-stress / pressure / SDR algebra is dimensionally consistent;
- PN is a nominal classification, not automatically the project operating limit;
- pipe rating is not automatically system rating;
- static pressure classification does not replace cyclic / transient assessment;
- lined / multilayer / local-geometry cases should not be forced into the simple homogeneous-wall equation.

This is the correct canonical role for Chapter 012.

### 3.2 Boundary with Chapter 009

Chapter 009 now owns the conceptual explanation of why long-term polymer behaviour differs from short-term behaviour.

Chapter 012 should therefore begin from that established principle and focus on the **classification-to-pressure chain**, rather than re-teaching viscoelasticity in detail.

### 3.3 Boundary with Chapter 010

Chapter 010 owns material-system selection and requires the selected candidate to pass long-term pressure-temperature verification.

Chapter 012 should provide that verification framework, not repeat candidate-selection governance.

### 3.4 Boundary with Chapter 011

Chapter 011 owns family-level qualitative pressure-temperature tendencies.

Chapter 012 should be the quantitative / standards-mediated layer and should avoid broad material-family comparisons except where required to explain different design frameworks.

### 3.5 Missing or underdeveloped chapter functions

The main missing or underdeveloped functions identified by the review were:

1. one explicit **classification-to-project-pressure chain** that separates material characterization, material classification, design stress, geometry, product classification, and project allowable pressure;
2. clearer distinction among **material value / pipe-classification value / component rating / system allowable pressure**;
3. stronger controlled terminology around the ISO 9080 statistical lower-bound concept pending full-text verification;
4. explicit warning that exact MRS assignment / rounding / designation rules remain standards-governed and should not be reconstructed informally;
5. clearer treatment of the design coefficient as an **application-governed input**, not a generic material constant;
6. a formal **equation applicability gate** before using the simple SDR pressure relation;
7. explicit separation of **reference-condition pressure classification** from project design pressure / MOP / allowable operating pressure;
8. clearer treatment of **PN and MOP as framework-specific terms**, not universal synonyms;
9. stronger link to Chapter 006 service cases so temperature / time / transients are evaluated case by case rather than as generic derating;
10. stronger link to Chapter 007 uncertainty where product data, chemical reduction factors, or service-time rules are incomplete;
11. worked-example governance should be strengthened so the PE100 SDR 11 example is visibly educational and not a reusable project approval;
12. the chapter is currently PE-heavy and should either add carefully bounded non-PE examples or explicitly state that the worked example is illustrative only while the method is broader;
13. no canonical `FIG-012-001` showing the test-data → classification → design-stress → geometry → pressure chain;
14. no compact terminology map showing PN / MOP / design pressure / operating pressure / test pressure ownership;
15. final checklist should be reframed as a **pressure-rating verification checklist** linked to the Design Basis and application standard;
16. standards / evidence holds should be surfaced in the manuscript rather than existing only in the review record.

**Gate B result: PASS — TARGETED PRESSURE-CHAIN AND TERMINOLOGY REFINEMENT REQUIRED.**

---

## 4. Gate C — Technical / methodological review

### 4.1 Core content retained

The revision retained the strong existing content:

- short-term-strength warning;
- long-term pipe-test framing;
- MRS interpretation cautions;
- PE100 / PE80 clarification;
- PE100-RC / PE100+ distinction;
- design-stress relationship concept;
- SDR definition;
- pressure / hoop-stress / SDR derivation;
- unit conversion to bar;
- PE100 SDR 11 worked example;
- PN cautions;
- MOP / operating / design / test pressure distinction;
- temperature/time, chemistry, cyclic/transient, component and geometry limitations;
- system-rating cautions.

### 4.2 Canonical pressure-design chain

Rev 1.0 now organizes the chapter around:

`long-term pipe-test evidence`
→ `statistical strength basis`
→ `material classification`
→ `application design stress`
→ `pipe geometry / SDR`
→ `product pressure classification`
→ `project service-case verification`
→ `allowable project decision`

The revised manuscript explicitly prevents jumping directly from material classification plus SDR to a project operating-pressure conclusion.

### 4.3 Equation applicability

Rev 1.0 adds a formal equation-applicability gate before:

`p = 2σ / (SDR - 1)`

or the MRS-substituted form is used.

The revised chapter explicitly excludes automatic application to:

- multilayer systems;
- lined systems;
- reinforced composites;
- local fittings / branches / fabricated geometry;
- systems governed by another pressure-design convention.

### 4.4 Design coefficient control

Rev 1.0 makes explicit that the design coefficient:

- is not selected by personal preference;
- is not transferable between services by habit;
- belongs to the relevant application / product / regulatory framework;
- may be supplemented by additional reductions or alternative procedures.

### 4.5 PN / MOP / design-pressure terminology

Rev 1.0 adds `TAB-012-001 — Pressure Terminology and Ownership Map` distinguishing:

- PN;
- MOP;
- design pressure;
- operating pressure;
- test pressure;
- allowable project pressure.

The table is explicitly interpretive and does not replace the governing standard definitions.

### 4.6 Statistical terminology

Rev 1.0 replaces over-precise manuscript language with controlled wording such as:

- `statistical strength basis`;
- `conservative lower statistical long-term strength basis`.

Exact ISO notation / terminology remains reserved for the full-text standards-lock pass.

### 4.7 Worked-example boundary

The PE100 / SDR 11 / C = 1.25 worked example remains because its algebra is useful and previously verified.

Rev 1.0 now states explicitly that it is:

- an illustrative reference-condition example;
- not a universal PE rule;
- not a chemical-service design;
- not a gas-service design;
- not proof of component or system rating;
- not a substitute for the governing product standard.

### 4.8 Temperature / time integration

Rev 1.0 connects pressure verification to Chapter 006 service cases rather than treating temperature merely as a generic derating note.

### 4.9 Uncertainty integration

Rev 1.0 connects missing product, chemical, time-at-temperature, component, and service evidence to Chapter 007 controls:

- bounded assumption;
- sensitivity;
- additional evidence;
- controlled hold;
- conditional or no-go disposition.

**Gate C result: PASS — REV 1.0 IMPLEMENTED.**

---

## 5. Gate D — Standards / evidence review

### 5.1 Existing strengths

The evidence package correctly identifies:

- ISO 9080 as the long-term hydrostatic extrapolation framework;
- ISO 12162 as the material classification / designation / design-coefficient framework;
- ISO 4427 and ISO 4437 as application-specific PE system families;
- ISO 15494 as industrial-system context;
- ISO 17456 as relevant to multilayer long-term strength;
- PPI / ASTM terminology as a related but non-identical framework;
- PE100+ Association as an industry source rather than an ISO strength-class authority.

### 5.2 Controlled standards holds remain open

Before final lock, the following still require authoritative full-text / edition-level verification:

- exact ISO 9080 lower-bound terminology / notation;
- exact MRS classification / rounding / designation rules;
- exact minimum / application design coefficient requirements;
- exact PN and MOP definitions and their product-standard context;
- exact temperature / time / cumulative exposure rules where stated normatively;
- current applicable product-standard parts / editions;
- any future ISO versus ASTM/PPI crosswalk.

### 5.3 No false standards closure

Rev 1.0 preserves the distinction between:

- **mathematical verification**;
- **engineering interpretation**;
- **normative standards terminology**.

The equation derivation is technically verified; the controlled standards holds above are not closed by the prose revision.

**Gate D result: PASS WITH CONTROLLED FULL-TEXT STANDARDS HOLDS.**

---

## 6. Gate E — Editorial and academic review

### Strengths retained

- clear explanation of pressure-classification logic;
- strong separation of material classification from pressure rating;
- unit discipline;
- bounded worked example;
- repeated warnings against catalogue-value misuse;
- chemistry, cyclic-service, component and local-geometry cautions.

### Rev 1.0 editorial / structure closures

- reader outcomes added;
- canonical pressure-design chain added;
- statistical wording reduced to evidence-supported precision;
- pressure terminology map added;
- worked example explicitly bounded;
- equation applicability gate added;
- controlled standards holds made visible in the chapter.

Final punctuation / visual polish remains deferred to the book-wide cleanup pass.

**Gate E result: PASS — CONTENT REVISION COMPLETE.**

---

## 7. Gate F — Gap Register

| Gap ID | Severity | Finding | Final status |
|---|---|---|---|
| GAP-012-01 | High | No canonical classification-to-project-pressure chain | CLOSED — chain added |
| GAP-012-02 | High | Material / pipe / component / system pressure levels can blur | CLOSED — hierarchy added |
| GAP-012-03 | High | ISO 9080 lower-bound terminology too precise for current verification | CLOSED FOR CONTENT — neutral terminology adopted; exact terminology remains final-lock hold |
| GAP-012-04 | High | Exact MRS assignment / rounding rules not clause-level verified | CLOSED FOR CONTENT — manuscript defers to governing standard; final-lock hold remains |
| GAP-012-05 | High | Design coefficient can be over-read as generic material factor | CLOSED — application-governed ownership explicit |
| GAP-012-06 | High | Equation applicability gate implicit | CLOSED — explicit gate added |
| GAP-012-07 | High | Reference classification versus project allowable pressure insufficiently separated | CLOSED — controlled hierarchy added |
| GAP-012-08 | Medium | Pressure terminology map missing | CLOSED — `TAB-012-001` added |
| GAP-012-09 | Medium | Temperature/time weakly integrated with Chapter 006 cases | CLOSED — service-case integration added |
| GAP-012-10 | Medium | Chapter 007 uncertainty discipline weakly integrated | CLOSED — assumptions / holds / dispositions added |
| GAP-012-11 | Medium | Worked example can be over-applied | CLOSED — illustrative boundary added |
| GAP-012-12 | Medium | Chapter PE-heavy | CLOSED FOR CONTENT — PE example retained as explicitly illustrative; unsupported numerical expansion avoided |
| GAP-012-13 | Medium | No canonical pressure-design visual | CLOSED — `FIG-012-001` added |
| GAP-012-14 | Medium | No classification-level map | CLOSED — `FIG-012-002` / hierarchy added |
| GAP-012-15 | Low | No reader outcomes / final verification framing | CLOSED — outcomes and release check added |
| GAP-012-16 | High | Standards holds not sufficiently visible in manuscript | CLOSED FOR CONTENT — explicit standards-holds section added; holds themselves remain open for final lock |

---

## 8. Final disposition

# AUGMENT / PRESSURE-DESIGN CHAIN AND TERMINOLOGY CONTROL — COMPLETED

Chapter 012 Rev 1.0 was explicitly approved and integrated into:

`chapters/chapter-012-long-term-strength-mrs-sdr-pressure-rating/chapter.md`

Integration commit:

`809b0f6c329bbf82918406ec5977c3d89a85ba21`

The content revision is closed.

The following are **not** reopened as content gaps and remain controlled final-lock actions:

- clause-level ISO 9080 / ISO 12162 terminology verification;
- exact MRS assignment / designation checks;
- application-specific coefficient checks;
- PN / MOP product-standard terminology checks;
- non-PE product-standard examples where desired and supported;
- ISO versus ASTM/PPI crosswalk;
- final figures;
- final cross-references;
- independent technical review;
- final visual / punctuation cleanup.

Any new substantive change to Chapter 012 after this closure should be recorded as a new finding or as a deliberate reopening of an existing controlled hold.

---

## 9. Book-wide review status

With Chapter 012 Rev 1.0 approved and integrated, the planned **Chapter 000–012 book-wide content review sequence is complete**.

The next phase is book-wide integration and final-lock preparation rather than another first-pass chapter review.
