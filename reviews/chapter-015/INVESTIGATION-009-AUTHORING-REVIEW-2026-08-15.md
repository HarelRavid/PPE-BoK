# Chapter 015 — Investigation 9 Authoring Review

**Date:** 2026-08-15  
**Investigation:** 9 — How Do Process Variables Become Molecular-Architecture Hypotheses?  
**Candidate:** `chapters/chapter-015-from-monomer-to-polymer/investigation-009-authoring.md`  
**Evidence gate:** `INVESTIGATION-009-PRIMARY-EVIDENCE-GATE-2026-08-15.md`  
**Disposition:** **PASS — AUTHORIZE INVESTIGATION 10 / CHAPTER CLOSURE AUTHORING**

## 1. Review basis

The candidate was checked against the four pre-approved primary cases:

- S015-014 — Czaja & Białek (2001): hydrogen in three MgCl2(THF)2-supported ethylene/alpha-olefin copolymerization catalyst systems;
- S015-015 — Zhang et al. (2021): E/P feed-ratio response in one TiCl4/Di/MgCl2–TEA/De supported Ziegler–Natta system;
- S015-016 — Wang et al. (1998): temperature / residence-time / ethylene-feed history in one continuous CGC-Ti solution ethylene polymerization system;
- S015-012 — Kenyon et al. (2022): support composition / reaction-condition effects on MWD in one supported `(EBI)ZrCl2` ethylene polymerization system.

## 2. Technical review

PASS.

The candidate correctly treats process variables as causal/provenance inputs rather than direct design parameters. The governing sequence is consistently maintained:

`process variable → mechanism/pathway hypothesis → architecture/composition hypothesis → direct measurement → qualification`.

No section converts hydrogen, comonomer feed, temperature, residence time, pressure/concentration, support chemistry or catalyst activation state into a universal resin-property rule.

## 3. Primary-evidence review

PASS within the controlled gate.

### S015-014

The manuscript states only that hydrogen addition reduced polymer molecular weight and catalyst activity in the three studied supported catalyst systems. It explicitly rejects universal transfer to all coordination-polymerization systems.

### S015-015

The manuscript uses the study only to show that E/P feed ratio changed active-center/fraction behavior and copolymer microstructure in the defined catalyst system. It does not transfer the trend to unrelated comonomers or catalysts.

### S015-016

The manuscript uses temperature, mean residence time and ethylene feed concentration only within the defined CGC-Ti continuous solution system. It does not universalize the observed LCB/active-center behavior.

### S015-012

The manuscript reuses the supported-metallocene paper only to show that support / immobilization / reaction environment can alter MWD response in the defined system. It does not infer that all supported metallocenes behave similarly.

## 4. Asset review

### TAB-015-003

PASS. It is a process-variable → hypothesis → required-characterization table, not a directional design table.

### TAB-015-004

PASS. The four source cases are explicitly bounded by system and transferability.

### FIG-015-005

PASS as scientific specification. The figure uses ethene as a common starting point but explicitly prohibits treating unrelated studies as a controlled head-to-head performance comparison.

### Supplier process-change evidence request

PASS as a precursor to EX-015-003. It requests evidence of equivalence/qualification without demanding proprietary catalyst recipes.

## 5. Editorial / engineering-use review

PASS.

The Investigation provides a practical change-control and failure-analysis workflow while keeping polymerization provenance separate from post-polymerization compounding/product-processing provenance.

## 6. Quantitative review

PASS.

No source-specific numerical value has been generalized into a design rule. No process variable is used in a pipe-design equation. The manuscript deliberately favors directionally bounded evidence over pseudo-precision.

## 7. Integration controls

At chapter closure:

1. integrate `investigation-009-authoring.md` after Investigation 8;
2. add S015-014 through S015-016 to canonical `references.md` and preserve S015-012 reuse notes;
3. preserve supported/unsupported/transferability boundaries in TAB-015-004;
4. ensure FIG-015-005 retains the non-head-to-head-study warning;
5. delete the temporary candidate after canonical integration.

## 8. Gate decision

**INVESTIGATION 9 — PASS.**

Investigation 10 is authorized as a synthesis/closure Investigation. It may synthesize only evidence already validated in Investigations 1–9. No new named catalyst/material/process case may be introduced without its own direct-source gate.