# Chapter 015 — Controlled Terminology / Classification Update

**Date:** 2026-08-15  
**Chapter:** 015 — From Monomer to Polymer: Polymerization, Catalysts and Process–Structure Relationships  
**PDS baseline:** 1.0  
**Change type:** authoritative-source terminology correction after CDB approval  
**Scope impact:** none — terminology hierarchy only  
**Disposition:** **APPLY DURING ENGINEERING DEVELOPMENT**

## 1. Trigger

During the mandatory Investigation 2 terminology gate, the current IUPAC publication record was rechecked rather than relying only on the older Gold Book / 1994 / 1996 / 2008 terminology path used in the initial planning package.

A newer controlling Recommendation was identified:

**S015-008 — Farrell, W. S.; Keddie, D. J.; Luscombe, C. K.; Matson, J. B.; Merna, J.; Moad, G.; Russell, G. T.; Sosa Vargas, L.; Théato, P.; Topham, P. D. — _Basic classification and definitions of polymerization reactions (IUPAC recommendations 2025)_. Pure and Applied Chemistry 98(7) (2026), 1105–1117. DOI `10.1515/pac-2025-0490`. First published online 2026-05-12; listed by IUPAC in the July 2026 PAC issue.**

This Recommendation explicitly updates the older 1994 basic-classification document.

## 2. Material change to the Chapter 015 terminology hierarchy

The approved CDB and first Technical Outline treated `step-growth` primarily as explanatory language and relied formally on `polyaddition` / `polycondensation` versus `chain polymerization`.

The 2026 published Recommendation now provides a clearer two-branch formal hierarchy:

1. **step polymerization** — growth by reactions between monomer, oligomer or polymer molecules of any length;
   - **additive step polymerization** — synonym: **polyaddition**;
   - **condensative step polymerization** — synonym: **polycondensation**.
2. **chain polymerization** — polymerization proceeding by a chain reaction in which monomer adds to active site(s) on polymer chains;
   - **additive chain polymerization**;
   - **condensative chain polymerization**.

Therefore Chapter 015 shall use **step polymerization** as a controlled formal term rather than treating the step concept as merely explanatory.

## 3. What does not change

The following approved CDB principles remain valid:

- `addition polymerization / condensation polymerization` is not an adequate modern top-level classification;
- `chain polymerization` refers to a chain-reaction mechanism, not merely to making a long chain;
- small-molecule elimination does not by itself determine whether a polymerization is step or chain;
- catalyst/process information remains mechanism/provenance evidence, not product-qualification evidence;
- Chapters 016–020 retain ownership of architecture, morphology and downstream behaviour;
- named catalyst/process/material outcome claims remain gated behind direct primary literature.

## 4. Controlled authoring rule from this checkpoint onward

For Investigation 2 and all downstream Chapter 015 text, use the hierarchy:

`polymerization`

→ `step polymerization`

&nbsp;&nbsp;&nbsp;&nbsp;→ `additive step polymerization (polyaddition)`  
&nbsp;&nbsp;&nbsp;&nbsp;→ `condensative step polymerization (polycondensation)`

→ `chain polymerization`

&nbsp;&nbsp;&nbsp;&nbsp;→ `additive chain polymerization`  
&nbsp;&nbsp;&nbsp;&nbsp;→ `condensative chain polymerization`

Further mechanism qualifiers such as radical, ionic, coordination, ring-opening or polyinsertion belong below the chain-polymerization branch as applicable.

## 5. Configuration-control disposition

This record does **not** silently rewrite the already approved CDB baseline on `main`.

Instead:

- this record is the controlled superseding clarification for Engineering Development;
- `references.md`, `technical-outline.md` and the CDB shall absorb the updated hierarchy during the final canonical integration / closure pass;
- Investigation 2 shall be authored directly to the 2026 Recommendation rather than to the superseded planning simplification;
- the final review shall verify that no stale statement remains saying that step polymerization is merely non-normative explanatory language.

No new chapter topic, material family, catalyst ranking or design claim is authorized by this terminology correction.