# Chapter 016 — Investigation 003 Authoring Review

**Date:** 2026-08-16  
**Investigation:** 3 — Why Does a Polymer Have Multiple Molar-Mass Averages?  
**Disposition:** **PASS**

## 1. Review scope

Reviewed the controlled Investigation 3 authoring candidate against CDB-016, the Technical Outline, active Standards/Evidence Plan and current IUPAC definitions for number-average molar mass, mass-average molar mass and dispersity.

## 2. Terminology and equations

**PASS.**

The candidate correctly retains:

- `M_n` as number-average molar mass;
- `M_m ≡ M_w` as mass-average molar mass;
- `Đ_M = M_m/M_n` as molar-mass dispersity;
- `Đ_X = X_m/X_n` as degree-of-polymerization dispersity;
- `PDI` only as familiar legacy/industry terminology, not the controlled preferred term.

Units are correctly dimensional for molar-mass averages and dimensionless for dispersity.

The discrete forms

`M_n = (ΣN_iM_i)/(ΣN_i)`

and

`M_w = (ΣN_iM_i²)/(ΣN_iM_i)`

are mathematically consistent with the IUPAC mass-fraction definitions used in the controlling terminology source.

## 3. Worked-example verification

**PASS.**

EX-016-001 was independently recalculated.

Population A:

- 60 molecules at `80,000 g/mol`;
- 40 molecules at `120,000 g/mol`;
- `M_n = 96,000 g/mol`;
- `M_w = 100,000 g/mol`;
- `Đ_M = 1.041666...`.

Population B:

- 75 molecules at `50,000 g/mol`;
- 25 molecules at `150,000 g/mol`;
- `M_n = 75,000 g/mol`;
- `M_w = 100,000 g/mol`;
- `Đ_M = 1.333333...`.

The example therefore validly demonstrates that equal `M_w` does not imply equal molecular populations or equal dispersity.

The candidate correctly states that the synthetic populations do not establish any material-performance ranking.

## 4. Distribution-shape boundary

**PASS.**

The manuscript correctly distinguishes a scalar dispersity from the full molar-mass distribution and blocks unsupported claims such as:

- high `Đ_M` → bimodal;
- low `Đ_M` → better resin;
- same `M_w` → same architecture;
- higher `M_w` → qualified SCG/fusion/pressure performance.

## 5. Copolymer boundary

**PASS.**

The `Đ_M` / `Đ_X` distinction is retained for compositionally heterogeneous copolymers. The candidate does not generalize the high-DP homopolymer/alternating-copolymer proportionality condition to arbitrary copolymers.

## 6. Asset review

**PASS for authoring stage.**

- `TAB-016-001` has one controlled owner in Investigation 3.
- `FIG-016-001` and `FIG-016-002` have explicit final specifications.
- No real-resin distribution shape or performance implication is embedded in the figure requirements.

## 7. Chapter-boundary review

**PASS.**

The candidate explains architecture statistics and stops before detailed morphology, rheology, fracture/SCG or design treatment.

## 8. Decision

**PASS. Investigation 4 authorized.**

Investigation 4 shall open the ISO 16014 method-scope gate and distinguish what SEC/GPC separates from what detectors/calibration models infer. Detailed laboratory procedure remains deferred to Part V.
