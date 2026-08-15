# Chapter 015 — Pre-Integration Technical Review

**Date:** 2026-08-15  
**Scope:** canonical Chapter 015 scaffold + controlled Investigation 2–10 authoring candidates  
**PDS baseline:** 1.0  
**Disposition:** **CONDITIONAL PASS — CANONICAL INTEGRATION AUTHORIZED WITH BOUNDED FINDINGS**

## 1. Review scope

This review assesses the complete logical engineering-development arc before the temporary Investigation 2–10 candidates are inserted into canonical `chapter.md`.

Reviewed content includes:

- canonical Investigation 1;
- controlled candidates Investigations 2–10;
- Technical Outline;
- active Evidence Plan + 2026 classification addendum;
- Investigation authoring reviews;
- primary-evidence gates for Investigations 7–9;
- CDB-015 and the controlled post-approval terminology correction record.

## 2. Overall technical disposition

**PASS for canonical integration.**

The chapter now forms a coherent technical sequence:

1. polymerization provenance as an engineering question;
2. current step/chain polymerization classification;
3. generic chain-carrier lifecycle;
4. radical polymerization as one chain mechanism;
5. additive/condensative step polymerization;
6. coordination polymerization / insertion;
7. heterogeneous coordination / industrial Ziegler–Natta language;
8. homogeneous/metallocene language and evidence limits;
9. process-variable → architecture-hypothesis evidence cases;
10. evidence stop-rule and Chapter 016 handoff.

No chapter-wide scientific rewrite is required.

## 3. Bounded findings to apply during canonical integration

### TR015-01 — apply the 2026 IUPAC classification correction everywhere

**Finding:** The approved CDB / initial Technical Outline were drafted before the final 2026 publication of the new IUPAC basic-classification Recommendation was incorporated into the project. They contain wording that treats `step-growth` mainly as explanatory language and formally foregrounds polyaddition/polycondensation rather than the now-published step/chain hierarchy.

**Required correction:** integrate the controlled update already recorded in `TERMINOLOGY-CLASSIFICATION-UPDATE-2026-08-15.md`:

- formal top-level classes: `step polymerization` and `chain polymerization`;
- additive step polymerization = polyaddition;
- condensative step polymerization = polycondensation;
- additive chain polymerization;
- condensative chain polymerization.

**Scope impact:** none. This is an authoritative terminology update, not a change in chapter purpose or downstream ownership.

### TR015-02 — synchronize Investigation 5 title / ownership with the updated hierarchy

Use the developed title:

**Investigation 5 — How Does Step Polymerization Build Macromolecules, and What Distinguishes Additive from Condensative Step Growth?**

The older planning title can remain in provenance records but canonical CDB/outline/manuscript navigation must use the updated title or an equivalent current-terminology title.

### TR015-03 — FIG-015-001 has one final asset owner

Investigations 2 and 5 both develop the classification figure.

Canonical rule:

- Investigation 2 establishes the top-level scientific map;
- Investigation 5 supplies the detailed step-polymerization panel;
- **one final `FIG-015-001` specification only** shall exist in the integrated chapter.

No duplicate asset ID.

### TR015-04 — FIG-015-004 has one final asset owner

Investigations 6–8 progressively build the coordination catalyst-environment figure.

Canonical rule:

- Inv. 6 = common trunk / coordination-insertion precursor;
- Inv. 7 = heterogeneous branch;
- Inv. 8 = final complete figure specification.

Earlier figure material may remain as development text only if it is clearly labelled as precursor; final asset register shall point to one `FIG-015-004`.

### TR015-05 — supporting tables must not collide with TAB-015-001 through TAB-015-005

Several Investigations contain useful supporting comparison/evidence tables beyond the five formal chapter tables.

At integration:

- retain formal IDs only for TAB-015-001 through TAB-015-005 as declared in the asset register;
- leave secondary lifecycle/evidence tables unnumbered or assign controlled secondary IDs only if publishing architecture later requires them;
- do not silently create duplicate formal table ownership.

### TR015-06 — normalize molar-mass terminology without corrupting source titles

Canonical prose should prefer:

- `molar mass` for the physical quantity;
- `molar-mass distribution (MWD)` or `molecular-weight distribution (MWD)` only where industry/source language is intentionally retained and defined;
- original paper titles must remain unchanged.

This is editorial/terminology normalization only; no numerical claim changes.

### TR015-07 — preserve `single-site` as descriptive language, not IUPAC classification

Investigation 8 correctly treats `single-site` as industrial/descriptive language requiring definition/evidence. Final integration must not promote it into a formal IUPAC taxonomy.

## 4. Scientific boundary checks

### Step versus chain classification

PASS. The 2026 IUPAC hierarchy is technically coherent and correctly separates mechanism class from additive/condensative reaction character.

### Chain lifecycle

PASS. Initiation + propagation are fundamental; termination/transfer are possible rather than universal. Dormancy/reversible deactivation is not conflated with irreversible termination.

### Radical polymerization

PASS. Initiator, primary radical/species, initiating species and propagating radical are distinguished. No universal rate law or directional process rule is introduced.

### Step polymerization

PASS. Functionality is used as possible connectivity, not guaranteed topology. Carothers equation is deliberately excluded to protect the Chapter 016 boundary.

### Coordination polymerization

PASS. Preliminary monomer coordination is the defining concept. `Metal-catalyzed polymerization` is not used as an unexplained synonym. Coordination polymerization is distinguished from coordination polymer.

### Heterogeneous / Ziegler–Natta

PASS. Heterogeneous catalyst is not definitionally converted into a quantified multi-site model or broad MWD rule.

### Homogeneous / metallocene

PASS. Metallocene is a subset of homogeneous coordination polymerization. `Single-site`, narrow MWD and uniform composition are not definition-level consequences.

### Process variables

PASS. Hydrogen, feed ratio, temperature, residence history and support environment remain system-specific evidence cases rather than universal process rules.

## 5. Chapter 016 boundary

PASS.

Chapter 015 explains **how chain architecture may be created**. It does not provide the detailed engineering treatment of:

- molar mass / MWD;
- branching;
- crosslinking;
- chain topology;
- architecture → creep/fracture/fusion/permeability performance.

Those remain downstream.

## 6. Quantitative-treatment disposition

PASS.

No design equation is introduced.

- `P_x + P_y` notation is mechanistic/definitional.
- `k_p` / `k_t` are terminology only.
- Carothers-type equation is explicitly excluded.
- no source-specific process condition is converted into a universal design number.

## 7. Integration authorization

Canonical integration is technically authorized if and only if it:

1. applies TR015-01 through TR015-07;
2. preserves all named-primary-source transferability boundaries;
3. creates one continuous Investigation 1–10 manuscript;
4. absorbs S015-008 through S015-016 into canonical `references.md`;
5. deletes temporary candidate/addendum files after validation;
6. changes no Chapters 000–014 technical content;
7. does not start Chapter 016.

Final full-file Technical Review remains mandatory after integration.