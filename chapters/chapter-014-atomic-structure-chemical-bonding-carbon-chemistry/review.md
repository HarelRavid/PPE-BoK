# Chapter 014 — Review Record

**Chapter:** Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers  
**PDS baseline:** 1.0  
**Current stage:** Engineering Development  
**CDB author approval:** 2026-08-14  
**Development checkpoint:** Investigations 1–5 authored

## 1. Gate status

| Gate | Status | Current disposition |
|---|---|---|
| CDB / Definition of Ready | PASS | Author explicitly approved CDB-014 on 2026-08-14 |
| Technical Outline | ACTIVE | 10-Investigation implementation path defined |
| Evidence Plan | ACTIVE | Terminology/evidence checkpoints complete through Investigation 5 |
| Engineering Development | IN PROGRESS | Investigations 1–5 authored; Investigations 6–10 not yet developed |
| Physics / scientific correctness review | PENDING | Formal review after broader development checkpoint |
| Standards / terminology validation | PARTIAL | Current ISO lifecycle recorded; IUPAC terminology/recommendations checked through Investigation 5; final validation later |
| Academic / primary evidence review | PARTIAL | IUPAC scientific recommendations reviewed for Investigation 5; polymer-specific primary literature remains mandatory before load-bearing structure→property claims |
| Equations | N/A CURRENT SCOPE | No design/calculation equation introduced through Investigation 5 |
| Units | N/A CURRENT SCOPE | No quantitative engineering calculation introduced through Investigation 5 |
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

### Evidence checkpoint

**PASS for authoring checkpoint.**

Directly checked/used:

- IUPAC Gold Book — van der Waals forces `V06597`;
- IUPAC Gold Book — dipole–dipole interaction `D01758`;
- IUPAC Gold Book — dipole-induced dipole interaction `D01759`;
- IUPAC Gold Book — London/dispersion forces `L03617`;
- IUPAC Gold Book — polarizability `P04711`;
- Arunan et al. — *Definition of the hydrogen bond (IUPAC Recommendations 2011)*, DOI `10.1351/PAC-REC-10-01-02`;
- Arunan et al. — *Defining the hydrogen bond: An account (IUPAC Technical Report)*, DOI `10.1351/PAC-REP-10-01-01`.

### Scope compliance

**PASS for current foundational scope.**

Investigation 5:

- distinguishes intramolecular/intermolecular location from interaction type;
- uses `van der Waals` as an umbrella term rather than duplicating it as an extra force alongside its included components;
- explicitly records that London/dispersion interactions also contribute in polar systems;
- separates permanent-dipole, induced-dipole and dispersion mechanisms;
- treats hydrogen bonding through the dedicated IUPAC 2011 evidence-based framework rather than as a simple `strong dipole–dipole` label;
- prevents hydrogen bonding from being confused with covalent crosslinking;
- explicitly rejects a one-dimensional intermolecular-force strength ladder as a bulk-property predictor;
- completes the scientific/conceptual specification for Level B of `FIG-014-002`;
- extends `TAB-014-001` with van der Waals, dipolar, London/dispersion and hydrogen-bond rows;
- introduces no material-specific quantitative property magnitude or piping design-acceptance value.

### Evidence disposition

**PASS for current stable-mechanism scope, subject to later formal scientific review.**

No polymer-specific primary literature is load-bearing in Investigation 5 because the text deliberately stops before quantitative or material-ranked structure→property conclusions. Any later claim that a named piping polymer obtains a measured thermal, mechanical, transport, chemical or joining advantage from a specific intermolecular interaction remains subject to the Chapter 014 primary-literature trigger.

## 7. Scientific simplification risks to monitor

1. Do not imply that the chapter hierarchy is a strict one-way causal chain; feedback and multiscale interactions exist.
2. Do not imply that a named bond type uniquely determines a material class or bulk property.
3. Do not force real bonds into perfectly pure ionic/covalent end-member categories where mixed character is more appropriate.
4. Do not present electron delocalization as a complete mechanical model of metals.
5. Do not treat ceramics as purely ionic or polymers as mechanically governed only by covalent backbone bonds.
6. Keep intrachain primary bonding and noncovalent intersegment interactions as separate structural levels.
7. Do not use `van der Waals` as a duplicate additive force outside the umbrella hierarchy used by IUPAC.
8. Do not imply London/dispersion interactions disappear in polar systems.
9. Do not reduce hydrogen bonding to a universal `strong dipole–dipole` label or infer it from heteroatom presence alone.
10. Avoid implying that stronger/more numerous intermolecular interactions always cause a monotonic increase/decrease in one bulk property.
11. Keep chemistry-to-compatibility examples qualitative until direct material-specific evidence is reviewed.
12. Preserve the distinction between an orbital as a wavefunction/model and a classical particle path.
13. Do not use electronegativity or polarity as deterministic polymer-property scales.

## 8. Controlled holds before Investigation 6

Investigation 6 may begin after a focused carbon-chemistry terminology/science pass confirms the preferred chapter treatment for:

- carbon valence / tetravalency at the appropriate teaching depth;
- carbon–carbon and carbon–heteroatom connectivity;
- chains, branches and rings as structural possibilities without pre-empting Chapter 016 chain architecture;
- single/double/triple bond awareness while deferring `sp`, `sp2`, `sp3`, sigma and pi detail to Investigation 7;
- structural formula / skeletal representation conventions useful to polymer engineers;
- the exact boundary between stable organic-chemistry explanation and unsupported claims about bulk polymer properties.

Investigation 6 shall explain **why carbon offers structural versatility**, not claim that carbon chemistry alone determines polymer performance.

## 9. Controlled holds before Investigation 9

Investigation 9 is **BLOCKED** until direct primary sources are selected and reviewed for each material-specific structure–property example retained in the chapter.

The authoring team shall not backfill unsupported examples after writing.

## 10. Current decision

**CONTINUE ENGINEERING DEVELOPMENT SEQUENTIALLY TO INVESTIGATION 6 RESEARCH.**

Investigations 1–5 are controlled authoring candidates on the development branch. The chapter is not ready for technical closure, merge to `main`, or publication. Formal scientific/technical review remains a later gate after a broader substantive checkpoint.
