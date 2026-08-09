# Chapter 13 — Standards Validation Pass 01

**Chapter:** 013 — Polyethylene (PE)  
**Branch:** `chapter-013-redevelopment`  
**PDS baseline:** 1.0 (frozen)  
**Status:** Standards Validation — Pass 01 complete / further clause-level validation required

## 1. Purpose

Begin the mandatory post-authoring Standards Validation gate using current authoritative ISO catalogue records and official ISO previews where available.

This pass validates **edition/status/scope-level facts** and identifies immediate chapter corrections or hold points. It does not claim clause-level verification where the full normative text has not been reviewed.

## 2. Authoritative current-edition map

| Standard / family | Current authoritative status checked in 2026-08 | Chapter use | Validation disposition |
|---|---|---|---|
| ISO 9080 | **ISO 9080:2012**, Edition 2, published; confirmed current | Long-term hydrostatic strength statistical extrapolation | Current edition identified; replace redevelopment reliance on 2003 edition during final source normalization |
| ISO 12162 | **ISO 12162:2009**, Edition 2, published; confirmed current | Classification, designation, design coefficient / design-stress method | Current edition identified; 1995 copy is obsolete and may not support final normative wording |
| ISO 4427-1 | **ISO 4427-1:2019**, Edition 2, published; revision in progress | General requirements for PE water / pressure-drainage systems | Current published edition identified; recheck immediately before Design Freeze because revision is active |
| ISO 4427-2 | **ISO 4427-2:2019**, Edition 2, published; Amendment 1:2023; revision in progress | PE water / pressure-drainage pipe requirements | Current published edition identified; amendment/revision status must be captured in final source register |
| ISO 4437-1 | **ISO 4437-1:2024**, Edition 2, published; replacement project at FDIS stage | General requirements for PE gaseous-fuel systems | Current published edition identified; recheck immediately before Design Freeze |
| ISO 4437-2 | **ISO 4437-2:2024**, Edition 2, published; expected replacement under active revision | PE gaseous-fuel pipe requirements | Current published edition identified; recheck immediately before Design Freeze |
| ISO 1167-1 | **ISO 1167-1:2006**, Edition 1, published/current | General internal hydrostatic-pressure test method | Current edition identified |
| ISO 1167-2 | **ISO 1167-2:2006**, Edition 1, published/current; confirmed 2025, revision planned | Preparation of pipe test pieces | Current edition identified; revision status noted |
| ISO 1167-3 | **ISO 1167-3:2007**, Edition 1, published/current | Preparation of components | Current edition identified |
| ISO 1167-4 | **ISO 1167-4:2007**, Edition 1, published; under systematic review | Preparation of assemblies | Current edition identified; review status noted |
| ISO 21307 | **ISO 21307:2017**, Edition 3, current, with **Amd 1:2020** | PE butt-fusion jointing procedures | Current edition and amendment identified |
| ISO 13479 | **ISO 13479:2022**, Edition 3, published/current | Notched-pipe hydrostatic SCG test | Current edition identified |
| ISO 18488 | **ISO 18488:2025**, Edition 2, published/current | Strain-hardening modulus in relation to SCG | Chapter reference to the 2015 edition must be updated; 2015 is withdrawn |
| ISO/TR 10358 | **ISO/TR 10358:2021**, Edition 2, published | Combined chemical-resistance data; explicitly includes PE100-RC among PE examples | Useful contextual source only; does not by itself establish PE100-RC pressure-design classification or product-standard acceptance |

## 3. Immediate validation findings

### SV-013-01 — ISO 9080 source age

**Finding:** redevelopment artifacts relied on an available full copy of ISO 9080:2003. The current authoritative edition is ISO 9080:2012.

**Disposition:** final normative/statistical terminology, definitions and any extrapolation-specific statements shall be validated against ISO 9080:2012. The chapter's high-level role description is consistent with the current ISO abstract, but the 2003 edition cannot remain the final source authority.

### SV-013-02 — ISO 12162 source age

**Finding:** redevelopment artifacts relied on an available full copy of ISO 12162:1995. The current authoritative edition is ISO 12162:2009.

**Disposition:** reopen MRS terminology, classification rules, design-coefficient framework, design-stress calculation and rounding rules against ISO 12162:2009 before publication. The 1995 edition remains historical drafting evidence only.

### SV-013-03 — ISO 4427 service terminology

**Finding:** ISO 4427-1:2019 uses a **maximum allowable operating pressure (PFA)** framework for the water / pressure-drainage family and uses 20 °C as the reference operating temperature; guidance for other operating temperatures is stated to be in Annex A.

**Disposition:** Chapter 13 should avoid using `MOP` as a universal PE pressure term. For water-family examples, product-standard terminology should be kept distinct from gas-family terminology. The chapter's neutral term **reference pressure basis** remains technically useful during the generic calculation chain.

### SV-013-04 — ISO 4437 gas-service conditions

**Finding:** ISO 4437-1:2024 states a gas-system MOP up to and including 10 bar at 20 °C reference temperature and an operating-temperature range of −20 °C to 40 °C; for 20 °C to 40 °C, derating coefficients are defined in ISO 4437-5.

**Disposition:** any gas-service numerical example or temperature treatment shall route to ISO 4437-5 rather than reuse a generic factor. This supports the chapter's decision not to universalize one temperature factor.

### SV-013-05 — ISO 4437 is actively moving

**Finding:** ISO 4437-1:2024 and ISO 4437-2:2024 are current published editions, but replacement projects are already in advanced development.

**Disposition:** perform a final current-status check immediately before Design Freeze. Do not cite a draft as the governing published standard unless the project specifically adopts it.

### SV-013-06 — ISO 4427 is actively moving

**Finding:** ISO 4427-1:2019 and ISO 4427-2:2019 remain current published editions, but third-edition revision projects are active; ISO 4427-2 also has Amendment 1:2023.

**Disposition:** source register must identify the amendment and must be rechecked immediately before Design Freeze.

### SV-013-07 — SCG test methods

**Finding:** ISO 13479:2022 is the current notched-pipe hydrostatic SCG method. ISO 18488:2025 is the current strain-hardening-modulus method; ISO 18488:2015 is withdrawn.

**Disposition:** update chapter/reference text from `ISO 18488:2015` to `ISO 18488:2025`. Preserve the chapter's warning that the two methods are different test concepts and are not automatically interchangeable evidence.

### SV-013-08 — PE100-RC status is not closed by catalogue search alone

**Finding:** the official ISO catalogue confirms that the term `PE100-RC` exists in ISO/TR 10358:2021 as an example within the PE family for chemical-resistance data. The available ISO catalogue abstracts/previews reviewed in this pass do **not** establish from themselves that PE100-RC is a separate MRS class, nor do they establish universal product-standard acceptance criteria or a changed design-stress basis.

**Disposition:** keep the chapter's conservative statement: PE100-RC / enhanced-SCG-resistance terminology must be tied to the governing product/application specification and qualification route. Do not state that PE100-RC changes MRS or pressure-rating basis unless the governing current standard explicitly says so. Clause-level/product-standard validation remains open.

### SV-013-09 — Butt fusion reference

**Finding:** ISO 21307:2017 remains current and has Amendment 1:2020.

**Disposition:** standards map/source register should identify the amendment. Detailed procedure content remains out of scope for Chapter 13.

## 4. Technical statements that remain valid at this pass

The following chapter-level engineering positions are supported by the authoritative scope/status information reviewed in Pass 01:

- ISO 9080 is the correct standards family for statistical extrapolation of long-term hydrostatic strength of thermoplastics in pipe form.
- ISO 12162 is the correct standards family for classification/designation and a design-stress calculation method for thermoplastics pressure-piping materials.
- Product/application standards must be identified separately from material classification.
- Water-family and gas-family product standards use different application terminology and service envelopes; therefore `PN`, `PFA`, `MOP` and project allowable pressure shall not be conflated.
- 20 °C is a reference temperature in the ISO 4427 and ISO 4437 families reviewed here, but non-reference-temperature treatment is application-standard dependent.
- SCG qualification routes include fundamentally different test concepts; method identity must remain explicit.
- Butt-fusion procedure requirements belong to a separate joining standard and should not be reproduced as a substitute for that standard.

## 5. Required next validation passes

Pass 01 closes only edition/status/scope-level validation. The following remain mandatory before Design Freeze:

1. **Pass 02 — ISO 12162 / pressure-design chain:** verify current definitions and exact normative relationship for MRS, design coefficient, design stress, rounding and the PE100 example basis.
2. **Pass 03 — Product standards:** verify SDR/pressure designation/marking and service limits for ISO 4427 and ISO 4437, including ISO 4437-5 temperature derating and current amendment/revision status.
3. **Pass 04 — ISO 9080 terminology:** verify current lower statistical bound terminology, reference conditions and engineering interpretation against ISO 9080:2012.
4. **Pass 05 — SCG / PE100-RC:** verify the governing product-standard qualification pathway, current role of ISO 13479:2022 and ISO 18488:2025, and precise limits of the PE100-RC statement.
5. **Pass 06 — final standards sweep:** reopen every standards-derived statement, equation/table label, example value and marking claim in the integrated chapter, then update the source register before Design Freeze.

## 6. Pass 01 decision

**PASS WITH OPEN CLAUSE-LEVEL ITEMS.**

The chapter may continue through Standards Validation. No finding in this pass requires reversal of the chapter architecture or technical reasoning. Several source editions and terminology paths require normalization before publication, most notably ISO 9080:2012, ISO 12162:2009 and ISO 18488:2025.
