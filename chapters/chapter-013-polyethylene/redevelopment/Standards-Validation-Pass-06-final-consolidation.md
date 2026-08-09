# Chapter 13 — Standards Validation Pass 06

**Scope:** final consolidation of Passes 01–05, validated chapter wording, controlled holds, and Design Freeze source requirements  
**Chapter:** 013 — Polyethylene (PE)  
**Branch:** `chapter-013-redevelopment`  
**Status:** Standards Validation consolidation — controlled holds remain  
**PDS baseline:** 1.0 (frozen)

## 1. Purpose

Consolidate the Standards Validation evidence accumulated in Passes 01–05 and define, in one place:

1. which standards-derived chapter statements are sufficiently validated to retain now;
2. which chapter wording should be normalized immediately;
3. which claims remain blocked until full authoritative clause-level source text is available;
4. the exact source set required before Chapter 13 may proceed to Design Freeze.

This pass does **not** convert a public-catalogue or abstract-level validation into clause-level normative verification. Where the authoritative public record does not expose the needed clause/table/text, the item remains a controlled hold.

---

## 2. Current authoritative source map

| Topic | Current publication basis identified during validation | Chapter role | Status |
|---|---|---|---|
| Long-term hydrostatic extrapolation | **ISO 9080:2012** | Statistical extrapolation / long-term hydrostatic-strength evidence | Current edition identified; clause-level terminology hold remains |
| Material classification / designation / design stress | **ISO 12162:2009** | Classification, designation, design coefficient / design-stress framework | Current edition identified; MRS/C/rounding details require full text |
| Water / pressure-drainage PE pipe product path | **ISO 4427-1:2019**, **ISO 4427-2:2019** (+ Amd 1:2023 for Part 2) | Product/application requirements, PFA terminology, 20 °C reference condition | Published basis identified; active revision requires final edition recheck |
| Gaseous-fuel PE product path | **ISO 4437 series, current 2024 publications**, including **ISO 4437-5:2024** | MOP terminology, 20 °C reference, system fitness, 20–40 °C derating path | Published basis identified; active revision requires final edition recheck |
| Internal hydrostatic pressure testing | **ISO 1167 series** | Test-method navigation | Edition/status identified in Pass 01 |
| Butt fusion | **ISO 21307:2017 + Amd 1:2020** | Chapter-level joining context only | Current source identified |
| Notched-pipe SCG test | **ISO 13479:2022** | SCG qualification/test navigation | Current source identified |
| Strain-hardening SCG test | **ISO 18488:2025** | SCG qualification/test navigation | Current source identified; 2015 edition withdrawn |
| PE100-RC contextual ISO usage | **ISO/TR 10358:2021** | Evidence that the term appears in ISO documentation; not a pressure-design-class authority | Context validated; pressure-design implications remain on hold |
| Reference-line concept | **ISO/TS 26873:2010** | Conceptual regression/reference-line support | Current source identified |

---

## 3. Standards architecture now validated at chapter level

The following Chapter 13 architecture is supported by the authoritative source scopes/statuses reviewed in Passes 01–05 and should be retained:

`pipe-form long-term evidence → statistical extrapolation → conservative lower-bound strength basis → standardized material classification → MRS → applicable design coefficient C → design stress → SDR / nominal geometry → reference pressure basis → governing product/application standard → temperature/time + system verification → engineering disposition`

The following distinctions are also validated at engineering/standards-architecture level:

- material classification is not product qualification;
- product qualification is not installed-system qualification;
- a generic calculated pressure result is not automatically project allowable operating pressure;
- water-service and gas-service standards use different pressure terminology and service frameworks;
- 20 °C is a reference condition in the current ISO 4427 / ISO 4437 public records reviewed;
- non-reference-temperature treatment is standards-path specific;
- SCG test routes are not automatically interchangeable;
- enhanced SCG-resistance terminology does not, by itself, justify changing the pressure-design basis.

---

## 4. Immediate wording normalization approved by Standards Validation

The following wording rules are approved for integration into the Chapter 13 body now.

### 4.1 Generic pressure terminology

Use **reference pressure basis** for the generic result of the MRS/design-stress/SDR arithmetic before product/application/service verification.

Do not use `MOP`, `PFA` or `PN` as universal generic synonyms.

### 4.2 Water-service branch

When explicitly discussing the ISO 4427 path, use **PFA — maximum allowable operating pressure** as the operating-pressure term exposed by the current official ISO public record.

ISO 4427 uses 20 °C as the reference operating temperature in the current published framework reviewed. Non-reference temperatures require the governing ISO 4427 treatment.

### 4.3 Gas-service branch

When explicitly discussing the ISO 4437 path, use **MOP — maximum operating pressure**.

The current ISO 4437-5:2024 public record identifies 20 °C as the reference temperature for design purposes, an operating range of −20 °C to 40 °C, and derating coefficients in Annex A for operation between 20 °C and 40 °C.

### 4.4 PN

Treat `PN` as a standards-defined product pressure designation only within the applicable product framework. Do not equate it generically with PFA, MOP or project allowable pressure without explicit governing-standard support.

### 4.5 Regression terminology

Use deliberately generic wording until full ISO 9080 clause text is checked:

- **lower statistical bound**;
- **conservative lower statistical strength basis**;
- **conservative lower statistical boundary**.

Do not present `LCL`, “lower prediction limit”, “lower confidence limit”, a confidence percentage, or a survival probability as current normative terminology unless verified from the authoritative full text.

### 4.6 Neutral notation at the regression → MRS handoff

Do not use `σ_LCL` as if it were a verified current normative symbol. Prefer prose or a neutral conceptual chain:

`conservative lower statistical strength basis → standardized classification → MRS`

### 4.7 PE100-RC / enhanced SCG resistance

Retain the principle that enhanced SCG-resistance terminology must be tied to the governing product/application specification and qualification route.

Do not state, without authoritative product-standard support, that PE100-RC:

- is a separate MRS class;
- changes design coefficient `C`;
- changes the pressure equation;
- automatically raises allowable pressure;
- permits arbitrary installation damage.

### 4.8 Pipe marking

Retain `TAB-013-002` as an **interpretation** table.

Do not publish a universal mandatory marking-field list, marking frequency, permanence requirement or syntax until the full current product-standard marking clauses are reviewed.

---

## 5. Items sufficiently validated to remain in the chapter

| Chapter claim / asset | Consolidated disposition |
|---|---|
| ISO 9080 is the long-term statistical-extrapolation framework | Retain |
| ISO 12162 is the material classification / designation / design-stress framework | Retain |
| ISO 4427 water path uses PFA and 20 °C reference condition | Retain with service-path context |
| ISO 4437 gas path uses MOP and 20 °C reference condition | Retain with service-path context |
| ISO 4437-5 defines 20–40 °C derating coefficients | Retain as standards-navigation statement; do not reproduce numbers without full clause/table check |
| `reference pressure basis` as chapter-generic terminology | Retain |
| `MRS → C → design stress → SDR → reference pressure basis` as engineering chain | Retain; exact clause/formula/rounding remains held |
| ISO 13479 and ISO 18488 are different SCG test concepts | Retain |
| ISO 18488 current edition is 2025; 2015 is withdrawn | Normalize all references accordingly |
| ISO 21307:2017 has Amd 1:2020 | Normalize source register accordingly |
| Pipe marking identifies product/traceability but does not prove project suitability | Retain |
| Example A arithmetic and unit conversion | Technically verified; standards applicability remains held |
| Example B decision-path logic | Retain |

---

## 6. Controlled holds that block Design Freeze

The following items remain **mandatory full-text source checks** before publication freeze.

### H-013-01 — ISO 12162 classification mechanics

Full current **ISO 12162:2009** text is required to verify:

- exact MRS definition;
- exact PE material designation/classification mapping, including the basis for the illustrative `PE100 → 10 MPa` statement;
- classification/rounding series;
- exact design coefficient `C` definition and selection/minimum rules;
- exact design-stress equation notation;
- required rounding after design-stress calculation.

### H-013-02 — ISO 9080 statistical terminology and method boundaries

Full current **ISO 9080:2012** text is required to verify:

- exact name, definition and notation of the conservative statistical quantity used for classification;
- confidence/prediction terminology, if any;
- test-data requirements;
- permitted extrapolation limits;
- branch / knee criteria and terminology;
- exact interface into the classification value used by ISO 12162.

### H-013-03 — Water product-standard pressure and marking details

Full current **ISO 4427-1:2019** and **ISO 4427-2:2019**, including applicable amendments, are required to verify:

- exact PFA/PN relationships and definitions;
- pressure/S-series/SDR tables and rounding conventions;
- exact temperature-treatment clauses/tables;
- mandatory marking content, frequency and permanence;
- exact product/material designation requirements relevant to Chapter 13.

### H-013-04 — Gas product-standard pressure, RCP, temperature and marking details

Full current **ISO 4437 series** text — especially Parts 1, 2 and 5 — is required to verify:

- exact MOP calculation / pressure-design chain;
- design coefficient application in the current edition;
- PN/MOP relationship where relevant;
- RCP effects or limits on final MOP;
- exact 20–40 °C derating coefficients/table use;
- exact pipe marking content and requirements;
- component/joint limits that affect the generic pressure interpretation.

### H-013-05 — PE100-RC acceptance route

The governing current product/application standard or authoritative normative specification is required to verify:

- whether and how PE100-RC terminology is recognized for the applicable product path;
- required SCG test method(s);
- acceptance threshold(s);
- whether the designation affects material classification, design stress or only adds SCG qualification evidence.

### H-013-06 — SCG method acceptance/equivalence

The governing product/application specification is required to verify:

- when ISO 13479:2022 is required;
- when ISO 18488:2025 is required;
- acceptance values;
- whether any formal equivalence/substitution relationship exists.

---

## 7. Must-have full-text source package before Design Freeze

Chapter 13 shall **not** be marked `standards: pass` until the required normative statements are checked against the following authoritative full-text sources, as applicable to the final wording:

1. ISO 9080:2012.
2. ISO 12162:2009.
3. ISO 4427-1:2019 and current amendments/corrigenda, with edition-status recheck.
4. ISO 4427-2:2019 and Amd 1:2023, with edition-status recheck.
5. Current published ISO 4437 Parts 1, 2 and 5, with edition-status recheck immediately before freeze.
6. ISO 13479:2022 where SCG notched-pipe qualification is cited normatively.
7. ISO 18488:2025 where strain-hardening SCG qualification is cited normatively.
8. ISO 21307:2017 + Amd 1:2020 only for any joining statement that goes beyond standards-navigation context.
9. Any project/national/product specification actually used to assert a PE100-RC acceptance route or marking requirement.

If the final chapter wording does not make a clause-level claim from one of these sources, that source need not be expanded into unnecessary procedural detail; the principle remains to validate only what the chapter actually asserts.

---

## 8. Edition-status recheck rule

A final lifecycle check shall be performed immediately before Design Freeze because the ISO 4427 and ISO 4437 families are in active revision cycles.

The publication basis shall be the current **published** standard adopted by the chapter/project at freeze time. Draft DIS/FDIS documents shall not silently replace the published standard unless the project explicitly chooses to adopt them.

---

## 9. Standards Validation gate decision after Pass 06

**Decision: PARTIAL PASS — PUBLIC-SOURCE VALIDATION COMPLETE; FULL-TEXT CONTROLLED HOLDS REMAIN.**

The standards architecture, source-family selection, current-edition identities, pressure terminology split, reference-temperature logic, SCG-method differentiation, marking interpretation boundary and chapter engineering logic are sufficiently validated to remain.

The chapter is **not yet eligible for Standards Validation PASS / Design Freeze** because several normative details require full authoritative clause/table text.

No evidence from Passes 01–06 requires reversal of the Chapter 13 architecture or Technical Review PASS.

---

## 10. Immediate chapter-integration delta

Before the final full-text closure pass, the integrated README should be normalized to:

1. identify current source editions in the standards map/source notes where useful;
2. use `reference pressure basis` generically, `PFA` on the ISO 4427 branch and `MOP` on the ISO 4437 branch;
3. state explicitly that PFA/MOP/PN are not generic synonyms;
4. replace `σ_LCL` with a neutral lower-statistical-basis description;
5. change FIG-013-003 wording from “lower prediction/confidence boundary” to “conservative lower statistical boundary”;
6. identify ISO 4437-5:2024 as the gas-service 20–40 °C derating route without reproducing coefficients;
7. normalize ISO 18488 references to 2025 and ISO 21307 to include Amd 1:2020;
8. preserve all numerical MRS/C/rounding/pressure examples under explicit clause-level hold language;
9. preserve `TAB-013-002` as non-normative marking interpretation rather than mandatory marking specification;
10. keep `review.standards` in a controlled-hold/pending state until H-013-01 through H-013-06 are closed.

## 11. Consolidated conclusion

Chapter 13 is now **standards-architecture validated and technically bounded**, with a finite, explicit set of normative source-access holds.

The remaining work is no longer exploratory research. It is a controlled clause/table verification exercise against the full authoritative standards listed in Section 7, followed by correction of any affected wording and a final edition-status recheck.