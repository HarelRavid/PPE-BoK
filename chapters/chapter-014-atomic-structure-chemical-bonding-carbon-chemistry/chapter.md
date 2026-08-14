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

**Table rule:** `TAB-014-001` is not yet complete. Investigation 5 will extend the chapter's bonding map with hydrogen bonding, dipole–dipole and London/dispersion interactions. Those are not to be silently merged into the primary-bond rows.

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

Investigation 5 will complete Level B.

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

**Authoring state:** planned. Evidence research required before development.

---

# Investigation 6 — Why Is Carbon Uniquely Useful for Polymer Backbones?

**Authoring state:** planned.

---

# Investigation 7 — What Do sp, sp2, sp3, Sigma and Pi Bonds Mean to the Engineer?

**Authoring state:** planned.

---

# Investigation 8 — What Is Special About Ethylene?

**Authoring state:** planned.

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
| FIG-014-002 | Primary and secondary bonding map | Partial placeholder integrated in Investigation 4; Level B completes in Investigation 5 |
| FIG-014-003 | Carbon hybridization and geometry | Planned |
| FIG-014-004 | Sigma and pi bonding in ethylene | Planned |
| FIG-014-005 | Ethylene to polyethylene bridge | Planned |
| FIG-014-006 | Molecular feature to engineering evidence chain | Concept introduced; figure planned |
| TAB-014-001 | Bonding types and engineering relevance | Primary-bonding rows integrated; extend in Investigation 5 |
| TAB-014-002 | Molecular feature / mechanism / invalid direct conclusion | Planned |
| TAB-014-003 | Controlled polymer-structure examples | Planned |
| TAB-014-004 | Downstream chapter ownership crosswalk | Planned |
| EX-014-001 | Reading ethylene and PE repeat unit | Planned |
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