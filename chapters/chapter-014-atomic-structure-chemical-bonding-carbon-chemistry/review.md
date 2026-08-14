# Chapter 014 — Review Record

**Chapter:** Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers  
**PDS baseline:** 1.0  
**Current stage:** Engineering Development  
**CDB author approval:** 2026-08-14  
**Development checkpoint:** Investigations 1–3 authored

## 1. Gate status

| Gate | Status | Current disposition |
|---|---|---|
| CDB / Definition of Ready | PASS | Author explicitly approved CDB-014 on 2026-08-14 |
| Technical Outline | ACTIVE | 10-Investigation implementation path defined |
| Evidence Plan | ACTIVE | Investigations 2–3 terminology checkpoints complete; staged evidence triggers retained |
| Engineering Development | IN PROGRESS | Investigations 1–3 authored; Investigations 4–10 not yet developed |
| Physics / scientific correctness review | PENDING | Formal review after broader development checkpoint |
| Standards / terminology validation | PARTIAL | Current ISO lifecycle recorded; IUPAC terminology checked through Investigation 3; final validation later |
| Academic / primary evidence review | PARTIAL | Not yet required for Investigations 1–3; mandatory before load-bearing material-specific claims |
| Equations | N/A CURRENT SCOPE | No equation introduced through Investigation 3 |
| Units | N/A CURRENT SCOPE | No quantitative engineering calculation introduced through Investigation 3 |
| Examples | PENDING | Planned in Investigations 8–9 |
| Editorial / Style | PENDING | Formal pass after substantive development |
| Desk Test | PENDING | Required before chapter closure |
| Final Author Approval | BLOCKED | Requires completion of all chapter gates |
| Design Freeze / publication | BLOCKED | Chapter remains in development |

## 2. Investigation 1 authoring review

### Scope compliance

**PASS for authoring checkpoint.**

Investigation 1:

- starts from the engineering question rather than an academic chemistry syllabus;
- establishes the atom → bond → molecule → chain → morphology → product → system hierarchy;
- makes the mechanism-versus-qualification boundary explicit;
- does not introduce polymerization mechanisms owned by Chapter 015;
- does not duplicate detailed chain architecture, morphology, thermal, viscoelastic or fracture content owned by Chapters 016–020;
- does not introduce a pressure-rating or chemical-compatibility design value.

### Evidence discipline

**PASS for current non-quantitative scope, subject to later formal review.**

Investigation 1 uses:

- CDB-014 / PPE-BoK architecture for scope;
- Chapter 009 only as internal context and non-duplication reference;
- ISO 472 / ISO 1043-1 as terminology/abbreviation sources only;
- IUPAC Gold Book as chemical terminology authority.

No material-specific quantitative property claim is used to support a design decision.

## 3. Investigation 2 authoring review

### Terminology checkpoint

**PASS for authoring checkpoint.**

The following IUPAC Gold Book entries were directly checked before authoring:

- atom — `A00493`;
- chemical element — `C01022`;
- atomic number / proton number — `A00499`;
- molecule — `M04002`;
- molecular entity — `M03986`;
- chemical substance — `C01039`;
- chemical species — `CT01038`.

### Scope compliance

**PASS for current foundational scope.**

Investigation 2:

- defines the minimum atomic/molecular vocabulary needed for later bonding work;
- distinguishes an individual atom from elemental identity/category;
- distinguishes molecule from the broader molecular-entity concept;
- explicitly prevents the false assumption that every chemical substance consists of discrete molecules;
- introduces atomic number only as an identity concept, not as a calculation exercise;
- stops before valence-electron/orbital treatment owned by Investigation 3;
- avoids nuclear-physics and quantum-mechanics detail that does not change the engineering reasoning;
- does not introduce any material-specific quantitative property or design-acceptance claim.

### Terminology risk controlled

The word `compound` has potential ambiguity between general chemical usage and the plastics-engineering meaning of a formulated polymer compound. Investigation 2 therefore establishes a wording rule: use precise entity/substance terminology for chemistry and use `polymer compound` / `piping compound` for the formulated engineering material when ambiguity is possible.

### Evidence disposition

**PASS for current stable-terminology scope, subject to final terminology validation.**

No primary polymer literature is required for the claims retained in Investigation 2 because the Investigation does not assert a material-specific structure→property magnitude or engineering acceptance conclusion.

## 4. Investigation 3 authoring review

### Terminology checkpoint

**PASS for authoring checkpoint.**

The following IUPAC Gold Book entries were directly checked before authoring:

- electron — `E01975`;
- atomic orbital — `A00500`;
- valence — `V06588`;
- electronegativity — `E01990`;
- electron-counting rules — `ET07022`;
- lone pair — `L03618`;
- Lewis formula — `L03513`.

### Scope compliance

**PASS for current foundational scope.**

Investigation 3:

- rejects the fixed planetary-orbit picture as a literal engineering/scientific model;
- defines atomic orbitals at the level needed to support later bonding and hybridization discussions;
- treats valence-electron language as a bounded introductory abstraction rather than a universal complete electronic-structure model;
- presents electronegativity as a relative atomic concept with multiple definitions/scales;
- keeps Lewis structures in the role of connectivity/electron-bookkeeping models rather than full molecular-geometry descriptions;
- stops before ionic/covalent/metallic bonding treatment owned by Investigation 4;
- does not introduce any material-specific quantitative property or design-acceptance claim.

### Evidence disposition

**PASS for current stable-terminology scope, subject to later formal scientific review.**

No primary polymer literature is required for Investigation 3 because the retained content concerns foundational electron/bonding terminology and explicitly avoids claiming measured polymer-property magnitudes.

## 5. Scientific simplification risks to monitor

The following items require explicit attention in later formal scientific review:

1. Do not imply that the chapter hierarchy is a strict one-way causal chain; feedback and multiscale interactions exist.
2. Do not imply that a named bond type uniquely determines a material class or bulk property.
3. Keep `chemical bond` terminology aligned with current IUPAC wording without reproducing extended source text unnecessarily.
4. Avoid implying that stronger intermolecular interaction always produces a monotonic increase/decrease in one bulk property.
5. Keep chemistry-to-compatibility examples qualitative until direct material-specific evidence is reviewed.
6. Do not use `molecule` as a universal synonym for every chemical entity or bulk substance.
7. Preserve the context-dependent dual usage of `chemical element` without confusing elemental identity with a separate elemental phase in a material.
8. Preserve the distinction between an orbital as a wavefunction/model and a classical particle path.
9. Do not imply that simple valence-shell drawings provide a complete electronic-structure description for every atom or bonding case.
10. Do not use electronegativity as a deterministic polymer-property or chemical-compatibility scale.

## 6. Controlled holds before Investigation 4

Investigation 4 may begin after a focused primary-bonding pass confirms the preferred chapter usage for:

- covalent bond;
- ionic bond;
- metallic bonding / delocalized-electron description;
- bond polarity versus bond type;
- controlled comparison among polymers, metals and ceramics without assigning bulk properties directly from a bond label.

If the Investigation uses statements such as “metals are generally ductile” or “ionic solids are brittle” as engineering teaching rules, those statements require appropriate materials-science evidence and qualification language rather than being presented as consequences of one bond type alone.

## 7. Controlled holds before Investigation 9

Investigation 9 is **BLOCKED** until direct primary sources are selected and reviewed for each material-specific structure–property example retained in the chapter.

The authoring team shall not backfill unsupported examples after writing.

## 8. Current decision

**CONTINUE ENGINEERING DEVELOPMENT SEQUENTIALLY TO INVESTIGATION 4 RESEARCH.**

Investigations 1–3 are controlled authoring candidates on the development branch. The chapter is not ready for technical closure, merge to `main`, or publication. Formal scientific/technical review remains a later gate after a broader substantive checkpoint.
