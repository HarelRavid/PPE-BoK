---
chapter: "014"
title_en: "Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers"
part: "III - Polymer Science for Piping Engineers"
status: engineering-development
language: en
technical_level: foundational
primary_domains:
  - polymer science
  - materials science
  - chemical foundations
  - engineering evidence
review:
  physics: pending
  standards: pending
  academic: pending
  equations: n-a-current-scope
  units: n-a-current-scope
  examples: pending
  editorial: pending
last_updated: 2026-08-14
pds_baseline: "1.0"
cdb: "docs/PDS/Chapter-Design-Briefs/CDB-014-Atomic-Structure-Chemical-Bonding-Carbon-Chemistry.md"
---

# Chapter 014 — Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers

## Chapter purpose

This chapter builds the chemical foundation required to reason correctly about polymeric piping materials.

It does not attempt to turn a piping engineer into a chemist. Its purpose is narrower and more practical: to show how atomic structure, bonding, molecular geometry and intermolecular interactions create **mechanisms** that later appear as engineering behaviour — and to show exactly where that reasoning stops being sufficient.

A chemical structure can help an engineer ask better questions. It can suggest why two polymers may differ in molecular mobility, polarity, packing, thermal response, diffusion, chemical interaction or joining behaviour. It cannot, by itself, establish a pipe pressure rating, allowable temperature, chemical-compatibility limit, design life or qualified joint performance.

That distinction — **mechanism versus qualified engineering evidence** — is the central discipline of this chapter.

## Chapter engineering question

> Why can materials that are all described as “plastics” behave very differently in real piping systems, and what can an engineer legitimately infer from atomic and molecular structure before measured or qualified evidence is required?

## What the engineer should be able to do after this chapter

After completing the chapter, the reader should be able to:

1. connect atoms, electrons and bonding to molecular structure without unnecessary quantum-mechanics detail;
2. distinguish primary chemical bonding from intermolecular interactions;
3. understand why carbon can form the structural variety required for polymer backbones;
4. read simple monomer and repeat-unit structures and identify chemically meaningful features;
5. understand `sp`, `sp2`, `sp3`, sigma and pi bonding at a level useful for polymer engineering;
6. explain why the carbon–carbon double bond in ethene/ethylene differs from the carbon–carbon single bonds of a polyethylene backbone;
7. form bounded structure–property hypotheses from features such as polarity, side groups and intermolecular interactions;
8. identify what additional measured property, test, qualification or standard is required before that hypothesis becomes an engineering decision;
9. avoid common false shortcuts such as “strong chemical bond = strong pipe” or “polar polymer = chemically compatible/incompatible”;
10. route the next technical question to the correct downstream PPE-BoK chapter.

## Scope and exclusions

### In scope

- atoms, elements, molecules and compounds at the useful engineering scale;
- electron structure and valence concepts required for bonding;
- electronegativity and bond polarity;
- ionic, covalent and metallic bonding;
- hydrogen bonding, dipole interactions and London/dispersion interactions;
- carbon tetravalency and structural diversity;
- `sp`, `sp2`, `sp3`, sigma and pi concepts;
- ethene/ethylene as the bridge to polymerization;
- structure-to-mechanism reasoning;
- evidence boundaries between chemistry and design acceptance.

### Explicitly outside this chapter

- polymerization mechanisms and catalysts — Working Chapter 015;
- molecular weight, branching, crosslinking and chain architecture — Working Chapter 016;
- crystallinity, lamellae, spherulites and morphology — Working Chapter 017;
- thermal transitions and thermophysical engineering — Working Chapter 018;
- viscoelasticity, creep and time–temperature behaviour — Working Chapter 019;
- fracture, SCG, RCP, fatigue, ESC and ageing — Working Chapter 020;
- detailed material-family selection — Chapters 021 onward;
- pressure rating, MRS, SDR and product/system qualification — Chapters 012–013 and later design/application chapters;
- detailed joining physics/procedures — Part VII.

---

# Chapter standards / evidence map

| Engineering question | Standard / evidence family | Engineering use | Current authoring state |
|---|---|---|---|
| What polymer terminology should be controlled? | ISO 472:2013 + Amd 1:2018 | Plastics/polymer vocabulary; not a design standard | Working; lifecycle recheck required |
| Which polymer abbreviations are standardized? | ISO 1043-1:2011 + Amd 1:2016 | Abbreviation/symbol discipline | Working; confirmed current at research checkpoint |
| How should chemical terms be defined? | IUPAC Gold Book, 5th ed., online v5.0.0 (2025) | Chemical terminology | Working authoritative terminology source |
| What is a hydrogen bond? | IUPAC Recommendations 2011 + Technical Report | Controlled definition and evidence boundary | Working authoritative scientific source |
| How should ethene/polyethylene terminology and CRU language be controlled? | IUPAC organic/polymer nomenclature recommendations | Monomer/common-name/repeat-unit discipline | Working; controlled through Investigation 8 |
| Does a named polymer exhibit a specific property trend because of chemistry? | Directly reviewed primary literature | Material-specific mechanism evidence | Required before load-bearing use |
| Is a material acceptable for a real piping service? | Product/application standards + qualified property evidence | Engineering acceptance | Outside Ch014 chemistry alone |

The detailed source-control record is maintained in `references.md`.

**Authoring rule:** a vocabulary definition may control words, but it does not create an allowable stress, temperature, pressure, chemical-compatibility limit or qualification requirement.

---

# Required scientific / engineering inputs

For this chapter, the relevant inputs are molecular descriptors rather than a project Design Basis. Depending on the Investigation, the engineer may need to know:

- elemental identity;
- valence-electron context;
- electronegativity / polarity;
- bond type and bond order;
- molecular geometry;
- rotational constraints;
- molecular symmetry where useful;
- permanent dipoles;
- hydrogen-bond donor/acceptor capability where applicable;
- polarizability / dispersion interaction context;
- carbon hybridization state;
- monomer and repeat-unit structure.

These descriptors are not engineering acceptance values.

> **Engineering decision rule:** when a conclusion depends on an actual magnitude of stiffness, strength, permeability, chemical resistance, thermal capability, crack resistance, pressure rating or joining performance, the molecular descriptor is no longer enough. Move to measured and qualified evidence.

---

# Engineering Quick Navigation

- **Why chemistry belongs in a piping book:** Investigation 1.
- **Atoms, elements and molecules:** Investigation 2.
- **Valence electrons / orbitals / electronegativity:** Investigation 3.
- **Primary bonding:** Investigation 4.
- **Intermolecular interactions:** Investigation 5.
- **Carbon chemistry:** Investigation 6.
- **Hybridization / sigma / pi:** Investigation 7.
- **Ethene / ethylene and the PE bridge:** Investigation 8.
- **Structure → property hypotheses:** Investigation 9.
- **Where first-principles reasoning must stop:** Investigation 10.

---

# Investigation 1 — Why Should a Piping Engineer Care About Atoms and Bonds?

A pipe is a macroscopic engineering component. At first sight, atoms and chemical bonds can seem remote from decisions about pressure, supports, joining, chemical service or failure.

They are not remote — but they are also not the whole answer.

The useful engineering position lies between two bad extremes:

- **Extreme 1:** chemistry is irrelevant because the engineer works with datasheets and pressure classes;
- **Extreme 2:** chemistry is sufficient, so a material can be designed or accepted directly from its molecular structure.

Both positions fail.

Chemistry matters because every polymer begins with a particular set of atoms connected in a particular way. Those connections affect molecular geometry, polarity, rotational freedom and the kinds of interactions that can occur between neighbouring molecular segments. These molecular features help create the mechanisms that later appear in thermal, mechanical, transport, chemical and joining behaviour.

But the final piping material is much more than a structural formula.

Between a chemical bond and an operating pipe sit several additional engineering levels:

`atomic structure → bonding → molecule / repeat unit → polymer chain → chain architecture → morphology → compounded material → manufacturing history → finished pipe / fitting / joint → system loads and environment`

Each level can preserve, amplify, mask or change the engineering consequence of the level below it.

That hierarchy is the reason molecular science is valuable — and the reason it must be used with discipline.

## 1.1 The first distinction: material family is not material behaviour

The word **plastic** identifies an enormous category of materials. It does not define one stiffness, one fracture response, one temperature limit, one diffusion rate or one joining method.

Even the word **polymer** is not enough to predict those quantities.

A polymeric piping material may differ from another because of:

- the elements present in its molecular structure;
- the types and polarity of its bonds;
- the shape and flexibility of its molecular backbone;
- side groups or heteroatoms;
- intermolecular interactions;
- molecular weight and molecular-weight distribution;
- branching or crosslinking;
- crystalline/amorphous morphology;
- additives, fillers, stabilizers and pigments;
- processing and cooling history;
- ageing and service exposure.

Chapter 014 owns only the first part of this chain. Later chapters own the other levels.

This matters because an engineer who understands only the broad family name can easily make invalid analogies. Two materials can both be thermoplastics and still require very different temperature, joining, chemical-service and mechanical-design treatment. Chapter 009 already establishes that thermoplastic response is strongly affected by time, temperature, molecular structure, chemical environment and processing history; this chapter now moves backward in the chain to explain the underlying chemical vocabulary and mechanisms.

## 1.2 What is a chemical bond — and why does that definition matter here?

IUPAC treats a chemical bond as a stabilizing interaction between atoms or groups of atoms that creates a molecular entity or bonded structure. The formal definition is more nuanced than the common classroom image of a line drawn between two atoms. [S014-003]

For this chapter, the engineering value of the concept is simple:

> A bond describes how atoms are connected and how electron distribution contributes to that connection. It does **not** directly state how a bulk pipe will carry load.

That distinction prevents one of the most persistent shortcuts in polymer discussions:

> “The C–C bond is strong, therefore polyethylene is mechanically strong.”

The statement skips too many structural levels.

Bulk mechanical behaviour depends not only on the strength of individual covalent bonds but also on how enormous populations of chains are arranged, how they move relative to one another, how crystalline and amorphous regions interact, how defects concentrate stress, how load duration changes response, and how the finished material was manufactured and qualified.

Individual bond strength is therefore a **mechanism input**, not a pipe allowable.

## 1.3 A useful engineering hierarchy

**FIG-014-001 — Atom-to-material hierarchy — PLACEHOLDER**

The final figure shall show:

`atom → chemical bond → molecule / repeat unit → polymer chain → chain architecture → morphology → compounded material → product → piping system`

A second overlay shall distinguish two kinds of evidence:

- **explanatory evidence:** why behaviour may occur;
- **qualification evidence:** whether the actual material/product may be used for the defined service.

The figure must make one message visually unavoidable:

> moving from left to right adds engineering information; a conclusion at the left side cannot silently substitute for evidence required on the right side.

### Level A — Atomic / bonding level

Questions include:

- Which elements are present?
- How are electrons shared or redistributed?
- Which bonds are polar?
- Which geometries and rotational constraints result?

This level helps explain chemical and molecular possibilities.

### Level B — Molecular / chain level

Questions include:

- What is the repeat-unit structure?
- How flexible is the backbone?
- Which side groups or functional groups are present?
- Which intermolecular interactions are possible?

This level begins to explain polymer-specific mechanisms.

### Level C — Architecture / morphology level

Questions include:

- What molecular-weight distribution exists?
- How much branching or crosslinking exists?
- How are crystalline and amorphous regions organized?
- What tie-molecule / connectivity structure exists where applicable?

These questions belong mainly to Chapters 016–017.

### Level D — Compounded material / product level

Questions include:

- Which additives and stabilizers are present?
- What manufacturing history exists?
- What measured properties does the compound achieve?
- What product-standard requirements have been satisfied?

This is where chemistry begins to meet qualification evidence.

### Level E — System level

Questions include:

- What pressure, temperature, fluid, load history and environment apply?
- Which joining method is used?
- What installation damage is credible?
- Which product/application standard governs?
- Which system-level checks remain?

This is the level at which an engineering acceptance decision is finally made.

## 1.4 Why molecular reasoning is still worth learning

If chemistry cannot give the final design answer by itself, why spend engineering time on it?

Because engineering decisions rarely begin with perfect data.

A practicing engineer may face questions such as:

- Why does one polymer soften or lose stiffness differently from another?
- Why might a polar fluid interact differently with two candidate materials?
- Why does one polymer require a different fusion temperature window or joining process?
- Why might gas permeation differ between material families?
- Why can a small change in molecular structure lead to a large change in observed material behaviour?
- Which laboratory test or qualification evidence should be requested to confirm a suspected mechanism?

Molecular reasoning helps **form the hypothesis and select the evidence**.

It can narrow the search space. It can reveal when two apparently similar materials should not be assumed equivalent. It can identify which downstream property is likely to matter. It can also expose an implausible explanation during failure analysis.

Those are real engineering benefits even when the chemistry does not produce a design number.

## 1.5 The mechanism-to-evidence boundary

The reasoning discipline for this chapter is:

`chemical feature → plausible mechanism → measurable property → qualified evidence → engineering decision`

Not:

`chemical feature → engineering decision`

For example, bond polarity can help explain why electron density is distributed unevenly in a bond. IUPAC defines bond polarity in terms of unequal electron sharing between atoms of different electronegativity. [S014-003]

That is useful chemistry.

It does **not** mean an engineer may use electronegativity difference alone to declare that a polymer is chemically compatible with a process fluid. Actual compatibility can depend on polymer structure, formulation, morphology, fluid concentration, temperature, stress, exposure duration and the failure criterion being considered.

Similarly, the presence of stronger intermolecular attraction may suggest reduced molecular mobility under some circumstances. It does not create a universal equation for modulus, melting behaviour, creep or allowable temperature.

Each structure–property bridge must therefore ask two questions:

1. **What mechanism does the chemistry make plausible?**
2. **What evidence is required to establish the engineering magnitude and applicability?**

Investigation 9 will formalize this method. Investigation 1 establishes it as a chapter-wide rule.

## 1.6 A second distinction: terminology authority is not design authority

This chapter uses ISO 472 and ISO 1043-1 because consistent plastics terminology and abbreviations matter. It also uses the IUPAC Gold Book and IUPAC recommendations for chemical terminology.

Those sources perform a specific role.

They help answer questions such as:

- What does a term mean?
- Which abbreviation is controlled?
- How should a bonding concept be described?

They do not answer:

- Is this pipe acceptable at 10 bar?
- Is this material compatible with 5 M KOH at 40 °C?
- What is the allowable temperature for 25 years?
- Is this fusion joint qualified?
- What is the required design coefficient?

Those questions belong to other evidence layers and other chapters.

The current public ISO record lists ISO 472:2013 as published but scheduled for revision, with Amendment 1:2018, while ISO 1043-1:2011 remains published/confirmed with Amendment 1:2016. Their lifecycle state is therefore recorded as an authoring input, not frozen publication metadata. Final Standards/Evidence Validation must recheck both.

## 1.7 Common mistakes / Failure Lens

### Mistake 1 — “Strong bonds mean a strong pipe”

Why it fails: bulk strength and long-term integrity emerge from multiple structural levels and loading mechanisms, not one bond-energy value.

### Mistake 2 — “A structural formula tells me chemical compatibility”

Why it fails: structure can generate a hypothesis, but service compatibility is a property of the real material/compound under defined exposure conditions.

### Mistake 3 — “All nonpolar polymers behave alike”

Why it fails: polarity is only one molecular descriptor. Chain architecture, morphology, additives, temperature and other factors may dominate the property of interest.

### Mistake 4 — “The standard defines the term, so it defines the design”

Why it fails: vocabulary and abbreviation standards control language, not pressure-system acceptance.

### Mistake 5 — “Chemistry is too theoretical to matter in failure analysis”

Why it fails: a chemically plausible mechanism can help identify what evidence to seek, what analyses to run and which hypotheses are inconsistent with the material structure.

## 1.8 Verification method for molecular inferences

Whenever Chapter 014 forms a molecular inference, verify it using this sequence:

1. **Identify the descriptor precisely.** Is the claim about bond type, polarity, side group, geometry, intermolecular interaction or another feature?
2. **State the proposed mechanism.** What physical or chemical process is expected to change?
3. **Identify the measurable engineering property.** Modulus? diffusion coefficient? uptake? transition temperature? fracture metric? fusion behaviour?
4. **Find evidence at the correct level.** Prefer direct measured evidence for the real material or an appropriately transferable system.
5. **Check transferability.** Grade, morphology, formulation, temperature, exposure and test mode may matter.
6. **Locate the governing engineering framework.** If the decision is design acceptance, identify the product/application standard or qualification route.
7. **Record what remains unknown.** Do not hide missing evidence behind mechanistic confidence.

This sequence becomes the formal `WF-014-001` later in the chapter.

## 1.9 Engineering decision from Investigation 1

> Atomic and molecular structure are engineering-relevant because they explain possible mechanisms and help select the right evidence. They are not substitutes for measured material properties, qualification data, product standards or system-level design checks.

After Investigation 1, the engineer should be able to classify a statement into one of three claim classes:

### Claim Class A — Chemistry fact

Example: a bond is polar; a molecular interaction is possible; a carbon atom is in a particular bonding geometry.

### Claim Class B — Mechanism hypothesis

Example: that structural feature may alter molecular interaction, mobility, packing or diffusion behaviour.

### Claim Class C — Engineering conclusion

Example: a particular material is acceptable for a defined pressure/temperature/fluid/lifetime service.

The rule for the rest of Chapter 014 is simple:

> **Never jump directly from Claim Class A to Claim Class C.**

The investigations that follow build the chemistry needed to make Claim Class A accurate and Claim Class B useful. The rest of PPE-BoK provides the evidence systems needed to reach Claim Class C.

---

# Investigation 2 — What Is Matter Made of at the Useful Engineering Scale?

A piping engineer does not need a complete model of subatomic physics to understand polymer chemistry. The useful starting point is simpler: identify the **chemical entities** that make up a material, distinguish the names used for different levels of description, and know which level is relevant to the engineering question.

The vocabulary matters because careless language produces careless reasoning. An atom is not an element. An element is not a molecule. A molecule is not the same thing as a bulk chemical substance. And not every chemical substance is best imagined as a collection of discrete molecules.

For Chapter 014, the working hierarchy is:

`atom → elemental identity → molecular entity / molecule → chemical substance → polymeric material → piping product`

This hierarchy is deliberately incomplete. Investigation 3 will add the electron structure required for bonding; later Investigations will add bond type, intermolecular interactions, carbon geometry and polymer-specific structure.

## 2.1 Atom: the smallest level that still carries elemental identity

IUPAC defines an **atom** as the smallest particle that still characterizes a chemical element. Its nucleus carries positive charge and almost all of the atom's mass, while the electrons determine the atom's spatial extent. [S014-003]

At the level needed here, the engineer should retain three ideas:

1. an atom has a positively charged nucleus and electrons;
2. the number of protons in the nucleus identifies the element;
3. the arrangement and availability of electrons are what will matter when we discuss bonding.

The third point is the bridge to Investigation 3.

The chapter intentionally stops here. Detailed nuclear structure, quantum numbers, wave functions and atomic spectroscopy are not required to answer the polymer-engineering questions defined by CDB-014.

### Engineering use

When reading a repeat-unit or molecular formula, the first useful question is simply:

> **Which elements are present?**

Carbon and hydrogen dominate many polymer backbones, but other piping polymers introduce atoms such as chlorine, fluorine or oxygen into the molecular structure. The presence of a different element changes the available bonding and electron-distribution possibilities. It does not, by itself, determine the finished material's engineering performance.

## 2.2 Atomic number: what makes carbon carbon?

IUPAC uses the symbol `Z` for **atomic number**, also called proton number, and defines it as the number of protons in the atomic nucleus. [S014-003]

That is the identity rule for an element.

If the proton number changes, the element changes. Carbon is carbon because its atoms have the proton number associated with carbon; fluorine and chlorine have different proton numbers and therefore different elemental identities.

For Chapter 014, atomic number is not introduced as a quantity to calculate with. Its value is conceptual: it explains why the periodic table represents different elemental identities rather than different grades of the same material.

### What atomic number does not tell the engineer

Atomic number alone does not establish:

- how atoms are bonded in a molecule;
- whether a bond is polar;
- molecular geometry;
- chain architecture;
- crystallinity;
- modulus or tensile strength;
- chemical resistance;
- pressure capability.

Those require additional structural and engineering information.

## 2.3 Chemical element: a category of atoms, not a piece of bulk material

IUPAC gives **chemical element** two closely related usages: a species of atoms having the same number of protons, and a pure chemical substance composed of such atoms. [S014-003]

The dual usage is worth knowing because engineering language often shifts between them without warning.

For example, the statement “the polymer contains fluorine” usually refers to elemental identity within the molecular structure. It does **not** mean the pipe contains bulk elemental fluorine as a separate phase.

Similarly, saying that polyethylene contains carbon and hydrogen identifies the elements from which its molecular structure is built. It does not describe the macroscopic material formulation, morphology or properties.

### Engineering decision rule

When an elemental name appears in a material discussion, ask:

> Is the speaker describing **elemental identity inside a chemical structure**, or a **separate chemical substance / phase** actually present in the material or process?

Those are different engineering statements.

## 2.4 Molecule versus molecular entity

The word **molecule** is useful but narrower than many engineers assume.

IUPAC defines a molecule as an electrically neutral entity consisting of more than one atom. [S014-003]

IUPAC uses **molecular entity** as the broader singular term. A molecular entity can be an atom, molecule, ion, ion pair, radical, complex or another constitutionally distinguishable entity. [S014-003]

This distinction becomes useful whenever charge or non-molecular structures matter.

### Why Chapter 014 prefers “molecular entity” when precision matters

If the chapter is discussing a neutral organic molecule such as ethene, **molecule** is appropriate.

If the discussion needs to include ions or other individually distinguishable chemical entities, **molecular entity** is safer and more general.

This prevents a common simplification in engineering explanations:

> “Everything in chemistry is a molecule.”

That statement is not precise enough for later discussions of ionic bonding, salts, charged species or chemical interactions.

## 2.5 Chemical substance: the macroscopic bridge

The phrase **chemical substance** moves the discussion from one entity to matter in bulk.

IUPAC describes a chemical substance as matter of constant composition best characterized by the entities from which it is made; those entities may be molecules, formula units or atoms. [S014-003]

This is an important boundary for engineers because it prevents another classroom shortcut:

> A bulk substance is not always best represented as a pile of identical discrete molecules.

Depending on the material, the useful entity may instead be an atom, a formula unit or another structural description.

For the polymer engineer, this distinction prepares the way for a later step: even a chemically identified polymer substance is still not the same thing as a **commercial piping compound**. A finished compound may contain stabilizers, pigments, fillers or other constituents and will also have a specific molecular-weight distribution, morphology and processing history.

Those additional levels are intentionally deferred to later chapters.

## 2.6 What should we do with the word “compound”?

In normal engineering language, **compound** is often used as a broad chemical word for matter formed from more than one element, and in plastics engineering the word **compound** is also commonly used for the formulated polymer material supplied for processing.

Those two usages can collide.

Chapter 014 therefore applies a terminology rule:

- use **chemical substance**, **molecule** or **molecular entity** when discussing chemistry at the atomic/molecular level;
- use **polymer compound** or **piping compound** when referring to the formulated engineering material;
- do not assume that the word “compound” by itself tells the reader which meaning is intended.

This terminology discipline is especially important in later material-selection and qualification chapters, where “compound” may refer to a qualified formulation rather than merely a chemical composition.

## 2.7 The engineering abstraction: stop at the scale that answers the question

A good engineering model contains enough detail to answer the question and no more detail than necessary.

For the current chapter:

- **Atomic identity** is needed to know which elements are present.
- **Electron structure** is needed to explain bonding — Investigation 3.
- **Bonding and molecular geometry** are needed to explain structural possibilities — Investigations 4–8.
- **Measured material properties** are needed to quantify engineering behaviour.
- **Product/application qualification** is needed to support real piping acceptance.

Going deeper into nuclear physics does not improve those decisions. Stopping before electron structure, however, would leave the bonding discussion unsupported.

That establishes the lower and upper boundaries of the atomic model used in PPE-BoK.

## 2.8 A practical reading method for chemical formulas

When a piping engineer encounters a chemical or repeat-unit formula, use the following first pass:

1. **Identify the elements.** Which elemental symbols are present?
2. **Identify the entity being represented.** Is this a molecule, repeat unit, ion or another representation?
3. **Do not infer bonding from composition alone.** The same elements can be connected in different structures.
4. **Do not infer bulk properties from the formula alone.** Molecular architecture, morphology, formulation and processing are still missing.
5. **Route the next question.** If the issue is how electrons produce bonds, move to Investigation 3; if it is how carbon geometry affects structure, move later in the chapter.

This five-step reading method is intentionally modest. Its purpose is to prevent category errors before more advanced structure–property reasoning begins.

## 2.9 Common mistakes / Failure Lens

### Mistake 1 — “Atom” and “element” mean the same thing

Why it fails: an atom is an individual chemical entity; an element identifies the species/category defined by proton number and may also refer to the corresponding pure substance depending on context.

### Mistake 2 — “Every chemical substance is made of molecules”

Why it fails: IUPAC's chemical-substance definition explicitly allows characterization by molecules, formula units or atoms.

### Mistake 3 — “If I know which elements are present, I know the material properties”

Why it fails: elemental composition does not specify connectivity, geometry, electron distribution, chain architecture, morphology, formulation or manufacturing history.

### Mistake 4 — “Compound” has one unambiguous meaning

Why it fails: chemical usage and plastics-compounding usage are different enough to create engineering ambiguity unless the intended meaning is stated.

### Mistake 5 — teaching atomic detail that has no engineering consequence

Why it fails: unnecessary quantum or nuclear detail obscures the chapter's actual purpose — explaining the chain from chemistry to bounded engineering reasoning.

## 2.10 Verification

Before accepting an atomic/molecular statement in Chapter 014, check:

1. Is the term being used consistently with the current IUPAC terminology source?
2. Is the statement about an individual entity, a species/category, or a bulk substance?
3. Does the wording accidentally imply that all substances are molecular?
4. Does the explanation include only the subatomic detail needed for the next engineering mechanism?
5. Has any bulk-property conclusion been introduced without the missing structural/material evidence?

If the answer to item 5 is yes, the statement has crossed the Chapter 014 evidence boundary and must be revised or supported at the correct evidence level.

## 2.11 Engineering decision from Investigation 2

> Use atomic and chemical terminology to identify **what the material is made from and what level of chemical entity is being described**. Do not treat elemental identity or a simple formula as a proxy for molecular structure or bulk engineering performance.

After Investigation 2, the engineer should be able to distinguish:

- **atom** — an individual entity carrying elemental identity;
- **atomic number `Z`** — the proton count defining that elemental identity;
- **chemical element** — the category/species of atoms sharing that proton number, with a context-dependent pure-substance usage;
- **molecule** — a neutral multi-atom entity;
- **molecular entity** — the broader singular chemical-entity concept;
- **chemical substance** — matter of defined composition characterized by its constituent entities.

The next question is now unavoidable:

> If elemental identity is fixed by the nucleus, **which electrons determine how those atoms can bond?**

That is the subject of Investigation 3.

---

# Investigation 3 — Which Electrons Actually Control Chemical Bonding?

Knowing which elements are present is not enough to explain a polymer's chemistry. The next useful question is how the electrons associated with those atoms can participate in bonding.

This is where introductory chemistry is often taught with pictures that are memorable but dangerous if taken literally. Electrons are sometimes drawn as small particles orbiting a nucleus on fixed circular paths. That picture may be useful as a historical teaching analogy, but it is not the model Chapter 014 will use for engineering reasoning.

For this chapter, the minimum useful framework is:

`electron → atomic orbital / electron distribution → valence context → electronegativity / electron attraction → bonding possibility`

The purpose is not to solve the Schrödinger equation. The purpose is to understand why atoms of different elements form different bonding patterns and why electron distribution later matters to bond polarity, molecular geometry and intermolecular interaction.

## 3.1 Electron: the negatively charged particle that enters the bonding problem

IUPAC defines the **electron** as an elementary particle carrying negative elementary charge. [S014-003]

Its spin and rest mass are part of the formal definition, but Chapter 014 does not need those quantities for the present engineering objective.

The point to retain is narrower:

> Chemical bonding depends on how electrons are distributed and shared, transferred or delocalized between atoms and molecular entities.

That is why two elements with different atomic identities can exhibit different bonding behaviour even before we discuss a specific polymer.

## 3.2 Orbitals are not planetary paths

IUPAC defines an **atomic orbital** as a one-electron wavefunction obtained from the Schrödinger equation for an atom. [S014-003]

That formal definition immediately establishes an important teaching boundary:

> An orbital is not a little circular track on which an electron travels around the nucleus.

For a piping engineer, the full mathematics behind the wavefunction is not needed. What matters is that orbitals provide a structured way to describe the spatial and energetic possibilities associated with electrons in an atom.

This lets us reason about bonding without pretending that electrons have fixed classical trajectories.

### Engineering-use simplification

When Chapter 014 later draws `s` or `p` orbitals, hybrid orbitals, sigma bonds or pi bonds, treat those drawings as **models of electron distribution and bonding geometry**, not photographs of physical objects.

That distinction becomes critical in Investigation 7.

## 3.3 Which electrons matter most? The valence context

The word **valence** has a long history in chemistry. IUPAC defines valence in terms of an atom's combining capacity with univalent atoms or fragments. [S014-003]

For introductory bonding work, engineers often use the phrase **valence electrons** for the electrons associated with the outer chemically active part of the atom — the electrons most directly involved in ordinary bond formation and electron-counting models.

That is a useful engineering abstraction, but it should not be treated as a universal statement that every bonding problem can be solved by drawing a simple outer shell.

IUPAC's electron-counting terminology itself points to the importance of the **valence electron shell** when relating molecular topology to bonding-electron counts. [S014-003]

For Chapter 014, the practical rule is:

> Focus on the electrons that participate in the atom's chemically accessible bonding states; do not carry every inner electron into the polymer-bonding discussion.

## 3.4 Why the periodic table becomes useful now

Investigation 2 used the periodic table only as a map of elemental identity. Investigation 3 adds a second use: elements in different positions exhibit different recurring patterns in their chemically active electron structure.

The engineer does not need to memorize the entire table.

Instead, use it as a navigation tool to ask:

- How many chemically active electrons are available in the simple bonding model?
- Is the atom likely to form, share or attract electron density in a particular way?
- Is the atom part of the carbon/hydrogen backbone or a more electronegative substituent or heteroatom?

The exact answer may require a deeper chemical model, but the periodic pattern helps organize the first hypothesis.

## 3.5 Electronegativity: useful, relative and easy to misuse

IUPAC describes **electronegativity** as the power of an atom to attract electrons to itself and notes that several definitions/scales exist. [S014-003]

That last point matters.

Electronegativity is not one universal directly measured material property. Different scales formalize the concept in different ways. In Chapter 014 it is therefore used as a **relative chemical descriptor** that helps reason about how electron density may be distributed in a bond.

### What electronegativity can help explain

It can support questions such as:

- Is a bond between unlike atoms likely to have uneven electron distribution?
- Which atom is the more electron-attracting partner in a simple bond model?
- Why might a bond acquire polarity?

### What electronegativity cannot establish by itself

It does not directly give:

- the dipole moment of a complete polymer chain;
- chemical compatibility with a process fluid;
- dielectric performance;
- permeability;
- melting temperature;
- modulus;
- allowable service temperature;
- pressure rating.

Those conclusions require additional molecular and material evidence.

## 3.6 From electron distribution to bond polarity — but no further yet

The next connection is conceptually simple:

`different electron-attracting tendencies → unequal electron distribution in a bond → possible bond polarity`

Investigation 1 already introduced the warning that bond polarity must not be turned directly into a compatibility rule. Investigation 3 now provides the electron-level reason that polarity can arise.

The full treatment of ionic and covalent bonding belongs to Investigation 4. Intermolecular consequences of permanent dipoles belong to Investigation 5.

This separation is intentional. It prevents the chapter from collapsing several different physical levels into one word such as “polar.”

## 3.7 Lewis structures: a controlled bookkeeping model

Lewis formulas are useful because they make valence-electron bookkeeping visible. They can show:

- which atoms are connected;
- bonding electron pairs in a simplified representation;
- nonbonding electron pairs where relevant;
- formal structural possibilities.

But a Lewis formula is still a model.

It does not show the full electron density, three-dimensional molecular geometry, orbital shape, molecular motion or bulk-material morphology. Later Investigations add those missing layers only where they affect the engineering question.

The engineer should therefore use Lewis structures as a **connectivity and electron-bookkeeping tool**, not as a literal map of electron positions.

## 3.8 Why this matters to polymer structures

The electron-level model becomes useful when comparing repeat-unit structures.

Consider the kinds of questions a piping engineer may eventually ask:

- Why does replacing hydrogen with another element change bond polarity?
- Why does a carbon–carbon double bond behave differently from a single bond?
- Why can some atoms support lone-pair interactions or hydrogen bonding while others do not?
- Why do different substituents change molecular geometry or intermolecular interactions?

All of those questions begin with electron distribution and valence possibilities.

But the chapter-wide evidence rule remains unchanged:

> Electron structure explains **why a mechanism is chemically possible**. It does not quantify the finished piping material's engineering performance.

## 3.9 Common mistakes / Failure Lens

### Mistake 1 — drawing electrons as fixed planets and treating the drawing as physical reality

Why it fails: atomic orbitals are quantum-mechanical wavefunctions, not classical circular trajectories.

### Mistake 2 — assuming “valence electrons” means every atom follows one simple outer-shell cartoon

Why it fails: the phrase is a useful introductory abstraction, but real electronic structure and bonding can require more detailed treatment.

### Mistake 3 — treating electronegativity as a universal material-property scale

Why it fails: IUPAC notes multiple definitions/scales, and electronegativity describes an atomic electron-attraction concept rather than a finished polymer property.

### Mistake 4 — using electronegativity difference alone to declare a bond or material fully ionic/covalent or chemically compatible

Why it fails: bonding character and bulk behaviour require a more complete model; compatibility requires measured service-relevant evidence.

### Mistake 5 — treating a Lewis drawing as complete molecular geometry

Why it fails: Lewis structures are useful bookkeeping/connectivity models, not full descriptions of electron density or three-dimensional molecular structure.

## 3.10 Verification

Before accepting an electron-level explanation in Chapter 014, check:

1. Does the wording avoid fixed-orbit planetary imagery except as an explicitly rejected historical analogy?
2. Is an orbital described as a model/wavefunction rather than a physical path?
3. Is valence language being used only to the depth required for bonding?
4. Is electronegativity presented as a relative concept with multiple formal definitions/scales?
5. Has any bond-polarity inference been kept separate from bulk-material qualification?
6. Does the explanation stop before quantum mathematics that adds no engineering capability?

## 3.11 Engineering decision from Investigation 3

> The chemically relevant difference between elements is not only the number of protons that identifies them, but also the accessible electron structure that governs how they can participate in bonding. For engineering use, orbitals and valence concepts are models for electron distribution and bonding possibilities — not direct predictors of bulk pipe performance.

After Investigation 3, the engineer should be able to use three disciplined ideas:

- **orbitals** describe electron-state/distribution possibilities, not classical paths;
- **valence context** identifies the electrons and combining capacity relevant to ordinary bonding models;
- **electronegativity** helps form a relative hypothesis about electron distribution and bond polarity, but does not by itself establish a material property.

The next engineering question is therefore:

> **What kinds of primary bonds result when atoms interact, and why do those bonds create different classes of material behaviour?**

That is the subject of Investigation 4.

---

# Investigation 4 — What Are Primary Bonds and Why Do Material Classes Differ?

Engineers often classify bonding into simple categories — covalent, ionic and metallic — and then attach a list of bulk properties to each category. That can be useful as a first orientation, but it becomes misleading if the categories are treated as perfectly pure or if a bulk material property is claimed to follow directly from one bond label.

Chapter 014 therefore uses **primary bonding** as an engineering teaching category, not as a claim that every real material belongs to one chemically pure box.

The working rule is:

> A bonding model describes how electron density and electrostatic interactions stabilize a structure. Bulk material behaviour emerges only after structure, scale, defects, morphology, processing and loading are added.

Investigation 4 establishes the primary-bonding models. Investigation 5 deals with interactions between molecular entities and polymer chains that are not the covalent backbone bonds themselves.

## 4.1 Covalent bonding: shared electron density between nuclei

IUPAC defines a **covalent bond** in terms of a region of relatively high electron density between nuclei that arises at least partly from electron sharing and produces an attractive force and characteristic internuclear distance. [S014-003]

For polymer engineering, this is the key model behind the bonds that build many organic polymer backbones and side groups.

The useful engineering statement is not “covalent bonds make polymers strong.” It is more precise:

> Covalent bonding establishes the chemical connectivity of the polymer molecule or network.

That connectivity determines which atoms belong to the same molecular structure and which bond rotations, geometries and reaction pathways are possible. Later chapters then add molecular weight, branching, crosslinking, morphology and other factors that govern how a population of those molecules behaves as a material.

### What covalent bonding does not establish by itself

Knowing that a backbone is covalently bonded does not directly establish tensile strength, elastic modulus, creep resistance, fracture toughness, melting/softening temperature, permeability, chemical compatibility or pressure rating.

Those are higher-level material and product questions.

## 4.2 Ionic bonding: electrostatic attraction, but not a perfectly separate universe

IUPAC describes an **ionic bond** in strict terms as electrostatic attraction between the charges of a cation and an anion. It also makes a particularly important qualification: in practice it is preferable to consider the **amount of ionic character** rather than forcing bonds into purely ionic or purely covalent categories. [S014-003]

This matters because introductory diagrams often imply a sharp boundary:

`electron shared → covalent`

`electron transferred → ionic`

Real bonding can contain mixed character. The binary picture is a useful teaching limit, not a complete description of every solid or chemical bond.

### Engineering consequence of the continuum

When a material or chemical species is described as “ionic,” the engineer should ask what is actually meant: discrete ions in a fluid, ionic crystal/salt, significant ionic character, or a chemical interaction with a polymer. Those are different contexts.

## 4.3 Metallic bonding: use verified electron delocalization rather than a cartoon

For the current authoring pass, Chapter 014 does not rely on an invented stand-alone IUPAC definition of “metallic bond.” Instead, it uses IUPAC's definition of **delocalization of electrons**.

IUPAC notes that a delocalized electron is not associated with one particular atom or one particular covalent bond, but occupies an extended orbital over several atoms or an entire lattice; extensive electron delocalization is typical of metals. [S014-003]

That gives the engineering model we need:

> In a metallic solid, bonding cannot be represented adequately as a collection of isolated two-atom covalent bonds. Electron density is extended through the structure.

The familiar phrase “sea of electrons” can be a teaching analogy, but it should not be mistaken for a complete electronic-structure model.

It does not, by itself, prove that a particular metal is ductile, strong, corrosion resistant or suitable for a piping interface.

## 4.4 Material classes are not bond labels

Many polymer molecules are built from covalent bonds along the backbone and side groups, but intermolecular interactions, chain entanglement, molecular architecture and morphology become essential to macroscopic behaviour.

Metals are usefully distinguished by extended electron delocalization through the lattice, but that is not a complete mechanical model.

Many ceramic and inorganic solids contain substantial ionic and/or covalent bonding character; `ceramic = purely ionic` is unsafe.

> Bonding helps explain why material classes require different physical models, but material class and bond type are not interchangeable labels.

## 4.5 Bond polarity is not the same question as bond category

- **bond category/model** asks how the stabilizing interaction is represented;
- **bond polarity / ionic character** asks how unevenly electron density or charge character is distributed.

A covalent bond can be polar. A bond can have partial ionic character. Therefore, “polar covalent” is not a contradiction.

## 4.6 TAB-014-001 — Primary bonding models and engineering relevance

| Bonding model / descriptor | Electron / charge picture | Useful engineering interpretation | What must **not** be concluded directly |
|---|---|---|---|
| Covalent bonding | Relatively high electron density between nuclei arising at least partly from sharing | Establishes chemical connectivity and local molecular structure | Bulk strength, creep, fracture, pressure rating or service temperature |
| Ionic character / ionic bonding | Electrostatic attraction between charged species; real bonds may contain varying ionic character | Helps interpret ions, salts and mixed bond character | A fixed mechanical-property set or universal chemical-compatibility rule |
| Extended electron delocalization typical of metals | Electrons occupy states/orbitals extended over many atoms or the lattice | Distinguishes metallic electronic/bonding structure from localized molecular bonding | Ductility, strength, corrosion resistance or interface suitability without material evidence |

## 4.7 FIG-014-002 — Primary Bonding and Noncovalent Interaction Map — partial placeholder

The final figure separates:

**Level A — chemical connectivity / extended solid bonding:** covalent, ionic character/ionic, extended electron delocalization.

**Level B — noncovalent interactions:** hydrogen bonding, permanent-dipole, dipole-induced-dipole, London/dispersion.

The figure must not rank these as though one universal energy scale determines bulk polymer properties.

## 4.8 Why this distinction matters in plastic piping

Statements such as “PE has strong C–C bonds,” “PVDF is polar because of C–F bonding,” “a salt is ionic,” or “metals have metallic bonding” may contain useful clues, but none is a design conclusion.

`bonding description → structural/mechanistic implication → measured material response → qualification / application evidence → engineering decision`

## 4.9 Common mistakes / Failure Lens

- forcing every bond into 100% ionic or 100% covalent;
- equating covalent backbone bonds with bulk polymer strength;
- equating ceramic with ionic;
- equating metallic bonding with guaranteed ductility;
- treating bond polarity and bond type as the same classification;
- ranking piping service temperature from primary-bond labels.

## 4.10 Verification

Before accepting a primary-bonding explanation, check terminology, degree of ionic character, use of verified electron-delocalization language, avoidance of direct bulk-property claims, and separation of intrachain covalent bonding from interchain interactions.

## 4.11 Engineering decision from Investigation 4

> Use covalent, ionic-character and extended-electron-delocalization models to describe **how a structure is chemically/electronically stabilized**. Do not use a bond label as a substitute for a bulk-material model or a piping qualification decision.

---

# Investigation 5 — What Holds Polymer Molecules Together When They Are Not Covalently Bonded to Each Other?

Polymer chains and chain segments interact continuously through electrostatic and quantum-mechanical interactions that do not require new covalent bonds between every pair of segments.

The misleading classroom ladder

`London < dipole–dipole < hydrogen bond < covalent bond`

is not a safe polymer-engineering model. Real behaviour depends on distance, orientation, number/distribution of sites, polarizability, geometry, architecture, morphology, temperature and the measured property.

> Identify the **interaction mechanism** first. Do not turn the interaction label into a universal ranking of bulk polymer properties.

## 5.1 Intramolecular versus intermolecular

- **Intramolecular** interactions occur within one molecular entity.
- **Intermolecular** interactions occur between different molecular entities.

For polymers, the same physical noncovalent interaction may act between segments of different chains or separated segments of the same chain. IUPAC's van der Waals definition explicitly allows interactions between entities or between groups within the same entity. [S014-003]

## 5.2 van der Waals forces: an umbrella, not one additional force

IUPAC uses **van der Waals forces** as an umbrella including dipole–dipole, dipole-induced dipole and London/dispersion interactions. [S014-003]

Thus `dipole–dipole + London + van der Waals` is a category error when `van der Waals` is being used in the IUPAC sense.

## 5.3 Dipole–dipole interaction

Permanent-dipole interactions depend on separation and orientation. A polar bond can contribute to a molecular dipole, but bond dipole and whole-molecule dipole are not identical concepts.

The presence of a permanent dipole does not by itself establish modulus, transition temperature, creep, compatibility, uptake, permeability, fusion temperature or pressure capability.

## 5.4 Dipole-induced dipole interaction

A permanent dipole can distort a neighbouring electron distribution and induce a dipole. The mechanism highlights **polarizability**, used qualitatively here and not converted into a material property without evidence.

## 5.5 London / dispersion forces

IUPAC identifies London/dispersion forces with mutual polarizability and states that they contribute in both apolar and polar systems. [S014-003]

> London forces are not switched off when a molecule is polar.

A polymer without a strong permanent dipole is therefore not interaction-free.

## 5.6 Hydrogen bonding

The 2011 IUPAC Recommendation gives hydrogen bonding a dedicated evidence-based definition and criteria; it should not be reduced to “strong dipole–dipole.” [S014-004][S014-005]

Safe sequence:

`possible donor/acceptor chemistry → geometrically possible interaction → evidence of H-bond relevance → measured material consequence`

Hydrogen bonding is also not the same as covalent crosslinking.

## 5.7 Multiple mechanisms can coexist

A molecular system may simultaneously contain covalent bonds, polar covalent bonds, permanent-dipole interactions, dipole-induced dipole interactions, London/dispersion forces and hydrogen bonding.

A better question than “which force holds this polymer together?” is:

> **Which interaction mechanisms are present, how are they distributed through the actual chain/morphology, and which measured property are we trying to explain?**

## 5.8 TAB-014-001 — Bonding and interaction map, continuation

| Interaction model / descriptor | Physical picture | Useful engineering interpretation | What must **not** be concluded directly |
|---|---|---|---|
| van der Waals forces | Umbrella including dipole–dipole, dipole-induced dipole and London/dispersion | Nonspecific family of non-bond-forming interactions | Treating it as a separate extra force |
| Dipole–dipole | Permanent dipoles; orientation/separation matter | Polarity can contribute to segment interaction | Bulk property from dipole presence alone |
| Dipole-induced dipole | Permanent dipole induces neighbour dipole | Connects polarity to polarizability | Quantitative property without evidence |
| London / dispersion | Mutual polarizability/fluctuating electron distributions | Attraction in apolar and polar systems | Assuming dispersion only in nonpolar systems |
| Hydrogen bonding | Specific H-centered attractive interaction with evidence criteria | Potentially important directional noncovalent interaction | Automatic H-bond assignment or design value |

## 5.9 FIG-014-002 — Primary Bonding and Noncovalent Interaction Map — conceptual specification complete

Level A shows primary/extended bonding; Level B shows van der Waals family with its dipolar/dispersion children and hydrogen bonding separately. Warnings: mechanisms coexist; dispersion occurs in polar systems; the map is not a bulk-property ranking.

## 5.10 Why labels do not directly predict polymer properties

Property response also depends on interaction-site distribution, geometry, distance/orientation, polarizability, chain architecture, molecular weight, morphology, temperature/time, additives and processing history.

## 5.11 Common mistakes / Failure Lens

- treating van der Waals as an extra force;
- limiting London forces to nonpolar molecules;
- defining H-bond as only a strong dipole interaction;
- deriving stiffness/Tm from polarity alone;
- saying a nonpolar polymer has no attraction;
- using one interaction type as a compatibility rule;
- confusing hydrogen bonding with covalent crosslinking.

## 5.12 Verification

Check umbrella terminology, coexistence of dispersion/dipolar mechanisms, H-bond evidence discipline, rejection of a one-axis force-strength ladder, and routing of bulk-property claims to material evidence.

## 5.13 Engineering decision from Investigation 5

> Polymer chains and chain segments can interact through several overlapping noncovalent mechanisms. Use the interaction map to identify **what physical mechanism is plausible**, then move to the measured property and material-specific evidence before making an engineering conclusion.

---

# Investigation 6 — Why Is Carbon Uniquely Useful for Polymer Backbones?

Carbon is the structural center of most organic polymers used in engineering, but “carbon has four bonds” is only part of the explanation.

IUPAC assigns carbon a **standard bonding number of four**; the same table assigns four to other relevant Group 14 elements, so tetravalency alone cannot explain carbon's structural diversity. [S014-006]

Useful engineering explanation combines four-bond connectivity, C–C connectivity, linear/branched/cyclic skeletons, multiple bond orders and substitution by other atoms/groups.

## 6.1 Tetravalency

The four-bond rule is a structural/electron-counting description, not anthropomorphic intent. Carbon can distribute bonding equivalents among four singles, double+singles, triple+single, or appropriate double-bond patterns.

It does not directly establish flexibility, packing, crystallinity, transition temperature, resistance or pressure rating.

## 6.2 Carbon–carbon connectivity

Repeating C–C connectivity allows extended molecular skeletons. A skeleton is a framework, not a material property; chain length, molecular-weight distribution, branching distribution, morphology and formulation remain separate questions.

## 6.3 Chains, branches and rings

IUPAC polymer terminology allows linear/branched chains and cyclic macromolecular contexts; carbocyclic structures contain carbon ring members. [S014-003]

Investigation 6 introduces structural possibility only. Real short/long-chain branching, crosslinking and architecture belong to Chapter 016.

## 6.4 Saturated and unsaturated frameworks

Single and multiple C–C bond orders are constitutionally different. Hybridization and σ/π explanation belongs to Investigation 7; ethene polymerization belongs to Investigation 8/Chapter 015.

## 6.5 Carbon skeleton does not mean hydrocarbon-only

Heteroatoms/substituents such as F, Cl, O or N can change local bonding, electron distribution, mass, steric environment and interaction possibilities. They do not directly establish compatibility, permeability or allowable temperature.

## 6.6 How to read a skeletal / bond-line formula

IUPAC skeletal formulas use lines for bonds, unlabeled vertices/ends for ordinary carbon, implicit attached H on those carbons, and explicit symbols for other atoms. [S014-003]

Use them to identify connectivity, branches, rings, multiple bonds, heteroatoms and candidate interaction sites — not 3D geometry.

## 6.7 Skeletal formula versus polymer skeletal structure

- **skeletal formula** — drawing convention;
- **skeletal structure** — essential atom sequence/topological representation in a macromolecule/chain.

## 6.8 Bounded inference

`carbon structural feature → molecular mechanism hypothesis → measured property → qualification → engineering decision`

## 6.9 Carbon feature → mechanism → evidence boundary — preliminary teaching table

| Feature | Immediate question | Plausible mechanism | What cannot be concluded directly |
|---|---|---|---|
| Linear C–C skeleton | Connectivity/rotation/geometry? | Local mobility hypothesis | Real architecture, crystallinity, modulus, creep |
| Branch point | Which group leaves main path? | Topological difference | Commercial grade branching distribution |
| Carbon ring | How does cyclic connectivity constrain skeleton? | Geometry/conformation | Stiffness/service temperature |
| C=C or C≡C | What changes with bond order? | Geometry/rotation/reactivity | Polymerization mechanism/bulk property |
| Heteroatom/substituent | How does local chemistry change? | Polarity/steric/interaction hypothesis | Compatibility/permeability/thermal capability |

## 6.10 Common mistakes / Failure Lens

Avoid tetravalency-only explanations, branch-drawing→grade conclusions, 2D formula→3D shape, carbon skeleton→hydrocarbon-only assumptions, double-bond=two singles, and repeat-unit→bulk-property shortcuts.

## 6.11 Verification

Check four-bond wording, chapter ownership, multiple-bond boundary, skeletal-formula convention and prevention of structure→bulk-property jumps.

## 6.12 Engineering decision from Investigation 6

> Carbon is exceptionally useful in polymer chemistry because its ordinary four-bond connectivity can be arranged into diverse carbon frameworks — including chains, branches, rings, multiple-bond patterns and substituted structures. This structural versatility creates many possible molecular mechanisms, but it does not by itself determine a piping material's engineering properties.

---

# Investigation 7 — What Do sp, sp2, sp3, Sigma and Pi Bonds Mean to the Engineer?

A 2D formula shows connectivity but not why local carbon geometry changes with bonding pattern or why C=C differs from C–C.

IUPAC defines hybridization as a linear combination of atomic orbitals and notes common use of `sp3`, `sp2`, `sp` for tetrahedral, trigonal and digonal/linear atoms. [S014-003]

Hybridization is a controlled explanatory model, not a bulk property.

## 7.1 Hybridization is a model

A hybrid orbital is derived by linear combination/hybridization of atomic orbitals at the same atom. The teaching word “mix” is acceptable only if recognized as mathematical/model language, not literal fluid mixing.

## 7.2 `sp3`: tetrahedral model

`sp3` carbon uses an ideal tetrahedral local model, reference angle about `109.5°`. The key point is 3D local geometry; real angles may deviate and the value is not a tolerance/property specification.

## 7.3 `sp2`: trigonal-planar model

`sp2` local geometry is idealized trigonal-planar, approximately `120°`, with one unhybridized `p` direction available for π bonding. This affects local geometry/orbital arrangement but does not directly determine bulk properties.

## 7.4 `sp`: linear model

`sp` local geometry is idealized linear/digonal, approximately `180°`, with two unhybridized `p` directions available for π components.

## 7.5 The map is local

A molecule/polymer can contain several hybridization environments. `This polymer is sp3` is normally too crude without specifying which centers.

## 7.6 Sigma and pi

IUPAC notes both rigorous MO-symmetry and localized two-centre uses of σ/π language. In the localized model used here:

- ordinary C–C single: one σ;
- ordinary C=C: σ + π;
- ordinary C≡C: σ + 2π.

A localized π bond has a nodal plane including the internuclear axis; the localized σ description lacks that nodal plane. [S014-003]

## 7.7 Rotation: use a barrier model

“Single bonds rotate freely” is too absolute. IUPAC defines rotational barriers and limits “free rotation” to sufficiently low barriers on the experimental time scale. [S014-003]

Rotation around a conventional C=C disrupts the parallel alignment required for effective π overlap, giving a qualitatively stronger rotational constraint than an ordinary single σ bond. No universal barrier value is asserted.

## 7.8 FIG-014-003 — Carbon hybridization and geometry

Conceptual spec complete:
- `sp3`: tetrahedral, ~109.5°;
- `sp2`: trigonal planar, ~120°, one unhybridized p;
- `sp`: linear, ~180°, two unhybridized p directions.
Warnings: ideal local models, real deviations possible, not bulk-property labels.

## 7.9 FIG-014-004 — Sigma and pi bonding in ethene — partial specification

Show C–C axis, σ component, unhybridized p orbitals, side-by-side π overlap, nodal plane, and rotation constraint. Complete in Investigation 8.

## 7.10 From geometry to mechanism hypothesis

Local hybridization can plausibly alter geometry, torsional freedom, planarity, electron distribution and reaction pathways. It cannot support `more sp2 → stronger/stiffer/higher-service pipe` without material evidence.

## 7.11 Common mistakes / Failure Lens

Avoid literal orbital mixing, exact-angle absolutism, whole-polymer hybridization labels, double bond = two identical singles, zero-barrier single-bond rotation, absolute impossibility statements about all double-bond rotation pathways, direct hybridization→property inference, and σ/π context ambiguity.

## 7.12 Verification

Check model language, ideal geometry boundaries, local-vs-whole-polymer scope, σ/π context, rotational-barrier language and stop before polymerization chemistry.

## 7.13 Engineering decision from Investigation 7

> Use `sp3`, `sp2` and `sp` hybridization as idealized local orbital/geometry models, and use σ/π language to explain why single and multiple carbon–carbon bonds differ in symmetry and rotational constraint. These descriptors explain local molecular mechanisms; they do not directly determine bulk polymer or piping performance.

---

# Investigation 8 — What Is Special About Ethene / Ethylene?

The molecule that bridges this chapter's first-principles chemistry to polyethylene is `CH2=CH2`.

In strict IUPAC organic nomenclature the monomer molecule is **ethene**. The traditional word **ethylene** remains deeply embedded in polymer and industrial language, but IUPAC nomenclature also uses `ethylene` for the divalent group `–CH2–CH2–`; older IUPAC polymer guidance explicitly warns not to use the group name as though it were the preferred monomer name. [S014-008]

PPE-BoK therefore uses the following terminology rule:

> **Ethene** is the controlled chemical name for `CH2=CH2`; **ethylene** may be retained when referring to established industrial/common usage, especially in the name polyethylene, provided the context is unambiguous.

This small naming point matters because the chapter is about engineering communication as much as chemistry.

## 8.1 Read the ethene structure before thinking about polymerization

Ethene contains:

- two carbon atoms;
- four hydrogen atoms;
- one carbon–carbon double bond;
- two hydrogen atoms attached to each carbon.

At the local orbital-model level developed in Investigation 7:

- each carbon is described as `sp2` in the conventional model;
- the local carbon environment is approximately trigonal planar;
- the C=C bond is represented as one σ component plus one π component;
- the unhybridized `p` orbitals are aligned to create the localized π description.

These statements describe the **starting molecular structure**. They do not yet describe a polymerization mechanism.

## 8.2 Why the C=C bond is the important structural feature

The C=C bond makes ethene chemically different from ethane.

In the localized model, the σ framework connects the carbon nuclei along the internuclear axis while the π component depends on side-by-side overlap of the unhybridized `p` orbitals.

That π component:

- changes the electron distribution relative to an ordinary C–C single bond;
- supports the local planar `sp2` description;
- imposes a strong rotational constraint in the ordinary bonded state;
- creates a multiple-bond chemical feature that can participate in polymer-forming reactions.

The last point is deliberately phrased at mechanism-boundary level.

Chapter 014 does **not** explain how an initiator, radical, coordination catalyst or other reactive site causes chain growth. That belongs to Chapter 015.

## 8.3 FIG-014-004 — Sigma and pi bonding in ethene — conceptual specification complete

The final figure shall show an idealized ethene molecule using the localized model.

Required elements:

1. both carbon atoms labeled `sp2`;
2. approximate trigonal-planar geometry around each carbon;
3. C–C internuclear axis;
4. σ component along that axis;
5. one unhybridized `p` orbital direction on each carbon, perpendicular to the molecular plane;
6. side-by-side overlap representing the π component above/below the molecular plane;
7. nodal-plane annotation;
8. a rotation annotation explaining that rotation would disrupt effective p-orbital alignment/π overlap.

Required warnings:

- orbital lobes are model representations, not hard physical objects;
- the drawing is idealized;
- no polymerization arrows/mechanistic intermediates belong in this figure.

## 8.4 What changes in the polyethylene skeleton?

A regular polyethylene chain is commonly represented with the repeating carbon skeleton:

`–CH2–CH2–`

IUPAC polymer terminology distinguishes the **monomer** from the **monomeric unit** and from the **constitutional repeating unit (CRU)**. A monomeric unit is the largest constitutional unit contributed by one monomer molecule to the macromolecule; a CRU is the smallest constitutional unit whose repetition constitutes a regular chain/macromolecule. [S014-003]

For the simple idealized PE representation, the engineering bridge is:

`CH2=CH2  →  [–CH2–CH2–]n`

The key **structural observation** is that the carbon–carbon double-bond representation of the monomer is not retained as a C=C between every pair in the saturated polyethylene backbone. The repeating chain skeleton is represented by C–C single-bond connectivity.

This is the bridge the reader must understand before Chapter 015 explains the reaction sequence that produces it.

## 8.5 Structural before/after is not a reaction mechanism

The arrow in

`CH2=CH2  →  [–CH2–CH2–]n`

is dangerously easy to misread.

In Chapter 014 it means only:

> **compare the connectivity/bond-order pattern of the monomer with the idealized repeating skeleton of the polymer.**

It does **not** specify:

- initiation;
- propagation;
- termination;
- chain transfer;
- radical chemistry;
- coordination chemistry;
- Ziegler–Natta catalysis;
- metallocene catalysis;
- reactor conditions;
- molecular-weight control;
- branching control.

IUPAC defines polymerization generally as converting monomer(s) into a polymer and defines chain polymerization through repeated reactions between monomer(s) and reactive sites with regeneration of the reactive site. Those definitions confirm that the true mechanism is a process sequence, not the single teaching arrow shown above. [S014-003]

All detailed mechanism/process content is owned by Chapter 015.

## 8.6 Polyethene, polyethylene and poly(methylene): know which naming layer you are using

IUPAC polymer nomenclature recognizes established source-based names **polyethene** and **polyethylene** for the common material and gives **poly(methylene)** as the corresponding structure-based name in the cited regular single-strand polymer guidance. [S014-008]

For PPE-BoK:

- **PE / polyethylene** remains the normal engineering/material term because it is the language used throughout piping standards and industry;
- **polyethene** may appear when discussing source-based IUPAC naming;
- **poly(methylene)** may appear when explaining structure-based nomenclature;
- these names shall not be mixed casually with `poly(ethene-1,2-diyl)`, which is a different structure referring to a vinylene/polyacetylene-type backbone rather than ordinary saturated PE. [S014-003]

That final warning is important because similar-looking systematic names can describe very different bond patterns.

## 8.7 FIG-014-005 — Ethene to polyethylene bridge — conceptual specification complete

The figure shall contain three panels.

### Panel A — Monomer identity

`ethene (industrial/common: ethylene)`

`CH2=CH2`

Annotations:
- C=C;
- local `sp2` carbon;
- σ+π localized double-bond model.

### Panel B — Controlled structural bridge

A large arrow labeled:

**STRUCTURAL COMPARISON ONLY — NOT A POLYMERIZATION MECHANISM**

No radical, catalyst or reaction intermediate shall be shown.

### Panel C — Idealized PE repeating skeleton

`[–CH2–CH2–]n`

Annotations:
- saturated C–C backbone representation;
- local carbon centers represented as `sp3` in the simple model;
- CRU / repeating-skeleton language;
- explicit cross-reference: **mechanism → Chapter 015; chain architecture → Chapter 016; morphology → Chapter 017**.

## 8.8 EX-014-001 — Reading ethene and the PE repeat unit

### Problem

An engineer is shown two formulas:

A. `CH2=CH2`

B. `[–CH2–CH2–]n`

What can be concluded directly from the structures, and what cannot?

### Step 1 — Identify A

A is ethene, commonly called ethylene in industry.

Direct observations:

- two carbon atoms;
- four H atoms;
- C=C;
- conventional `sp2` local model;
- σ+π localized double-bond description;
- local planar geometry and restricted rotation in the ordinary C=C state.

### Step 2 — Identify B

B is the idealized repeating skeleton used for ordinary polyethylene/PE.

Direct observations:

- saturated carbon backbone representation;
- repeating `–CH2–CH2–` pattern;
- conventional local `sp3` description for the backbone carbon centers;
- single-bond connectivity rather than C=C repetition.

### Step 3 — State the legitimate bridge

The ethene monomer's C=C connectivity is transformed during polymer formation into the saturated C–C backbone connectivity represented in PE.

### Step 4 — State what the formulas do **not** tell us

The formulas alone do not specify:

- polymerization mechanism/catalyst;
- molecular weight or molecular-weight distribution;
- branching;
- crystallinity;
- density grade;
- additive package;
- SCG resistance;
- pressure rating;
- service temperature;
- fusion parameters;
- chemical compatibility.

### Engineering decision

> The monomer/repeat-unit comparison is sufficient to understand the structural bridge from C=C chemistry to a saturated PE backbone. It is insufficient to identify or qualify a real PE piping compound.

## 8.9 Why a polyethylene repeat unit is not a PE100 specification

This distinction deserves an explicit piping-engineering statement.

`[–CH2–CH2–]n` tells the engineer the idealized repeating chemical skeleton associated with polyethylene.

It does not tell the engineer whether the material is:

- a particular density class;
- PE80;
- PE100;
- enhanced-SCG-resistance PE;
- a listed/qualified piping compound;
- suitable for a particular gas, water, chemical or hydrogen service.

Those classifications emerge at much higher evidence levels. Chapter 013 and the later design/application chapters own those questions.

This is exactly why Chapter 014 separates **chemical identity** from **engineering qualification**.

## 8.10 Common mistakes / Failure Lens

### Mistake 1 — using `ethylene` and `ethene` without context

Why it fails: `ethene` is the controlled name for `CH2=CH2`, while `ethylene` also has a specific group-name use in IUPAC nomenclature even though industry commonly uses it for the monomer.

### Mistake 2 — reading the monomer→polymer arrow as the mechanism

Why it fails: the one-line structural bridge omits initiation, propagation, reactive sites, catalysts and process conditions.

### Mistake 3 — saying “the double bond opens” and treating that as a complete mechanism

Why it fails: it is at most a coarse structural shorthand; Chapter 015 must explain the actual reaction model appropriate to the polymerization route.

### Mistake 4 — treating the PE repeat-unit drawing as a grade specification

Why it fails: the repeat unit does not encode molecular-weight distribution, branching, morphology, additives or product qualification.

### Mistake 5 — confusing polyethylene with poly(ethene-1,2-diyl)

Why it fails: the latter denotes a backbone retaining ethene-1,2-diyl/vinylene C=C repeating units and corresponds to polyacetylene-type chemistry, not ordinary saturated PE.

### Mistake 6 — assuming `sp3` backbone description fixes polymer flexibility

Why it fails: local hybridization is only one mechanism input; torsional barriers, side groups, chain architecture, intermolecular interactions and morphology still matter.

## 8.11 Verification

Before accepting an ethene→PE explanation, check:

1. Is `CH2=CH2` identified as ethene, with industrial `ethylene` usage explicitly disambiguated?
2. Is C=C described through the already-controlled `sp2`, σ+π model?
3. Is `[–CH2–CH2–]n` presented as an idealized repeating skeleton rather than a complete commercial-material definition?
4. Is the structural comparison arrow explicitly labeled **not a reaction mechanism**?
5. Are initiation/catalysis/kinetics/branching-control topics deferred to Chapter 015/016?
6. Are monomer, monomeric unit and CRU terminology kept distinct?
7. Has any PE grade, property or pressure qualification been inferred from the repeat unit alone?
8. Are confusing structure-based/source-based names checked before use?

## 8.12 Engineering decision from Investigation 8

> Ethene (`CH2=CH2`) is the controlled chemical starting structure for the polyethylene bridge: its `sp2` C=C σ+π bonding pattern differs fundamentally from the saturated C–C backbone pattern represented by `[–CH2–CH2–]n`. That structural comparison explains **what changes in connectivity**, but not **how polymerization occurs** and not **which engineering grade of PE results**.

After Investigation 8, the reader has the complete first-principles chain required for the next stage:

`atom → electrons → bonding → intermolecular interaction → carbon skeleton → local hybridization / σπ → ethene monomer → idealized PE repeating skeleton`

The next question is no longer “what does the chemistry look like?” It is:

> **How can a molecular feature be turned into a defensible engineering-property hypothesis without overclaiming?**

That is Investigation 9 — and unlike Investigations 1–8, it requires direct primary polymer literature for every retained material-specific bridge.

---

# Investigation 9 — How Do Molecular Features Become Engineering-Property Hypotheses?

## 9.1 The useful question is not “what property does this structure have?”

A chemical structure is valuable to an engineer because it helps formulate **mechanism hypotheses**.

It is dangerous when it is treated as though it already contains the answer to a bulk engineering-property question.

The disciplined question is therefore not:

> “What pressure capability, permeability, compatibility or modulus does this chemical structure have?”

It is:

> “Which molecular feature suggests a physically plausible mechanism, which measurable property would reveal whether that mechanism matters, and what additional evidence is required before the result can influence an engineering decision?”

That distinction is the central engineering capability of this Investigation.

A molecular drawing can show features such as:

- polar or strongly polarizable groups;
- potential hydrogen-bond donor/acceptor sites;
- fluorination or other substitution;
- side groups;
- local rotational constraints;
- heteroatoms;
- backbone connectivity;
- potential symmetry or packing differences.

Those observations may suggest changes in:

- interaction with penetrant molecules;
- segmental mobility;
- intermolecular association;
- packing or free-volume tendencies;
- crystallization behaviour;
- diffusion or sorption pathways.

But the drawing does not specify the magnitude of the final response in a real polymer product.

Between chemical structure and engineering performance sit additional levels that may dominate the result:

`molecular structure → chain architecture → morphology → processing history → conditioning / environment → specimen or product geometry → measured property → qualification → engineering decision`

This is why the same repeat-unit chemistry can produce materially different measured behaviour when molecular architecture, crystallinity, processing, additives or conditioning differ.

---

## 9.2 A controlled structure-to-property reasoning chain

PPE-BoK uses the following seven-step reasoning chain for a structure-derived hypothesis.

### Step 1 — Observe the molecular or structural feature

State only what is actually visible or otherwise established.

Examples:

- an amide group is present;
- a polymer is highly fluorinated;
- an ether-containing comonomer is present;
- two specimens were processed using different cooling histories.

Do not convert the observation into a property claim yet.

### Step 2 — State a mechanism hypothesis

Describe the mechanism as a hypothesis, not a conclusion.

Examples:

- water may interact strongly with polar amide-containing regions;
- penetrant transport may depend on polarity as well as available free volume and morphology;
- cooling history may change crystallinity and therefore change gas transport.

### Step 3 — Identify the property that must be measured

A mechanism becomes useful only when it points to an observable quantity.

Possible quantities include:

- mass uptake / sorption;
- dimensional swelling;
- diffusion coefficient;
- permeability or transmission;
- modulus;
- glass-transition response;
- crystallinity;
- spectroscopic change;
- fracture or joining response.

The correct property depends on the engineering question.

### Step 4 — Obtain direct evidence

The evidence must actually measure or otherwise directly support the proposed bridge.

A plausible mechanism without measurement remains a hypothesis.

### Step 5 — Identify confounders

Ask what else changed or could control the measured response.

Common confounders include:

- molecular weight and molecular-weight distribution;
- branching / comonomer content;
- crystallinity;
- orientation;
- additives and fillers;
- thermal history;
- specimen thickness;
- geometry / surface-to-volume ratio;
- conditioning history;
- penetrant concentration;
- temperature;
- time;
- test configuration.

### Step 6 — Set the transferability boundary

State how far the evidence can legitimately travel.

A thin membrane result is not automatically a pressure-pipe-wall result.

A molded PA6 specimen is not automatically a reinforced PA piping component.

A compression-molded PFA coupon is not automatically a qualified PFA pipe or fitting.

### Step 7 — Route the result to qualification

If the hypothesis matters to a real project, the engineer must move to the owning evidence layer:

- material-specific characterization;
- product qualification;
- application standard;
- manufacturer data under controlled conditions;
- project testing;
- specialist analysis.

Only then may the evidence enter a design decision.

---

## 9.3 TAB-014-002 — Molecular feature, mechanism hypothesis and invalid direct conclusion

| Molecular / structural observation | Plausible mechanism question | Property or evidence that should be measured | Invalid direct conclusion |
|---|---|---|---|
| Polar functional group | Does the service molecule interact preferentially with this region? | Sorption, swelling, diffusion, spectroscopy, mechanical change under conditioning | “Polar polymer = chemically compatible/incompatible” |
| Potential hydrogen-bonding sites | Does exposure alter the intermolecular H-bond network or segmental mobility? | Spectroscopy plus sorption / mechanical / thermal response | “Hydrogen bonding gives a fixed modulus or service limit” |
| High fluorination | How do polarity, polarizability, packing and morphology affect penetrant transport? | Permeability / diffusion / solubility for the actual penetrant and morphology | “More fluorine always means lower permeability” |
| Ether-containing comonomer / heteroatom | Does local chemistry alter penetrant interaction or chain packing? | Material-specific transport / sorption measurements | “Ether group alone determines gas selectivity” |
| Local single-bond rotational freedom | Does chain-level architecture permit greater segmental mobility under the relevant state? | DMA / relaxation / thermal / mechanical characterization | “More single bonds = flexible pipe” |
| Different cooling history | Did processing change crystallinity or other morphology? | DSC / density / morphology characterization plus target property | “The repeat unit determines the property independently of processing” |
| Different crystallinity | Does the amorphous/crystalline balance alter transport or mechanical response? | Crystallinity plus property measurement under matched conditions | “Higher crystallinity is universally better” |

**Interpretation rule:** this table is a question generator, not a material-selection table.

---

## 9.4 Case A — PA6 + water: when chemistry gives a useful mechanism, but not a design value

Polyamide 6 provides a useful example because the chain contains polar amide groups and the material is known experimentally to respond to water conditioning.

The chemical observation is straightforward:

- the polymer contains amide functionality;
- water is a small polar molecule;
- intermolecular hydrogen-bonding interactions are scientifically plausible.

That is enough to formulate a hypothesis:

> Water uptake may alter intermolecular association and segmental mobility in PA6, producing measurable sorption, swelling and mechanical changes.

It is **not** enough to specify the magnitude of those changes.

### 9.4.1 What the direct evidence shows

Shinzawa and Mizukado studied dry- and wet-treated PA6 using near-infrared correlation spectroscopy together with mechanical comparison. Their reported observations include a substantial decrease in Young's modulus after wet treatment and spectroscopic interpretation consistent with absorbed water disrupting H-bonded bridges particularly in amorphous regions and increasing chain mobility. They also reported a change in the crystalline/amorphous population, which immediately prevents a simplistic one-variable explanation. [S014-009]

Sambale et al. experimentally characterized water sorption and moisture-induced swelling of PA6 specimens under controlled conditioning and different geometry conditions. Their work required concentration-dependent diffusion behaviour and explicitly treated geometry, concentration and swelling rather than reducing the phenomenon to the presence of an amide group. [S014-010]

Together these studies support the mechanism-level statement:

> **Amide/H-bond chemistry is a defensible starting hypothesis for PA6–water interaction, and water exposure produced measurable sorption, swelling and mechanical/molecular changes in the studied PA6 systems.**

### 9.4.2 What the evidence does not establish

The papers do not establish one universal value for:

- PA6 water absorption;
- allowable swelling;
- modulus reduction;
- pressure derating;
- allowable temperature;
- chemical-service acceptance;
- dimensional tolerance for every product;
- reinforced or compounded PA performance.

The measured behaviour depends on specimen form, conditioning, concentration, temperature, morphology and geometry.

The correct engineering response is therefore not “PA6 absorbs X, so apply X to the design.”

It is:

`amide-containing PA structure → water-interaction hypothesis → characterize actual material/conditioning → quantify relevant property change → apply product/application qualification`

### 9.4.3 Engineering lesson from Case A

A chemistry hypothesis can be **scientifically correct and experimentally supported** while still being **insufficient for direct design use**.

That is not a weakness of chemistry. It is the correct separation between mechanism and qualification.

---

## 9.5 Case B — Fluoropolymer membranes: when a simple chemistry ranking fails

Fluoropolymers are tempting targets for shortcut reasoning.

An engineer may look at fluorine substitution, polarity and symmetry and try to create a simple ranking such as:

> “more fluorination → more/less polarity → lower gas permeability.”

The problem is that penetrant transport in a polymer is not controlled by one descriptor alone.

Graunke et al. experimentally compared multiple fluoropolymer membranes chosen to vary fluorination and structural features including ether-containing monomers. Their measurements showed strong influences from polymer-specific structure and crystallinity, and the paper includes cases where an expected simple relation between density/crystallinity/polarity and permeability did not hold generally. [S014-011]

The controlled conclusion is therefore:

> **Fluorination, polarity and functional-group chemistry can generate useful transport hypotheses, but they do not provide a universal permeability or selectivity ranking across fluoropolymers.**

### 9.5.1 Why this is an important engineering failure mode

A repeat-unit comparison hides variables such as:

- crystalline fraction;
- packing / morphology-related free-volume effects;
- chain packing;
- copolymer architecture;
- membrane thickness;
- processing history;
- penetrant identity;
- penetrant concentration;
- test geometry.

A chemically elegant ranking can therefore be physically incomplete.

### 9.5.2 What may be transferred to piping engineering

The transferable lesson is **methodological**, not quantitative:

1. use chemistry to propose which interactions may matter;
2. identify morphology/processing variables that may alter the transport pathway;
3. measure the actual penetrant/material system;
4. do not use thin-film sensor-membrane transmission as a pipe-wall permeability allowance.

No ranking of piping-grade PVDF, PTFE, PFA, ECTFE, ETFE or other fluoropolymers is authorized from this case.

---

## 9.6 Case C — PFA cooling history: when processing changes the result without changing the family name

The third case attacks a different shortcut:

> “If the polymer family and nominal grade are known, the transport property should be essentially fixed.”

Monson, Moon and Extrand tested several PFA/PTFE-copolymer grades using specimens prepared with different cooling techniques. They measured permeability, diffusion and solubility coefficients for hydrogen, nitrogen and oxygen. Slow-cooled specimens showed markedly greater permeation resistance than rapidly cooled specimens, and the authors attributed the differences to crystallinity arising from molecular architecture and processing. They concluded that processing can be as important as polymer grade for the measured permeation response. [S014-012]

This is a high-value teaching case because the chemical family label remained insufficient.

### 9.6.1 The engineering chain

The defensible reasoning chain is:

`PFA family / architecture + cooling history → different morphology / crystallinity hypothesis → measured H2/N2/O2 transport → bounded specimen-level conclusion`

not:

`PFA repeat unit → universal gas permeability`

### 9.6.2 What this case proves at Chapter 014 level

It supports the general mechanism statement that **processing-induced morphology can materially influence a measured property that an engineer might otherwise try to infer from chemistry or grade name alone**.

It does not establish:

- a universal slow-cooling manufacturing prescription;
- an allowable H2 permeation rate for PFA pipe;
- a service-life value;
- a pipe-wall design rule;
- superiority of one commercial grade.

Those require product-specific evidence and the later materials/design framework.

---

## 9.7 TAB-014-003 — Controlled structure–property teaching cases

| Case | Starting feature / hypothesis | Direct evidence | Confounders made visible by the evidence | Defensible conclusion | Design conclusion explicitly prohibited |
|---|---|---|---|---|---|
| A — PA6 + water | amide functionality / H-bond interaction with water | sorption, swelling, modulus and spectroscopic/morphology response in studied PA6 systems [S014-009][S014-010] | conditioning, concentration, geometry, amorphous/crystalline balance | chemistry correctly identifies a relevant interaction mechanism, but magnitude requires measurement | universal PA modulus derating, swelling allowance or compatibility limit |
| B — fluoropolymer membranes | fluorination / polarity / ether groups may influence penetrant transport | measured gas/water-vapour transport across selected membranes [S014-011] | crystallinity, density/packing/free-volume interpretation, copolymer structure, film/test configuration | simple chemical descriptors are insufficient as a universal transport ranking | piping-grade fluoropolymer permeability ranking or service qualification |
| C — PFA process/morphology | grade chemistry alone may not control permeation if processing changes morphology | H2/N2/O2 permeability, diffusion and solubility under different cooling histories [S014-012] | cooling history, crystallinity, comonomer/filler, specimen preparation | processing/morphology can rival grade chemistry in measured transport | universal cooling prescription or pipe-wall permeability value |

The table deliberately contains no ranking column.

---

## 9.8 EX-014-002 — Comparing two apparently “simple” polymer hypotheses

### Problem

An engineer is asked to predict service behaviour from two observations:

1. **Polymer A** contains a polar functional group capable of strong intermolecular interaction with water.
2. **Polymer B** is highly fluorinated and appears chemically inert from its repeat-unit drawing.

The engineer is asked to decide which material has lower moisture uptake, lower gas permeability and higher stiffness in service.

### Step 1 — Refuse the requested ranking

The structural information is insufficient for the requested engineering ranking.

It can support hypotheses, not final values.

### Step 2 — Form the Polymer A hypothesis

A polar / hydrogen-bond-capable structure suggests that water interaction and sorption may be important.

Required evidence could include:

- equilibrium uptake;
- sorption kinetics;
- swelling;
- modulus versus conditioning;
- thermal response;
- morphology/conditioning state.

The PA6 evidence demonstrates why this is a legitimate research path, but not why all polar polymers behave identically. [S014-009][S014-010]

### Step 3 — Form the Polymer B hypothesis

A highly fluorinated structure may suggest low interaction with some penetrants, but gas transport still depends on morphology, packing/free-volume effects, crystallinity, copolymer structure and processing.

The fluoropolymer and PFA cases show why chemistry-only ranking can fail. [S014-011][S014-012]

### Step 4 — Define the engineering tests instead of guessing the answer

For a real project, specify evidence for the actual:

- polymer grade / compound;
- product form;
- temperature;
- penetrant or process fluid;
- exposure concentration / pressure;
- conditioning history;
- geometry;
- property of interest.

### Step 5 — State the engineering decision

> The chemical structures are sufficient to identify different **questions to test**. They are not sufficient to decide the requested service ranking.

### What this example does **not** prove

It does not prove that PA6 is more permeable than a fluoropolymer, that fluoropolymers are universally non-polar, that one family is more chemically resistant, or that either material is appropriate for piping service.

---

## 9.9 Evidence-chain design requirements for FIG-014-006

The figure shall show a gated sequence rather than a simple causal arrow.

### Gate 1 — Molecular observation

Examples: functional group, substitution, local bond type, repeat-unit feature.

**Question:** what is actually known from the structure?

### Gate 2 — Mechanism hypothesis

Examples: preferential interaction, altered mobility, packing/free-volume effect, crystallization tendency.

**Question:** what physical mechanism is proposed?

### Gate 3 — Direct measurement

Examples: sorption, diffusion, permeability, modulus, DSC, spectroscopy.

**Question:** was the predicted response measured?

### Gate 4 — Confounder review

Examples: morphology, processing, additives, conditioning, geometry, temperature.

**Question:** what else could control the result?

### Gate 5 — Transferability

**Question:** does the evidence apply to this material grade, product form and service state?

### Gate 6 — Qualification / governing evidence

**Question:** what product/application standard, qualified manufacturer data or project test converts the observation into usable engineering evidence?

### Gate 7 — Engineering decision

Only after the previous gates may a design decision be made.

The visual shall include a red stop marker between **mechanism hypothesis** and **design decision** with the caption:

**NO DIRECT JUMP**

---

## 9.10 Workflow checkpoint before the final chapter decision tool

Cases A–C have now validated the reasoning sequence used throughout this Investigation:

`observe structure → state mechanism hypothesis → define measurable property → obtain direct evidence → identify confounders → set transferability boundary → qualify → decide`

The final controlled `WF-014-001` is intentionally placed in Investigation 10, where the scientific reasoning track is joined to product/application qualification and the chapter stop-rule.

---

## 9.11 Verification — how to audit a structure→property statement

Before retaining any material-specific statement, ask:

1. What exact molecular/structural feature is being observed?
2. Is the proposed mechanism stated as a mechanism rather than a design fact?
3. Which property was actually measured?
4. Is the cited source direct primary evidence for that property?
5. Were morphology, processing, additives, conditioning and geometry considered?
6. Does the specimen/product form match the intended engineering use?
7. Is the conclusion qualitative or quantitative?
8. If quantitative, is transfer of the numerical value explicitly justified?
9. Is a product/application standard or qualification route still required?
10. Could the sentence be misread as a material ranking or acceptance criterion?

If item 10 is yes, rewrite it.

---

## 9.12 Common mistakes / Failure Lens

### Mistake 1 — plausible mechanism = proven property

A mechanism can be physically reasonable and still have negligible engineering effect under the actual service condition.

### Mistake 2 — one primary paper = universal material rule

A paper establishes what occurred in its tested system. Transfer to another grade, geometry, morphology or service requires justification.

### Mistake 3 — repeat unit = complete material state

The repeat unit does not encode molecular-weight distribution, crystallinity, orientation, additives, residual stress or processing history.

### Mistake 4 — polarity = chemical compatibility database

Polarity can guide a question. It does not replace service-specific compatibility evidence.

### Mistake 5 — permeability result = pipe-wall allowance

Permeability depends on penetrant, temperature, pressure/concentration, morphology and geometry. A membrane or coupon result is not automatically a pressure-pipe design value.

### Mistake 6 — processing is “manufacturing detail” rather than material state

Case C shows why processing can change morphology enough to change a measured transport property materially.

### Mistake 7 — adding a numerical value because a paper reports one

Chapter 014 uses these studies to teach evidence discipline. Numeric results are not imported unless a later chapter has a justified engineering use and transferability basis.

---

## 9.13 Engineering decision from Investigation 9

> A chemical structure is an efficient generator of **engineering hypotheses**, not engineering acceptance values. The correct path is `feature → mechanism hypothesis → measurement → confounder review → transferability → qualification → decision`. Cases A–C demonstrate three complementary outcomes: a plausible mechanism can be supported but remain non-transferable as a design value; a simple chemical ranking can fail; and processing/morphology can change a property even within the same polymer family.

Investigation 9 therefore closes the chapter's final scientific bridge.

The remaining question is governance of the boundary itself:

> **When is chemistry sufficient to guide engineering judgement, and when must the engineer stop and hand the question to characterization, qualification, standards or a downstream PPE-BoK chapter?**

That is the purpose of Investigation 10.

---

# Investigation 10 — What Can Chemistry Tell Us, and Where Must the Engineer Stop?

## 10.1 Chemistry is a powerful filter, not a product certificate

A practicing engineer should leave this chapter with more confidence in molecular reasoning — and less willingness to misuse it.

Chemistry can help the engineer:

- recognize important molecular features;
- reject chemically impossible explanations;
- formulate plausible mechanisms;
- identify which property should be measured;
- anticipate which environmental interactions deserve attention;
- select useful characterization methods;
- detect when a simple material-family label is hiding important uncertainty;
- ask better questions of suppliers, laboratories and specialists.

Chemistry cannot, by itself, establish:

- pressure rating;
- allowable stress;
- maximum service temperature;
- long-term lifetime;
- chemical compatibility for a specific service;
- permeation allowance;
- fusion parameters;
- slow-crack-growth resistance;
- product conformity;
- installation acceptance;
- system qualification.

Those decisions belong to higher evidence levels.

The final engineering discipline of Chapter 014 is therefore knowing **where to stop**.

---

## 10.2 The evidence ladder: from chemical identity to an engineering decision

A useful way to prevent overclaiming is to separate evidence into levels.

> **PPE-BoK framework:** The following levels are a PPE-BoK reasoning framework for controlling evidence transfer; they are not a normative classification defined by ISO, IUPAC or another single standards body.

### Level 1 — Chemical identity / structural description

Typical evidence:

- molecular formula;
- repeat-unit representation;
- functional groups;
- local bonding / hybridization model;
- elemental substitution;
- qualitative polarity / intermolecular-interaction features.

This level answers:

> **What structure are we talking about?**

It does not answer whether a commercial piping product is acceptable.

### Level 2 — Mechanism hypothesis

Typical statements:

- a penetrant may interact with a polar group;
- segmental mobility may change with conditioning;
- morphology may influence transport;
- a local structural feature may alter packing or crystallization behaviour.

This level answers:

> **What physical mechanism should be tested?**

A mechanism hypothesis is still not a property value.

### Level 3 — Material characterization

Typical evidence:

- DSC / thermal analysis;
- spectroscopy;
- density / crystallinity indicators;
- sorption / swelling;
- permeability / diffusion;
- modulus / tensile / impact response;
- molecular-weight or rheological characterization;
- microscopy.

This level answers:

> **What did this material state actually do under defined test conditions?**

The result is bounded by specimen, method and conditions.

### Level 4 — Compound / grade qualification

A real engineering polymer is not only a repeating chemical skeleton.

The compound or grade may include controlled:

- molecular architecture;
- comonomer distribution;
- additives / stabilizers;
- pigments / fillers;
- processing requirements;
- quality-control limits;
- traceability / certification requirements.

This level answers:

> **Is the defined material formulation / grade qualified for the intended evidence framework?**

### Level 5 — Product qualification

Pipe, fitting, valve or sheet form introduces additional variables:

- geometry;
- manufacturing process;
- residual stress;
- wall-thickness control;
- surface condition;
- joining interface;
- product testing;
- dimensional / marking / conformity requirements.

This level answers:

> **Does the finished product meet the applicable product requirements?**

### Level 6 — Application / system qualification

The engineering environment finally adds:

- process fluid;
- pressure;
- temperature;
- time;
- cycling / transients;
- external loading;
- installation;
- joining;
- inspection;
- supports / restraints;
- environment;
- maintenance philosophy;
- jurisdiction / project requirements.

This level answers:

> **Is this product/system suitable for this actual application?**

A correct molecular explanation can exist at Level 2 while the system still fails at Level 6.

---

## 10.3 The stop-rule

The Chapter 014 stop-rule is intentionally simple:

> **Stop molecular inference at the first point where the engineering conclusion requires a magnitude, acceptance threshold, lifetime, product state or service-specific performance that the available evidence has not directly established.**

When the stop-rule triggers, do not “fill the gap” with intuition.

Route the question to:

- direct characterization;
- the applicable material chapter;
- the applicable test standard;
- product qualification;
- manufacturer data under controlled conditions;
- project-specific testing;
- specialist analysis;
- the governing design/application framework.

The absence of evidence is an engineering input, not permission to invent one.

---

## 10.4 Final FIG-014-006 — Molecular feature to engineering evidence chain

The final scientific figure shall show **two parallel tracks**.

### Track A — Scientific reasoning

`Chemical / structural observation`

→ `Mechanism hypothesis`

→ `Predicted measurable response`

→ `Characterization / experiment`

→ `Mechanism interpretation`

This track develops understanding.

### Track B — Engineering qualification

`Defined compound / grade`

→ `Qualified material evidence`

→ `Finished product qualification`

→ `Application / system requirements`

→ `Engineering decision`

This track develops acceptance.

### Mandatory connection between tracks

The tracks may connect only through verified evidence.

A prominent prohibition shall be shown:

`molecular feature  ✕→  direct design acceptance`

Caption:

> **Chemistry explains why a property may exist. Qualification establishes whether the property is sufficient for the engineering application.**

### Required callouts

- processing / morphology can modify the measured result;
- service state can modify the measured result;
- a material-family name is not a product qualification;
- numerical transfer requires a transferability basis.

---

## 10.5 WF-014-001 — Chemical structure to engineering decision boundary — final chapter version

### Phase 1 — Identify

1. Define the actual material / product identity as far as known.
2. Read the chemical / repeat-unit structure only at the level justified by evidence.
3. Identify functional groups, substitution, bonding and intermolecular-interaction features relevant to the engineering question.

### Phase 2 — Hypothesize

4. State the proposed mechanism.
5. State the expected measurable response.
6. Identify alternative mechanisms and likely confounders.

### Phase 3 — Verify

7. Obtain direct material-specific evidence.
8. Verify specimen, conditioning, temperature, time and test configuration.
9. Separate measured result from interpretation.
10. Check morphology / processing / additive effects where relevant.

### Phase 4 — Transfer

11. Define what product/material states the evidence actually represents.
12. Identify whether transfer to the intended product form is justified.
13. Reject unsupported transfer of numerical values.

### Phase 5 — Qualify

14. Identify the applicable material / product / application qualification framework.
15. Confirm conformity and traceability of the actual product.
16. Add project Design Basis conditions that may invalidate nominal qualification.

### Phase 6 — Decide

17. Make the engineering decision only from the complete evidence chain.
18. Record assumptions, exclusions and residual uncertainty.
19. Route unresolved issues to the owning specialist / chapter / test program.

### Stop condition

At any step:

> **If the next conclusion depends on evidence that has not been established, stop. Record the hypothesis and define the missing evidence.**

---

## 10.6 CL-014-001 — Before inferring engineering behaviour from a chemical structure

| ID | Review question | Required evidence / disposition |
|---|---|---|
| CL-014-01 | Have I separated the chemical structure from the commercial material/compound identity? | Identify known resin/compound/product information and unknowns |
| CL-014-02 | Is the molecular feature actually established, or am I assuming it from a family name? | Structural / composition source |
| CL-014-03 | Have I stated a mechanism hypothesis rather than a property fact? | Explicit hypothesis wording |
| CL-014-04 | Which measurable property would test the hypothesis? | Defined characterization / test output |
| CL-014-05 | Do I have direct evidence for that property in the actual or transferable material state? | Primary / qualified material evidence |
| CL-014-06 | Have I considered morphology, crystallinity and processing history? | Characterization or justified disposition |
| CL-014-07 | Have I considered additives, fillers, pigments, stabilizers or reinforcement? | Compound / supplier / qualification data |
| CL-014-08 | Have I considered conditioning, temperature, time and concentration/pressure? | Test / service-condition match |
| CL-014-09 | Does specimen geometry / product form affect transferability? | Geometry / product-form justification |
| CL-014-10 | Am I using a membrane/coupon/resin result as though it were a pipe/fitting result? | Explicit transferability check |
| CL-014-11 | Am I converting a qualitative trend into a numerical design value? | Source and validated numerical transfer basis |
| CL-014-12 | Does a product or application standard govern the actual decision? | Applicable standards path |
| CL-014-13 | Has the actual material grade / product been qualified and traced? | Conformity / traceability evidence |
| CL-014-14 | Does the project Design Basis introduce service conditions outside the qualification envelope? | Design Basis comparison |
| CL-014-15 | Have I documented what chemistry cannot establish? | Explicit limitation statement |
| CL-014-16 | If evidence is missing, have I stopped rather than guessed? | Hold / test / specialist action |

A checked item means the evidence has been reviewed and found acceptable. `N/A` requires a written justification.

---

## 10.7 TAB-014-004 — Downstream chapter ownership crosswalk

| Engineering question after Chapter 014 | Owning PPE-BoK chapter / block | What moves beyond Chapter 014 |
|---|---|---|
| How does ethene actually become polyethylene? | Working Chapter 015 — Polymerization, Catalysts and Process–Structure Relationships | initiation / propagation concepts, catalysts, reactor/process history |
| How do molecular weight, branching and crosslinking change behaviour? | Working Chapter 016 — Polymer Chain Architecture | chain length, MWD, branching, connectivity, crosslinking |
| How do crystalline and amorphous regions form and interact? | Working Chapter 017 — Crystallinity and Morphology | lamellae, spherulites, tie molecules, morphology development |
| How do temperature and thermal transitions change response? | Working Chapter 018 — Thermal Transitions and Thermophysical Behaviour | Tg, Tm, thermal expansion, conductivity, temperature-dependent state |
| Why do polymers creep and relax with time? | Working Chapter 019 — Viscoelasticity, Creep and Time–Temperature Behaviour | constitutive/time-dependent response, TTS, Arrhenius/WLF concepts |
| Why and how do polymers crack, fatigue or age? | Working Chapter 020 — Fracture, Crack Growth, Fatigue, ESC and Ageing | SCG/RCP/fatigue/ESC/oxidation/UV/degradation |
| Which material family should be selected? | Part IV — Engineering Material Families | family-specific properties, limits and application evidence |
| What does a laboratory test actually measure? | Part V — Material Characterization and Testing | test methods, specimen control, uncertainty, interpretation |
| How is long-term performance qualified? | Part VI — Long-Term Performance and Engineering Evidence | qualification, validation, certification, technical files |
| How should joining be selected and controlled? | Part VII — Joining and Connection Engineering | fusion/welding/mechanical joint procedure, qualification and inspection |
| How are pressure, thermal, support and other loads designed? | Part VIII — Pipe and System Mechanical Design | stress/load/system calculations and design decisions |
| How is chemical/service suitability established? | material-selection, material-family and application chapters | fluid-specific compatibility evidence and project Design Basis |
| How is a real failure investigated? | Part XIII — Failure Analysis and Root-Cause Investigation | evidence preservation, fractography, lab methods, hypothesis testing |

This table is a routing tool, not a final Table of Contents freeze. Working chapter numbers remain controlled by `BOOK_STRUCTURE.md`.

---

## 10.8 What “first principles” should mean in engineering practice

First-principles thinking is sometimes misused as permission to ignore empirical qualification.

That is the opposite of the intended method.

For PPE-BoK, first-principles reasoning means:

1. start from mechanisms that are physically and chemically defensible;
2. use those mechanisms to identify the right variables and failure hypotheses;
3. test the variables that matter;
4. reject explanations that conflict with evidence;
5. preserve uncertainty when evidence is incomplete;
6. apply qualified standards / product evidence at the correct decision level.

A first-principles explanation and a standards-based qualification are complementary.

One explains **why**.

The other controls **whether the evidence is sufficient for use**.

---

## 10.9 Common mistakes / Failure Lens

### Mistake 1 — “I understand the chemistry, therefore I can calculate the service limit.”

Why it fails: service limits depend on qualified material/product/system evidence, not chemical identity alone.

### Mistake 2 — treating a material family as a material specification

Why it fails: `PE`, `PA`, `PVDF`, `PFA` or another family name does not define molecular architecture, formulation, product manufacture or qualification.

### Mistake 3 — using one test result outside its state

Why it fails: temperature, time, conditioning, morphology and specimen geometry can alter the response.

### Mistake 4 — hiding uncertainty behind a qualitative phrase

Statements such as `excellent resistance`, `low permeability` or `high strength` require a defined comparison, condition and evidence source when used for engineering decisions.

### Mistake 5 — assuming a standard replaces mechanism understanding

Why it fails: a standard can define qualification or acceptance while not explaining every physical reason behind the requirement.

### Mistake 6 — assuming mechanism understanding replaces a standard

Why it fails: understanding why a material might perform well does not prove conformity with the governing product/application requirements.

### Mistake 7 — continuing after the evidence chain breaks

Why it fails: once transferability is unsupported, every downstream conclusion inherits the unsupported assumption.

---

## 10.10 Verification — the chapter desk test

A reader should be able to answer the following without ambiguity:

1. Can I infer a mechanism from a chemical structure? **Yes, if stated and bounded appropriately.**
2. Can I infer an exact engineering property value from the structure alone? **No.**
3. Can a primary research paper support a mechanism? **Yes.**
4. Does one paper automatically qualify another grade/product/application? **No.**
5. Can processing and morphology change behaviour even within one family? **Yes; this chapter demonstrates why the possibility must be checked.**
6. Does a repeat unit identify a piping grade? **No.**
7. Is chemistry useful for material selection? **Yes, as part of the evidence chain.**
8. Does chemistry replace material/product/application qualification? **No.**
9. What should I do when the next inference is unsupported? **Stop, define the missing evidence and route the question.**
10. Where do I go next? **Use `TAB-014-004` and the applicable later PPE-BoK chapter.**

If a reader can interpret Chapter 014 as authorizing a material, pressure, temperature, chemical service or lifetime from molecular structure alone, the chapter has failed its Desk Test.

---

## 10.11 Engineering decision from Investigation 10

> **Use chemistry to identify mechanisms, variables, evidence needs and plausible failure hypotheses. Do not promote molecular reasoning into engineering acceptance until the relevant property has been measured, transferability has been justified, the actual material/product state is qualified and the application Design Basis has been checked.**

This closes the first-principles scope of Chapter 014.

The reader now has the bridge:

`atom → electron structure → bonding → intermolecular interactions → carbon chemistry → local geometry / σπ → ethene → idealized PE backbone → structure-property hypothesis → measured evidence → qualification boundary`

The next chapter begins where this one intentionally stops:

> **How does polymerization transform monomers into real macromolecular architectures, and how do catalysts and process history shape the material that the engineer ultimately receives?**

That question belongs to Working Chapter 015.

---

# Chapter engineering closure

Chapter 014 has established three distinctions that shall remain visible throughout PPE-BoK:

1. **Chemical structure is not material state.** Molecular identity is only the lowest level of the engineering evidence hierarchy.
2. **Mechanism is not qualification.** A scientifically defensible explanation can guide testing without establishing a design value.
3. **Material qualification is not system suitability.** Product and application conditions must still be checked against the project Design Basis.

The practical use of first-principles chemistry is therefore not to replace standards, testing or qualification. It is to make those activities more intelligent: to identify the right variables, challenge weak explanations, detect hidden confounders and know when an engineering claim has exceeded its evidence.

## Residual project-specific engineering

Chapter 014 does not close:

- polymerization/process chemistry;
- real chain architecture;
- morphology;
- temperature/time-dependent constitutive behaviour;
- fracture/degradation;
- family-specific compatibility;
- material/product qualification;
- joining qualification;
- pressure/mechanical design;
- service-specific acceptance.

Those questions are deliberately routed to the downstream PPE-BoK architecture.

---

# Chapter engineering assets — current register

| ID | Asset | Status |
|---|---|---|
| FIG-014-001 | Atom-to-material hierarchy | Placeholder integrated; graphic production pending |
| FIG-014-002 | Primary Bonding and Noncovalent Interaction Map | Scientific specification complete; graphic production pending |
| FIG-014-003 | Carbon hybridization and geometry | Scientific specification complete; graphic production pending |
| FIG-014-004 | Sigma and pi bonding in ethene | Scientific specification complete; graphic production pending |
| FIG-014-005 | Ethene to polyethylene bridge | Scientific specification complete; graphic production pending |
| FIG-014-006 | Molecular feature to engineering evidence chain | Final scientific specification integrated; graphic production pending |
| TAB-014-001 | Bonding types and engineering relevance | Integrated |
| TAB-014-002 | Molecular feature / likely mechanism / invalid direct conclusion | Integrated in Investigation 9 |
| TAB-014-003 | Controlled structure–property teaching cases | Integrated; Investigation 9 authoring review PASS |
| TAB-014-004 | Downstream chapter ownership crosswalk | Integrated in Investigation 10 |
| EX-014-001 | Reading ethene and PE repeat unit | Integrated; final full-chapter review pending |
| EX-014-002 | Comparing two simple polymer hypotheses | Integrated; Investigation 9 authoring review PASS |
| WF-014-001 | Chemical structure → evidence → engineering decision boundary | Final chapter version integrated |
| CL-014-001 | Before inferring engineering behaviour from chemical structure | Integrated |

---

# Publication hold points

Chapter 014 has completed its approved Engineering Development arc, but publication closure is not implied.

Before publication, the chapter still requires:

- final full-file Technical Review after canonical integration;
- final claim-level Standards/Evidence publication pass;
- final Editorial / Style Review;
- continuous-manuscript Desk Test;
- final figure production where required for Publishing;
- explicit author review / Human Approval Gate;
- synchronization with current `main` and controlled merge.

No chemistry, vocabulary source or primary-study result in this chapter independently authorizes a piping material, pressure, temperature, chemical service, permeability allowance, lifetime or joining condition.

# References

See `references.md` for the controlled Chapter 014 source and evidence register.
