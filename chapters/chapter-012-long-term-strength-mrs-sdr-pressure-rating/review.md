# Chapter 012 — Book-Wide Review Package

**Chapter:** 012 — Long-Term Strength, MRS, Design Stress, SDR and Pressure Rating  
**Review framework:** `docs/BOOK-WIDE-REVIEW-PLAN.md`  
**Branch:** `chapter-013-redevelopment`  
**Status:** REVIEW COMPLETE — REVISION APPROVAL PENDING  
**Disposition:** AUGMENT / PRESSURE-DESIGN CHAIN AND TERMINOLOGY CONTROL

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

The main missing or underdeveloped functions are:

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

### 4.1 Core content to retain

The following are strong and should remain substantially intact:

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

### 4.2 Add one canonical pressure-design chain

Recommended organizing chain:

`pipe test data`
→ `statistical long-term strength basis`
→ `classified material value (e.g. MRS framework)`
→ `application-governed design coefficient / design stress`
→ `pipe geometry / SDR`
→ `product-standard pressure classification`
→ `temperature / time / chemistry / transient / component checks`
→ `project allowable operating / design basis`

The chapter should repeatedly distinguish these levels rather than allowing readers to jump directly from PE100 + SDR to an operating-pressure decision.

### 4.3 Equation applicability must be explicit

Before using:

`p = 2σ / (SDR - 1)`

or the MRS-substituted form, the engineer should confirm that the case actually matches the homogeneous-wall, conventional outside-diameter / wall-thickness pressure-pipe convention used by the governing framework.

The equation should not be presented as automatically valid for:

- multilayer systems;
- lined systems;
- reinforced composites;
- local fittings / branches / fabricated geometry;
- systems governed by another pressure-design convention.

### 4.4 The design coefficient is not a generic safety factor

The chapter currently describes the coefficient carefully, but the revision should make the control stronger:

- it is not selected by personal preference;
- it is not transferable between services by habit;
- it belongs to the relevant application / product / regulatory framework;
- additional reductions or alternative procedures may still apply.

### 4.5 PN / MOP / design pressure need a terminology ownership map

The chapter already says the terms are not interchangeable.

The revision should add a compact map showing that:

- PN belongs to a nominal component/system classification context;
- MOP is defined by specific application standards where used;
- design pressure belongs to the project's governing design basis / code framework;
- operating pressure describes the actual or expected operating condition;
- test pressure belongs to a defined test procedure.

No one term should be back-calculated from another without preserving the governing definition.

### 4.6 The 50-year reference requires careful wording

The current chapter correctly warns that 50 years is not a guaranteed installation life.

The revised text should also avoid over-specifying the exact statistical terminology unless verified against the authoritative standards text.

Preferred manuscript-level language until full-text closure:

- `lower statistical bound`;
- `conservative lower statistical strength basis`;

with exact ISO notation / terminology reserved for the final standards-lock pass.

### 4.7 Worked example needs a stronger educational boundary

The PE100 / SDR 11 / C = 1.25 example is useful and algebraically correct within its stated assumptions.

The revision should label it explicitly as:

- an **illustrative reference-condition example**;
- not a universal PE rule;
- not a chemical-service design;
- not a gas-service design;
- not proof of component or system rating;
- not a substitute for the governing product standard.

### 4.8 Temperature / time should consume Chapter 006 cases

Instead of generic “derating” language alone, the chapter should instruct the reader to evaluate the discrete service cases already defined in Chapter 006:

- continuous hot service;
- short cleaning cycle;
- transient excursion;
- multiple temperature-pressure states;
- test / commissioning case.

This keeps the chapter aligned with the book architecture.

### 4.9 Uncertainty should remain visible

Where the pressure-temperature relationship, chemical reduction, cumulative-time rule, or component limit is uncertain, the chapter should use Chapter 007's discipline:

- bounded assumption;
- sensitivity;
- additional product evidence;
- controlled hold;
- conditional approval.

**Gate C result: PASS WITH PRESSURE-CHAIN, APPLICABILITY AND TERMINOLOGY AUGMENTATION.**

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

### 5.2 Controlled standards holds

Before final lock, the following require authoritative full-text / edition-level verification:

- exact ISO 9080 lower-bound terminology / notation;
- exact MRS classification / rounding / designation rules;
- exact minimum / application design coefficient requirements;
- exact PN and MOP definitions and their product-standard context;
- exact temperature / time / cumulative exposure rules where stated normatively;
- current applicable product-standard parts / editions;
- any future ISO versus ASTM/PPI crosswalk.

### 5.3 Avoid false closure

The existing equation derivation can be technically verified without claiming that every normative term around it has been clause-level verified.

The content revision should therefore distinguish:

- **mathematical verification**;
- **engineering interpretation**;
- **normative standards terminology**.

**Gate D result: PASS WITH CONTROLLED FULL-TEXT STANDARDS HOLDS.**

---

## 6. Gate E — Editorial and academic review

### Strengths

- unusually clear explanation of a difficult pressure-classification topic;
- correct effort to separate material classification from pressure rating;
- strong unit discipline;
- good worked-example structure;
- repeated warnings against catalogue-value misuse;
- useful discussion of chemistry, cyclic service, components and local geometry.

### Editorial / structure gaps

1. No reader outcomes.
2. No single visual chain tying the chapter together.
3. Statistical terminology is more precise than the current full-text evidence allows.
4. PN / MOP / design / operating / test-pressure definitions would benefit from a compact ownership table.
5. The PE worked example can dominate the chapter and should be more explicitly framed as illustrative.
6. The chapter needs a clearer equation-applicability gate.
7. Controlled standards holds should be visible in the chapter.
8. Final punctuation / visual polish remains deferred to the book-wide cleanup pass.

**Gate E result: PASS — TARGETED AUGMENTATION / TERMINOLOGY CONTROL.**

---

## 7. Gate F — Gap Register

| Gap ID | Severity | Finding | Required disposition |
|---|---|---|---|
| GAP-012-01 | High | No canonical classification-to-project-pressure chain | Add chapter-level chain and use it consistently |
| GAP-012-02 | High | Material / pipe / component / system pressure levels can still blur | Add explicit hierarchy |
| GAP-012-03 | High | ISO 9080 lower-bound terminology is more precise than current full-text verification supports | Use neutral controlled terminology pending standards lock |
| GAP-012-04 | High | Exact MRS assignment / rounding rules are not clause-level verified | State that assignment remains standards-governed; do not reconstruct informally |
| GAP-012-05 | High | Design coefficient can still be over-read as a generic material factor | Make application-governed ownership explicit |
| GAP-012-06 | High | Equation applicability gate is implicit | Add explicit homogeneous-wall / governing-framework gate |
| GAP-012-07 | High | Reference-condition classification versus project allowable pressure needs stronger separation | Add controlled distinction |
| GAP-012-08 | Medium | PN / MOP / design / operating / test-pressure terminology needs a compact map | Add `TAB-012-001 — Pressure Terminology and Ownership Map` |
| GAP-012-09 | Medium | Temperature/time section is not fully integrated with Chapter 006 discrete cases | Reframe around service cases |
| GAP-012-10 | Medium | Chapter 007 uncertainty discipline is weakly integrated | Add holds / bounded assumptions / sensitivity route |
| GAP-012-11 | Medium | Worked example can be over-applied | Add explicit illustrative-example boundary |
| GAP-012-12 | Medium | Chapter remains PE-heavy | Keep PE example but state method breadth; add only carefully bounded non-PE references if supported |
| GAP-012-13 | Medium | No canonical process visual | Add `FIG-012-001 — Long-Term Strength to Project Pressure Decision` |
| GAP-012-14 | Medium | No concise classification-level map | Add material → pipe → component → system hierarchy asset |
| GAP-012-15 | Low | No reader outcomes / final verification framing | Add outcomes and pressure-rating verification checklist |
| GAP-012-16 | High | Controlled standards holds are not sufficiently visible in manuscript | Add explicit final-lock standards note |

---

## 8. Disposition

# AUGMENT / PRESSURE-DESIGN CHAIN AND TERMINOLOGY CONTROL

Chapter 012 is technically strong and should **not** be rewritten from scratch.

The major revision should preserve the mathematics and engineering cautions while making the pressure-design logic more controlled:

`long-term test evidence → statistical strength basis → material classification → application design stress → geometry → product pressure classification → project service-case verification → allowable project decision`

The revision should reduce—not increase—unsupported normative precision until the full standards text is available.

---

## 9. Proposed Chapter 012 Rev 1.0 scope

1. Retain the existing long-term-strength, MRS, SDR, PN, pressure-equation, worked-example, chemistry, cyclic-service, and component-limit content.
2. Add concise reader outcomes.
3. Add `FIG-012-001 — Long-Term Strength to Project Pressure Decision`.
4. Add a canonical material → pipe → component → system pressure hierarchy.
5. Use neutral `lower statistical bound` terminology until ISO 9080 full-text terminology is closed.
6. State explicitly that exact MRS classification / rounding / designation rules remain governed by ISO 12162 and the applicable standard.
7. Strengthen the rule that `C` is application-governed and not a generic safety factor.
8. Add an equation-applicability gate before the SDR pressure equations.
9. Preserve the verified algebra and unit conversion.
10. Reframe the PE100 SDR 11 worked example as an illustrative reference-condition example only.
11. Add `TAB-012-001 — Pressure Terminology and Ownership Map` covering PN, MOP, design pressure, operating pressure and test pressure.
12. Connect temperature / time evaluation explicitly to Chapter 006 service cases.
13. Connect uncertain product / chemical / time-at-temperature data to Chapter 007 controls and holds.
14. Keep the chapter method broad while avoiding unsupported non-PE numerical examples.
15. Replace the current general checklist with a **Pressure Rating Verification Checklist** tied to the Design Basis, application standard and complete system.
16. Add an explicit controlled standards-holds note before the final summary.
17. Preserve all final-lock evidence actions rather than treating Rev 1.0 prose revision as standards closure.

---

## 10. Approval gate

No substantive change has been made to `chapter.md` by this book-wide review.

If the revision scope above is approved, prepare **Chapter 012 Rev 1.0** as a complete proposed replacement, present the integrated text for review, and only after explicit approval commit the revised manuscript.
