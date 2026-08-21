# Chapter 016 — Investigation 002 Terminology / Units Gate

**Date:** 2026-08-16  
**Investigation:** 2 — What Are Chain Length, Degree of Polymerization and Molar Mass?  
**Disposition:** **PASS**

## 1. Sources checked

Current terminology was checked against the active IUPAC path in S016-001 / S016-002 / S016-004, including current Gold Book entries for:

- `degree of polymerization` — D01569;
- `average degree of polymerization` — A00540;
- `molar mass` — 12214;
- `molar-mass average` — 12215;
- `relative molecular mass` — R05271;
- `relative molar mass` — R05270;
- `chain length` — C00956;
- `kinetic-chain length` — 15409.

## 2. Controlled findings

### TG016-02-01 — unqualified `chain length` is not a safe structural quantity

PASS.

The Gold Book term `chain length` is already defined in chain-reaction kinetics. `Kinetic-chain length` is likewise a polymerization-kinetics quantity. The candidate therefore correctly avoids using unqualified `chain length` as the formal molecular-size descriptor and requires the actual quantity to be named.

### TG016-02-02 — degree of polymerization

PASS.

The candidate treats degree of polymerization as a count of monomeric units in the specified macromolecule/block/chain and therefore dimensionless. It does not equate DP with molar mass or topology.

### TG016-02-03 — molar mass

PASS.

`M` is treated as a dimensional quantity with `g mol^-1` or `kg mol^-1` units. The manuscript correctly postpones population averages to Investigation 3.

### TG016-02-04 — relative molecular mass / molecular weight

PASS.

`M_r` is treated as dimensionless. The candidate explicitly records the IUPAC synonym relationship between relative molecular mass and historical `molecular weight` language while preserving the project's rule that canonical explanatory prose should prefer molar mass for the dimensional quantity.

### TG016-02-05 — numerical equality does not make quantities identical

PASS.

The candidate correctly explains that the numerical value of `M` expressed in `g mol^-1` can equal the corresponding relative molecular mass while the two quantities remain dimensionally different.

## 3. Bounded equation / units review

Candidate teaching relation:

`M_chain = x M_0 + M_end`

Disposition: **PASS WITH EXPLICIT ASSUMPTION BOUNDARY ALREADY PRESENT IN CANDIDATE.**

The relation is retained only as bookkeeping for a simple uniform chain representation where:

- `x` is dimensionless;
- `M_0` and `M_end` use the same molar-mass units;
- the incorporated unit is explicitly defined;
- end contribution is explicitly separated.

The approximate form:

`M_chain ≈ x M_0`

is allowed only when the end contribution is negligible relative to the repeated-unit contribution.

The candidate explicitly blocks universal use for copolymers, low-molar-mass oligomers, chemically modified chains or systems where the unit definition/composition is not fixed.

No architecture-to-pipe-performance equation is introduced.

## 4. Chapter-boundary check

PASS.

The candidate does not pull forward:

- `M_n`, `M_m/M_w` population mathematics beyond preview language;
- dispersity;
- SEC/GPC method detail;
- morphology;
- rheology;
- SCG/fracture;
- product/design qualification.

Those remain owned by Investigations 3–10 and downstream chapters.

## 5. Decision

**PASS.**

Investigation 2 is authorized for canonical integration at the end-of-chapter integration step.

Investigation 3 is authorized next, subject to the full quantitative/equation/units gate for `M_n`, `M_m/M_w`, distribution weighting and `Đ_M`.