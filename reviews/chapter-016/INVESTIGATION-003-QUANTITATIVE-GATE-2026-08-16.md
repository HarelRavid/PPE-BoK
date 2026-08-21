# Chapter 016 — Investigation 003 Quantitative / Equation / Units Gate

**Date:** 2026-08-16  
**Investigation:** 3 — Why Does a Polymer Have Multiple Molar-Mass Averages?  
**Disposition:** **PASS**

## 1. Authoritative definitions checked

Current IUPAC Gold Book / IUPAC 2014 Recommendations were checked for:

- `molar-mass average` — 12215;
- `number-average molar mass` — 12216;
- `mass-average molar mass` — 12217;
- `molar-mass dispersity` — 12224;
- `degree-of-polymerisation dispersity` — 12225;
- `dispersity` — 12226.

## 2. Equation verification

### 2.1 Number-average molar mass

Retained discrete-population form:

`M_n = (Σ N_i M_i)/(Σ N_i)`

PASS.

This is the number-count representation corresponding to the IUPAC mass-fraction form:

`M_n = 1/Σ(w_M/M)`.

Units: molar mass (`g mol^-1` or `kg mol^-1`).

### 2.2 Mass-average molar mass

Retained discrete-population form:

`M_m ≡ M_w = (Σ N_i M_i^2)/(Σ N_i M_i)`

and mass-fraction form:

`M_m = Σ w_i M_i`.

PASS.

Units: molar mass (`g mol^-1` or `kg mol^-1`).

### 2.3 Molar-mass dispersity

`Đ_M = M_m/M_n`

PASS.

Dimensionless. The manuscript correctly uses `molar-mass dispersity` as the controlled term and treats `polydispersity index / PDI` only as common/historical source language requiring mapping.

### 2.4 DP dispersity

`Đ_X = X_m/X_n`

PASS.

The manuscript correctly preserves the IUPAC caveat that `Đ_X` and `Đ_M` must not be silently equated for a non-alternating copolymer where DP and molar mass are not simply proportional across compositionally differing molecules.

## 3. Synthetic worked example verification

### Population A

- 60 molecules at 80 000 g mol^-1;
- 40 molecules at 120 000 g mol^-1.

Independent recalculation:

- `M_n = 96 000 g mol^-1`;
- `M_m = 100 000 g mol^-1`;
- `Đ_M = 1.041666...` → reported `1.0417`.

PASS.

### Population B

- 75 molecules at 50 000 g mol^-1;
- 25 molecules at 150 000 g mol^-1.

Independent recalculation:

- `M_n = 75 000 g mol^-1`;
- `M_m = 100 000 g mol^-1`;
- `Đ_M = 1.333333...` → reported `1.3333`.

PASS.

The example correctly demonstrates that identical `M_m` does not establish identical distribution/population.

The example is explicitly synthetic and is not used to infer PE/PP/process/property performance.

## 4. Scientific boundary checks

PASS:

- `M_m ≥ M_n` is used only for the positive molar-mass population defined by the standard averages;
- `Đ_M` is not treated as a unique distribution-shape descriptor;
- high dispersity is not treated as proof of bimodality;
- low dispersity is not treated as a quality ranking;
- no molar-mass statistic is converted into a piping design/acceptance criterion;
- method dependence is acknowledged and routed to Investigation 4.

## 5. Asset check

PASS for controlled candidate development:

- EX-016-001 developed;
- TAB-016-001 developed;
- FIG-016-001 final specification developed;
- FIG-016-002 final specification developed.

No real resin curve or unsupported universal distribution is introduced.

## 6. Decision

**PASS.**

Investigation 3 is authorized for canonical integration at the end-of-chapter integration step.

Investigation 4 is authorized next, subject to the ISO 16014 SEC/GPC method-scope gate.