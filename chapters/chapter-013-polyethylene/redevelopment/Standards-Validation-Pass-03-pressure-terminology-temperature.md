# Chapter 13 — Standards Validation Pass 03

**Chapter:** 013 — Polyethylene (PE)  
**Branch:** `chapter-013-redevelopment`  
**Validation focus:** pressure terminology, SDR/design chain context, reference temperature and temperature derating  
**Status:** PARTIAL PASS / CONTROLLED HOLD  
**PDS baseline:** 1.0 (frozen)

## 1. Validation question

Clarify what the current ISO product/application standards support regarding:

- water-service pressure terminology;
- gas-service pressure terminology;
- reference temperature;
- elevated-temperature treatment;
- the relationship between nominal/product pressure designations and project allowable operating pressure;
- whether Chapter 13 should use PFA, MOP, PN, or a neutral `reference pressure basis` label in the generic engineering narrative.

Primary-source basis for this pass is restricted to official ISO records and official ISO standard abstracts/previews that are publicly accessible.

---

## 2. Current ISO 4427 water-service basis

### ISO 4427-1:2019

Official ISO record confirms that ISO 4427-1:2019 is the currently published Part 1 for PE systems for water supply and pressure drainage/sewerage. The public abstract states that the series applies, in conjunction with its other parts, under the following relevant conditions:

- **maximum allowable operating pressure (PFA) up to and including 25 bar**;
- **20 °C as the reference operating temperature**;
- for other operating temperatures, guidance is given in **Annex A**;
- the purchaser/specifier is responsible for making appropriate selections for the particular project and installation practice/code.

The record also shows that ISO 4427-1:2019 is at lifecycle stage `90.92 — to be revised`, with ISO/DIS 4427-1 under development.

### ISO 4427-2:2019 + Amd 1:2023

Official ISO records confirm that ISO 4427-2:2019 remains published and has **Amendment 1:2023**. A replacement ISO/DIS 4427-2 is under development.

### Engineering disposition for Chapter 13

For generic water-service discussion:

- `PFA` is the standards-family operating-pressure term explicitly exposed in the public ISO 4427-1 record.
- The chapter should **not** use `MOP` as the generic water-service label.
- `20 °C` is a validated reference temperature for the ISO 4427 framework.
- Elevated-temperature capability is not automatically equal to the 20 °C pressure basis and must follow the governing ISO 4427 temperature treatment.
- The existing chapter principle that nominal/product pressure information does not by itself establish project allowable operating pressure is supported by the ISO statement that the purchaser/specifier must make the project-appropriate selection.

**Controlled hold:** the public ISO record does not expose enough clause-level text to validate all exact PN/PFA definitions, SDR series, pressure-series tables, marking requirements, or the exact formula that maps material/design stress and SDR to a standardized pressure designation.

---

## 3. Current ISO 4437 gas-service basis

### ISO 4437-1:2024

Official ISO record confirms that ISO 4437-1:2024 is the currently published Part 1 for PE systems for gaseous fuels. The public abstract states:

- **maximum operating pressure (MOP) up to and including 10 bar** at a **reference temperature of 20 °C for design purposes**;
- operating-temperature range **−20 °C to 40 °C**;
- for **20 °C to 40 °C**, derating coefficients are defined in **ISO 4437-5**;
- purchaser/specifier selection remains project-dependent and must consider relevant national regulations and installation practices/codes.

The record also shows that ISO 4437-1:2024 is already at lifecycle stage `90.92 — to be revised`, and an ISO/FDIS 4437-1 replacement is under development.

### ISO 4437-5:2024

Official ISO record confirms that ISO 4437-5:2024 applies to fitness-for-purpose assessment of pipes/fittings/valves/joints in the ISO 4437 system and states:

- **MOP up to and including 10 bar at 20 °C reference temperature for design purposes**;
- operating-temperature range **−20 °C to 40 °C**;
- **derating coefficients for 20 °C to 40 °C are defined in Annex A**.

It also explicitly states that the document is intended for manufacturers/test laboratories for system-component performance assessment and is **not intended for on-site testing of pipe systems**.

### Supporting terminology evidence

The official ISO record for ISO 4437-4:2022 states, for that valve standard, that MOP is considered to be nominal pressure for the purpose of that document and references to ISO 8233. This is standards-context-specific and should not be generalized into a universal PN=MOP rule across all PE applications.

The withdrawn ISO 4437-1:2014 public abstract explicitly stated that MOP was based on design stress determined from compound MRS divided by the C factor, while also taking RCP requirements into account. This historical wording is technically consistent with the chapter architecture, but because the current 2024 public abstract does not expose the same clause-level wording, Chapter 13 should not use the withdrawn edition as the final normative authority.

### Engineering disposition for Chapter 13

For gas-service discussion:

- `MOP` is the validated operating-pressure term exposed in the current ISO 4437 public record.
- `20 °C` is the validated reference temperature for design purposes.
- For service between 20 °C and 40 °C, the chapter should point to the governing derating coefficients in ISO 4437-5 rather than inventing or importing a universal temperature factor.
- The chapter should maintain a distinction between straight-pipe/reference arithmetic and the final gas-system MOP, because the ISO 4437 framework also contains system/component/joint and RCP-related requirements.

**Controlled hold:** the public ISO records do not expose sufficient current-edition clause text to validate the exact MOP formula, all C-factor rules, PN/MOP mapping, SDR table relationships, RCP reduction logic, or rounding requirements.

---

## 4. Terminology rule for Chapter 13

The validation supports the following editorial/engineering rule:

### Generic chapter narrative

Use:

> **reference pressure basis**

for the result of the generic material/design-stress/SDR arithmetic before the governing product/application/service conditions have been fully applied.

This avoids incorrectly importing a service-specific standards term into a generic section.

### Water-service branch

Use:

> **PFA — maximum allowable operating pressure**

when explicitly discussing the ISO 4427 standards path.

### Gas-service branch

Use:

> **MOP — maximum operating pressure**

when explicitly discussing the ISO 4437 standards path.

### PN

Treat `PN` only as a standards-defined pressure designation within the applicable product framework. Do **not** equate PN generically with PFA, MOP or project allowable operating pressure unless the governing standard explicitly establishes the relationship for that context.

### Key chapter rule

`reference pressure basis` → governing product/application standard → service temperature/time treatment → components/joints/system checks → standards-defined operating-pressure designation → project engineering disposition

not:

`PE100 + SDR + familiar formula → universal MOP/PN/PFA`

---

## 5. Temperature-chain validation

The current official records support the chapter's architecture strongly:

### ISO 4427

- 20 °C is the reference operating temperature.
- Other temperatures require additional treatment/guidance under the ISO 4427 framework.

### ISO 4437

- 20 °C is the reference temperature for design purposes.
- Service is addressed over −20 °C to 40 °C.
- For 20 °C to 40 °C, derating coefficients are defined in ISO 4437-5.

### Chapter implication

The wording in Investigation 9 is appropriate:

> the correct engineering question is not "what universal derating factor do I multiply by?" but "what does the governing standards path require for this temperature/service condition?"

No generic numerical temperature factor should be introduced until the applicable service/product standard is fixed and the authoritative clause/table is available.

---

## 6. Required Chapter 13 wording changes from Pass 03

The following changes are recommended before Standards Validation closure:

1. In the chapter standards map, make the pressure terminology distinction explicit:
   - ISO 4427 → PFA / water-service product framework;
   - ISO 4437 → MOP / gaseous-fuel product framework.
2. In Investigation 8, retain `reference pressure basis` as the generic result label.
3. Where the supporting project literature formula is currently introduced as `MOP = 20 MRS/[C(SDR-1)]`, label that occurrence clearly as **supporting-project-literature terminology**, not the chapter's generic normative designation.
4. Add a short terminology note near pipe marking / pressure designation:
   - PFA, MOP and PN are not interchangeable generic synonyms.
5. In Investigation 9 temperature treatment, explicitly name:
   - ISO 4427 Annex A for non-reference water temperatures, subject to clause-level confirmation during final source review;
   - ISO 4437-5 Annex A for gas-service derating between 20 °C and 40 °C.
6. Preserve the rule that project allowable operating pressure requires the complete service/system verification chain.

---

## 7. Validation status matrix

| Item | Status | Evidence basis |
|---|---|---|
| ISO 4427 water pressure term = PFA | PASS | Current official ISO 4427-1:2019 public record |
| ISO 4427 reference temperature = 20 °C | PASS | Current official ISO 4427-1:2019 public record |
| ISO 4427 non-20 °C treatment exists | PASS | Official record points to Annex A |
| ISO 4437 gas pressure term = MOP | PASS | Current official ISO 4437-1:2024 public record |
| ISO 4437 reference temperature = 20 °C | PASS | Current official ISO 4437-1:2024 public record |
| ISO 4437 operating range −20 °C to 40 °C | PASS | Current official ISO 4437-1:2024 / 4437-5:2024 records |
| ISO 4437 derating for 20–40 °C | PASS | Current official ISO 4437-1:2024 and 4437-5:2024 records |
| Generic PN=PFA=MOP equivalence | NOT VALIDATED / DO NOT ASSERT | Standards-context dependent |
| Exact current pressure formula from MRS/C/SDR | CONTROLLED HOLD | Full authoritative clause text required |
| Exact SDR-pressure table / series relationships | CONTROLLED HOLD | Full product-standard text required |
| Exact marking pressure-designation requirements | CONTROLLED HOLD | Full Part 2 / marking clauses required |
| RCP influence on final gas MOP | CONTROLLED HOLD | Full current ISO 4437 clause text required |

---

## 8. Current-standard lifecycle warning

At the date of this review:

- ISO 4427-1:2019 and ISO 4427-2:2019 remain published, with ISO 4427-2 Amd 1:2023, but replacement DIS work is active.
- ISO 4437-1:2024 remains published, but an FDIS replacement is already under development.

Therefore edition numbers and wording must be rechecked immediately before Design Freeze/publication.

---

## 9. Pass 03 disposition

**Decision: PARTIAL PASS / CONTROLLED HOLD**

The standards-family pressure terminology and reference-temperature architecture are now sufficiently validated to support Chapter 13 editorial corrections:

- water branch → PFA;
- gas branch → MOP;
- generic calculation → reference pressure basis;
- 20 °C reference condition retained;
- elevated-temperature treatment remains standards-path specific.

The following remain open for authoritative clause-level validation before publication:

- exact MRS/C/SDR pressure formula and rounding;
- exact PN relationship within each product framework;
- exact SDR series/product tables;
- exact marking requirements;
- RCP-related constraints on gas pressure designation;
- any numerical temperature coefficients used in a worked example.

## 10. Official ISO sources used

- ISO 4427-1:2019 — official ISO record: https://www.iso.org/standard/72183.html
- ISO/DIS 4427-1 — official ISO development record: https://www.iso.org/standard/93677.html
- ISO 4427-2:2019 — official ISO record: https://www.iso.org/standard/72184.html
- ISO 4427-2:2019/Amd 1:2023 — official ISO record: https://www.iso.org/standard/82985.html
- ISO 4437-1:2024 — official ISO record: https://www.iso.org/standard/79721.html
- ISO/FDIS 4437-1 — official ISO development record: https://www.iso.org/standard/90388.html
- ISO 4437-5:2024 — official ISO record: https://www.iso.org/standard/79724.html
- ISO 4437-4:2022 — official ISO record: https://www.iso.org/standard/82300.html
