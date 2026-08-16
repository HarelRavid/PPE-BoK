# Chapter 016 — Pre-Integration Editorial / Style / Desk Review

**Date:** 2026-08-16  
**Scope:** canonical Investigation 1 + controlled Investigation 2–10 candidates  
**Disposition:** **CONDITIONAL PASS — NO STRUCTURAL REWRITE REQUIRED**

## 1. Overall editorial disposition

The chapter has a coherent progression from vocabulary and quantitative descriptors through measurement logic, topology/network concepts, evidence cases and practical engineering workflow.

It does not read as a disconnected polymer-characterization glossary.

The controlling narrative remains visible:

`architecture descriptor → measurement → hypothesis → downstream verification → qualification → decision`.

No structural rewrite is required before canonical integration.

## 2. Desk Test at logical-candidate level

PASS.

A reader can follow the chapter to answer:

1. why process/catalyst provenance is not measured architecture;
2. why `chain length`, DP, molar mass and relative molecular mass must be separated;
3. why `M_n`, `M_m/M_w`, MMD and `Đ_M` are different descriptors;
4. why one average/dispersity does not define distribution shape;
5. what SEC/GPC separates and why calibration/detector provenance matters;
6. why `more branching` is not one variable;
7. how SCB differs from LCB and where ISO 18177 applies;
8. how branch point, covalent crosslink, physical network and entanglement differ;
9. what ISO 10147 gel content can and cannot establish;
10. how architecture→behaviour primary evidence should be bounded;
11. what data to request from a supplier/laboratory;
12. where inference must stop and which downstream chapter owns the next question.

A final continuous-file Desk Test remains mandatory after integration.

## 3. Editorial findings for integration

### ED016-01 — normalize current-state metadata

Canonical `review.md` and Technical Outline still contain planning-era text indicating that CDB metadata sync is open. Current canonical development files shall reflect the completed CDB approval/metadata sync.

Historical review records may retain their time-correct wording.

### ED016-02 — keep one terminology convention

Reader-facing explanatory prose shall consistently prefer:

- `molar mass`;
- `molar-mass distribution (MMD)`;
- `M_m ≡ M_w` at first controlled use, then whichever symbol is contextually clearest without silently changing source notation;
- `molar-mass dispersity (Đ_M)`.

Source titles must retain original `molecular weight` wording.

### ED016-03 — protect acronym clarity

Define at first reader-facing use in the integrated chapter:

- MMD;
- SEC/GPC;
- SCB;
- LCB;
- MFR/MVR;
- PE-X;
- SH / CRB / NPT where used in the evidence case.

Do not assume an engineer arrives from the previous chapter with every acronym loaded.

### ED016-04 — one final formal asset label per asset

Final reader-facing text shall contain one formal specification/use for each controlled FIG/TAB/EX/WF/CL ID. Supporting evidence matrices can remain unnumbered if necessary.

### ED016-05 — preserve evidence limits close to each case

For S016-013 through S016-016, keep `supported / confounders / unsupported / transferability` immediately adjacent to each case. Do not move limitations into a distant generic disclaimer.

### ED016-06 — avoid disclaimer saturation

The chapter intentionally repeats evidence boundaries, but integration should not create duplicated generic warnings at candidate seams. Retain mechanism-specific cautions; remove only literal repetition caused by file concatenation.

### ED016-07 — preserve chapter handoff

Final closure must end with:

`chain architecture → crystallization/packing possibilities`

not a claim that architecture guarantees morphology. Chapter 017 ownership must remain visually clear.

## 4. Style consistency

PASS with bounded normalization.

Maintain:

- engineering-question openings;
- controlled equations followed by units/meaning/limits;
- short evidence matrices;
- `Failure lens / Common mistakes` sections;
- explicit Verification Method and Engineering Decision closures;
- practical supplier-data examples.

Avoid converting the final chapter into either a lab manual or a repetitive compliance checklist.

## 5. Decision

**CONDITIONAL PASS — CANONICAL INTEGRATION AUTHORIZED.**

Conditions ED016-01 through ED016-07 require only bounded normalization and no scientific scope expansion.