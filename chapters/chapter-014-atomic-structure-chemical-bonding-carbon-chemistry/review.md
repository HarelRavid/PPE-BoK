# Chapter 014 — Review Record

**Chapter:** Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers  
**PDS baseline:** 1.0  
**Current stage:** Engineering Development  
**CDB author approval:** 2026-08-14  
**Development checkpoint:** Investigations 1–6 authored

## 1. Gate status

| Gate | Status | Current disposition |
|---|---|---|
| CDB / Definition of Ready | PASS | Author explicitly approved CDB-014 on 2026-08-14 |
| Technical Outline | ACTIVE | 10-Investigation implementation path defined |
| Evidence Plan | ACTIVE | Terminology/evidence checkpoints complete through Investigation 6 |
| Engineering Development | IN PROGRESS | Investigations 1–6 authored; Investigations 7–10 not yet developed |
| Physics / scientific correctness review | PENDING | Formal review after broader development checkpoint |
| Standards / terminology validation | PARTIAL | Current ISO lifecycle recorded; IUPAC terminology/recommendations checked through Investigation 6; final validation later |
| Academic / primary evidence review | PARTIAL | IUPAC scientific recommendations reviewed where needed; polymer-specific primary literature remains mandatory before load-bearing structure→property claims |
| Equations | N/A CURRENT SCOPE | No design/calculation equation introduced through Investigation 6 |
| Units | N/A CURRENT SCOPE | No quantitative engineering calculation introduced through Investigation 6 |
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

**PASS for authoring checkpoint.** Directly checked IUPAC terminology for covalent bond, ionic bond, electron delocalization and chemical bond. The Investigation preserves degree-of-ionic-character reasoning, uses electron-delocalization language for metallic solids, separates bond model from material class, and prevents deterministic bond-type → bulk-property shortcuts.

## 6. Investigation 5 authoring review

**PASS for authoring checkpoint.** Directly checked the IUPAC Gold Book hierarchy for van der Waals, dipole–dipole, dipole-induced dipole and London/dispersion interactions, plus the 2011 IUPAC Hydrogen Bond Recommendation and Technical Report. The Investigation avoids duplicate van der Waals categorization, recognizes dispersion contributions in polar systems, rejects a one-dimensional intermolecular-force strength ladder, and distinguishes hydrogen bonding from covalent crosslinking.

## 7. Investigation 6 authoring review

### Evidence checkpoint

**PASS for authoring checkpoint.**

Directly checked/used:

- IUPAC Blue Book — standard bonding number framework, including standard bonding number `4` for carbon;
- IUPAC Gold Book — chain `C00946`;
- IUPAC Gold Book — branched chain `B00721`;
- IUPAC Gold Book — skeletal formula / bond-line formula `08208`;
- IUPAC Gold Book — skeletal structure `S05708`;
- IUPAC Gold Book — carbocyclic compounds `C00818`;
- IUPAC Gold Book — alkanes `A00222`.

### Scope compliance

**PASS for current foundational scope.**

Investigation 6:

- treats carbon's standard bonding number four as a structural/electron-counting convention, not anthropomorphic intent;
- explicitly prevents the false explanation that carbon's usefulness is due to tetravalency alone, noting that the same IUPAC bonding-number table assigns four to other relevant Group 14 elements;
- explains carbon–carbon connectivity as the framework enabling diverse carbon skeletons without converting that fact into a bulk material property;
- introduces linear, branched and cyclic connectivity only as structural possibilities and defers real polymer branching distributions/chain architecture to Chapter 016;
- introduces single versus multiple bond order only at the constitutional level and defers `sp`, `sp2`, `sp3`, sigma and pi mechanisms to Investigation 7;
- distinguishes carbon skeleton from hydrocarbon-only chemistry by keeping heteroatoms/substituents explicit;
- gives a controlled engineering reading method for skeletal/bond-line formulas;
- distinguishes the drawing term `skeletal formula` from polymer `skeletal structure`;
- initiates `TAB-014-002` as an inference-control table rather than a property-ranking table;
- introduces no material-specific quantitative property magnitude or piping design-acceptance value.

### Evidence disposition

**PASS for current stable organic/polymer-terminology scope, subject to later formal scientific review.**

No polymer-specific primary paper is load-bearing in Investigation 6 because the text stops at structural possibility and formula-reading discipline. Any later claim that a specific carbon skeleton or substituent causes a measured material property remains subject to the Chapter 014 primary-literature trigger.

## 8. Scientific simplification risks to monitor

1. Do not imply that the chapter hierarchy is a strict one-way causal chain; feedback and multiscale interactions exist.
2. Do not imply that a named bond type uniquely determines a material class or bulk property.
3. Do not force real bonds into perfectly pure ionic/covalent end-member categories where mixed character is more appropriate.
4. Do not present electron delocalization as a complete mechanical model of metals.
5. Keep intrachain primary bonding and noncovalent intersegment interactions as separate structural levels.
6. Do not use `van der Waals` as a duplicate additive force outside the umbrella hierarchy used by IUPAC.
7. Do not imply London/dispersion interactions disappear in polar systems.
8. Do not reduce hydrogen bonding to a universal `strong dipole–dipole` label or infer it from heteroatom presence alone.
9. Do not imply that tetravalency alone explains carbon's structural importance.
10. Do not interpret a visible branch in a teaching molecule as the branching distribution of a commercial polymer grade.
11. Do not treat a skeletal/bond-line drawing as actual 3D molecular geometry.
12. Do not allow a carbon skeleton or substituent to become a deterministic property/compatibility ranking without evidence.
13. Preserve the distinction between orbital models and classical particle paths.
14. Keep chemistry-to-compatibility examples qualitative until direct material-specific evidence is reviewed.

## 9. Controlled holds before Investigation 7

Investigation 7 may begin after a focused terminology/science pass confirms the preferred chapter treatment for:

- hybridization and hybrid orbitals;
- `sp`, `sp2`, `sp3` as useful models of local carbon bonding geometry;
- sigma and pi bonding terminology;
- approximate linear / trigonal-planar / tetrahedral geometry at the intended engineering depth;
- rotation about single bonds versus the additional constraint introduced by a pi component in a double bond;
- model limitations — especially avoiding presentation of hybrid orbitals as literal physical objects or hybridization labels as direct bulk-property predictors.

The Investigation shall stop before the ethylene-to-polyethylene reaction mechanism owned by Investigation 8 / Chapter 015.

## 10. Controlled holds before Investigation 9

Investigation 9 is **BLOCKED** until direct primary sources are selected and reviewed for each material-specific structure–property example retained in the chapter.

The authoring team shall not backfill unsupported examples after writing.

## 11. Current decision

**CONTINUE ENGINEERING DEVELOPMENT SEQUENTIALLY TO INVESTIGATION 7 RESEARCH.**

Investigations 1–6 are controlled authoring candidates on the development branch. The chapter is not ready for technical closure, merge to `main`, or publication. Formal scientific/technical review remains a later gate after a broader substantive checkpoint.
