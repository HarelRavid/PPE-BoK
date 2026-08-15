# Chapter 014 — Pre-Integration Technical Review

**Date:** 2026-08-14  
**PR:** #12  
**Branch:** `chapter-014-engineering-development`  
**Logical manuscript reviewed:** canonical `chapter.md` Investigations 1–8 + approved controlled authoring candidates for Investigations 9–10  
**Review class:** pre-integration scientific / engineering consistency review  

## 1. Purpose

Review the complete logical Chapter 014 engineering arc before mechanically integrating Investigations 9–10 into the canonical manuscript.

This review is intentionally performed before canonical integration so that terminology, evidence hierarchy, chapter ownership and scientific-model inconsistencies are corrected once during integration rather than patched after the manuscript is assembled.

## 2. Overall disposition

**PRE-INTEGRATION TECHNICAL REVIEW: CONDITIONAL PASS.**

The logical manuscript is technically coherent and within CDB-014 scope. No blocking physics/chemistry error, unsupported piping-design conclusion, direct chemistry→acceptance shortcut or material-ranking claim was found.

Canonical integration is authorized **only with the findings in Section 3 applied**.

This is not yet the final full-chapter Technical Review because the canonical manuscript has not yet been assembled and re-read as one file.

## 3. Required integration findings

### TR-014-01 — Resolve competing `Level` numbering systems

**Severity:** integration-blocking terminology inconsistency.  
**Location:** Investigation 1.9 versus Investigation 10.2.

Investigation 1 currently classifies statements as:

- Level 1 — Chemistry fact;
- Level 2 — Mechanism hypothesis;
- Level 3 — Engineering conclusion.

Investigation 10 later introduces the final six-level evidence ladder:

1. chemical identity / structural description;
2. mechanism hypothesis;
3. material characterization;
4. compound / grade qualification;
5. product qualification;
6. application / system qualification.

Both models are useful, but reusing `Level 1`, `Level 2`, `Level 3` for two different hierarchies can cause a reader to map them onto each other incorrectly.

**Required correction:** retain the three-way concept in Investigation 1 but rename it to:

- **Claim Class A — Chemistry fact**;
- **Claim Class B — Mechanism hypothesis**;
- **Claim Class C — Engineering conclusion**.

Update the rule from `Never jump directly from Level 1 to Level 3` to:

> **Never jump directly from Claim Class A to Claim Class C.**

Reserve `Level 1–6` terminology for the final Chapter 014 PPE-BoK evidence ladder in Investigation 10.

### TR-014-02 — Replace `secondary bonding` asset terminology with `noncovalent interactions`

**Severity:** required scientific terminology improvement.  
**Location:** `FIG-014-002` title / references to `Primary and secondary bonding map`.

The chapter content itself correctly distinguishes covalent/ionic-character/electron-delocalization primary bonding from hydrogen bonding and the van der Waals family. Current IUPAC Gold Book terminology explicitly treats van der Waals forces as an umbrella that includes dipole–dipole, dipole-induced-dipole and London/dispersion interactions, and IUPAC treats hydrogen bonding through its own definition/recommendation framework.

`Secondary bonding` is common materials-science teaching language but is not needed here and can obscure the adopted IUPAC taxonomy.

**Required correction:** preserve asset ID `FIG-014-002` but rename the asset to:

> **Primary Bonding and Noncovalent Interaction Map**

Use `noncovalent interactions` / specific interaction names in the prose unless a source-specific context explicitly requires another term.

### TR-014-03 — Label the six-level evidence ladder as PPE-BoK framework

**Severity:** required evidence-governance clarification.  
**Location:** Investigation 10.2.

Apply finding `E10-01` from the Investigation 10 review. Insert before the ladder:

> **The following levels are a PPE-BoK reasoning framework for controlling evidence transfer; they are not a normative classification defined by a single standard.**

This prevents readers from treating the framework as an ISO/IUPAC taxonomy.

### TR-014-04 — Apply Investigation 9 transferability wording controls

**Severity:** required integration wording control.

Carry forward the three findings from `INVESTIGATION-009-AUTHORING-REVIEW-2026-08-14.md`:

1. processing history is an input/confounder, not a molecular feature;
2. in the fluoropolymer teaching case, do not imply that free volume was directly measured in every membrane; prefer wording such as `density / packing / morphology / free-volume interpretation` where supported;
3. distinguish `same family / nominal chemistry` from `identical material state`.

## 4. Scientific-model review

### 4.1 Atom / molecule / substance terminology

**PASS for current development state.**

The chapter keeps atom, element, molecule, molecular entity and chemical substance conceptually separate and does not force all matter into a discrete-molecule picture.

### 4.2 Orbitals / valence / electronegativity

**PASS.**

The chapter explicitly rejects the planetary-orbit picture, treats orbitals as model/wavefunction constructs, uses valence concepts only to the depth required for bonding, and does not turn electronegativity into a polymer-property scale.

### 4.3 Primary bonding

**PASS.**

Covalent bonding, ionic character and extended electron delocalization are used as structural/electronic models rather than direct bulk-property predictors. The chapter explicitly avoids a false pure ionic/covalent dichotomy and avoids using metallic bonding as a ductility/strength guarantee.

### 4.4 Noncovalent interactions

**PASS subject to TR-014-02 title correction.**

Current IUPAC Gold Book recheck supports the chapter's key taxonomy controls:

- van der Waals is an umbrella including dipole–dipole, dipole-induced-dipole and London/dispersion forces;
- London/dispersion contributions also occur in polar systems;
- hydrogen bonding is treated through the dedicated IUPAC 2011 definition/evidence framework rather than reduced to a universal `strong dipole–dipole` label.

The chapter correctly rejects a one-dimensional universal intermolecular-force ladder.

### 4.5 Carbon structural versatility

**PASS.**

The chapter does not use tetravalency alone as the explanation for carbon chemistry. It adds C–C connectivity, chains/branches/rings, bond-order diversity and substitution while deferring real commercial chain architecture to Chapter 016.

### 4.6 Hybridization / sigma / pi / rotation

**PASS.**

Current IUPAC terminology recheck supports:

- hybridization as linear combination of atomic orbitals;
- `sp3`, `sp2`, `sp` as idealized tetrahedral/trigonal/digonal-local descriptions;
- the need to distinguish rigorous MO symmetry from localized two-centre σ/π language;
- the localized π nodal-plane distinction used in the chapter.

The chapter correctly treats ideal bond angles as reference geometry rather than exact universal values and avoids `single bond = zero rotational barrier` wording.

### 4.7 Ethene / polyethylene bridge

**PASS FOR DEVELOPMENT; FINAL NOMENCLATURE VALIDATION STILL REQUIRED.**

The structural comparison `CH2=CH2 → [–CH2–CH2–]n` is repeatedly labeled as a structural bridge rather than a polymerization mechanism. Catalyst, initiation, propagation, kinetics, branching control and process history remain correctly deferred to Working Chapter 015/016.

Final publication validation shall recheck exact IUPAC usage for `ethene`, industrial/common `ethylene`, CRU terminology, source-based versus structure-based polymer names and the warning concerning `poly(ethene-1,2-diyl)`.

## 5. Structure → property / evidence review

**PASS.**

The chapter's strongest book-wide contribution is the repeated separation:

`structure → mechanism hypothesis → measurable property → direct evidence → transferability → qualification → engineering decision`

Investigations 9–10 improve rather than contradict the earlier version of this logic.

The three material-specific teaching cases remain bounded by primary evidence and explicitly prohibit direct conversion into piping design values.

## 6. Equations / units / quantitative treatment

**N/A / PASS FOR SCOPE.**

No engineering equation is required to make the Chapter 014 decision logic work. The absence of equations is consistent with the CDB and PDS rule that equations shall not be invented to satisfy a quota.

Ideal reference angles (`~109.5°`, `~120°`, `~180°`) are explanatory geometry values rather than design tolerances. Final terminology/scientific validation should retain the explicit ideal-model qualifier.

## 7. Examples and engineering assets

### EX-014-001

**PASS candidate.**

The ethene / PE repeat-unit exercise correctly separates direct structural observations from polymerization route, molecular architecture, morphology and PE grade qualification.

### EX-014-002

**PASS candidate.**

The example refuses an underdetermined material ranking and converts the problem into an evidence specification, which is exactly the intended engineering behaviour.

### Tables / workflow / checklist

**PASS subject to integration synchronization.**

After integration, ensure the canonical asset register marks:

- `TAB-014-002` integrated;
- `TAB-014-003` integrated;
- `TAB-014-004` integrated;
- `EX-014-002` integrated;
- `FIG-014-006` scientific specification complete / graphic pending;
- `WF-014-001` integrated;
- `CL-014-001` integrated.

## 8. Standards / evidence lifecycle holds

These are not blockers to canonical integration but remain blockers to publication closure:

- ISO 472 lifecycle/current replacement status must be rechecked;
- ISO 1043-1 lifecycle/amendment state must be rechecked;
- the exact current IUPAC Gold Book version/date and term records used in final wording must be captured;
- IUPAC polymer-nomenclature terms used in Investigation 8 must be revalidated;
- final claim-level citation placement for primary-study material must be checked after canonical wording stabilizes.

No vocabulary or nomenclature source shall be treated as a pressure/design acceptance standard.

## 9. Editorial / navigation findings for later gate

Not blocking Technical Integration, but retain for Editorial/Style Review:

1. Investigation 1 already introduces a detailed mechanism→evidence workflow; after final `WF-014-001` is integrated in Investigation 10, shorten or cross-reference the earlier version if repetition impairs flow.
2. Several Investigations repeat the warning that chemistry does not establish pressure rating / temperature / compatibility. Repetition is justified pedagogically but should be checked for diminishing returns in the editorial pass.
3. Preserve the chapter's strong `why → mechanism → evidence boundary → decision` rhythm; do not turn the final manuscript into a chemistry glossary.

## 10. Pre-integration gate decision

**CONDITIONAL PASS — CANONICAL INTEGRATION MAY PROCEED AFTER APPLYING TR-014-01 THROUGH TR-014-04.**

No new research gate is required to integrate the currently approved Chapter 014 content.

After integration, perform a final full-file Technical Review because:

- section transitions will have changed;
- duplicate warnings/workflows may need consolidation;
- the asset register and review front matter must be synchronized;
- the full chapter must be Desk-Tested as one continuous manuscript.

## 11. Current chapter disposition

- CDB: approved.
- Technical Outline: approved.
- Investigations 1–10: authored as controlled candidates.
- Investigation 9 evidence gate: PASS.
- Investigation 9 authoring review: PASS.
- Investigation 10 / chapter-closure review: PASS.
- Pre-integration Technical Review: **CONDITIONAL PASS**.
- Canonical integration: OPEN.
- Final Technical Review: pending integration.
- Standards/Evidence Validation: pending.
- Editorial/Style Review: pending.
- Human Approval / merge: not authorized.
