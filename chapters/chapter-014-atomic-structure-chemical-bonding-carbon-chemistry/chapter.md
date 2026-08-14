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

**Authoring state:** planned. Evidence research required before development.

---

# Investigation 3 — Which Electrons Actually Control Chemical Bonding?

**Authoring state:** planned. Evidence research required before development.

---

# Investigation 4 — What Are Primary Bonds and Why Do Material Classes Differ?

**Authoring state:** planned.

---

# Investigation 5 — What Holds Polymer Molecules Together When They Are Not Covalently Bonded to Each Other?

**Authoring state:** planned.

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
| FIG-014-001 | Atom-to-material hierarchy | Placeholder integrated in Investigation 1 |
| FIG-014-002 | Primary and secondary bonding map | Planned |
| FIG-014-003 | Carbon hybridization and geometry | Planned |
| FIG-014-004 | Sigma and pi bonding in ethylene | Planned |
| FIG-014-005 | Ethylene to polyethylene bridge | Planned |
| FIG-014-006 | Molecular feature to engineering evidence chain | Concept introduced; figure planned |
| TAB-014-001 | Bonding types and engineering relevance | Planned |
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
