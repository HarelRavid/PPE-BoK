# Investigation 2 — What Does “Polymerization” Actually Mean, and How Should the Reactions Be Classified?

**Authoring status:** controlled candidate  
**Evidence gate:** PASS for terminology/classification authoring  
**Controlling current source:** S015-008 — IUPAC basic classification Recommendation published 2026  
**Canonical integration:** deferred to end-of-chapter integration

A piping engineer does not need to memorize every polymer synthesis route. The engineer does need a classification system that prevents the wrong inference from being made before the material is even characterized.

The classification problem matters because common teaching language can hide two separate questions:

1. **How does molecular growth occur?**
2. **Does a growth step eliminate a low-molar-mass molecule?**

Those are not the same question.

If they are collapsed into the old pair `addition polymerization` versus `condensation polymerization`, different mechanisms can be placed in the same box and similar mechanisms can be separated for the wrong reason.

The current IUPAC Recommendation provides a better hierarchy. At the top level, Chapter 015 will distinguish **step polymerization** from **chain polymerization**. Each of those can then be qualified by whether the growth step is additive or condensative. [S015-008]

The engineering value is simple:

> **Classify the growth mechanism first. Then add the reaction qualifier. Do not infer material performance from either label.**

## 2.1 Start with the broad term: polymerization

The Gold Book defines polymerization as the process that converts a monomer or mixture of monomers into a polymer. [S015-001, Gold Book `P04740`]

That definition is intentionally broad. It does not tell us whether the growth proceeds through active sites on growing chains, through reactions between molecules of many different lengths, through coordination chemistry, radical chemistry, ionic chemistry or another mechanism.

Likewise, the Gold Book term **monomer** identifies the substance composed of monomer molecules. [Gold Book `M04017`]

For engineering reasoning, this gives a useful starting point:

`monomer/feed` is the input identity.

`polymerization class` describes the route by which macromolecular growth occurs.

Neither is a complete description of the final resin.

## 2.2 The 2026 IUPAC hierarchy: two common mechanism classes

The current IUPAC basic-classification Recommendation identifies two common top-level classes of polymerization mechanism. [S015-008]

### Class A — step polymerization

In **step polymerization**, growth occurs by reactions between monomer, oligomer or polymer molecules of any length.

The key idea is not that one molecule literally grows in visually discrete “steps.” All chemical reactions occur as events. The classification concerns **which molecular sizes are capable of reacting in the growth process**.

A monomer can react with another monomer.

A monomer can react with an oligomer.

An oligomer can react with another oligomer.

A polymer-length molecule can react with another reactive molecule when suitable functional groups remain.

The growth network therefore does not require one special active site to remain attached to the same growing chain after every growth event.

### Class B — chain polymerization

In **chain polymerization**, polymer growth proceeds by a chain reaction in which monomer reacts with active/reactive site(s) on growing polymer chains, with the active site regenerated through the propagation event. [S015-008; S015-001, Gold Book `C00958`]

This distinction is central:

> **The word `chain` refers to the chain reaction, not merely to the fact that the product is a polymer chain.**

A polymer made by step polymerization also consists of polymer chains. That does not make the mechanism a chain polymerization.

The chain-polymerization branch will be developed in detail in Investigation 3.

## 2.3 A second axis: additive versus condensative growth

Once the growth mechanism is identified, the current hierarchy adds another useful question:

> Does the growth step join the reacting species without generating a low-molar-mass by-product, or is the growth event condensative?

This produces four controlled categories for the basic map. [S015-008]

### 2.3.1 Additive step polymerization

**Additive step polymerization** is the current mechanism-class name corresponding to **polyaddition**.

Growth occurs between molecules of different degrees of polymerization by addition reactions, without the defining condensative elimination in the growth step.

The older Gold Book `polyaddition` entry remains useful because it captures the core all-degrees-of-polymerization growth concept. S015-008 places that concept explicitly under the step-polymerization branch.

### 2.3.2 Condensative step polymerization

**Condensative step polymerization** is the current mechanism-class name corresponding to **polycondensation**.

Growth occurs between molecules of different degrees of polymerization through condensation reactions.

The low-molar-mass by-product is a reaction qualifier, but the top-level mechanism is still **step polymerization** because growth can occur between molecules across the size distribution rather than exclusively through monomer addition at a persistent active site on a growing chain.

### 2.3.3 Additive chain polymerization

In **additive chain polymerization**, the top-level mechanism is chain polymerization and the propagation step is additive.

The important feature is the chain-reaction structure:

`growing chain active site + monomer → longer growing chain with active site regenerated`

The absence of a small-molecule by-product is not what makes it a chain polymerization. The active-site/chain-reaction propagation pattern does.

### 2.3.4 Condensative chain polymerization

**Condensative chain polymerization** is the category that immediately exposes the weakness of the old addition/condensation split.

Here the process is still a **chain polymerization** because growth proceeds by monomer reacting at a reactive site on a growing chain with regeneration of that site. However, propagation also forms a low-molar-mass by-product. [S015-001, Gold Book `C00958`; S015-008]

Therefore:

`small-molecule elimination ≠ automatically step polymerization`

and

`no small-molecule elimination ≠ automatically chain polymerization`.

This is one of the most important classification controls in the chapter.

## 2.4 FIG-015-001 — Polymerization Classification Map

The final figure shall use the following hierarchy:

```text
POLYMERIZATION
│
├── STEP POLYMERIZATION
│   │
│   ├── Additive step polymerization
│   │      synonym: polyaddition
│   │
│   └── Condensative step polymerization
│          synonym: polycondensation
│
└── CHAIN POLYMERIZATION
    │
    ├── Additive chain polymerization
    │
    └── Condensative chain polymerization
```

A second annotation layer shall show that chain polymerization can be further classified by chain carrier / propagation mechanism where appropriate, for example:

- radical;
- ionic;
- coordination;
- ring-opening or other propagation descriptors where the controlled terminology supports them.

The figure must carry a visible warning:

> **Do not use `addition polymerization` versus `condensation polymerization` as the controlling top-level classification. Mechanism class and additive/condensative reaction character are separate descriptors.**

The figure is a terminology/classification map. It is not a material-performance map.

## 2.5 Why the historical “addition polymerization” label is inadequate

The older term **addition polymerization** is a common textbook phrase, but it is not sufficiently precise for this chapter.

The Gold Book `polyaddition` entry already notes that the earlier expression `addition polymerization` covered more than one present-day concept: both polyaddition and chain polymerization. [S015-001, Gold Book `P04720`]

The 2026 IUPAC Recommendation resolves the hierarchy more directly by separating **step polymerization** and **chain polymerization**, then applying additive/condensative qualifiers below those mechanism classes. [S015-008]

Therefore, if a supplier document, old textbook or failure report says only:

> “This is an addition polymer.”

Chapter 015 treats that statement as **insufficient mechanism information**.

The next question is:

> Is the growth a step polymerization or a chain polymerization, and what reaction/mechanism qualifier actually applies?

## 2.6 Why the historical “condensation polymerization” label is also insufficient by itself

The same problem exists on the condensation side.

If a polymer-forming reaction releases a low-molar-mass by-product, it may be tempting to classify it immediately as a step-growth/condensation process.

That is unsafe.

Condensative chain polymerization demonstrates that a chain-reaction growth mechanism can also contain condensative propagation. [S015-001, Gold Book `C00958`; S015-008]

Therefore the engineer should not classify a polymerization by asking only:

> “Was water, alcohol or another small molecule released?”

The correct first question is:

> **Who reacts with whom during growth?**

If molecules of many lengths react with one another as the growth process, the route is in the step-polymerization branch.

If monomer adds at an active site on a growing chain and that active site is regenerated, the route is in the chain-polymerization branch.

Then the additive/condensative qualifier can be applied.

## 2.7 TAB-015-001 — Controlled Polymerization Terminology and Common Misuse

| Controlled term | Engineering-use meaning | Common misuse to avoid | What it does **not** establish |
|---|---|---|---|
| Polymerization | Broad conversion of monomer(s) to polymer | Treating it as one universal mechanism | final architecture or properties |
| Step polymerization | Growth by reactions among monomer/oligomer/polymer molecules of any length | Assuming “step” means slow, literal or visually sequential growth | reaction by-product, final molar mass, material quality |
| Additive step polymerization | Step polymerization by additive growth; polyaddition | Calling every no-by-product polymerization “addition polymerization” | chain mechanism, catalyst route, properties |
| Condensative step polymerization | Step polymerization by condensative growth; polycondensation | Assuming all condensative polymerization is step polymerization without checking mechanism | chain architecture or performance |
| Chain polymerization | Chain reaction; monomer reacts at active site(s) on growing chain with active-site regeneration | Thinking `chain` means simply “a polymer chain is formed” | radical/ionic/coordination subtype or final properties |
| Additive chain polymerization | Chain polymerization with additive propagation | Treating it as synonymous with all historical `addition polymerization` | catalyst identity or grade properties |
| Condensative chain polymerization | Chain polymerization whose propagation is condensative | Assuming a small-molecule by-product automatically makes the route step polymerization | product/material qualification |
| Addition polymerization | Historical/ambiguous phrase | Using it as the formal top-level class | precise mechanism |
| Condensation polymerization | Historical/general phrase that can hide mechanism distinctions | Using by-product formation alone as the classification rule | precise mechanism |

**Table rule:** no row may be read as a ranking of polymer quality or piping suitability.

## 2.8 Reaction outcome is not the same as growth mechanism

This distinction deserves its own engineering rule.

Two polymerizations can both show overall addition-like stoichiometry yet have different growth mechanisms.

Two polymerizations can both generate low-molar-mass products yet belong to different growth-mechanism branches.

Therefore the overall reaction equation is often not enough to classify the process.

A simplified overall equation can tell us which atoms appear in products and by-products. It may not reveal:

- whether growth occurs at a persistent active site;
- whether all molecular sizes can participate directly in growth;
- whether initiation is required;
- whether propagation is a chain-reaction process;
- whether termination or chain transfer occurs;
- what the chain carrier is.

For a piping engineer reading a resin or supplier document, this means that a familiar repeat-unit drawing or net stoichiometric equation should not be mistaken for a mechanism description.

## 2.9 EX-015-002 — Why “Addition Polymer” Is Not Enough Information

Consider four simplified polymer-forming descriptions. The purpose is classification, not prediction of material properties.

### Case A — active-site growth with no low-molar-mass by-product

A growing polymer chain carries a reactive site. Monomer reacts at that site, the chain becomes one monomer unit longer and the reactive site is regenerated.

**Classification:** additive chain polymerization.

**Why:** the top-level feature is chain-reaction propagation at a growing-chain active site; the growth event is additive.

**Still unknown:** chain carrier, catalyst/initiator environment, transfer/termination behaviour, architecture distribution and product properties.

### Case B — active-site growth with a low-molar-mass by-product

A growing chain carries a reactive site. Monomer reacts at that site, the chain grows, the reactive site is regenerated and a low-molar-mass species is produced during propagation.

**Classification:** condensative chain polymerization.

**Why:** it remains a chain polymerization despite the condensative propagation event.

**Teaching value:** this case falsifies the shortcut `small molecule formed → step/condensation polymerization`.

### Case C — molecules across the size distribution combine without a low-molar-mass by-product

Monomers, oligomers and longer molecules bearing suitable reactive groups can react with other molecules of varying length. Growth proceeds through additive reactions.

**Classification:** additive step polymerization; synonym polyaddition.

**Why:** molecules of multiple degrees of polymerization participate in the growth network; no persistent growing-chain active site defines the propagation sequence.

### Case D — molecules across the size distribution combine with a low-molar-mass by-product

Monomers, oligomers and longer molecules bearing suitable reactive groups can react with one another, and the growth event eliminates a low-molar-mass species.

**Classification:** condensative step polymerization; synonym polycondensation.

### Engineering conclusion from the exercise

The old question:

> “Is this an addition or condensation polymerization?”

is replaced by two questions:

1. **Is the growth mechanism step polymerization or chain polymerization?**
2. **Is the relevant growth event additive or condensative?**

Only after those questions are answered should more specific mechanism labels be added.

## 2.10 Why classification still does not tell us whether a piping resin is “better”

A correct mechanism label is useful, but it remains upstream evidence.

Knowing that a polymer was produced by chain polymerization does not establish:

- molar mass;
- molar-mass distribution;
- short- or long-chain branching;
- comonomer distribution;
- tacticity;
- crystallinity;
- density;
- rheology;
- SCG resistance;
- RCP resistance;
- permeability;
- fusion response;
- hydrostatic strength;
- pressure rating or service life.

Likewise, knowing that a polymer is made by step polymerization does not establish whether stoichiometry, conversion, functionality, side reactions or process history produced the intended molecular population.

Classification answers:

> **What type of growth mechanism are we discussing?**

It does not answer:

> **What exact material did the process produce, and is that material qualified for this piping application?**

That boundary remains non-negotiable.

## 2.11 Classification as a diagnostic tool

In engineering work, classification becomes useful when technical claims conflict.

### Example — supplier statement

A supplier states that two materials are “both addition polymers” and therefore should behave similarly.

Controlled response:

1. `addition polymer` is not sufficiently precise;
2. identify the actual step/chain mechanism class;
3. identify more specific mechanism/catalyst information only if relevant;
4. identify which molecular features are claimed to differ or remain equivalent;
5. verify those features through material and product evidence.

### Example — failure analysis

A report attributes a failure to “condensation chemistry” because a low-molar-mass by-product is associated with polymer formation.

Controlled response:

1. by-product formation does not alone establish the top-level growth mechanism;
2. determine whether the growth is step or chain polymerization;
3. separate polymerization history from later compounding, processing, joining, ageing and service mechanisms;
4. require evidence connecting the polymerization variable to the measured failed-material state.

Classification helps structure the investigation. It does not close it.

## 2.12 Common mistakes / Failure Lens

### Mistake 1 — `step polymerization` means “the chain grows one step at a time”

Why it fails: the controlled distinction concerns reactions among molecules across the size distribution, not the philosophical fact that chemical reactions occur as events.

### Mistake 2 — `chain polymerization` means “a chain is produced”

Why it fails: `chain` refers to the chain-reaction mechanism. Step polymerization also produces polymer chains.

### Mistake 3 — no small-molecule by-product means chain polymerization

Why it fails: additive step polymerization/polyaddition exists.

### Mistake 4 — small-molecule by-product means step polymerization

Why it fails: condensative chain polymerization exists.

### Mistake 5 — `polyaddition` and `chain polymerization` are synonyms

Why it fails: the historical phrase `addition polymerization` once blurred these concepts, but current classification separates them.

### Mistake 6 — `polycondensation` is the only possible condensative polymerization

Why it fails: condensative chain polymerization is a separate mechanism class.

### Mistake 7 — a classification label predicts pipe performance

Why it fails: classification does not measure the material state or establish product qualification.

## 2.13 Verification method

Before accepting a polymerization classification, ask:

1. Is the source using current terminology or historical shorthand?
2. During growth, can molecules of many different lengths react with one another?
3. Or does monomer react at an active site on a growing chain?
4. Is the active/reactive site regenerated during propagation?
5. Is the process therefore step polymerization or chain polymerization?
6. Is the growth event additive or condensative?
7. Has the classification been confused with the overall reaction equation?
8. Has a small-molecule by-product been used as the sole classification criterion?
9. Has `addition polymerization` been used without resolving its ambiguity?
10. Has a mechanism label been converted into a property or qualification claim?

If questions 2–6 cannot be answered from the available source, the correct disposition is **classification not established**, not a guessed category.

## 2.14 Engineering decision from Investigation 2

> **Use the current IUPAC hierarchy: first distinguish step polymerization from chain polymerization by the growth mechanism; then qualify the growth as additive or condensative. Treat `polyaddition` as additive step polymerization and `polycondensation` as condensative step polymerization. Do not classify solely by the presence or absence of a low-molar-mass by-product, and do not use the historical phrase `addition polymerization` as a precise technical mechanism.**

This gives Chapter 015 a controlled map.

The next question is now narrower:

> **Once a polymerization is identified as a chain polymerization, how does that chain reaction actually build the macromolecule?**

That is Investigation 3.

---

## Investigation 2 controlled asset disposition

- `FIG-015-001` — scientific/classification specification established in this candidate.
- `TAB-015-001` — final terminology/common-misuse candidate established here.
- `EX-015-002` — controlled classification exercise established here.
- S015-008 — mandatory source to integrate into canonical `references.md` at chapter closure.
- No named commercial material, catalyst technology or piping-performance claim introduced.