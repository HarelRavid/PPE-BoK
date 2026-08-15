# Investigation 5 — How Does Step Polymerization Build Macromolecules, and What Distinguishes Additive from Condensative Step Growth?

**Authoring status:** controlled candidate  
**Evidence gate:** PASS for stable terminology/mechanism layer  
**Controlling current source:** S015-008 — IUPAC basic classification Recommendation published 2026  
**Canonical integration:** deferred to end-of-chapter integration

Investigation 4 followed one chain-polymerization family from radical generation through propagation and competing carrier fates. Step polymerization requires a different mental model.

The defining question is not:

> Where is the active chain end?

It is:

> **Which molecules can react with which other molecules as macromolecular growth proceeds?**

In **step polymerization**, growth occurs through reactions between monomer, oligomer or polymer molecules of any length. [S015-008]

That means the material can evolve through reactions such as:

`monomer + monomer`

`monomer + oligomer`

`oligomer + oligomer`

`oligomer + longer chain`

or other combinations allowed by the actual reactive functional groups.

There is no requirement that every growth event occur by adding one monomer to one persistent active site on a single growing chain.

## 5.1 The core growth notation

The classical IUPAC polyaddition and polycondensation definitions use a compact growth notation that remains useful under the 2026 hierarchy.

For additive step polymerization / polyaddition:

`P_x + P_y → P_(x+y)`

For condensative step polymerization / polycondensation:

`P_x + P_y → P_(x+y) + L`

where:

- `P_x` is a molecule/chain with degree of polymerization `x`;
- `P_y` is a molecule/chain with degree of polymerization `y`;
- `L` is a low-molar-mass by-product in the condensative case;
- both `x` and `y` can range across molecules of different degrees of polymerization. [Gold Book `P04720`; `P04722`]

The notation captures the key mechanism difference from chain polymerization:

> **Growth can occur through reactions between two species that are both already larger than monomer.**

## 5.2 Additive step polymerization = polyaddition

The current 2026 IUPAC classification uses **additive step polymerization** with **polyaddition** as a synonym. [S015-008]

The growth reactions combine molecules of different degrees of polymerization without the defining condensative low-molar-mass by-product.

This immediately prevents a common mistake:

`no low-molar-mass by-product` does **not** imply `chain polymerization`.

An additive step polymerization can proceed without a persistent chain carrier and without a chain-reaction propagation mechanism.

The process belongs to the step branch because molecules across the size distribution can react in growth steps.

## 5.3 Condensative step polymerization = polycondensation

The current hierarchy uses **condensative step polymerization** with **polycondensation** as a synonym. [S015-008]

The defining growth pattern is still step polymerization — reactions among molecules of different degrees of polymerization — but the growth reaction is condensative and forms a low-molar-mass by-product. [Gold Book `P04722`]

The by-product is therefore a qualifier of the growth reaction, not the top-level mechanism classifier.

This matters because Investigation 2 already established the counterexample:

**condensative chain polymerization also exists.**

So the presence of a small molecule such as water, alcohol or another low-molar-mass species is not enough to classify the polymerization as step polymerization.

## 5.4 Functionality: how many covalent connections can a monomer form?

Step-polymerization reasoning often depends on **functionality**.

IUPAC defines the functionality `f` of a monomer as the number of covalent bonds that a monomer molecule or monomeric unit can form with other reactants. [Gold Book `FT07505`]

The controlled IUPAC notes provide a useful architecture bridge:

- with `f = 2`, a linear-chain macromolecule or a macrocycle can be formed;
- with `f > 2`, a branch point can be formed, potentially leading to a branched macromolecule, network or micronetwork. [Gold Book `FT07505`]

Chapter 015 uses this only as a **formation possibility**.

It does not imply:

`f = 2 → guaranteed linear commercial resin`

or

`f > 2 → guaranteed network product`.

Actual architecture depends on which reactions occur, reaction extent, stoichiometric balance, side reactions, intramolecular reactions, processing history and other system-specific factors.

Detailed branching/network architecture remains Chapter 016 territory.

## 5.5 Functional groups are the reaction handles, but the final material is not defined by them alone

In step polymerization, reactive functional groups determine which molecules can connect through the polymer-forming reactions.

That makes the following upstream information engineering-relevant:

- monomer functionality;
- identity of complementary/reactive functional groups;
- feed proportions;
- reaction conversion/extent;
- side reactions;
- removal or retention of condensative by-products where relevant;
- conditions that affect which functional groups actually react.

These are **process-provenance variables**.

They can generate hypotheses about the molecular population, but they do not directly establish the final architecture or piping performance.

## 5.6 Why step polymerization does not have the same “propagating chain carrier” lifecycle

For the basic step-polymerization mechanism, growth is not organized around one chain carrier that is regenerated each time monomer adds.

Instead, reactive molecules throughout the population can participate in growth reactions.

This means the generic chain-polymerization sequence:

`initiation → propagation → termination / transfer`

is the wrong template to impose on a step polymerization.

A more appropriate conceptual picture is:

```text
reactive monomers
      │
      ├── monomer + monomer
      ├── monomer + oligomer
      ├── oligomer + oligomer
      ├── oligomer + polymer
      └── polymer + polymer
                │
                ▼
      evolving molecular population
```

The available reactions are constrained by functional groups and the actual chemistry, not by one universal sequence.

## 5.7 FIG-015-001 extension — mechanism class versus reaction character

Investigation 2 established the top-level classification figure. Investigation 5 supplies the step-polymerization detail panel.

The figure shall show:

```text
STEP POLYMERIZATION
│
├── Additive step polymerization (polyaddition)
│      P_x + P_y → P_(x+y)
│
└── Condensative step polymerization (polycondensation)
       P_x + P_y → P_(x+y) + L
```

A side annotation shall read:

> `x` and `y` are not restricted to monomer. Growth can involve molecules across the degree-of-polymerization distribution.

A second warning shall read:

> **By-product formation distinguishes additive from condensative growth; it does not distinguish step from chain polymerization.**

## 5.8 Why high molecular size is a population outcome, not one propagation sequence

In chain polymerization, an individual propagating chain can undergo many successive monomer-addition events while it retains propagation capability.

In step polymerization, molecular size increases through reactions among molecules across the population.

This changes the evidence question.

For a chain polymerization, an engineer may ask:

- how often did propagation compete with termination/transfer?

For a step polymerization, useful questions include:

- what reactive functionality was available?
- what fraction of the reactive groups actually reacted?
- were complementary functional groups supplied in the intended balance?
- were side reactions or intramolecular reactions significant?
- in condensative growth, was the reaction environment consistent with the required equilibrium/by-product handling?

These questions identify causal provenance. They do not by themselves produce a validated molar-mass distribution.

## 5.9 Why stoichiometry and reaction extent matter without using a premature Carothers equation

A step-polymerization system is sensitive to the availability of complementary reactive groups because growth requires molecules to find partners with usable functionality.

If reactive-group populations are materially unbalanced, or if a significant fraction of functional groups remain unreacted, the population of possible connections differs from an ideal fully reacted balanced system.

That statement is enough for Chapter 015's engineering purpose.

A classical Carothers-type relationship can quantify idealized degree-of-polymerization behavior under specific assumptions, but introducing it here would pull the chapter toward detailed molecular-weight architecture and requires explicit control of functionality, stoichiometry, reaction extent and ideality.

**Decision:** no Carothers equation is retained in Chapter 015 Investigation 5.

Instead, the chapter routes the question to:

`feed/functionality + reaction extent → architecture hypothesis → measured molar-mass / end-group / composition evidence → Chapter 016 interpretation`.

This preserves the chapter boundary and avoids turning an ideal synthesis equation into a commercial-resin predictor.

## 5.10 Additive versus condensative does not mean “better” versus “worse”

The two step-polymerization subclasses describe reaction character.

They do not create a quality hierarchy.

A condensative process is not inherently inferior because it forms a by-product.

An additive process is not inherently superior because all reacting atoms/groups are retained in the growing product.

The engineering questions remain:

- was the intended molecular population produced?
- was it characterized?
- was the compound/product qualified?
- is the product suitable for the application?

## 5.11 A step-polymerization provenance matrix

| Provenance input | Mechanism question | Evidence needed next | Invalid direct conclusion |
|---|---|---|---|
| Monomer functionality | How many connections can the monomer potentially form? | composition/end-group/architecture evidence | `f` alone proves final topology |
| Functional-group ratio | Are complementary reactive groups available in the intended balance? | feed record + chemical/molecular characterization | ratio alone predicts final molar mass |
| Reaction extent / conversion | How much reactive functionality actually reacted? | direct conversion/end-group/molecular evidence | high conversion alone proves product qualification |
| Condensative by-product handling | Does the reaction environment support the intended condensative growth? | process record + chemistry/molecular characterization | by-product removal alone proves target polymer |
| Side reactions | Are functional groups consumed by non-growth pathways? | mechanism + analytical evidence | nominal recipe equals actual connectivity |
| `f > 2` component | Is branching/network formation possible? | topology/network characterization | multifunctional monomer guarantees a network |

## 5.12 Worked interpretation — same classification, different evidence questions

Consider two hypothetical processes, both correctly classified as condensative step polymerizations.

### Process A

The feed uses molecules with two reactive connections per monomer and the process record indicates balanced complementary functionality.

### Process B

The feed includes a component capable of more than two covalent connections.

From classification alone, both are still condensative step polymerizations.

But their architecture hypotheses differ.

For Process A, a reasonable next question is whether predominantly linear/macrocyclic connectivity was achieved or whether side reactions/imbalance altered the population.

For Process B, branch/network formation becomes a plausible additional hypothesis because functionality greater than two can create branch points. [Gold Book `FT07505`]

In neither case may the engineer skip directly to stiffness, pressure rating, weldability or lifetime.

The correct next layer is characterization.

## 5.13 Common mistakes / Failure Lens

### Mistake 1 — step polymerization means every chain grows by monomer adding one at a time

Why it fails: growth can occur between monomers, oligomers and polymers of different lengths.

### Mistake 2 — polyaddition is another name for chain polymerization

Why it fails: under the current hierarchy polyaddition is additive **step** polymerization.

### Mistake 3 — polycondensation is identified only by a low-molar-mass by-product

Why it fails: the top-level step classification also requires growth among molecules of varying degrees of polymerization; condensative chain polymerization is a counterexample.

### Mistake 4 — functionality fixes final architecture

Why it fails: functionality establishes possible connectivity, not actual final topology.

### Mistake 5 — a difunctional feed guarantees a linear material

Why it fails: IUPAC notes that `f = 2` can form a linear chain or macrocycle; actual reaction history and side/intramolecular reactions matter.

### Mistake 6 — a multifunctional monomer guarantees a network

Why it fails: `f > 2` creates the possibility of branch points; actual network formation must be established.

### Mistake 7 — use an ideal Carothers equation as a commercial-grade predictor

Why it fails: the ideal relation depends on assumptions about functionality, stoichiometry and reaction extent and belongs downstream of controlled evidence, not as a shortcut to piping performance.

## 5.14 Verification method

Before accepting a step-polymerization explanation, ask:

1. Is the process actually step polymerization under the current IUPAC mechanism definition?
2. Can molecules of different degrees of polymerization react in growth steps?
3. Is the growth additive or condensative?
4. Has by-product formation been incorrectly used as the top-level classifier?
5. What monomer functionality is actually present?
6. Are complementary functional groups and feed proportions documented?
7. What reaction extent/end-group state was achieved?
8. Are side reactions or intramolecular reactions relevant?
9. Has possible connectivity been confused with measured final architecture?
10. Has an ideal synthesis relationship been converted into product/property acceptance?

## 5.15 Engineering decision from Investigation 5

> **In step polymerization, macromolecular growth occurs through reactions among monomer, oligomer and polymer molecules across the size distribution. Additive step polymerization (polyaddition) joins those species without a condensative low-molar-mass by-product; condensative step polymerization (polycondensation) joins them through condensative reactions. Monomer functionality defines possible connectivity, not guaranteed final architecture. Feed balance, reaction extent and side reactions are provenance inputs that must be connected to measured molecular evidence before they affect a piping decision.**

The chapter now has both top-level growth classes under control.

The next Investigation returns to a chain-polymerization mechanism that is central to industrial polyolefins:

> **What is coordination polymerization, and what does preliminary coordination of monomer to a chain carrier mean at engineering-use depth?**

That is Investigation 6.

---

## Investigation 5 controlled asset disposition

- step-polymerization detail panel for `FIG-015-001` established;
- step-polymerization provenance matrix retained as supporting evidence-routing table;
- Gold Book functionality term `FT07505` is load-bearing and shall enter canonical `references.md`;
- Carothers-type equation explicitly **not retained** in this chapter;
- no named polymer/process performance trend introduced;
- Investigation 6 requires current coordination-polymerization terminology verification before authoring.