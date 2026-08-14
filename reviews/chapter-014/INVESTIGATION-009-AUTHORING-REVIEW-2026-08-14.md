# Chapter 014 — Investigation 9 Authoring Review

**Date:** 2026-08-14  
**PR:** #12  
**Branch:** `chapter-014-engineering-development`  
**Reviewed artifact:** `chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry/investigation-009-authoring.md`  
**Gate:** Technical Outline Checkpoint D — primary evidence and transferability review  

## 1. Review question

Does the Investigation 9 authoring candidate move from molecular/structural observation to a defensible mechanism hypothesis and measured evidence without converting the retained primary studies into universal material rules, piping design values, compatibility criteria or unsupported material rankings?

## 2. Evidence set reviewed

The authoring candidate is restricted to the already authorized evidence set:

- `S014-009` — Shinzawa & Mizukado (2020), PA6 water treatment / spectroscopy / Young's-modulus response, DOI `10.1016/j.molstruc.2020.128389`.
- `S014-010` — Sambale et al. (2021), PA6 water sorption / swelling / concentration-dependent diffusion / geometry, DOI `10.3390/polym13091480`.
- `S014-011` — Graunke et al. (2016), fluoropolymer membrane gas/water-vapour transport, DOI `10.3390/s16101605`.
- `S014-012` — Monson, Moon & Extrand (2009), PFA/PTFE-copolymer processing / crystallinity / H2-N2-O2 transport, DOI `10.1002/app.28858`.

No additional named-polymer evidence claim was introduced.

## 3. Case-by-case review

### 3.1 Case A — PA6 + water

**Disposition: PASS.**

The candidate accurately keeps the claim at mechanism/evidence level:

- polar amide / H-bond chemistry is treated as a hypothesis basis;
- wet-treated PA6 mechanical change and spectroscopic interpretation are attributed to `S014-009`;
- sorption, swelling, geometry and concentration-dependent diffusion are attributed to `S014-010`;
- morphology/conditioning are explicitly retained as confounders;
- no universal PA6 or PA piping modulus, swelling or compatibility value is created.

The manuscript correctly demonstrates that a scientifically plausible mechanism may be experimentally supported while still being insufficient for direct design transfer.

### 3.2 Case B — fluoropolymer membranes

**Disposition: PASS WITH WORDING CONTROL.**

The retained lesson is appropriately methodological:

- the study compared selected fluoropolymer membranes with different fluorination / structural features;
- polarity, crystallinity/density and polymer-specific structure affected transport;
- the paper itself contains examples where a simple expected density/crystallinity relationship was not generally valid;
- the candidate therefore rejects a universal chemistry-only transport ranking.

The candidate does **not** rank piping-grade PVDF/PTFE/PFA/ECTFE/ETFE and explicitly rejects transfer of thin-film sensor-membrane results into pipe-wall allowances.

**Integration wording note:** when this material is merged into `chapter.md`, prefer `density / packing / free-volume interpretation` rather than wording that could imply free volume was independently measured in every membrane.

### 3.3 Case C — PFA processing / morphology

**Disposition: PASS.**

The candidate correctly represents the primary-study conclusion:

- permeability, diffusion and solubility were measured for H2, N2 and O2;
- different cooling histories produced materially different permeation resistance;
- the study attributed differences to crystallinity arising from architecture and processing;
- process is retained as potentially as important as grade for the measured system.

The candidate explicitly prohibits a universal cooling prescription, PFA pipe-wall permeability value, service-life conclusion or commercial-grade ranking.

## 4. Evidence-chain review

The proposed Chapter 014 reasoning sequence is accepted:

`observation → mechanism hypothesis → measurable property → direct evidence → confounder review → transferability → qualification → engineering decision`

This is consistent with the CDB rule that molecular reasoning is a mechanism tool rather than a substitute for material/product/system qualification.

## 5. Asset review

### TAB-014-002

**PASS as authoring content.**

It functions as a question generator and explicitly includes an `Invalid direct conclusion` column. No material ranking is created.

### TAB-014-003

**PASS.**

Cases A–C preserve source, confounder, defensible conclusion and prohibited design conclusion. The deliberate absence of a ranking column is appropriate.

### EX-014-002

**PASS.**

The example correctly refuses an underdetermined material ranking and converts the problem into an evidence specification.

### FIG-014-006 specification

**PASS.**

The gated figure concept prevents a direct jump from mechanism hypothesis to design decision. Final graphic production remains a later controlled publishing task.

### WF-014-001 first formal version

**PASS FOR DEVELOPMENT.**

The stop condition is explicit and appropriately routes insufficient evidence to testing, qualification or the owning downstream chapter.

## 6. Scientific simplification / transferability findings

No blocking scientific overclaim was found.

Three integration notes shall be retained:

1. Treat processing history as a controlled **input/confounder**, not as though it were itself a molecular feature.
2. In the fluoropolymer discussion, do not imply that a free-volume quantity was directly measured unless the cited source actually reports that measurement; use morphology/packing/density language where appropriate.
3. Preserve the distinction between `same polymer family / nominal chemistry` and `identical material state`; Case C is valuable specifically because process and morphology change the state represented by a family/grade label.

These are wording controls, not evidence-gate failures.

## 7. Gate decision

**INVESTIGATION 9 AUTHORING REVIEW: PASS — CONTROLLED INTEGRATION AUTHORIZED.**

The current Investigation 9 candidate is scientifically bounded enough to proceed to canonical manuscript integration after the three wording controls above are applied.

The Investigation 10 hold is therefore released for controlled authoring under the approved CDB.

## 8. Investigation 10 authorization boundary

Investigation 10 may now develop only the chapter-closing evidence boundary and required closure assets:

- final `FIG-014-006` scientific specification;
- final `WF-014-001`;
- `TAB-014-004` downstream chapter ownership crosswalk;
- `CL-014-001 — Before inferring engineering behaviour from a chemical structure`;
- final chemistry→measurement→qualification→engineering-decision boundary;
- chapter closure / handoff to Chapters 015–020 and later material/design chapters.

Investigation 10 shall not add new named-material property claims or new numerical design values without a new evidence gate.

## 9. Chapter status after this review

- Investigations 1–8: authored controlled candidates.
- Investigation 9: **AUTHORING REVIEW PASS / INTEGRATION AUTHORIZED**.
- Investigation 10: **AUTHORIZED FOR CONTROLLED AUTHORING**.
- Chapter 014 Technical Review: not yet complete.
- Standards/Evidence Validation: not yet complete.
- Editorial/Style Review: not yet complete.
- Ready-for-Review: not yet reached.
- Merge/publication: not authorized.
