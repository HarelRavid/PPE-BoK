# Investigation 9 — How Do Molecular Features Become Engineering-Property Hypotheses?

> **Controlled authoring file.** This file is a temporary development artifact for PR #12. Its approved content shall be integrated into `chapter.md` and this file removed before the PR is eligible for Ready-for-Review.

**Authoring basis:** CDB-014, Technical Outline Checkpoint D, and the Investigation 9 Evidence Matrix in `references.md`.

**Authorized evidence scope:** Cases A–C only. No additional named-material structure→property claim is introduced here.

---

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

# 9.4 Case A — PA6 + water: when chemistry gives a useful mechanism, but not a design value

Polyamide 6 provides a useful example because the chain contains polar amide groups and the material is known experimentally to respond to water conditioning.

The chemical observation is straightforward:

- the polymer contains amide functionality;
- water is a small polar molecule;
- intermolecular hydrogen-bonding interactions are scientifically plausible.

That is enough to formulate a hypothesis:

> Water uptake may alter intermolecular association and segmental mobility in PA6, producing measurable sorption, swelling and mechanical changes.

It is **not** enough to specify the magnitude of those changes.

## 9.4.1 What the direct evidence shows

Shinzawa and Mizukado studied dry- and wet-treated PA6 using near-infrared correlation spectroscopy together with mechanical comparison. Their reported observations include a substantial decrease in Young's modulus after wet treatment and spectroscopic interpretation consistent with absorbed water disrupting H-bonded bridges particularly in amorphous regions and increasing chain mobility. They also reported a change in the crystalline/amorphous population, which immediately prevents a simplistic one-variable explanation. [S014-009]

Sambale et al. experimentally characterized water sorption and moisture-induced swelling of PA6 specimens under controlled conditioning and different geometry conditions. Their work required concentration-dependent diffusion behaviour and explicitly treated geometry, concentration and swelling rather than reducing the phenomenon to the presence of an amide group. [S014-010]

Together these studies support the mechanism-level statement:

> **Amide/H-bond chemistry is a defensible starting hypothesis for PA6–water interaction, and water exposure produced measurable sorption, swelling and mechanical/molecular changes in the studied PA6 systems.**

## 9.4.2 What the evidence does not establish

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

## 9.4.3 Engineering lesson from Case A

A chemistry hypothesis can be **scientifically correct and experimentally supported** while still being **insufficient for direct design use**.

That is not a weakness of chemistry. It is the correct separation between mechanism and qualification.

---

# 9.5 Case B — Fluoropolymer membranes: when a simple chemistry ranking fails

Fluoropolymers are tempting targets for shortcut reasoning.

An engineer may look at fluorine substitution, polarity and symmetry and try to create a simple ranking such as:

> “more fluorination → more/less polarity → lower gas permeability.”

The problem is that penetrant transport in a polymer is not controlled by one descriptor alone.

Graunke et al. experimentally compared multiple fluoropolymer membranes chosen to vary fluorination and structural features including ether-containing monomers. Their measurements showed strong influences from polymer-specific structure and crystallinity, and the paper includes cases where an expected simple relation between density/crystallinity/polarity and permeability did not hold generally. [S014-011]

The controlled conclusion is therefore:

> **Fluorination, polarity and functional-group chemistry can generate useful transport hypotheses, but they do not provide a universal permeability or selectivity ranking across fluoropolymers.**

## 9.5.1 Why this is an important engineering failure mode

A repeat-unit comparison hides variables such as:

- crystalline fraction;
- amorphous free volume;
- chain packing;
- copolymer architecture;
- membrane thickness;
- processing history;
- penetrant identity;
- penetrant concentration;
- test geometry.

A chemically elegant ranking can therefore be physically incomplete.

## 9.5.2 What may be transferred to piping engineering

The transferable lesson is **methodological**, not quantitative:

1. use chemistry to propose which interactions may matter;
2. identify morphology/processing variables that may alter the transport pathway;
3. measure the actual penetrant/material system;
4. do not use thin-film sensor-membrane transmission as a pipe-wall permeability allowance.

No ranking of piping-grade PVDF, PTFE, PFA, ECTFE, ETFE or other fluoropolymers is authorized from this case.

---

# 9.6 Case C — PFA cooling history: when processing changes the result without changing the family name

The third case attacks a different shortcut:

> “If the polymer family and nominal grade are known, the transport property should be essentially fixed.”

Monson, Moon and Extrand tested several PFA/PTFE-copolymer grades using specimens prepared with different cooling techniques. They measured permeability, diffusion and solubility coefficients for hydrogen, nitrogen and oxygen. Slow-cooled specimens showed markedly greater permeation resistance than rapidly cooled specimens, and the authors attributed the differences to crystallinity arising from molecular architecture and processing. They concluded that processing can be as important as polymer grade for the measured permeation response. [S014-012]

This is a high-value teaching case because the chemical family label remained insufficient.

## 9.6.1 The engineering chain

The defensible reasoning chain is:

`PFA family / architecture + cooling history → different morphology / crystallinity hypothesis → measured H2/N2/O2 transport → bounded specimen-level conclusion`

not:

`PFA repeat unit → universal gas permeability`

## 9.6.2 What this case proves at Chapter 014 level

It supports the general mechanism statement that **processing-induced morphology can materially influence a measured property that an engineer might otherwise try to infer from chemistry or grade name alone**.

It does not establish:

- a universal slow-cooling manufacturing prescription;
- an allowable H2 permeation rate for PFA pipe;
- a service-life value;
- a pipe-wall design rule;
- superiority of one commercial grade.

Those require product-specific evidence and the later materials/design framework.

---

# 9.7 TAB-014-003 — Controlled structure–property teaching cases

| Case | Starting feature / hypothesis | Direct evidence | Confounders made visible by the evidence | Defensible conclusion | Design conclusion explicitly prohibited |
|---|---|---|---|---|---|
| A — PA6 + water | amide functionality / H-bond interaction with water | sorption, swelling, modulus and spectroscopic/morphology response in studied PA6 systems [S014-009][S014-010] | conditioning, concentration, geometry, amorphous/crystalline balance | chemistry correctly identifies a relevant interaction mechanism, but magnitude requires measurement | universal PA modulus derating, swelling allowance or compatibility limit |
| B — fluoropolymer membranes | fluorination / polarity / ether groups may influence penetrant transport | measured gas/water-vapour transport across selected membranes [S014-011] | crystallinity, density/free volume, copolymer structure, film/test configuration | simple chemical descriptors are insufficient as a universal transport ranking | piping-grade fluoropolymer permeability ranking or service qualification |
| C — PFA process/morphology | grade chemistry alone may not control permeation if processing changes morphology | H2/N2/O2 permeability, diffusion and solubility under different cooling histories [S014-012] | cooling history, crystallinity, comonomer/filler, specimen preparation | processing/morphology can rival grade chemistry in measured transport | universal cooling prescription or pipe-wall permeability value |

The table deliberately contains no ranking column.

---

# 9.8 EX-014-002 — Comparing two apparently “simple” polymer hypotheses

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

A highly fluorinated structure may suggest low interaction with some penetrants, but gas transport still depends on morphology, free volume, crystallinity, copolymer structure and processing.

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

# 9.9 FIG-014-006 — Molecular feature to engineering evidence chain — scientific specification

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

# 9.10 WF-014-001 — Chemical structure → evidence → engineering decision boundary — first formal version

`Observe structure`

→ `State mechanism hypothesis`

→ `Define measurable property`

→ `Find / generate direct evidence`

→ `Identify morphology / processing / conditioning confounders`

→ `Set transferability boundary`

→ `Check material / product / application qualification`

→ `Use in engineering decision`

At any step, if the evidence is missing or not transferable:

> **STOP — retain the statement as a hypothesis and route the question to testing, a material-specific chapter, or the governing qualification framework.**

---

# 9.11 Verification — how to audit a structure→property statement

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

# 9.12 Common mistakes / Failure Lens

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

# 9.13 Engineering decision from Investigation 9

> A chemical structure is an efficient generator of **engineering hypotheses**, not engineering acceptance values. The correct path is `feature → mechanism hypothesis → measurement → confounder review → transferability → qualification → decision`. Cases A–C demonstrate three complementary outcomes: a plausible mechanism can be supported but remain non-transferable as a design value; a simple chemical ranking can fail; and processing/morphology can change a property even within the same polymer family.

Investigation 9 therefore closes the chapter's final scientific bridge.

The remaining question is governance of the boundary itself:

> **When is chemistry sufficient to guide engineering judgement, and when must the engineer stop and hand the question to characterization, qualification, standards or a downstream PPE-BoK chapter?**

That is the purpose of Investigation 10.
