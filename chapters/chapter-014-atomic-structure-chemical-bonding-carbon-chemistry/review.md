# Chapter 014 — Review Record

**Chapter:** Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers  
**PDS baseline:** 1.0  
**Current stage:** Engineering Development  
**CDB author approval:** 2026-08-14  
**Development checkpoint:** Investigations 1–8 authored; Investigation 9 primary-literature gate passed for controlled Cases A–C

## 1. Gate status

| Gate | Status | Current disposition |
|---|---|---|
| CDB / Definition of Ready | PASS | Author explicitly approved CDB-014 on 2026-08-14 |
| Technical Outline | ACTIVE | 10-Investigation implementation path defined |
| Evidence Plan | ACTIVE | Terminology/evidence checkpoints complete through Investigation 8; Investigation 9 Evidence Matrix complete |
| Engineering Development | IN PROGRESS | Investigations 1–8 authored; Investigation 9 now authorized for Cases A–C only; Investigation 10 not yet developed |
| Physics / scientific correctness review | PENDING | Formal review after broader development checkpoint |
| Standards / terminology validation | PARTIAL | Current ISO lifecycle recorded; IUPAC terminology/recommendations checked through Investigation 8; final validation later |
| Academic / primary evidence review | PASS FOR INV9 ENTRY | Four primary studies directly reviewed; Cases A–C have explicit transferability limits |
| Equations | N/A CURRENT SCOPE | No design/calculation equation introduced through Investigation 8 |
| Units | N/A CURRENT SCOPE | No quantitative engineering calculation introduced through Investigation 8 |
| Examples | PARTIAL | `EX-014-001` integrated; `EX-014-002` now authorized for evidence-bounded development using Cases A–C only |
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

**PASS for current nomenclature/structural-bridge scope.**

Investigation 8 directly controls ethene/ethylene nomenclature, monomer/monomeric-unit/CRU concepts, the `sp2`/σ+π ethene model, and the structural-only `CH2=CH2 → [–CH2–CH2–]n` bridge. It completes the scientific specifications for `FIG-014-004` and `FIG-014-005`, integrates `EX-014-001`, and explicitly prevents the PE repeat-unit drawing from being treated as PE80/PE100/material qualification.

`EX-014-001` remains subject to independent scientific/editorial checking before chapter closure.

## 6. Investigation 9 primary-literature gate review

### Gate evidence

**PASS FOR CONTROLLED AUTHORING — CASES A–C ONLY.**

The gate was closed with four directly reviewed primary studies:

1. **S014-009 — Shinzawa & Mizukado (2020)**, *Water absorption by polyamide (PA) 6 studied with two-trace two-dimensional (2T2D) near-infrared (NIR) correlation spectroscopy*, Journal of Molecular Structure 1217, 128389, DOI `10.1016/j.molstruc.2020.128389`.
2. **S014-010 — Sambale, Stanko, Emde & Stommel (2021)**, *Characterisation and FE Modelling of the Sorption and Swelling Behaviour of Polyamide 6 in Water*, Polymers 13(9), 1480, DOI `10.3390/polym13091480`.
3. **S014-011 — Graunke, Schmitt, Raible & Wöllenstein (2016)**, *Towards Enhanced Gas Sensor Performance with Fluoropolymer Membranes*, Sensors 16(10), 1605, DOI `10.3390/s16101605`.
4. **S014-012 — Monson, Moon & Extrand (2009)**, *Gas permeation resistance of various grades of perfluoroalkoxy–polytetrafluoroethylene copolymers*, Journal of Applied Polymer Science 111(1), 141–147, DOI `10.1002/app.28858`.

### Controlled Cases

#### Case A — PA6 amide/H-bond chemistry → water sorption / swelling / mechanical response

**Evidence supports:** water exposure measurably changes PA6 sorption/swelling and, in the Shinzawa/Mizukado study, Young's modulus; the spectroscopy-based interpretation connects absorbed water with disruption of H-bonded bridges, increased chain mobility and concurrent morphology changes.

**Confounders retained:** amorphous/crystalline fraction, conditioning, concentration, geometry, specimen form and test method.

**Transferability:** mechanism-level only. No universal polyamide compatibility, swelling allowance, modulus derating or piping acceptance may be derived.

#### Case B — fluoropolymer chemistry → gas/water-vapor transport

**Evidence supports:** repeat-unit chemistry/fluorination/polarity can motivate transport hypotheses, but measured transport across the studied fluoropolymer membranes is not reducible to one simple chemical ranking; morphology/free-volume/film variables remain relevant.

**Confounders retained:** membrane form/thickness, commercial grade, crystallinity/free volume, humidity/gas and sensor-test configuration.

**Transferability:** deliberately low for pipe-specific magnitude; retained as a falsification/discipline example.

#### Case C — PFA grade/process/morphology → H2/N2/O2 transport

**Evidence supports:** slow-cooled compression-molded PFA specimens showed substantially better permeation resistance than fast-cooled specimens; the authors concluded that process can be as important as polymer grade, with differences attributed to crystallinity arising from architecture/processing.

**Confounders retained:** cooling rate, crystallinity, comonomer content, filler, specimen processing and gas.

**Transferability:** general mechanism that processing/morphology matter is useful; no pipe-specific permeability or hydrogen-service acceptance may be transferred.

### Gate discipline

The Investigation 9 Evidence Matrix records for each case:

- exact feature/hypothesis;
- measured property;
- direct source;
- confounders;
- supported conclusion;
- unsupported conclusion;
- transferability to piping compounds.

No fourth material example may be added without passing the same gate.

### Metadata correction recorded

Two pre-gate draft metadata errors were corrected before entering the repository as controlled evidence:

- Sambale et al. is **Polymers 13(9), 1480**, DOI `10.3390/polym13091480`, not the previously drafted Materials/2623 reference;
- the 2020 PA6 NIR paper authors are **Hideyuki Shinzawa and Junji Mizukado**.

This correction is evidence that publisher/primary metadata verification is functioning as intended.

## 7. Scientific simplification risks to monitor

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
21. Do not convert PA6 water data into a universal PA/piping rule.
22. Do not convert fluoropolymer membrane data into a piping-grade permeability ranking.
23. Do not convert the PFA cooling experiment into a universal processing prescription.
24. Treat processing, morphology and conditioning as possible confounders whenever a chemical structure→property claim is evaluated.
25. Keep every Investigation 9 conclusion paired with an explicit unsupported conclusion.

## 8. Authorized scope for Investigation 9 authoring

Investigation 9 may now author only:

- the evidence workflow for moving from molecular feature to measured-property hypothesis;
- Case A, Case B and Case C above;
- `TAB-014-003` using those cases;
- `EX-014-002` only if it compares hypotheses/evidence rather than ranking commercial materials;
- the first formal version of `FIG-014-006` and `WF-014-001`.

No piping design number, compatibility threshold, permeability allowance, modulus derating or material ranking is authorized from these studies.

## 9. Controlled hold before Investigation 10

Investigation 10 shall not be authored until Investigation 9 is complete and its transferability wording has passed an authoring review. Investigation 10 will then formalize:

- final `FIG-014-006`;
- final `WF-014-001`;
- `CL-014-001`;
- `TAB-014-004` downstream chapter ownership;
- the final chemistry→engineering decision boundary.

## 10. Current decision

**AUTHORIZE INVESTIGATION 9 CONTROLLED AUTHORING FOR CASES A–C ONLY.**

Investigations 1–8 remain controlled authoring candidates; the Investigation 9 primary-literature entry gate is now passed. The chapter is still not ready for technical closure, Ready-for-Review transition, merge to `main`, or publication.

## 11. Canonical-integration checkpoint — 2026-08-15

Investigations 9–10 were integrated into `chapter.md` only after their controlled authoring reviews, the pre-integration Technical Review, the logical-manuscript Technical/Evidence Review and the logical-manuscript Editorial/Desk Review. The integration applied TR-014-01 through TR-014-04, including claim-class/evidence-level disambiguation, noncovalent-interaction terminology for FIG-014-002, explicit non-normative labeling of the PPE-BoK evidence ladder, and Investigation 9 transferability wording controls.

**Current disposition:** Engineering Development arc integrated; final full-file Technical Review is the next gate. Final claim-level Standards/Evidence publication pass, final Editorial/Style Review, final Desk Test, Human Approval and merge remain open.
