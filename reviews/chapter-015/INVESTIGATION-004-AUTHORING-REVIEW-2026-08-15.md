# Chapter 015 — Investigation 4 Authoring Review

**Date:** 2026-08-15  
**Investigation:** 4 — How Does Radical Polymerization Work, and What Process Variables Matter?  
**Candidate:** `chapters/chapter-015-from-monomer-to-polymer/investigation-004-authoring.md`  
**Disposition:** **PASS — AUTHORIZE INVESTIGATION 5**

## 1. Review basis

Current IUPAC terminology was checked against the Gold Book and _Terminology for Chain Polymerization (IUPAC Recommendations 2021)_, published 2022.

Key controlled entries used in the candidate include:

- `R05075` — radical polymerization;
- `14375` — primary radical;
- `08965` — primary species;
- `08959` — initiating species;
- `08960` — initiator efficiency;
- `08948` — combination;
- `D01799` — disproportionation / radical disproportionation;
- `15409` — kinetic-chain length, including recognition of termination by combination/disproportionation;
- `08972` — substitution chain transfer;
- `08939` — catalytic chain transfer;
- `08914` — living radical polymerization;
- `08921` — stable-radical-mediated polymerization, including IUPAC's deprecation of `free radical` terminology.

## 2. Technical review

PASS.

The candidate correctly:

- defines radical polymerization by radical kinetic-chain carriers rather than monomer/catalyst/product identity;
- distinguishes initiator, primary radical, primary species, initiating species and propagating radical;
- does not assume 100% initiator efficiency;
- separates propagation, combination termination, disproportionation termination, chain transfer and reversible deactivation;
- uses `combination` rather than the commonly misused `recombination` term;
- does not claim one termination route dominates universally;
- preserves the strict IUPAC boundary between reversible-deactivation radical polymerization and living radical polymerization;
- avoids a universal radical-polymerization rate law and any direct resin-property prediction.

## 3. Evidence review

PASS for stable mechanism layer.

The process-variable section identifies temperature, initiator concentration, transfer chemistry, medium, pressure/concentration context and residence/reaction history only as hypothesis variables.

The manuscript explicitly rejects universal directional rules such as `more initiator → lower molecular weight` or `higher temperature → lower molecular weight` without named-system evidence.

Therefore the Class-C primary-literature gate remains untriggered in Investigation 4.

## 4. Quantitative review

PASS.

The candidate retains `k_p`, `k_t` and initiator-efficiency concepts as terminology but intentionally does not introduce a steady-state rate law or molecular-weight equation. This is appropriate because the required assumptions, kinetic coefficients, transfer pathways, conversion dependence and reactor history are not defined for a named system.

## 5. Asset review

### FIG-015-003

PASS as scientific specification.

The figure must retain:

- initiator / energy path → primary radicals;
- initiation → propagating radical;
- repeated propagation;
- competing combination/disproportionation termination;
- transfer;
- optional reversible-deactivation path where applicable;
- explicit note that radical generation does not equal successful chain initiation.

No material-performance ranking is permitted on the figure.

### Mechanism-to-measurement matrix

PASS as a supporting engineering evidence-routing asset.

## 6. Editorial / engineering-use review

PASS.

The Investigation provides enough radical-mechanism depth to explain process provenance and later chain-architecture hypotheses without becoming a polymer-reaction-engineering chapter.

The transition to step polymerization is clean and now uses the 2026 IUPAC terminology update established during Investigation 2.

## 7. Integration controls

At chapter closure:

1. integrate `investigation-004-authoring.md` after Investigation 3;
2. preserve current terminology (`radical polymerization`; `free radical` deprecated);
3. retain the evidence gate on named temperature/initiator/transfer trends;
4. final review must check that no later section introduces a generic steady-state rate law as a product-property predictor;
5. delete the temporary candidate after canonical integration.

## 8. Gate decision

**INVESTIGATION 4 — PASS.**

Investigation 5 is authorized using the current formal terminology:

> **How Does Step Polymerization Build Macromolecules, and What Distinguishes Additive from Condensative Step Growth?**

No Carothers-type quantitative relationship is pre-authorized. It may be retained only if its assumptions and teaching value are explicitly established and if it does not duplicate Chapter 016.