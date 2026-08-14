# Chapter 014 — Review Record

**Chapter:** Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers  
**PDS baseline:** 1.0  
**Current stage:** Engineering Development  
**CDB author approval:** 2026-08-14  
**Development checkpoint:** Investigations 1–4 authored

## 1. Gate status

| Gate | Status | Current disposition |
|---|---|---|
| CDB / Definition of Ready | PASS | Author explicitly approved CDB-014 on 2026-08-14 |
| Technical Outline | ACTIVE | 10-Investigation implementation path defined |
| Evidence Plan | ACTIVE | Terminology/evidence checkpoints complete through Investigation 4 |
| Engineering Development | IN PROGRESS | Investigations 1–4 authored; Investigations 5–10 not yet developed |
| Physics / scientific correctness review | PENDING | Formal review after broader development checkpoint |
| Standards / terminology validation | PARTIAL | Current ISO lifecycle recorded; IUPAC terminology checked through Investigation 4; final validation later |
| Academic / primary evidence review | PARTIAL | Not yet required for current foundational claims; mandatory before load-bearing material-specific claims |
| Equations | N/A CURRENT SCOPE | No design/calculation equation introduced through Investigation 4 |
| Units | N/A CURRENT SCOPE | No quantitative engineering calculation introduced through Investigation 4 |
| Examples | PENDING | Planned in Investigations 8–9 |
| Editorial / Style | PENDING | Formal pass after substantive development |
| Desk Test | PENDING | Required before chapter closure |
| Final Author Approval | BLOCKED | Requires completion of all chapter gates |
| Design Freeze / publication | BLOCKED | Chapter remains in development |

## 2. Investigation 1 authoring review

**PASS for authoring checkpoint.** Investigation 1 establishes the atom → bond → molecule → chain → morphology → product → system hierarchy and the chapter-wide rule that chemistry explains mechanisms but does not replace qualification or design evidence.

## 3. Investigation 2 authoring review

**PASS for authoring checkpoint.** Directly checked IUPAC terminology for atom, chemical element, atomic number, molecule, molecular entity, chemical substance and chemical species. The Investigation prevents a molecule-only model of matter and disambiguates chemical `compound` from a formulated polymer/piping compound.

## 4. Investigation 3 authoring review

**PASS for authoring checkpoint.** Directly checked IUPAC terminology for electron, atomic orbital, valence, electronegativity, electron-counting rules, lone pair and Lewis formula. The Investigation rejects literal planetary-orbit imagery, treats valence language as a bounded abstraction and prevents electronegativity from being used as a direct polymer-property predictor.

## 5. Investigation 4 authoring review

### Terminology checkpoint

**PASS for authoring checkpoint.**

Directly checked current IUPAC Gold Book entries for:

- covalent bond — `C01384`;
- ionic bond — `IT07058`;
- delocalization of electrons — `08789`;
- chemical bond — `CT07009`.

### Scope compliance

**PASS for current foundational scope.**

Investigation 4:

- defines covalent bonding from shared/high electron density without converting bond strength into pipe strength;
- preserves IUPAC's explicit preference for considering degree of ionic character rather than a false pure ionic/pure covalent binary;
- uses verified electron-delocalization language for metallic solids instead of inventing an authoritative `metallic bond` definition not found in the current terminology pass;
- separates bond model from bulk material class;
- explicitly prevents `ceramic = ionic`, `metallic bonding = ductile`, and `covalent backbone = strong pipe` shortcuts;
- distinguishes bond polarity/ionic character from bond category;
- introduces the primary rows of `TAB-014-001` and the Level-A placeholder for `FIG-014-002`, both to be completed with intermolecular interactions in Investigation 5;
- introduces no material-specific property magnitude or design-acceptance value.

### Evidence disposition

**PASS for current foundational scope, subject to later formal scientific review.**

The material-class comparisons are deliberately bounded and do not rely on unsourced quantitative property rankings. A later scientific review shall specifically check that the text has not implied deterministic bond-type → bulk-property relationships.

## 6. Scientific simplification risks to monitor

1. Do not imply that the chapter hierarchy is a strict one-way causal chain; feedback and multiscale interactions exist.
2. Do not imply that a named bond type uniquely determines a material class or bulk property.
3. Do not force real bonds into perfectly pure ionic/covalent end-member categories where mixed character is more appropriate.
4. Do not present electron delocalization as a complete mechanical model of metals.
5. Do not treat ceramics as purely ionic or polymers as mechanically governed only by covalent backbone bonds.
6. Keep intrachain primary bonding and interchain/intermolecular interactions as separate structural levels.
7. Avoid implying that stronger intermolecular interaction always produces a monotonic change in one bulk property.
8. Keep chemistry-to-compatibility examples qualitative until direct material-specific evidence is reviewed.
9. Preserve the distinction between an orbital as a wavefunction/model and a classical particle path.
10. Do not use electronegativity as a deterministic polymer-property or chemical-compatibility scale.

## 7. Controlled holds before Investigation 5

Investigation 5 may begin after direct verification of the preferred terminology/evidence for:

- hydrogen bond — IUPAC 2011 Recommendation and Technical Report;
- dipole–dipole interaction;
- London forces / dispersion interaction;
- van der Waals forces and the hierarchy/overlap of these terms;
- distinction between an intramolecular chemical bond and an intermolecular interaction;
- any claim connecting intermolecular attraction to polymer mobility, thermal response or mechanical behaviour.

Stable definitions may be authored from IUPAC. Any retained polymer-specific property consequence requires either clearly bounded qualitative wording or directly reviewed material evidence.

## 8. Controlled holds before Investigation 9

Investigation 9 is **BLOCKED** until direct primary sources are selected and reviewed for each material-specific structure–property example retained in the chapter.

The authoring team shall not backfill unsupported examples after writing.

## 9. Current decision

**CONTINUE ENGINEERING DEVELOPMENT SEQUENTIALLY TO INVESTIGATION 5 RESEARCH.**

Investigations 1–4 are controlled authoring candidates on the development branch. The chapter is not ready for technical closure, merge to `main`, or publication. Formal scientific/technical review remains a later gate after a broader substantive checkpoint.
