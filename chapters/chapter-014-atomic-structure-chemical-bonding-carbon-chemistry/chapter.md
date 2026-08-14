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
6. explain why the carbon–carbon double bond in ethylene differs from the carbon–carbon single bonds of a polyethylene backbone;
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
- ethylene as the bridge to polymerization;
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
- **Ethylene:** Investigation 8.
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

After Investigation 1, the engineer should be able to classify a statement into one of three levels:

### Level 1 — Chemistry fact

Example: a bond is polar; a molecular interaction is possible; a carbon atom is in a particular bonding geometry.

### Level 2 — Mechanism hypothesis

Example: that structural feature may alter molecular interaction, mobility, packing or diffusion behaviour.

### Level 3 — Engineering conclusion

Example: a particular material is acceptable for a defined pressure/temperature/fluid/lifetime service.

The rule for the rest of Chapter 014 is simple:

> **Never jump directly from Level 1 to Level 3.**

The investigations that follow build the chemistry needed to make Level 1 accurate and Level 2 useful. The rest of PPE-BoK provides the evidence systems needed to reach Level 3.

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

If the chapter is discussing a neutral organic molecule such as ethylene, **molecule** is appropriate.

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

Investigation 4 establishes the primary-bonding models. Investigation 5 will deal with interactions between molecular entities and polymer chains that are not the covalent backbone bonds themselves.

## 4.1 Covalent bonding: shared electron density between nuclei

IUPAC defines a **covalent bond** in terms of a region of relatively high electron density between nuclei that arises at least partly from electron sharing and produces an attractive force and characteristic internuclear distance. [S014-003]

For polymer engineering, this is the key model behind the bonds that build many organic polymer backbones and side groups.

The useful engineering statement is not “covalent bonds make polymers strong.” It is more precise:

> Covalent bonding establishes the chemical connectivity of the polymer molecule or network.

That connectivity determines which atoms belong to the same molecular structure and which bond rotations, geometries and reaction pathways are possible. Later chapters then add molecular weight, branching, crosslinking, morphology and other factors that govern how a population of those molecules behaves as a material.

### What covalent bonding does not establish by itself

Knowing that a backbone is covalently bonded does not directly establish:

- tensile strength;
- elastic modulus;
- creep resistance;
- fracture toughness;
- melting or softening temperature;
- permeability;
- chemical compatibility;
- pressure rating.

Those are higher-level material and product questions.

## 4.2 Ionic bonding: electrostatic attraction, but not a perfectly separate universe

IUPAC describes an **ionic bond** in strict terms as electrostatic attraction between the charges of a cation and an anion. It also makes a particularly important qualification: in practice it is preferable to consider the **amount of ionic character** rather than forcing bonds into purely ionic or purely covalent categories. [S014-003]

This matters because introductory diagrams often imply a sharp boundary:

`electron shared → covalent`

`electron transferred → ionic`

Real bonding can contain mixed character. The binary picture is a useful teaching limit, not a complete description of every solid or chemical bond.

### Engineering consequence of the continuum

When a material or chemical species is described as “ionic,” the engineer should ask what is actually meant:

- Are discrete ions present in a fluid?
- Is an ionic crystal or salt being described?
- Is the statement really about significant ionic character in a bond?
- Is the issue chemical interaction with a polymer rather than the bonding inside the polymer itself?

These are different engineering contexts.

The chapter therefore avoids using “ionic” as a shortcut for a fixed set of mechanical properties.

## 4.3 Metallic bonding: use verified electron delocalization rather than a cartoon

For the current authoring pass, Chapter 014 does not rely on an invented stand-alone IUPAC definition of “metallic bond.” Instead, it uses IUPAC's current definition of **delocalization of electrons**.

IUPAC notes that a delocalized electron is not associated with one particular atom or one particular covalent bond, but occupies an extended orbital over several atoms or an entire lattice; extensive electron delocalization is typical of metals. [S014-003]

That gives the engineering model we need:

> In a metallic solid, bonding cannot be represented adequately as a collection of isolated two-atom covalent bonds. Electron density is extended through the structure.

The familiar phrase “sea of electrons” can be a teaching analogy, but it should not be mistaken for a complete electronic-structure model.

### What this does and does not explain

Extended electron delocalization helps explain why metallic bonding must be treated differently from localized molecular bonding. It is also relevant to electronic behaviour.

It does **not**, by itself, prove that a particular metal is ductile, strong, corrosion resistant or suitable for a piping interface. Alloy composition, crystal structure, phases, defects, grain structure, heat treatment, temperature and environment all remain relevant.

## 4.4 Material classes are not bond labels

A useful materials-science orientation is to compare polymers, metals and ceramics. But the comparison must be made at the correct level.

### Polymers

Many polymer molecules are built from covalent bonds along the backbone and side groups. The bulk polymer, however, is not held together only by one type of interaction. Intermolecular interactions, chain entanglement, molecular architecture and morphology become essential to macroscopic behaviour.

Investigation 5 owns the intermolecular-interaction layer; Chapters 016–020 own the larger chain/morphology/time/failure consequences.

### Metals

Metals are usefully distinguished by extended electron delocalization through the lattice. That is a bonding/electronic-structure distinction.

It is not a complete mechanical model of a metal.

### Ceramics and inorganic solids

Many ceramic and inorganic solids contain substantial ionic and/or covalent bonding character. Treating “ceramic” as synonymous with “purely ionic” is therefore unsafe.

Chapter 014 does not attempt to derive ceramic fracture mechanics or metal plasticity from bonding alone. Those would require a proper materials-science treatment beyond this chapter's purpose.

### The engineering lesson

> Bonding helps explain why material classes require different physical models, but material class and bond type are not interchangeable labels.

## 4.5 Bond polarity is not the same question as bond category

Investigation 3 introduced electronegativity and uneven electron distribution. Investigation 4 now needs one more distinction:

- **bond category/model** asks how the stabilizing interaction is represented;
- **bond polarity / ionic character** asks how unevenly electron density or charge character is distributed.

A covalent bond can be polar. A bond can have partial ionic character. Therefore, “polar covalent” is not a contradiction, and the covalent/ionic distinction should not be treated as a simple on/off switch.

This becomes important when the chapter later discusses C–H, C–F, C–Cl and other bonds in polymer structures.

## 4.6 TAB-014-001 — Primary bonding models and engineering relevance

| Bonding model / descriptor | Electron / charge picture | Useful engineering interpretation | What must **not** be concluded directly |
|---|---|---|---|
| Covalent bonding | Relatively high electron density between nuclei arising at least partly from sharing | Establishes chemical connectivity and local molecular structure | Bulk strength, creep, fracture, pressure rating or service temperature |
| Ionic character / ionic bonding | Electrostatic attraction between charged species; real bonds may contain varying ionic character | Helps interpret ions, salts and mixed bond character | A fixed mechanical-property set or universal chemical-compatibility rule |
| Extended electron delocalization typical of metals | Electrons occupy states/orbitals extended over many atoms or the lattice | Distinguishes metallic electronic/bonding structure from localized molecular bonding | Ductility, strength, corrosion resistance or interface suitability without material evidence |

**Table rule:** `TAB-014-001` is not yet complete. Investigation 5 extends the chapter's bonding map with hydrogen bonding, dipole–dipole and London/dispersion interactions. Those are not silently merged into the primary-bond rows.

## 4.7 FIG-014-002 — Primary and secondary bonding map — partial placeholder

The final figure shall separate two levels visually:

**Level A — chemical connectivity / extended solid bonding**

- covalent bonding;
- ionic character / ionic bonding;
- extended electron delocalization typical of metallic solids.

**Level B — interactions between molecular entities / chain segments**

- hydrogen bonding;
- permanent-dipole interactions;
- London/dispersion interactions;
- other van der Waals interactions where relevant.

Investigation 5 completes the conceptual specification of Level B.

The figure must explicitly avoid ranking these interactions as though one universal energy scale determines all bulk polymer properties.

## 4.8 Why this distinction matters in plastic piping

A piping engineer may encounter statements such as:

- “PE has strong C–C bonds.”
- “PVDF is polar because of C–F bonding.”
- “A salt is ionic.”
- “Metal backing rings behave differently because metals have metallic bonding.”

Each statement may contain a useful chemical clue, but none is yet an engineering design conclusion.

The proper sequence is still:

`bonding description → structural/mechanistic implication → measured material response → qualification / application evidence → engineering decision`

The bonding description is strongest when used to choose the next question, not when used to skip the next question.

## 4.9 Common mistakes / Failure Lens

### Mistake 1 — “Every bond is either 100% ionic or 100% covalent”

Why it fails: IUPAC explicitly recommends considering degree of ionic character rather than forcing real bonds into pure end-member categories.

### Mistake 2 — “Polymer chains have covalent bonds, therefore polymers are mechanically strong in the same way as covalent solids”

Why it fails: intramolecular connectivity is only one structural level. Chain interactions, architecture, morphology, defects, time and temperature still control bulk response.

### Mistake 3 — “Ceramic means ionic”

Why it fails: many ceramic and inorganic solids contain mixed ionic/covalent character; the material class cannot be reduced to one bond label.

### Mistake 4 — “Metallic bonding means the metal will be ductile”

Why it fails: electron delocalization is part of the electronic/bonding picture, while ductility depends on crystal structure, defects, microstructure, temperature, strain rate and other material variables.

### Mistake 5 — “Bond polarity and bond type are the same classification”

Why it fails: polarity/ionic character can vary within bonding models; a covalent bond can be polar.

### Mistake 6 — “Primary bond strength ranks the service temperature of piping materials”

Why it fails: service temperature is a material/product/system property influenced by molecular mobility, morphology, degradation, load duration, qualification and the applicable standard.

## 4.10 Verification

Before accepting a primary-bonding explanation in Chapter 014, check:

1. Is the covalent-bond description consistent with current IUPAC terminology?
2. Has ionic bonding been treated as a continuum of ionic character rather than an absolute binary where inappropriate?
3. If metallic behaviour is discussed, is the chapter using verified electron-delocalization language rather than inventing a formal definition?
4. Has any bulk property been presented as a direct consequence of a single bond label?
5. Are polymer intrachain covalent bonding and interchain interactions kept as separate structural levels?
6. Are ceramics and metals used only as bounded comparison classes rather than simplified stereotypes?
7. Does the wording route property magnitude and design acceptance to measured/qualified evidence?

## 4.11 Engineering decision from Investigation 4

> Use covalent, ionic-character and extended-electron-delocalization models to describe **how a structure is chemically/electronically stabilized**. Do not use a bond label as a substitute for a bulk-material model or a piping qualification decision.

The engineer should now retain four distinctions:

1. covalent bonding establishes localized chemical connectivity through shared electron density;
2. ionic character exists on a continuum, even though the ideal ionic model is electrostatic attraction between cations and anions;
3. metals require an extended-electron/delocalized-lattice model rather than only localized two-atom bonds;
4. bulk properties emerge from bonding **plus** higher structural levels.

That leaves a critical polymer question unanswered:

> If the atoms within a polymer chain are covalently bonded, **what holds neighbouring chains or molecular entities near one another?**

That is the subject of Investigation 5.

---

# Investigation 5 — What Holds Polymer Molecules Together When They Are Not Covalently Bonded to Each Other?

Polymer chains are not isolated objects floating independently through a solid. Neighbouring chains and chain segments interact continuously through electrostatic and quantum-mechanical interactions that do **not** require new covalent bonds between every pair of segments.

These interactions matter because a polymer's bulk response depends not only on the covalent connectivity inside each chain, but also on how chains and segments attract, repel, orient, pack and move relative to one another.

The engineering challenge is that the vocabulary is often taught as a misleading ladder:

`London < dipole–dipole < hydrogen bond < covalent bond`

That ranking may be convenient for a classroom mnemonic, but it is not a safe polymer-engineering model. Real behaviour depends on distance, orientation, number and distribution of interacting sites, polarizability, molecular geometry, chain architecture, morphology, temperature and the property being measured.

Chapter 014 therefore uses the following rule:

> Identify the **interaction mechanism** first. Do not turn the interaction label into a universal ranking of bulk polymer properties.

## 5.1 Intramolecular versus intermolecular: keep the structural levels separate

The first distinction is positional rather than energetic.

- **Intramolecular** interactions occur within one molecular entity.
- **Intermolecular** interactions occur between different molecular entities.

For polymers, the distinction can become visually confusing because one chain may be extremely long and may fold back near itself. The same physical type of noncovalent interaction may therefore occur between segments of different chains or between separated segments of the same chain.

IUPAC's definition of van der Waals forces explicitly allows such forces between molecular entities **or between groups within the same molecular entity**. [S014-003]

The engineering point is:

> “Intermolecular force” is useful shorthand in polymer discussions, but the actual interaction may be segment-to-segment, and the chain identity of the two segments does not by itself determine the physics.

## 5.2 van der Waals forces: an umbrella, not one additional force

IUPAC uses **van der Waals forces** as an umbrella term for attractive or repulsive interactions between molecular entities, excluding bond formation and the direct electrostatic interactions of ionic groups. The term includes:

- dipole–dipole interactions;
- dipole-induced dipole interactions;
- London / dispersion forces. [S014-003]

This resolves a common terminology error.

The list:

`dipole–dipole + London + van der Waals`

incorrectly suggests that van der Waals is a separate fourth mechanism to add on top of the others. In the terminology used here, **van der Waals is the broader family name** that includes those mechanisms.

### Engineering implication

When a datasheet, textbook or failure discussion says only “van der Waals forces,” the phrase is not specific enough to identify which component of the interaction is important. The engineer should ask whether the reasoning concerns permanent dipoles, induced dipoles, dispersion/polarizability, or simply a nonspecific noncovalent attraction.

## 5.3 Dipole–dipole interaction: permanent charge separation meets orientation

A polar bond can contribute to a permanent molecular dipole, but a bond dipole and a whole-molecule dipole are not the same thing. Molecular geometry can reinforce or cancel individual bond contributions.

When molecular entities possess permanent dipoles, **dipole–dipole interactions** depend on the electrostatic interaction between those dipoles and on their relative separation and orientation. [S014-003]

This orientation dependence is important for polymers because repeat-unit chemistry alone does not tell the engineer how all chain segments will orient in the real material.

### What the engineer may infer

A structure containing polar bonds or a permanent dipole can justify asking whether permanent-dipole interactions contribute materially to segment interactions.

### What the engineer may not infer directly

The presence of a permanent dipole does not by itself establish:

- elastic modulus;
- glass-transition or melting temperature;
- creep resistance;
- chemical compatibility;
- solvent uptake;
- permeability;
- fusion temperature;
- pressure capability.

Those quantities require the actual polymer structure, morphology, formulation and measured evidence.

## 5.4 Dipole-induced dipole interaction: one entity polarizes another

A permanent dipole can distort the electron distribution of a neighbouring entity and create an **induced dipole**. The resulting interaction is classified by IUPAC within the van der Waals family as dipole-induced dipole interaction. [S014-003]

The mechanism highlights another useful engineering descriptor: **polarizability** — how readily an electron distribution can be distorted by an electric field or neighbouring charge distribution.

For Chapter 014, polarizability is used qualitatively. It is not converted into a polymer property without direct evidence.

The important lesson is that an entity does not need to carry a permanent dipole before it can participate in an electrostatically induced interaction.

## 5.5 London / dispersion forces: present even when permanent polarity is absent

IUPAC defines **London forces**, also called **dispersion forces**, as attractive interactions associated with mutual polarizability. They are important between apolar molecules and are also components of the interaction between polar molecules. [S014-003]

That last clause prevents a common error:

> London forces are **not** switched off when a molecule is polar.

A polar polymer can have permanent-dipole interactions **and** dispersion contributions at the same time.

Likewise, a polymer that lacks a strong permanent dipole is not interaction-free. Fluctuating electron distributions and mutual polarizability still create dispersion attraction.

### Engineering significance

London/dispersion forces help explain why nominally nonpolar molecular structures can still condense, pack and interact.

But the chapter does not convert “more dispersion” into a universal claim of higher stiffness, higher melting temperature or lower permeability. Those outcomes depend on the complete molecular and morphological system.

## 5.6 Hydrogen bonding: a specific interaction with its own evidence criteria

Hydrogen bonding deserves separate treatment because it is frequently reduced to the phrase “a strong dipole–dipole force.” That description is too crude for a professional reference.

The 2011 IUPAC Recommendation defines a hydrogen bond as an attractive interaction involving a hydrogen atom bound to a more electronegative atom or group and an interacting atom or group in the same or another molecular entity, where there is evidence of bond formation character. The Recommendation is accompanied by experimental and theoretical criteria used to support identification of a hydrogen bond. [S014-004]

The companion IUPAC Technical Report explains the rationale, evidence base and broader historical treatment. [S014-005]

### Why this matters to Chapter 014

Hydrogen bonding is therefore not identified merely because a drawing contains hydrogen near an electronegative atom. The structural arrangement must support the interaction, and the formal IUPAC treatment is evidence-based rather than a simple distance-only cartoon.

For engineering reasoning, the safe sequence is:

`possible donor/acceptor chemistry → geometrically possible interaction → evidence that hydrogen bonding is relevant → measured material consequence`

not:

`contains O/N/F → hydrogen-bonded polymer → known bulk property`

### Do not confuse hydrogen bonding with a new covalent backbone bond

Hydrogen bonding can include contributions that are not purely classical electrostatics, which is one reason IUPAC treats it carefully. It still must not be represented in the chapter as though every hydrogen bond were simply another permanent covalent link in the polymer backbone.

If actual covalent crosslinking occurs, that is a different structural level and belongs mainly to Chapter 016.

## 5.7 One polymer can contain several interaction mechanisms at once

The interaction map is **additive and overlapping**, not a set of mutually exclusive boxes.

A molecular system can simultaneously exhibit:

- covalent bonds within its chemical structure;
- polar covalent bonds;
- permanent-dipole interactions;
- dipole-induced dipole interactions;
- London/dispersion interactions;
- hydrogen bonding where the required chemistry and geometry exist.

The presence of one mechanism does not cancel the others.

This is why the question “Which force holds this polymer together?” is usually too simple. A better question is:

> **Which interaction mechanisms are present, how are they distributed through the actual chain/morphology, and which measured property are we trying to explain?**

That question routes the engineer toward the correct evidence instead of toward a one-word answer.

## 5.8 TAB-014-001 — Bonding and interaction map, continuation

| Interaction model / descriptor | Physical picture | Useful engineering interpretation | What must **not** be concluded directly |
|---|---|---|---|
| van der Waals forces | Umbrella family including dipole–dipole, dipole-induced dipole and London/dispersion interactions | Signals non-bond-forming interactions between molecular entities or separated groups | Treating “van der Waals” as one extra force to add separately to its included components |
| Dipole–dipole interaction | Interaction between permanent dipoles; depends on separation and orientation | Helps explain why permanent molecular polarity can contribute to segment interaction | Bulk modulus, compatibility, permeability or service temperature from dipole presence alone |
| Dipole-induced dipole interaction | A permanent dipole distorts a neighbouring electron distribution, inducing a dipole | Connects permanent polarity to neighbour polarizability | A quantitative material property without measured evidence |
| London / dispersion forces | Attraction arising from mutual polarizability and fluctuating/induced electron distributions | Explains attraction even in apolar systems and contributes also in polar systems | Assuming dispersion exists only in nonpolar polymers or ranking bulk properties from it alone |
| Hydrogen bonding | Specific attractive interaction involving H bound to an electronegative atom/group and an interacting partner, supported by structural/evidence criteria | Identifies a potentially important directional noncovalent interaction | Treating every O/N/F-containing polymer as automatically hydrogen-bonded or using H-bond presence as a design value |

**Table rule:** the table separates **chemical connectivity / primary-bonding models** from **noncovalent interaction mechanisms**. It does not rank them on one universal “strength” axis.

## 5.9 FIG-014-002 — Primary and secondary bonding map — conceptual specification complete

The final graphic shall contain two visually separated layers.

### Level A — chemical connectivity / extended solid bonding

- covalent connectivity;
- ionic character / ionic bonding;
- extended electron delocalization typical of metallic solids.

### Level B — noncovalent interactions between entities or chain segments

A parent box labeled **van der Waals family** contains:

- dipole–dipole;
- dipole-induced dipole;
- London / dispersion.

A separate adjacent box shows **hydrogen bonding**, with a note that its identification follows the IUPAC 2011 evidence-based definition and is not reduced to a generic dipole label.

The figure shall include three explicit warnings:

1. interaction mechanisms can coexist;
2. London/dispersion contributions also occur in polar systems;
3. the map is **not** a bulk-property ranking.

Graphic production remains a later asset task; the scientific content/specification is now defined.

## 5.10 Why interaction labels do not directly predict polymer properties

Intermolecular and intersegment interactions can affect the energetic landscape for chain packing and motion. That makes them scientifically relevant to thermal, mechanical, transport and joining behaviour.

But the actual bulk response depends on more than the existence of an interaction site.

At minimum, the engineer may need to consider:

- number and distribution of interaction sites;
- molecular geometry;
- distance and orientation;
- polarizability;
- chain flexibility and architecture;
- molecular weight and entanglement;
- crystalline/amorphous morphology;
- temperature and time scale;
- additives, plasticizers, fillers or absorbed species;
- processing history.

Those variables explain why the sentence “polymer A has stronger intermolecular forces than polymer B” is usually too vague to support an engineering decision.

The correct next step is to name the **specific measured property** and seek evidence at that level.

## 5.11 Common mistakes / Failure Lens

### Mistake 1 — “van der Waals” is a separate force added on top of London and dipole–dipole

Why it fails: IUPAC uses van der Waals as the umbrella that includes dipole–dipole, dipole-induced dipole and London forces.

### Mistake 2 — “London forces exist only in nonpolar molecules”

Why it fails: IUPAC explicitly notes that London/dispersion forces are also components of the interactions between polar molecules.

### Mistake 3 — “Hydrogen bond = very strong dipole–dipole force”

Why it fails: the IUPAC 2011 treatment uses a dedicated definition and evidence criteria and does not reduce hydrogen bonding to one simplistic electrostatic label.

### Mistake 4 — “If a repeat unit is polar, the polymer must have a known high stiffness or high melting point”

Why it fails: polarity is one descriptor among many; architecture, morphology, orientation, temperature and the measured property still matter.

### Mistake 5 — “A nonpolar polymer has no intermolecular attraction”

Why it fails: dispersion interactions remain present through mutual polarizability.

### Mistake 6 — “One interaction type determines chemical compatibility”

Why it fails: compatibility is an exposure-dependent material response involving chemistry, morphology, concentration, temperature, stress and time.

### Mistake 7 — “Hydrogen bonding means covalent crosslinking”

Why it fails: hydrogen bonding is a noncovalent interaction; covalent crosslinking changes chemical connectivity and is a different structural mechanism.

## 5.12 Verification

Before accepting an intermolecular-interaction explanation in Chapter 014, check:

1. Is `van der Waals` being used as an umbrella term consistently with IUPAC rather than as a duplicate category?
2. Are London/dispersion forces allowed to coexist with permanent-dipole interactions?
3. Is dipole–dipole reasoning kept dependent on actual molecular dipole and orientation rather than bond polarity alone?
4. Is hydrogen bonding identified using the IUPAC 2011 framework rather than a proximity cartoon alone?
5. Has the text avoided a one-dimensional “force strength” ladder as a predictor of bulk polymer behaviour?
6. If a bulk property is mentioned, has the statement remained a mechanism hypothesis rather than an unsupported magnitude or ranking?
7. Are chain architecture and morphology routed to Chapters 016–017 instead of being silently collapsed into intermolecular-force language?

## 5.13 Engineering decision from Investigation 5

> Polymer chains and chain segments can interact through several overlapping noncovalent mechanisms. Use the interaction map to identify **what physical mechanism is plausible**, then move to the measured property and material-specific evidence before making an engineering conclusion.

The engineer should now retain five distinctions:

1. covalent bonds define much of the polymer's chemical connectivity, while noncovalent interactions act between nearby entities or segments;
2. van der Waals is an umbrella family, not an extra force separate from dipole/dispersion components;
3. permanent dipoles, induced dipoles and London/dispersion contributions can coexist;
4. hydrogen bonding has a specific evidence-based IUPAC definition and is not merely shorthand for “strong polarity”;
5. no interaction label directly supplies stiffness, thermal capability, permeability, compatibility or pressure rating.

With the noncovalent interaction layer established, the next question moves from **how molecules interact** to **why carbon can build the enormous structural variety of polymer backbones in the first place**.

That is the subject of Investigation 6.

---

# Investigation 6 — Why Is Carbon Uniquely Useful for Polymer Backbones?

Carbon is the structural center of most organic polymers used in engineering, but the explanation is often reduced to one sentence: “carbon has four bonds.” That is a useful starting point and an incomplete answer.

IUPAC organic nomenclature assigns carbon a **standard bonding number of four**. The same table assigns standard bonding number four to other Group 14 elements such as silicon, so tetravalency alone cannot explain why carbon chemistry supports such extraordinary structural diversity. [S014-006]

For Chapter 014, the useful engineering explanation is the combination of:

- carbon's standard four-bond connectivity;
- carbon–carbon covalent connectivity;
- the ability to form linear, branched and cyclic carbon skeletons;
- the ability to participate in different bond orders;
- substitution of hydrogen by other atoms or groups;
- the resulting freedom to build many different local chemical environments along a molecular skeleton.

The purpose here is to understand **structural possibility**, not yet hybridization, polymerization, chain architecture or bulk material performance.

## 6.1 Tetravalency: what “carbon forms four bonds” should mean

In the IUPAC Blue Book framework, the standard bonding number of neutral carbon in ordinary organic skeletal structures is four. [S014-006]

For an engineer, that means carbon can satisfy four bonding equivalents in many constitutional arrangements.

This statement should not be anthropomorphized as:

> “Carbon wants four bonds.”

Atoms do not make engineering choices. The four-bond rule is a useful structural/electron-counting description of common carbon chemistry.

### Examples of different connectivity with the same bonding-number framework

A carbon atom can appear in structures where its bonding equivalents are distributed among:

- four single-bond connections;
- one double bond plus two single-bond connections;
- one triple bond plus one single-bond connection;
- two double-bond connections in appropriate structures.

Investigation 7 will explain the `sp`, `sp2`, `sp3`, sigma and pi models behind those differences. Investigation 6 uses only the constitutional fact that different bond-order patterns are possible.

### Engineering boundary

Standard bonding number four does not directly establish:

- molecular flexibility;
- chain packing;
- crystallinity;
- transition temperature;
- chemical resistance;
- crack resistance;
- pressure rating.

Those require the actual structure and higher-level evidence.

## 6.2 Carbon–carbon connectivity creates a framework, not a material property

Carbon can bond covalently to other carbon atoms. Repeating C–C connectivity makes it possible to construct extended molecular skeletons.

This is the structural bridge from small organic molecules to the large carbon-containing molecular frameworks encountered in polymer science.

The important word is **framework**.

A carbon skeleton tells the engineer which atoms are constitutionally connected. It does not yet tell the engineer how long the polymer chain is, how the chain population is distributed in molecular weight, how much branching exists in a real polymer grade, whether the material is crystalline, or what additives are present.

Those questions belong mainly to Chapters 015–017 and the later material-family chapters.

## 6.3 Linear chains, branches and rings are structural possibilities

IUPAC polymer terminology defines a **chain** as a linear or branched sequence of constitutional units between selected boundary units and notes that a cyclic macromolecule may also be regarded as a chain. [S014-003]

A **branched chain** contains at least one branch point between its boundary units. [S014-003]

Organic chemistry also includes **carbocyclic** structures in which the members of a ring are carbon atoms. [S014-003]

Together, these ideas show that carbon connectivity is not restricted to one straight line.

At the molecular-structure level, carbon can participate in:

- unbranched sequences;
- branched sequences;
- rings;
- side chains attached to a main skeleton;
- combinations of cyclic and acyclic features.

### Critical ownership boundary

Investigation 6 is **not** the chapter on polymer branching.

The existence of branch points as a chemical possibility is introduced here. The engineering consequences of molecular-weight distribution, short/long-chain branching, crosslinking and chain architecture belong to Chapter 016.

This prevents a structural drawing from silently becoming a statement about a commercial polymer grade.

## 6.4 Saturated and unsaturated carbon frameworks: recognize the distinction, defer the orbital explanation

Carbon skeletons can contain different carbon–carbon bond orders.

For example, IUPAC defines alkanes as acyclic branched or unbranched hydrocarbons built from saturated carbon atoms, while organic nomenclature separately recognizes structures containing carbon–carbon double or triple bonds. [S014-003]

For Chapter 014, the immediate engineering lesson is simply:

> A single bond and a multiple bond are not constitutionally equivalent features.

They differ in bond order and later will differ in geometry and rotational freedom.

But the reason is intentionally deferred:

- hybridization → Investigation 7;
- sigma / pi bonding → Investigation 7;
- why ethylene's C=C matters to polymerization → Investigation 8 and Chapter 015.

Investigation 6 should make the engineer notice the bond-order difference without pre-empting the mechanism.

## 6.5 Carbon skeleton does not mean hydrocarbon-only polymer

A carbon framework can carry atoms or groups other than hydrogen.

This matters immediately for piping polymers because the structural formula may include elements such as:

- fluorine;
- chlorine;
- oxygen;
- nitrogen;
- other heteroatoms or functional groups where relevant.

Replacing a hydrogen or carbon-containing substituent changes local bonding, electron distribution, mass, steric environment and possible intermolecular interactions.

That makes substitution chemically meaningful.

It does **not** justify a direct material ranking. For example, the presence of fluorine or chlorine in a repeat-unit structure is a chemistry fact; chemical resistance, permeability or allowable temperature remain measured/qualified material properties.

## 6.6 How to read a skeletal / bond-line formula

IUPAC defines a **skeletal formula**, also called a bond-line formula, as a two-dimensional representation in which lines show bonds, vertices represent ordinary carbon atoms, attached hydrogens on those carbon atoms are omitted, and other atoms are shown by their element symbols. [S014-003]

This representation is exceptionally useful for engineers because it strips away repetitive C/H labels and makes **connectivity** visible.

### Practical reading rules

When reading a skeletal formula:

1. **Each unlabeled vertex or line end is normally carbon** under the convention.
2. **Lines are bonds.** Multiple parallel lines indicate higher bond order.
3. **Hydrogens attached to ordinary carbon vertices are usually implicit.** Infer only the number needed to satisfy the standard bonding pattern represented.
4. **Heteroatoms are written explicitly.** Their presence is therefore visually important.
5. **Do not confuse a two-dimensional drawing with the three-dimensional molecular geometry.** Investigation 7 owns that next step.

### Why this matters in PPE-BoK

A piping engineer who can read a bond-line structure can rapidly identify:

- carbon skeleton connectivity;
- branch points in a simple molecular drawing;
- rings;
- double/triple bonds;
- heteroatoms;
- candidate polar bonds or interaction sites requiring later analysis.

That is enough to support mechanism questions without requiring full organic-nomenclature training.

## 6.7 Skeletal formula versus polymer skeletal structure

A terminology distinction is useful here.

IUPAC's **skeletal formula** is a drawing convention for a molecular entity. IUPAC polymer terminology also uses **skeletal structure** for the sequence of atoms in the constitutional units of a macromolecule or chain that defines its essential topological representation. [S014-003]

The phrases sound similar but answer different questions:

- **skeletal formula** — how a structure is drawn;
- **skeletal structure** — which atoms form the essential molecular skeleton/topology.

Chapter 014 uses the drawing convention to help the engineer see the polymer-relevant skeleton without pretending the drawing contains every aspect of the real macromolecule.

## 6.8 From carbon versatility to polymer diversity — the bounded inference

Carbon's structural versatility makes many molecular architectures chemically possible.

A change in carbon skeleton, substituent, heteroatom or bond order can change:

- the local electron distribution;
- possible intermolecular interactions;
- local geometry;
- possible rotational constraints;
- the chemical reactions available to the molecular structure.

Those are legitimate **mechanism-level** consequences.

The next step — claiming a specific modulus, transition temperature, diffusion coefficient, chemical resistance or fracture response — requires material-specific evidence.

This is the same chapter-wide discipline in a new form:

`carbon structural feature → molecular mechanism hypothesis → measured property → qualification → engineering decision`

## 6.9 TAB-014-002 — Carbon structural feature → mechanism question → evidence boundary

| Structural feature visible in a formula | Immediate chemistry question | Plausible mechanism level | What cannot be concluded directly |
|---|---|---|---|
| Linear C–C skeleton | How is the backbone connected and what rotations/geometries are possible? | Molecular connectivity / local mobility hypothesis | Actual chain architecture, crystallinity, modulus or creep |
| Branch point in a simple structure | Which atom/group departs from the selected main path? | Topological/constitutional difference | Branching distribution or properties of a commercial polymer grade |
| Carbon ring | How does cyclic connectivity constrain the local skeleton? | Geometry / conformational hypothesis | Stiffness or service temperature without material evidence |
| C=C or C≡C | What changes when bond order increases? | Geometry / rotation / reactivity hypothesis | Polymerization mechanism or bulk property; see Investigations 7–8 |
| Heteroatom / substituent | How does the new atom/group alter polarity, size or interaction possibilities? | Electron-distribution / interaction hypothesis | Compatibility, permeability or thermal capability without testing/qualification |

**Table rule:** `TAB-014-002` is an inference-control tool. Its right-hand column is as important as its mechanism column.

## 6.10 Common mistakes / Failure Lens

### Mistake 1 — “Carbon is special only because it has valence four”

Why it fails: IUPAC's standard bonding-number table gives four to other Group 14 elements as well. Tetravalency is part of the explanation, not the entire explanation.

### Mistake 2 — “A branch drawn in one molecule tells me the branching of the commercial polymer”

Why it fails: a structural possibility is not a measured chain-architecture distribution. Chapter 016 owns that engineering layer.

### Mistake 3 — “A bond-line drawing is the real 3D shape of the molecule”

Why it fails: skeletal formulas are two-dimensional connectivity representations. Three-dimensional geometry requires the bonding/orbital treatment of Investigation 7.

### Mistake 4 — “Carbon skeleton means the polymer contains only carbon and hydrogen”

Why it fails: many polymer structures contain heteroatoms or substituted carbon skeletons.

### Mistake 5 — “A double bond just means two single bonds drawn together”

Why it fails: multiple bond order changes the bonding model, geometry and rotation constraints. Investigation 7 explains the sigma/pi distinction.

### Mistake 6 — “Knowing the repeat-unit skeleton gives the material properties”

Why it fails: molecular weight, architecture, morphology, formulation, processing and qualification remain missing.

## 6.11 Verification

Before accepting a carbon-chemistry explanation in Chapter 014, check:

1. Is carbon's standard bonding number four stated as a structural/electron-counting convention rather than anthropomorphic intent?
2. Has the text avoided claiming tetravalency alone explains carbon's importance?
3. Are chains, branches and rings introduced only as structural possibilities without pre-empting Chapter 016?
4. Are multiple bonds recognized without prematurely teaching the hybridization/sigma/pi mechanism owned by Investigation 7?
5. Is the skeletal-formula convention being used correctly for implicit carbon/hydrogen and explicit heteroatoms?
6. Has any structure→bulk-property jump been stopped at the mechanism/evidence boundary?
7. Does the explanation distinguish a drawing convention from actual three-dimensional geometry and real polymer morphology?

## 6.12 Engineering decision from Investigation 6

> Carbon is exceptionally useful in polymer chemistry because its ordinary four-bond connectivity can be arranged into diverse carbon frameworks — including chains, branches, rings, multiple-bond patterns and substituted structures. This structural versatility creates many possible molecular mechanisms, but it does not by itself determine a piping material's engineering properties.

After Investigation 6, the engineer should be able to look at a simple organic or polymer-relevant structural formula and identify:

- the carbon skeleton;
- branch points or rings;
- single versus multiple bonds;
- explicitly shown heteroatoms/substituents;
- the next mechanism question that must be asked.

The next missing capability is three-dimensional/electronic interpretation:

> **Why do single, double and triple bonded carbon centers adopt different bonding geometries, and what do `sp`, `sp2`, `sp3`, sigma and pi actually mean?**

That is the subject of Investigation 7.

---

# Investigation 7 — What Do sp, sp2, sp3, Sigma and Pi Bonds Mean to the Engineer?

A two-dimensional structural formula can show which atoms are connected, but it does not explain why the local geometry around carbon changes with bonding pattern or why a carbon–carbon double bond behaves differently from a carbon–carbon single bond.

The common organic-chemistry language for this bridge is **hybridization** together with **sigma (σ)** and **pi (π)** bonding.

These are useful models. They must not be mistaken for literal mechanical parts inside the molecule.

IUPAC defines hybridization as a linear combination of atomic orbitals on an atom and notes that hybrid orbitals are commonly used in organic chemistry to describe tetrahedral (`sp3`), trigonal (`sp2`) and digonal/linear (`sp`) atoms. [S014-003]

The chapter therefore uses hybridization as a controlled explanatory model for local bonding geometry and bond symmetry — not as a direct material-property classification.

## 7.1 Hybridization is a model of orbitals, not a physical mixing process

IUPAC defines a **hybrid orbital** as an atomic orbital derived by hybridization of atomic orbitals with different angular-momentum quantum numbers located at the same atom. [S014-003]

The common teaching language says that an `s` orbital and one or more `p` orbitals “mix” to produce hybrid orbitals. That language is acceptable only if the reader remembers what the formal model actually means: a mathematical linear combination used to represent bonding and geometry.

The safe Chapter 014 interpretation is:

> Hybridization is a model for constructing orbitals that are convenient for describing local bonding directions and geometry.

It is **not**:

- a photograph of orbitals physically blending like fluids;
- a standalone measurable bulk property of the polymer;
- a rule that every atom in every molecular environment must be described by one perfectly pure `sp`, `sp2` or `sp3` label.

The model is powerful because it organizes geometry. It is dangerous when the label is treated as the engineering conclusion.

## 7.2 `sp3`: the tetrahedral carbon model

In the common localized bonding model, carbon centers associated with four approximately tetrahedrally directed bonding domains are described using `sp3` hybrid orbitals.

IUPAC explicitly connects `sp3` hybridization with tetrahedral atoms. The ideal regular tetrahedral angle is approximately `109.5°` (more precisely about 109°28′ in the regular-tetrahedron reference used by IUPAC terminology). [S014-003]

### Engineering meaning

The important point is not memorizing 109.5°.

It is recognizing that an `sp3` carbon is **not planar**. Its four bonding directions extend in three dimensions.

This matters when an engineer reads a zig-zag skeletal drawing: the printed line drawing is a projection/representation of connectivity, not evidence that the carbon backbone is literally a flat two-dimensional zig-zag.

### Model boundary

Real bond angles can depart from the ideal tetrahedral value because of ring strain, substituents, electronic effects and molecular constraints. The ideal geometry is therefore a reference model, not a tolerance or property specification.

## 7.3 `sp2`: the trigonal-planar carbon model

IUPAC connects `sp2` hybridization with trigonal atoms. For the common trigonal-planar carbon representation, three bonding directions lie approximately in one plane and are separated by about `120°` in the idealized geometry. [S014-003]

The key engineering observation is **planarity at the local center**.

A carbon involved in a conventional carbon–carbon double-bond description is commonly treated as `sp2`-hybridized. Three `sp2` hybrid orbitals provide the local sigma-bonding framework, while one unhybridized `p` orbital remains available for the π component discussed below.

### Why this matters

Compared with a tetrahedral local carbon center, the trigonal-planar model changes:

- local geometry;
- orientation of substituents;
- the orbital arrangement available for multiple bonding;
- rotational constraints when a π interaction is present.

It still does **not** directly provide a polymer modulus, glass-transition temperature, crystallinity or pressure capability.

## 7.4 `sp`: the linear carbon model

IUPAC connects `sp` hybridization with digonal/linear atoms.

In the idealized carbon model, two principal sigma-bonding directions are collinear, corresponding to a local angle near `180°`. Two unhybridized `p` orbitals remain available for π bonding in structures such as a carbon–carbon triple bond.

For Chapter 014, `sp` is included mainly to complete the geometry/bond-order map. Most immediate piping-polymer examples in later Investigations will be dominated by `sp3` and `sp2` carbon chemistry.

The same evidence boundary applies: linear local geometry is a chemistry fact, not a macroscopic material property.

## 7.5 The `sp3 / sp2 / sp` map is local, not a polymer-wide label

A polymer or monomer can contain more than one local bonding environment.

Therefore statements such as:

> “This polymer is sp3.”

are usually too crude unless the speaker is explicitly referring to the relevant carbon centers in a simplified backbone model.

A molecular structure may contain:

- `sp3` carbon centers in saturated regions;
- `sp2` centers in double bonds or aromatic structures;
- `sp` centers in triple-bonded structures;
- heteroatoms whose bonding is not adequately communicated by copying the carbon labels without analysis.

The hybridization descriptor belongs to the **local atom/bonding environment**.

It should not be silently elevated to the level of a complete macromolecule, compound or pipe material.

## 7.6 Sigma and pi: symmetry language with a localized-bond engineering use

IUPAC's `sigma, pi` terminology carries an important caveat: the terms can be used rigorously for molecular orbitals based on symmetry and are also commonly used in a localized two-centre bond description. The chapter must keep those uses conceptually distinct. [S014-003]

At the localized organic-chemistry level useful here:

- a **σ bond** has electron density arranged with symmetry around the internuclear axis and no nodal plane containing that axis in the localized description;
- a **π bond** has a nodal plane containing the internuclear axis and electron density on opposite sides of that plane in the localized description. [S014-003]

### Why this is useful to an engineer

The model explains why a conventional double bond is not simply “two identical single bonds drawn next to each other.”

In the localized picture:

- a carbon–carbon single bond is represented primarily as one σ bond;
- a carbon–carbon double bond is represented as one σ component plus one π component;
- a carbon–carbon triple bond is represented as one σ component plus two mutually oriented π components.

This is the orbital-level reason bond order changes geometry and rotational behavior.

## 7.7 Rotation: replace the phrase “single bonds rotate freely” with a barrier model

A common textbook shortcut says:

> “Single bonds rotate freely; double bonds do not rotate.”

The first half is too absolute.

IUPAC defines a **rotational barrier** as the potential-energy barrier associated with changing torsion angle. IUPAC also restricts the phrase **free rotation** to cases where the barrier is low enough that different conformations are not perceptible on the experimental time scale. [S014-003]

So the correct engineering model is:

> Rotation about a formally single bond may permit conformational change, but it normally occurs on an energy landscape with a finite rotational barrier.

### Why a double bond is more constrained

In the localized σ/π model, rotation around the internuclear axis of a carbon–carbon double bond would disrupt the parallel alignment required for effective π overlap.

That creates a qualitatively different rotational constraint from an ordinary single σ bond.

The chapter intentionally does **not** attach one universal numerical rotation barrier to “single” or “double” bonds. Actual barriers depend on molecular context, substituents, conjugation, sterics and other factors.

### Polymer relevance

The local ability or inability to change torsion angle is one ingredient in chain conformational freedom.

It is not the whole polymer mobility problem. Real chain mobility also depends on:

- neighboring bond sequences;
- side groups;
- intermolecular interactions;
- chain architecture;
- morphology;
- temperature;
- time scale.

Those higher-level effects belong mainly to Chapters 016–019.

## 7.8 FIG-014-003 — Carbon hybridization and geometry — conceptual specification complete

The figure shall show three side-by-side idealized local carbon environments.

### Panel A — `sp3`

- four directed hybrid-orbital/bonding domains;
- tetrahedral geometry;
- ideal reference angle approximately `109.5°`;
- explicit label: **3D local geometry — not a flat skeletal drawing**.

### Panel B — `sp2`

- three `sp2` directions in one plane;
- ideal trigonal-planar spacing approximately `120°`;
- one unhybridized `p` orbital perpendicular to the plane;
- explicit label: **local model used for conventional C=C description**.

### Panel C — `sp`

- two collinear `sp` directions;
- ideal local angle approximately `180°`;
- two mutually perpendicular unhybridized `p` orbital directions;
- explicit label: **local model used for conventional C≡C description**.

### Figure warnings

The final graphic shall state:

1. these are idealized local models;
2. actual molecular geometry can deviate from ideal angles;
3. hybridization is an explanatory orbital model, not a bulk polymer property;
4. a molecule may contain multiple local hybridization environments.

Graphic production remains pending; the scientific specification is now defined.

## 7.9 FIG-014-004 — Sigma and pi bonding in ethylene — partial specification

Investigation 7 establishes the generic orbital concept. Investigation 8 will complete the ethylene-specific figure.

The figure shall eventually show:

- the C–C internuclear axis;
- the σ component along that axis;
- one unhybridized `p` orbital on each `sp2` carbon;
- side-by-side overlap producing the localized π description above/below the molecular plane;
- the nodal-plane concept;
- a rotation arrow crossed out or annotated to show that loss of `p`-orbital alignment would disrupt the π interaction.

The final figure must **not** imply that electrons travel in fixed loops or that the colored lobes are hard physical objects.

## 7.10 From local geometry to an engineering mechanism hypothesis

Hybridization and σ/π descriptions help an engineer identify local structural constraints.

For example, a change from a saturated single-bonded carbon framework to a region containing `sp2` centers can plausibly change:

- local geometry;
- torsional freedom;
- planarity;
- electron distribution;
- chemical reactivity pathways.

Those are mechanism-level statements.

The chapter does not allow the next unsupported leap:

`more sp2 carbon → stiffer / stronger / hotter-service pipe`

The actual material consequence depends on how much of the structure is affected, how the units are distributed, molecular weight, chain architecture, morphology, processing and the measured property of interest.

## 7.11 Common mistakes / Failure Lens

### Mistake 1 — “Hybrid orbitals are physical objects that literally mix”

Why it fails: IUPAC defines hybridization as a linear combination of atomic orbitals. The model is a representation of bonding/electron distribution.

### Mistake 2 — “sp3 means 109.5° exactly everywhere”

Why it fails: tetrahedral geometry is an idealized reference; real bond angles can deviate because of molecular environment and constraints.

### Mistake 3 — “sp2 means the whole polymer is planar”

Why it fails: `sp2` describes a local atom/bonding environment. A macromolecule can contain many local environments and higher-level conformations.

### Mistake 4 — “A double bond is two identical single bonds”

Why it fails: in the localized model a double bond contains σ and π components with different symmetry/orbital character.

### Mistake 5 — “Single bonds rotate with zero resistance”

Why it fails: IUPAC's rotational-barrier concept recognizes a finite energy landscape; `free rotation` is conditional on barrier and observation time scale.

### Mistake 6 — “Double bonds can never rotate under any circumstance”

Why it fails: the useful engineering statement is that the π component creates a substantial rotational constraint in the ordinary bonded state; reaction, excitation or bond-breaking pathways are different questions.

### Mistake 7 — “Hybridization predicts the pipe property”

Why it fails: hybridization is a local chemistry descriptor. Bulk behavior requires architecture, morphology, formulation, processing and material evidence.

### Mistake 8 — “σ and π always refer to one simple localized bond picture”

Why it fails: IUPAC notes rigorous molecular-orbital symmetry usage as well as localized bond usage. The context must be stated.

## 7.12 Verification

Before accepting a hybridization/σ–π explanation in Chapter 014, check:

1. Is hybridization described as a linear-combination/model concept rather than a literal physical mixing event?
2. Are `sp3`, `sp2` and `sp` tied to idealized local tetrahedral, trigonal and linear/digonal geometries?
3. Are numerical angles presented as ideal/reference values rather than tolerances or universal measured values?
4. Is the local hybridization descriptor kept separate from whole-polymer morphology or property claims?
5. Are σ and π uses clearly identified as localized-bond language where that model is being used?
6. Is rotation around a single bond described with a rotational barrier rather than as absolutely free?
7. Is double-bond rotational constraint linked to the π-overlap model without inventing a universal barrier value?
8. Has the text stopped before ethylene polymerization chemistry owned by Investigation 8 / Chapter 015?

## 7.13 Engineering decision from Investigation 7

> Use `sp3`, `sp2` and `sp` hybridization as idealized local orbital/geometry models, and use σ/π language to explain why single and multiple carbon–carbon bonds differ in symmetry and rotational constraint. These descriptors explain local molecular mechanisms; they do not directly determine bulk polymer or piping performance.

The engineer should now be able to interpret a simple carbon structure at three levels:

1. **connectivity** — which atoms are connected;
2. **local geometry/orbital model** — `sp3`, `sp2` or `sp` where appropriate;
3. **bond-component model** — σ only for the ordinary single-bond picture, σ+π for the ordinary double-bond picture, and σ+2π for the ordinary triple-bond picture.

The chapter can now apply this framework to the most important bridge molecule for polyethylene:

> **ethylene (ethene), with its carbon–carbon double bond.**

That is the subject of Investigation 8.

---

# Investigation 8 — What Is Special About Ethylene?

**Authoring state:** planned. Evidence research required before development.

---

# Investigation 9 — How Do Molecular Features Become Engineering-Property Hypotheses?

**Authoring state:** blocked pending direct primary-literature research for material-specific claims.

---

# Investigation 10 — What Can Chemistry Tell Us, and Where Must the Engineer Stop?

**Authoring state:** planned after Investigations 1–9.

---

# Chapter engineering assets — current register

| ID | Asset | Status |
|---|---|---|
| FIG-014-001 | Atom-to-material hierarchy | Placeholder integrated in Investigation 1; terminology boundary reinforced in Investigation 2 |
| FIG-014-002 | Primary and secondary bonding map | Scientific/conceptual specification complete through Investigation 5; graphic production pending |
| FIG-014-003 | Carbon hybridization and geometry | Scientific/conceptual specification complete in Investigation 7; graphic production pending |
| FIG-014-004 | Sigma and pi bonding in ethylene | Partial scientific specification integrated in Investigation 7; complete in Investigation 8 |
| FIG-014-005 | Ethylene to polyethylene bridge | Planned |
| FIG-014-006 | Molecular feature to engineering evidence chain | Concept introduced; figure planned |
| TAB-014-001 | Bonding types and engineering relevance | Primary-bonding + intermolecular-interaction rows integrated through Investigation 5 |
| TAB-014-002 | Molecular feature / mechanism / invalid direct conclusion | Initial carbon-structure inference table integrated in Investigation 6; extend in Investigation 9 |
| TAB-014-003 | Controlled polymer-structure examples | Planned |
| TAB-014-004 | Downstream chapter ownership crosswalk | Planned |
| EX-014-001 | Reading ethylene and PE repeat unit | Planned for Investigation 8 |
| EX-014-002 | Comparing two simple polymer structures | Planned |
| WF-014-001 | Chemical structure → evidence → decision boundary | Logic introduced; final asset planned |
| CL-014-001 | Before inferring engineering behaviour from chemical structure | Planned |

---

# Publication hold points

Chapter 014 is in Engineering Development. Publication closure is not implied by completion of an Investigation.

Before publication the chapter requires, as applicable:

- completion of all approved Investigations;
- direct evidence review for material-specific structure–property claims;
- scientific review of molecular drawings and terminology;
- current ISO/IUPAC terminology recheck;
- Technical Review;
- Standards/Evidence Validation;
- Editorial/Style Review;
- Desk Test;
- final author approval and merge.

# References

See `references.md` for the controlled Chapter 014 source and evidence plan.