# TO-014 — Technical Outline

**Chapter:** Working Chapter 014 — Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers  
**PDS baseline:** 1.0  
**CDB:** `docs/PDS/Chapter-Design-Briefs/CDB-014-Atomic-Structure-Chemical-Bonding-Carbon-Chemistry.md`  
**Status:** Active Engineering Development Outline  
**Date:** 2026-08-14

## 1. Primary engineering question

> Why can materials that are all described as plastics behave very differently in pressure piping, chemical service, temperature exposure, permeation, cracking and fusion joining, and what can an engineer legitimately infer from molecular structure before measured/qualified evidence is required?

## 2. Chapter engineering chain

The chapter shall progressively build this reasoning model:

`atom → electron structure → bond → molecular geometry / polarity → intermolecular interaction → carbon framework → monomer structure → plausible molecular mechanism → measured material property → qualification evidence → engineering decision`

The first half of the chain explains **why a mechanism is plausible**. The second half determines **whether the mechanism is engineering evidence**.

The chapter must make that boundary visible repeatedly.

## 3. Depth policy

### Include

- first-principles chemistry needed to reason about polymer behaviour;
- simple structural formulas and molecular geometry;
- distinction between primary and intermolecular bonding;
- carbon tetravalency and structural diversity;
- `sp`, `sp2`, `sp3`, sigma and pi concepts at engineering-use depth;
- ethylene as the controlled bridge to Chapter 015;
- structure-to-property hypotheses with explicit evidence limits;
- common piping polymers only as bounded examples.

### Exclude

- wave functions, quantum-number derivations and orbital mathematics without engineering payoff;
- polymerization kinetics, catalyst chemistry or reaction engineering — Ch015;
- molecular-weight distribution, branching/crosslinking engineering — Ch016;
- crystallinity/morphology — Ch017;
- `Tg`, `Tm` and thermophysical design — Ch018;
- viscoelasticity/creep/TTS — Ch019;
- fracture/SCG/RCP/fatigue/ESC/ageing — Ch020;
- material-selection rankings and pressure design values;
- chemical-compatibility tables or simplified solubility rules presented as design acceptance.

## 4. Investigation structure

# Investigation 1 — Why should a piping engineer care about atoms and bonds?

### Engineering capability

Establish that macroscopic pipe behaviour emerges through multiple structural levels and teach the evidence boundary between mechanism and qualification.

### Core concepts

- “Plastic” is a broad material category, not a single engineering behaviour.
- Molecular chemistry is one level in a hierarchy, not the complete material description.
- Bonding and molecular interactions can explain trends and mechanisms.
- Bulk properties also depend on chain architecture, morphology, additives, processing history, time/temperature and product qualification.
- First-principles reasoning is useful for framing the right question, not for inventing allowable values.

### Required asset

- introduce `FIG-014-001 — Atom-to-material hierarchy` as a controlled figure placeholder;
- introduce the chapter-level reasoning boundary that later becomes `FIG-014-006`.

### Evidence

- CDB-014 and Chapter 009 for architecture/non-duplication;
- IUPAC terminology source for the meaning of chemical bond;
- no material-specific quantitative property claim.

### End decision

The engineer should know when a chemistry-based inference is useful, and when to stop and demand a measured property, qualified material or governing standard.

---

# Investigation 2 — What is matter made of at the useful engineering scale?

### Engineering capability

Use atom, element, molecule, compound and molecular entity correctly and distinguish those levels from polymer chains, phases and bulk pipe material.

### Technical content

- atoms and atomic number;
- elements versus compounds;
- molecule / molecular entity;
- nucleus and electrons only to the depth needed for bonding;
- why isotopic detail, nuclear physics and subatomic-particle theory are normally outside piping engineering;
- scale transition: atom → small molecule → repeat unit → chain → bulk material.

### Required asset

- develop the first complete version of `FIG-014-001`.

### Common error to prevent

Using “molecule”, “polymer”, “resin”, “compound” and “pipe material” as interchangeable terms.

---

# Investigation 3 — Which electrons actually control chemical bonding?

### Engineering capability

Understand valence electrons, orbitals and the minimum periodic/electronegativity concepts needed to interpret polymer chemical structures.

### Technical content

- inner versus valence electrons;
- atomic orbitals as a useful model;
- valence capacity;
- electronegativity as a relative concept with multiple definitions/scales;
- bond polarity as unequal electron sharing;
- why electronegativity difference is a qualitative guide, not a universal property equation.

### Candidate asset

- small controlled table: descriptor → useful inference → invalid inference.

### Common error to prevent

Turning a single electronegativity number into a chemical-resistance or adhesion prediction.

---

# Investigation 4 — What are primary bonds and why do material classes differ?

### Engineering capability

Distinguish ionic, covalent and metallic bonding and understand why different bonding architectures enable different classes of material behaviour.

### Technical content

- covalent bonding and directional/shared-electron models;
- ionic character as a continuum rather than a simplistic pure-bond binary;
- metallic bonding at only the depth needed for polymer-versus-metal comparison;
- material class is not determined by one bond label alone;
- network structure, molecular mobility and microstructure govern bulk response.

### Required assets

- `TAB-014-001 — Bonding types and engineering relevance`;
- first half of `FIG-014-002 — Primary Bonding and Noncovalent Interaction Map`.

### Common error to prevent

“Covalent bonds are strong, therefore the polymer is strong.”

---

# Investigation 5 — What holds polymer molecules together when they are not covalently bonded to each other?

### Engineering capability

Separate intramolecular covalent bonding from intermolecular attraction and identify the major non-covalent interaction classes relevant to polymer reasoning.

### Technical content

- intermolecular versus intramolecular interaction;
- permanent dipoles and dipole–dipole interaction;
- London/dispersion forces;
- van der Waals terminology and scope;
- hydrogen bonding using current IUPAC recommendation;
- dependence on orientation, polarizability and molecular context;
- why these interactions can affect packing, mobility and phase behaviour but do not uniquely fix a bulk property.

### Required assets

- complete `FIG-014-002`;
- expand `TAB-014-001`.

### Evidence

- IUPAC Gold Book terms;
- IUPAC 2011 H-bond Recommendation and Technical Report.

### Common error to prevent

Treating “van der Waals”, “dispersion” and “hydrogen bond” as synonyms.

---

# Investigation 6 — Why is carbon uniquely useful for polymer backbones?

### Engineering capability

Understand why carbon can produce the structural diversity required for long-chain organic molecules without teaching a complete organic chemistry course.

### Technical content

- carbon valence/tetravalency at the useful model level;
- C–C and C–H frameworks;
- chains, branches and rings;
- single versus multiple bonds;
- structural diversity from heteroatoms/side groups only as a preview;
- controlled examples from common piping-polymer repeat units.

### Required asset

- begin `TAB-014-003 — Controlled polymer-structure examples`.

### Common error to prevent

Assuming all carbon-backbone polymers should have similar engineering performance.

---

# Investigation 7 — What do sp, sp2, sp3, sigma and pi bonds mean to the engineer?

### Engineering capability

Use hybridization as a molecular-geometry model and distinguish single/double-bond rotational and geometric consequences at a practical level.

### Technical content

- hybridization as linear combination / model of atomic orbitals;
- `sp3` tetrahedral, `sp2` trigonal, `sp` linear as bounded geometry models;
- sigma and pi labels;
- why double bonds constrain geometry differently from ordinary C–C single bonds;
- model limitations and avoidance of unnecessary orbital mathematics.

### Required assets

- `FIG-014-003 — Carbon hybridization and geometry`;
- `FIG-014-004 — Sigma and pi bonding in ethylene`.

### Common error to prevent

Treating hybridization as a standalone predictor of stiffness, melting temperature or pressure capability.

---

# Investigation 8 — What is special about ethylene?

### Engineering capability

Read the ethylene structure, identify the C=C bonding state and understand exactly where Chapter 014 stops and Chapter 015 begins.

### Technical content

- ethene/ethylene structure;
- planar `sp2` carbon geometry;
- sigma + pi description of the double bond;
- conceptual comparison to the saturated C–C backbone structure after polymerization;
- no catalyst, propagation, kinetics or process-mechanism treatment.

### Required assets

- finalize `FIG-014-004`;
- `FIG-014-005 — Ethylene to polyethylene bridge`;
- `EX-014-001 — Reading ethylene and the polyethylene repeat unit`.

### Common error to prevent

Presenting “opening the double bond” as a complete polymerization mechanism.

---

# Investigation 9 — How do molecular features become engineering-property hypotheses?

### Engineering capability

Translate structure into a testable mechanism hypothesis while explicitly identifying the missing evidence needed before design use.

### Controlled comparison fields

- polarity;
- side-group chemistry;
- rotational freedom;
- intermolecular attraction;
- packing potential;
- molecular symmetry where useful;
- heteroatoms / halogen substitution where relevant.

### Engineering properties that may be discussed only at mechanism level unless directly evidenced

- stiffness;
- softening/thermal response;
- diffusion/permeation;
- solvent/chemical interaction;
- fusion behaviour;
- fracture response.

### Required primary-literature rule

Any claim that a real named polymer or piping compound has a specific property trend because of one of these molecular features requires a directly reviewed source and an applicability limit.

### Required assets

- `TAB-014-002 — Molecular feature / likely mechanism / what cannot be concluded directly`;
- complete `TAB-014-003`;
- `EX-014-002 — Comparing two simple polymer structures`;
- `FIG-014-006 — Molecular feature to engineering evidence chain`.

### Common error to prevent

Using molecular intuition as a substitute for property data or qualification.

---

# Investigation 10 — What can chemistry tell us, and where must the engineer stop?

### Engineering capability

Close the chapter with a disciplined decision boundary and route the next question to the correct PPE-BoK chapter.

### Technical content

- mechanism hypothesis versus measured property;
- resin versus compound versus product qualification;
- trend versus design value;
- transferability and uncertainty;
- when to require testing;
- when to require material-specific evidence;
- when a product/application standard governs;
- when the next question belongs to Ch015–020 or later material/design Parts.

### Required assets

- finalize `FIG-014-006`;
- `TAB-014-004 — Chapter ownership crosswalk`;
- `WF-014-001 — Chemical structure to engineering decision boundary`;
- `CL-014-001 — Before inferring engineering behaviour from a chemical structure`.

### End decision

A competent engineer should be able to use chemistry to form and test hypotheses while refusing to promote those hypotheses into design acceptance without the required evidence.

## 5. Asset register — Technical Outline state

| ID | Asset | Outline state |
|---|---|---|
| FIG-014-001 | Atom-to-material hierarchy | Defined; introduce in Investigation 1, develop in Investigation 2 |
| FIG-014-002 | Primary Bonding and Noncovalent Interaction Map | Defined; Investigations 4–5 |
| FIG-014-003 | Carbon hybridization and geometry | Defined; Investigation 7 |
| FIG-014-004 | Sigma and pi bonding in ethylene | Defined; Investigations 7–8 |
| FIG-014-005 | Ethylene to polyethylene bridge | Defined; Investigation 8 |
| FIG-014-006 | Molecular feature to engineering evidence chain | Defined; introduced in Investigation 1, finalized in 9–10 |
| TAB-014-001 | Bonding types and engineering relevance | Defined; Investigations 4–5 |
| TAB-014-002 | Molecular feature / likely mechanism / invalid direct conclusion | Defined; Investigation 9 |
| TAB-014-003 | Controlled polymer-structure examples | Defined; Investigations 6–9 |
| TAB-014-004 | Downstream chapter ownership crosswalk | Defined; Investigation 10 |
| EX-014-001 | Reading ethylene and PE repeat unit | Defined; Investigation 8 |
| EX-014-002 | Comparing two simple polymer structures | Defined; Investigation 9 |
| WF-014-001 | Chemical structure → evidence → decision boundary | Defined; Investigation 10 |
| CL-014-001 | Before inferring engineering behaviour from chemical structure | Defined; Investigation 10 |

## 6. Review checkpoints

### Checkpoint A — Investigations 1–3

Confirm terminology depth, quantum-detail boundary and no duplicated Chapter 009 material.

### Checkpoint B — Investigations 4–5

Review bonding taxonomy and intermolecular-force terminology against current IUPAC sources.

### Checkpoint C — Investigations 6–8

Review carbon/hybridization/ethylene drawings for scientific correctness and verify clean handoff to Ch015.

### Checkpoint D — Investigation 9

Primary-evidence review for every material-specific structure–property bridge.

### Checkpoint E — Investigation 10 / chapter closure

Desk-test the evidence boundary: a reader must not be able to interpret the chapter as authorizing a material, pressure, temperature, chemical service or lifetime from chemistry alone.

## 7. Technical Outline disposition

**APPROVED CDB IMPLEMENTATION PATH — Engineering Development may proceed sequentially.**

Investigations 1–10 have now been authored through their required evidence checkpoints. Canonical integration has been completed; final full-chapter Technical Review and downstream validation gates remain required before Ready-for-Review.

## 8. Engineering Development completion checkpoint — 2026-08-15

- Investigations 1–8: authored controlled candidates.
- Investigation 9: primary-literature gate PASS; authoring review PASS; canonical integration complete.
- Investigation 10 / chapter closure: authoring review PASS; canonical integration complete.
- Pre-integration Technical Review: CONDITIONAL PASS; TR-014-01 through TR-014-04 applied during integration.
- Logical-manuscript Technical/Evidence Review: PASS FOR CANONICAL INTEGRATION.
- Logical-manuscript Editorial/Desk Review: CONDITIONAL PASS.
- Next gate: final full-file Technical Review of the integrated manuscript.

This checkpoint does not imply final Standards/Evidence publication validation, final Editorial/Style Review, Human Approval or publication readiness.
