# Chapter 13 — Standards Validation Pass 05

**Topic:** ISO 9080 regression / lower-bound terminology / reference-line interface / classification handoff  
**Chapter:** 013 — Polyethylene (PE)  
**Branch:** `chapter-013-redevelopment`  
**Status:** Standards Validation evidence  
**PDS baseline:** 1.0 (frozen)

## 1. Purpose

Validate the Chapter 13 engineering narrative around long-term hydrostatic testing, statistical extrapolation, lower-bound interpretation, reference lines and the handoff from regression evidence into material classification.

This pass intentionally distinguishes:

- what can be verified from current official ISO public records;
- what is technically consistent but still requires clause-level authoritative text;
- what terminology should remain deliberately generic until the full standard text is available.

No unsupported statistical terminology, probability statement, equation, clause number or numerical classification rule is introduced in this pass.

---

## 2. Current authoritative edition status

### ISO 9080

Current official ISO record:

- **ISO 9080:2012** — *Plastics piping and ducting systems — Determination of the long-term hydrostatic strength of thermoplastics materials in pipe form by extrapolation*;
- Edition 2, published 2012-10;
- status: Published / Confirmed;
- last confirmed in 2023;
- ISO 9080:2003 is withdrawn and was replaced by ISO 9080:2012.

The official abstract confirms that ISO 9080:2012 specifies a method for predicting long-term hydrostatic strength of thermoplastics materials by **statistical extrapolation**, is applicable to thermoplastics pipe at applicable temperatures, and was developed using test data from pipe systems.

### ISO/TS 26873

Current official ISO record:

- **ISO/TS 26873:2010** — *Plastics pipes and fittings — Definition and construction procedures for reference lines*;
- Edition 1;
- still current and confirmed in 2024.

The official abstract defines reference lines as a generic representation of the **creep rupture properties** of thermoplastics pipes and states that the document gives mathematical procedures for constructing those reference lines.

### ISO 12162 interface

Current official ISO record:

- **ISO 12162:2009** — *Thermoplastics materials for pipes and fittings for pressure applications — Classification, designation and design coefficient*;
- Edition 2;
- current and confirmed;
- establishes classification and designation of thermoplastics materials in pipe form and specifies a method for calculating design stress.

This confirms the standards architecture used by Chapter 13:

`long-term hydrostatic evidence / extrapolation → material classification / designation → design-stress framework`

The exact clause-level mechanics of the handoff remain subject to the controlled hold points below.

---

## 3. Validation of Investigation 5 — long-term testing and extrapolation

### 3.1 Statements supported by the official record

The following Chapter 13 concepts are supported and may remain:

1. Long-term hydrostatic behaviour is established from testing of thermoplastics materials in **pipe form**.
2. The engineering method is based on **statistical extrapolation** rather than waiting for the full intended service life.
3. Temperature is part of the method because ISO 9080 applies at applicable temperatures.
4. The purpose is prediction of **long-term hydrostatic strength**, not qualification of the complete installed piping system.
5. The regression/extrapolation output belongs upstream of material classification and design-stress use.

### 3.2 Statements that should remain qualitative

The Chapter should continue to avoid specifying, unless verified from full authoritative text:

- minimum specimen count;
- mandatory number of stress levels;
- exact test duration requirements;
- exact required temperature spacing;
- permitted extrapolation-time ratios;
- mathematical regression equations;
- statistical confidence percentages;
- branch-selection rules;
- exact treatment of outliers;
- exact rules for detecting or locating a knee.

The current Chapter wording is appropriately qualitative in these areas.

### 3.3 Engineering wording to retain

The Chapter's current statement that accelerated testing is useful only inside a validated extrapolation methodology is technically consistent with the official ISO scope and should remain.

---

## 4. Validation of Investigation 6 — regression interpretation

### 4.1 Mean behaviour versus conservative classification input

The Chapter currently distinguishes:

`observations → fitted behaviour → lower statistical bound → classification input`

The official public ISO records confirm the statistical-extrapolation purpose of ISO 9080 and the separate classification role of ISO 12162. Therefore the architectural distinction is valid.

However, the exact normative name of the conservative statistical quantity is **not resolved from the public ISO record**.

### 4.2 Controlled terminology rule

Until the full authoritative ISO 9080 text is reviewed, Chapter 13 should use one of the following deliberately non-normative phrases:

- **lower statistical bound**;
- **conservative lower statistical strength basis**;
- **lower-bound output from the regression/extrapolation process**.

The Chapter should **not** assert as normative terminology, without clause verification:

- “lower prediction limit”;
- “lower confidence limit”;
- “97.5% lower confidence limit”;
- “LCL” as a universal current ISO 9080 term;
- any probabilistic interpretation such as “97.5% probability that every pipe survives”.

This supports the caution already written in Investigation 6.

### 4.3 Probability interpretation

The existing Chapter warning should remain:

> A conservative statistical bound from the regression framework must not be reinterpreted as a universal survival probability for every manufactured pipe or installed system.

This is an engineering interpretation statement, not a replacement for the exact statistical definition in ISO 9080.

---

## 5. Reference lines and the “knee” concept

ISO/TS 26873:2010 officially confirms that **reference lines** represent generic creep-rupture properties of thermoplastics pipe and can be expressed mathematically.

This supports use of a conceptual regression/reference-line figure in Chapter 13.

### 5.1 What may remain in FIG-013-003

The figure may show conceptually:

- individual test observations;
- fitted or representative long-term behaviour;
- a conservative lower-bound concept;
- a change in slope / branch where relevant;
- the distinction between evidence and classification output.

### 5.2 Controlled hold on “knee” terminology

The public ISO records used in this pass do not expose the exact current ISO 9080 definition, detection rule or normative terminology for a **knee** / change of failure branch.

Therefore Chapter 13 may retain the explanatory wording:

> A change in slope may indicate a transition between different long-term failure behaviours and should prevent uncritical use of one regression branch across the entire time range.

But the Chapter shall not present a normative knee criterion, equation or acceptance rule until the full ISO 9080 text is checked.

---

## 6. Classification interface — what ISO 9080 does and does not establish

A critical distinction is retained:

> ISO 9080 establishes a long-term hydrostatic-strength prediction / extrapolation framework; ISO 12162 is the classification/designation and design-stress interface.

Therefore the Chapter should continue to separate:

`regression output ≠ MRS ≠ design stress ≠ allowable project pressure`

The exact standardized mapping from the regression result to MRS, including classification series and rounding rules, remains a **Pass 02 / clause-level hold** under ISO 12162.

---

## 7. Findings against current Chapter 13 wording

| Chapter item | Validation result | Disposition |
|---|---|---|
| Long-term performance evaluated using pipe-form hydrostatic evidence | Supported by ISO 9080 scope | Retain |
| Statistical extrapolation used to predict long-term strength | Supported by ISO 9080 abstract | Retain |
| Temperature participates in the long-term method | Supported at scope level | Retain qualitatively |
| Regression line is not automatically the design value | Consistent with separate ISO 9080 / ISO 12162 roles | Retain |
| Conservative lower-bound concept | Technically appropriate | Retain generic wording only |
| Exact term “lower prediction/confidence limit” | Not verified from public record | Controlled hold |
| Probability interpretation | Not supported by public record | Continue explicit warning against misuse |
| Knee / branch-change concept | Engineeringly appropriate; exact normative rule not publicly exposed | Retain concept; hold exact rule |
| Reference-line concept | Supported by ISO/TS 26873:2010 | Retain |
| Regression → MRS handoff | Standards architecture supported | Exact mapping remains ISO 12162 hold |
| Specimen counts / stress levels / duration / extrapolation ratios | Not publicly verified | Do not state numerically |

---

## 8. Required Chapter 13 edits resulting from Pass 05

No structural rewrite is required.

Recommended controlled edits before final Standards Freeze:

1. In Investigation 6.2, prefer **“lower statistical bound”** as the primary term.
2. In FIG-013-003 description, use **“conservative lower statistical boundary”** rather than committing to “prediction” or “confidence” terminology until the full text is checked.
3. In Investigation 7.1, avoid using `σ_LCL` as if it were verified current normative notation. Replace it with a neutral symbol or prose until clause-level validation is available.
4. Preserve the explicit sequence:
   `test data → extrapolation/regression → conservative lower-bound basis → standardized classification → MRS → C → design stress`.
5. Keep all exact classification and rounding mechanics under the ISO 12162 controlled hold.

---

## 9. Pass 05 disposition

**Decision: PASS AT ENGINEERING / ARCHITECTURE LEVEL — CONTROLLED TERMINOLOGY HOLD.**

The Chapter 13 treatment of long-term hydrostatic evidence and regression is technically sound and correctly bounded. No physics or engineering-logic correction is required.

Remaining hold points are clause-level and terminology-specific:

- exact name and statistical definition of the conservative lower-bound quantity;
- exact notation;
- exact branch/knee criteria;
- exact test data requirements and extrapolation limits;
- exact regression-output → MRS classification mapping.

These must be resolved from the full authoritative current ISO 9080:2012 and ISO 12162:2009 texts before publication freeze.

---

## 10. Source register for this pass

Official ISO sources used:

- ISO 9080:2012 official ISO standard record and lifecycle page;
- ISO 12162:2009 official ISO standard record and lifecycle page;
- ISO/TS 26873:2010 official ISO standard record and lifecycle page;
- ISO/TC 138/SC 5 official catalogue for status confirmation.

No secondary source was used to close a normative statement in this pass.
