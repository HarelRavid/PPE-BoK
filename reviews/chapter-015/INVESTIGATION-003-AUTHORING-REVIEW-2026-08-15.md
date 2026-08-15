# Chapter 015 — Investigation 3 Authoring Review

**Date:** 2026-08-15  
**Investigation:** 3 — How Does Chain Polymerization Build a Macromolecule?  
**Candidate:** `chapters/chapter-015-from-monomer-to-polymer/investigation-003-authoring.md`  
**Disposition:** **PASS — AUTHORIZE INVESTIGATION 4 MECHANISM RESEARCH/AUTHORING**

## 1. Review basis

Controlled terminology was checked against the IUPAC Gold Book entries sourced to _Terminology for Chain Polymerization (IUPAC Recommendations 2021)_, published in Pure and Applied Chemistry 94 (2022), 1093–1147, plus the general chain-reaction terms where applicable.

Key controlled entries used:

- `C00958` — chain polymerization;
- `C00949` — chain carrier;
- `C00955` — chain initiation;
- `08959` — initiating species;
- `08944` — chain propagation;
- `08946` — chain termination;
- `08947` — chain-transfer agent;
- `08950` — dead polymer chain;
- `08952` — dormant species;
- `15387` — chain depropagation;
- `L03597` — living polymerization.

## 2. Technical review

PASS.

The candidate correctly preserves the chain-polymerization definition and lifecycle:

- initiation creates a chain carrier / initiating path;
- propagation grows the chain while regenerating propagation capability;
- chain termination is irreversible loss of a carrier without creation of a new carrier;
- chain transfer deactivates/transfers the original carrier while generating a new carrier through the transfer process;
- reversible deactivation is distinguished from irreversible termination;
- dead and dormant chain states are not conflated;
- termination and chain transfer are not presented as mandatory for every chain polymerization.

The use of living polymerization as a limiting counterexample is bounded and technically appropriate: it is used only to prove that termination/irreversible transfer are not universal lifecycle requirements.

## 3. Evidence review

PASS for stable mechanism layer.

No named material, commercial catalyst, reactor process or property trend is introduced. The candidate therefore remains entirely within the A/B terminology/mechanism evidence layer.

No statement of the form `named process variable → measured architecture/property trend` is retained, so the Class-C primary-evidence gate is not triggered.

## 4. Quantitative review

PASS with bounded use.

`k_p` and `k_t` are introduced only as IUPAC-controlled rate-coefficient symbols. No rate equation, value, unit set, material prediction or process calculation is introduced.

The manuscript explicitly states that quantitative use would require a defined mechanism, species concentrations, validated coefficients, competing pathways and reactor/process history.

## 5. Asset review

### FIG-015-002

PASS as scientific specification.

Mandatory final figure controls:

- initiation and propagation on the core path;
- termination and transfer shown as possible branches rather than universal mandatory stages;
- reversible deactivation/dormancy visually separated from irreversible termination;
- no implication that pathway presence alone predicts MWD.

### Supporting lifecycle table

PASS. Final asset numbering can be assigned at canonical integration without changing technical content.

## 6. Editorial / engineering-use review

PASS.

The candidate stays at the correct depth for a piping engineer. It explains why chain-carrier lifecycle matters to material provenance and change control without becoming a kinetics or controlled-polymerization monograph.

The bridge to Investigation 4 is clean: radical polymerization can now be treated as a concrete chain-polymerization family after the generic lifecycle has been controlled.

## 7. Integration actions retained

At end-of-chapter canonical integration:

1. integrate `investigation-003-authoring.md` after Investigation 2;
2. preserve current IUPAC term identifiers in canonical `references.md` where load-bearing;
3. ensure `FIG-015-002` final art distinguishes irreversible termination from reversible deactivation;
4. delete the temporary candidate after canonical integration;
5. continuous-manuscript review shall check that the lifecycle is not later simplified back into a universal `initiation → propagation → termination` recipe.

## 8. Gate decision

**INVESTIGATION 3 — PASS.**

Investigation 4 is authorized for general radical-polymerization mechanism authoring at the A/B evidence layer.

Any named monomer, initiator, temperature, transfer-agent or process-condition trend that claims a specific molecular/material outcome remains **BLOCKED pending direct primary evidence**.