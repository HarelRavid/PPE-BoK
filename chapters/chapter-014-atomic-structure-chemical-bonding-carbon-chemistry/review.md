# Chapter 014 — Review Record

**Chapter:** Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers  
**PDS baseline:** 1.0  
**Current stage:** Engineering Development  
**CDB author approval:** 2026-08-14  
**Development checkpoint:** Investigations 1–8 authored

## 1. Gate status

| Gate | Status | Current disposition |
|---|---|---|
| CDB / Definition of Ready | PASS | Author explicitly approved CDB-014 on 2026-08-14 |
| Technical Outline | ACTIVE | 10-Investigation implementation path defined |
| Evidence Plan | ACTIVE | Terminology/evidence checkpoints complete through Investigation 8; Investigation 9 primary-literature gate now active |
| Engineering Development | IN PROGRESS | Investigations 1–8 authored; Investigation 9 blocked on primary literature; Investigation 10 not yet developed |
| Physics / scientific correctness review | PENDING | Formal review after broader development checkpoint |
| Standards / terminology validation | PARTIAL | Current ISO lifecycle recorded; IUPAC terminology/recommendations checked through Investigation 8; final validation later |
| Academic / primary evidence review | ACTIVE GATE | Foundational IUPAC sources reviewed; direct polymer primary literature now required before Investigation 9 prose |
| Equations | N/A CURRENT SCOPE | No design/calculation equation introduced through Investigation 8 |
| Units | N/A CURRENT SCOPE | No quantitative engineering calculation introduced through Investigation 8 |
| Examples | PARTIAL | `EX-014-001` integrated; independent scientific/editorial check later; `EX-014-002` blocked with Investigation 9 |
| Editorial / Style | PENDING | Formal pass after substantive development |
| Desk Test | PENDING | Required before chapter closure |
| Final Author Approval | BLOCKED | Requires completion of all chapter gates |
| Design Freeze / publication | BLOCKED | Chapter remains in development |

## 2. Investigations 1–5 authoring disposition

**PASS for their current authoring checkpoints.**

- Investigation 1 establishes the chemistry → mechanism → measured property → qualification → engineering decision boundary.
- Investigation 2 controls atom/element/molecule/molecular-entity/substance terminology.
- Investigation 3 controls electron/orbital/valence/electronegativity language and rejects literal planetary-orbit imagery.
- Investigation 4 controls covalent/ionic-character/electron-delocalization models without bond-type → bulk-property determinism.
- Investigation 5 controls van der Waals/dipolar/dispersion/hydrogen-bond terminology without a one-dimensional interaction-strength ladder.

## 3. Investigation 6 authoring review

**PASS for current foundational scope.**

Investigation 6 uses the IUPAC Blue Book standard bonding-number framework and Gold Book chain/branch/skeletal terminology. It treats carbon's four-bond convention as necessary context rather than the sole explanation of carbon chemistry, keeps real chain architecture in Chapter 016, distinguishes skeletal formula from 3D geometry, and introduces `TAB-014-002` as an inference-control tool rather than a property-ranking table.

## 4. Investigation 7 authoring review

**PASS for current foundational scope.**

Directly checked IUPAC terminology for hybridization, hybrid orbital, sigma/pi, rotational barrier, free rotation, conformation and angle strain, plus IUPAC graphical-representation guidance. The Investigation:

- treats hybridization as a local orbital model, not literal physical mixing;
- uses idealized `sp3` / `sp2` / `sp` geometry with bounded `109.5°` / `120°` / `180°` reference values;
- distinguishes localized σ/π language from rigorous MO-symmetry use;
- replaces `single bonds rotate freely` with rotational-barrier/time-scale language;
- defines `FIG-014-003` and the initial scientific specification for `FIG-014-004`;
- stops before polymerization chemistry.

## 5. Investigation 8 authoring review

### Evidence checkpoint

**PASS for authoring checkpoint.**

Directly checked/used:

- IUPAC nomenclature guidance distinguishing monomer `CH2=CH2` as **ethene** from `ethylene` as a divalent-group name in strict nomenclature, while preserving established industrial/common `ethylene` usage where unambiguous;
- IUPAC Gold Book — monomer `M04017`;
- IUPAC Gold Book — monomeric unit `M04018`;
- IUPAC Gold Book — polymerization `P04740`;
- IUPAC Gold Book — chain polymerization `C00958`;
- IUPAC Gold Book — polyolefin `15255`;
- IUPAC Gold Book — `poly(ethene-1,2-diyl)` `08890`, used specifically as a false-friend warning rather than as a polyethylene synonym;
- IUPAC regular single-strand polymer nomenclature guidance for `polyethene` / `polyethylene` source-based naming and `poly(methylene)` structure-based context.

### Scope compliance

**PASS for current foundational scope.**

Investigation 8:

- identifies `CH2=CH2` as ethene and explicitly controls industrial/common `ethylene` usage;
- applies the Investigation 7 local `sp2` / σ+π model to ethene without reopening orbital theory;
- explains why the C=C feature is chemically relevant while stopping before an actual chain-growth mechanism;
- presents `CH2=CH2 → [–CH2–CH2–]n` only as a **structural comparison**, explicitly not as a polymerization mechanism;
- distinguishes monomer, monomeric unit and CRU concepts;
- defers initiation, propagation, termination, chain transfer, radical chemistry, Ziegler–Natta/metallocene catalysis, kinetics, molecular-weight control and branching control to Chapters 015–016;
- explicitly warns that ordinary saturated polyethylene is not `poly(ethene-1,2-diyl)`;
- completes the scientific specifications for `FIG-014-004` and `FIG-014-005`;
- integrates `EX-014-001 — Reading ethene and the PE repeat unit`;
- explicitly states that `[–CH2–CH2–]n` does not define PE80, PE100, SCG resistance, morphology, additive package, pressure rating, chemical compatibility, service temperature or joining parameters;
- introduces no material-specific design-acceptance value.

### Evidence disposition

**PASS for current nomenclature/structural-bridge scope, subject to later formal scientific/editorial review.**

`EX-014-001` is integrated as a controlled teaching example but still requires an independent scientific/editorial check before chapter closure.

No material-specific structure→property claim is load-bearing in Investigation 8. The next Investigation deliberately changes that evidence level and therefore remains blocked until direct primary literature is reviewed.

## 6. Scientific simplification risks to monitor

1. Do not treat the chapter hierarchy as a strict one-way causal chain.
2. Do not assign bulk properties directly from bond type, polarity, interaction type or hybridization.
3. Do not force real bonds into pure ionic/covalent end-member categories.
4. Do not present electron delocalization as a complete mechanical model of metals.
5. Keep covalent connectivity, noncovalent interactions, chain architecture and morphology as separate levels.
6. Do not duplicate `van der Waals` as an extra force beside its included components.
7. Do not imply dispersion disappears in polar systems.
8. Do not reduce hydrogen bonding to `strong dipole–dipole` or infer it from heteroatom presence alone.
9. Do not imply tetravalency alone explains carbon's importance.
10. Do not infer commercial branching from a teaching structure.
11. Do not treat skeletal/bond-line drawings as actual 3D geometry.
12. Do not present hybrid orbitals as hard physical objects or literal mixtures.
13. Do not treat ideal angles as universal exact molecular values.
14. Do not say a whole polymer is simply `sp2`/`sp3` without local context.
15. Do not say single bonds have zero rotational barrier.
16. Do not say double bonds are merely two identical single bonds.
17. Distinguish localized σ/π language from rigorous molecular-orbital symmetry usage.
18. Do not use a one-line ethene→PE arrow as a reaction mechanism.
19. Do not silently mix strict ethene/ethylene nomenclature contexts.
20. Do not use a PE repeat-unit drawing as a grade/material qualification.
21. Keep chemistry-to-property/compatibility examples qualitative until direct material-specific evidence is reviewed.

## 7. Controlled hold before Investigation 9 — PRIMARY LITERATURE GATE

Investigation 9 is **BLOCKED** until each retained material-specific structure→property bridge has direct primary evidence.

Before authoring any Investigation 9 prose, the authoring team shall define a small controlled set of examples and, for each example, record:

1. the exact molecular feature being compared;
2. the proposed physical/chemical mechanism;
3. the measured engineering property used to test that mechanism;
4. the direct primary study/studies reviewed;
5. material identity and condition;
6. test temperature/environment/method;
7. confounders such as molecular weight, crystallinity, morphology, formulation or processing;
8. transferability to commercial piping compounds;
9. what conclusion is supported;
10. what conclusion remains unsupported.

A review paper may locate candidate literature but shall not close the gate for a load-bearing claim. The underlying primary work must be reviewed directly.

`EX-014-002` and `TAB-014-003` remain blocked with this gate.

## 8. Controlled hold before Investigation 10

Investigation 10 shall not be authored until Investigation 9 establishes the final evidence-qualified structure→property examples. Investigation 10 will then formalize:

- `FIG-014-006`;
- `WF-014-001`;
- `CL-014-001`;
- `TAB-014-004` downstream chapter ownership;
- the final chemistry→engineering decision boundary.

## 9. Current decision

**STOP SEQUENTIAL AUTHORING AT THE INVESTIGATION 9 PRIMARY-LITERATURE GATE; BEGIN DIRECT PRIMARY-LITERATURE RESEARCH.**

Investigations 1–8 are controlled authoring candidates on the development branch. The chapter is not ready for technical closure, Ready-for-Review transition, merge to `main`, or publication. Investigation 9 prose must not be written until its direct-evidence gate is formally satisfied.
