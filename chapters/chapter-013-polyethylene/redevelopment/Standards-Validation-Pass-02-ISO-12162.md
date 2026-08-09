# Chapter 13 — Standards Validation Pass 02

**Focus:** ISO 12162 / material classification → design stress chain  
**Branch:** `chapter-013-redevelopment`  
**Status:** Partial validation complete; clause-level numerical validation remains open  
**Date:** 2026-08-09

## 1. Authoritative source status verified

The currently published International Standard is **ISO 12162:2009**, Edition 2, published 2009-11. ISO states that this edition was reviewed and confirmed in 2021 and remains current. ISO 12162:1995 is withdrawn and was replaced by ISO 12162:2009.

The public ISO record confirms that ISO 12162:2009:

- establishes classification of thermoplastics materials in pipe form;
- specifies material designation;
- specifies a method for calculating design stress;
- applies to materials intended for pipes and fittings for pressure applications.

Therefore Chapter 13 is correct to use ISO 12162 as the classification / designation / design-coefficient framework, but references to the 1995 edition are obsolete and shall not be used as the publication basis.

## 2. Items that can be validated from the public authoritative ISO record

| Chapter concept | Validation disposition |
|---|---|
| ISO 12162 is the material-classification framework | **VALIDATED** |
| ISO 12162 covers material designation | **VALIDATED** |
| ISO 12162 includes a method for calculating design stress | **VALIDATED** |
| ISO 12162:2009 is the current published edition | **VALIDATED** |
| ISO 12162:1995 is withdrawn | **VALIDATED** |
| Using a separate design-coefficient step conceptually between classification and design stress | **CONSISTENT WITH STANDARD SCOPE/TITLE; exact normative formula still clause-level hold** |

## 3. Items not closed from the public ISO record alone

The public ISO abstract does **not** expose enough normative detail to close the following chapter claims without the authoritative standard text or an equally authoritative clause-level source:

1. the exact current definition and notation for **MRS**;
2. the exact classification/rounding series used to derive MRS from the long-term statistical result;
3. the exact normative design-stress equation and symbol convention;
4. the exact definition, minimum value, selection rules and application limits of design coefficient `C`;
5. the exact normative basis for the illustrative statement `PE100 → MRS = 10 MPa`;
6. any standard-prescribed rounding required after `MRS / C`;
7. any claim that `C = 1.25` is generally applicable to PE100 pressure piping.

These remain **Standards Validation Hold Points**.

## 4. Disposition of Chapter 13 equations and example values

### EQ-013-002 — `σ_s = MRS / C`

**Technical status:** algebraically and dimensionally sound.  
**Standards status:** conceptually consistent with ISO 12162's stated role in calculating design stress, but the exact normative equation, symbols, coefficient definition and rounding rules are not closed from the public ISO record alone.

**Chapter disposition:** retain with explicit Standards Validation hold language. Do not label the equation clause-verified until the full current standard text is checked.

### PE100 → `MRS = 10 MPa`

**Technical/editorial status:** familiar classification interpretation and internally consistent with the chapter example.  
**Standards status:** **NOT YET CLAUSE-VERIFIED** against the full text of ISO 12162:2009 from the public record available in this review.

**Chapter disposition:** retain only as an illustrative example under an explicit validation hold; do not present as a newly standards-verified fact in the validation record.

### `C = 1.25`

**Technical/editorial status:** used only as an illustrative assumed coefficient in the chapter.  
**Standards status:** **NOT VALIDATED AS UNIVERSAL OR PROJECT-APPLICABLE**.

**Chapter disposition:** retain the current wording that the value is illustrative only and that the governing product/application standard must establish the applicable coefficient.

## 5. Product-standard cross-check relevant to the chain

The current published ISO 4427-1:2019 public record confirms for its water / pressure-drainage scope:

- maximum allowable operating pressure (PFA) up to and including 25 bar;
- **20 °C as the reference operating temperature**;
- guidance for other operating temperatures in Annex A;
- responsibility of the purchaser/specifier to select appropriate aspects based on project requirements and installation practices/codes.

ISO 4427-2:2019 likewise states 20 °C as the reference temperature and points to ISO 4427-1 Annex A for other operating temperatures.

This supports the chapter's core separation:

`material classification / reference calculation ≠ unconditional project allowable operating pressure`.

It also supports keeping temperature/service verification after the reference pressure calculation rather than embedding an invented universal derating factor in EQ-013-002 or EQ-013-004.

## 6. Draft-revision awareness

ISO/DIS 4427-1 and ISO/DIS 4427-2 are currently under development and are intended to replace the 2019 editions. They are **drafts**, not the current publication basis. Chapter 13 shall continue to reference the current published 2019 edition for publication validation unless a replacement International Standard is actually published before Design Freeze.

## 7. Standards-validation decision for the MRS / C / design-stress chain

### PASS — framework and source identity

The following are now closed:

- ISO 12162:2009 is the correct current source family/edition for thermoplastics material classification, designation and design-stress methodology;
- the withdrawn 1995 edition shall not be used as the final publication source;
- the chapter architecture that separates classification, design coefficient and design stress is appropriate;
- temperature/application verification belongs outside a bare material-classification calculation.

### HOLD — clause-level numerical/normative details

The following cannot be honestly closed without full current authoritative text:

- exact MRS definition and class/rounding series;
- `PE100 = 10 MPa` as a clause-verified classification statement;
- exact `C` rules and minimum/application-specific values;
- exact design-stress formula notation and rounding requirements.

## 8. Required Chapter 13 publication wording discipline

Until clause-level validation is completed, Chapter 13 shall:

- say **“for illustration only”** for `MRS = 10 MPa`, `C = 1.25` and the resulting worked pressure value;
- state that the applicable `C` must come from the governing standards/design path;
- avoid saying that 1.25 is the universal PE100 coefficient;
- avoid saying that the worked 16 bar result is project allowable pressure;
- retain the explicit post-calculation temperature/service/system verification chain;
- identify ISO 12162:2009 as the current classification/design-stress standard during final references cleanup.

## 9. Pass 02 conclusion

**Decision: PARTIAL PASS / CONTROLLED HOLD.**

No technical contradiction requiring immediate removal of the chapter's MRS → `C` → design-stress logic was found. The current text is appropriately conservative because it labels the example inputs as illustrative and keeps coefficient applicability, rounding and final pressure acceptance behind Standards Validation.

The remaining uncertainty is not an engineering-logic defect; it is a **source-access / clause-level verification gap**. It shall remain explicitly open rather than being filled from memory or secondary sources.
