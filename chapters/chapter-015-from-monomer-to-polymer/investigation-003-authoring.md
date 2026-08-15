# Investigation 3 — How Does Chain Polymerization Build a Macromolecule?

**Authoring status:** controlled candidate  
**Evidence gate:** PASS for stable mechanism / terminology layer  
**Primary controlled source:** S015-004 — IUPAC Terminology for Chain Polymerization (Recommendations 2021; published 2022)  
**Canonical integration:** deferred to end-of-chapter integration

Investigation 2 established the top-level classification: chain polymerization is not simply “polymer chains being formed.” It is a **chain-reaction mechanism**.

Investigation 3 now asks the engineering-use question:

> **What actually has to happen for a chain polymerization to continue, stop, transfer or temporarily pause?**

The answer is best understood by following the **chain carrier / propagating species**, not by staring only at the repeat unit of the final polymer.

The minimum controlled lifecycle is:

`chain initiation → chain propagation`

with possible additional events including:

`chain termination`

`chain transfer`

and, in some controlled/reversible systems:

`reversible deactivation ↔ reactivation`.

IUPAC explicitly states that a chain polymerization consists of initiation and propagation and **may** also include termination and chain transfer. Termination and transfer are therefore not universal mandatory steps. [S015-001, Gold Book `C00958`; S015-004]

## 3.1 The central object is not merely a chain — it is a propagating chain carrier

A **chain carrier** is a species involved in chain-propagating reactions. [Gold Book `C00949`]

In polymerization language, the useful engineering picture is a growing macromolecular species that contains the reactive/active feature enabling the next propagation event.

Depending on the mechanism, the chain carrier may involve:

- a radical;
- an ion or ion pair;
- a coordination complex;
- another controlled reactive species defined by the relevant mechanism.

The chemistry of the carrier matters because it determines which propagation reactions are possible. But the carrier identity alone still does not establish the final chain-length distribution or piping properties.

The chapter therefore separates three ideas:

1. **polymer chain** — the molecular chain being formed;
2. **chain carrier / propagating species** — the reactive species responsible for continuing chain propagation;
3. **final chain architecture** — the population-level result measured after the polymerization history is complete.

Chapter 015 owns items 1–2 only to the extent needed to explain formation history. Chapter 016 owns the detailed population-level architecture.

## 3.2 Chain initiation — creating a chain carrier that can start growth

IUPAC defines **chain initiation** as the process in a chain reaction responsible for formation of a chain carrier. [Gold Book `C00955`]

The newer chain-polymerization terminology also distinguishes an **initiating species**: a species to which monomer adds or becomes inserted to start a chain polymerization. That initiating species may be formed from an initiator or may itself be the initiator. [Gold Book `08959`; S015-004]

This distinction prevents a common shortcut:

`initiator ≠ automatically the species that directly propagates the polymer chain`.

A real mechanism can involve several upstream events before a propagating chain is established.

For engineering purposes, the important questions are:

- what species actually starts a polymer chain?
- how quickly are propagating chains created relative to later propagation?
- does initiation produce one uniform population of chains or several histories?
- does a change in initiator/catalyst environment plausibly change the number or type of chains that begin growing?

The last two questions generate hypotheses only. They require direct evidence before becoming named material claims.

## 3.3 Chain propagation — the defining repeating growth event

Current IUPAC terminology defines **chain propagation** in chain polymerization as a reaction between a chain carrier and a monomer that grows the polymer chain and regenerates at least one chain carrier. [Gold Book `08944`; S015-004]

A generic additive propagation event can be represented conceptually as:

`P_x* + M → P_(x+1)*`

where:

- `P_x*` is a growing chain carrier;
- `M` is monomer;
- `P_(x+1)*` is the longer chain carrier after propagation;
- `*` represents the continuing reactive/active character, not a universal literal radical symbol.

For condensative chain polymerization, a low-molar-mass product may also be formed during propagation, but the defining chain-reaction feature remains regeneration of the reactive site / chain carrier. [Gold Book `C00958`]

The engineering implication is important:

> **Propagation describes the repeated growth chemistry. It does not tell us how long any individual chain will ultimately grow.**

Final chain length depends on the competition among propagation and other events in the actual system.

## 3.4 FIG-015-002 — Chain-Polymerization Lifecycle

The figure specification shall show the following logic:

```text
PRECURSOR / INITIATOR / CATALYST ENVIRONMENT
                │
                ▼
          CHAIN INITIATION
                │
                ▼
      PROPAGATING CHAIN CARRIER
                │
       ┌────────┼─────────────┐
       │        │             │
       ▼        ▼             ▼
 PROPAGATION  TRANSFER    TERMINATION
       │        │             │
       │        │             └──→ non-propagating/dead chain
       │        │
       │        ├──→ original chain stops or changes state
       │        └──→ new chain carrier can be generated
       │
       └──→ longer propagating chain carrier
```

A separate optional branch shall show:

`propagating species ↔ dormant species`

for reversible-deactivation systems, clearly labelled as **not universal to all chain polymerizations**.

Mandatory figure warnings:

1. initiation + propagation are fundamental to the chain-polymerization definition;
2. termination and transfer are possible lifecycle events, not mandatory identical steps in every system;
3. reversible deactivation is not the same as irreversible termination;
4. the figure describes reaction-state pathways, not final molecular-weight distribution.

## 3.5 Chain termination — irreversibly removing a chain carrier

Current IUPAC chain-polymerization terminology defines **chain termination** as a reaction in which a chain carrier is converted irreversibly into a non-propagating species **without formation of a new chain carrier**. [Gold Book `08946`; S015-004]

This is more precise than saying merely “the chain stops growing.”

A chain can stop propagating for several reasons, and not all are equivalent.

Termination means the carrier is irreversibly lost as a propagating species under the mechanism being described.

The product may be a **dead polymer chain** — a chain that plays no active role in the polymerization and is unlikely to be reactivated on the polymerization timescale. [Gold Book `08950`]

That distinction matters later because the population of living/propagating, dormant and dead chains affects how a polymerization history should be interpreted.

Chapter 015 does not yet convert that distinction into a final MWD prediction.

## 3.6 Reversible deactivation is not termination

A propagating chain can become temporarily non-propagating without being irreversibly terminated.

Current IUPAC terminology uses **dormant species** for a temporarily deactivated chain carrier that can be reactivated under polymerization conditions within the polymerization timescale. [Gold Book `08952`; S015-004]

Therefore:

`temporarily not propagating ≠ dead chain`

and

`deactivation ≠ termination`.

This distinction becomes important in controlled/reversible-deactivation polymerizations, but Investigation 3 uses it only to prevent a lifecycle misconception. Detailed families such as RAFT, ATRP or other specialized controlled radical systems are not required for the piping-engineering objective of this chapter.

## 3.7 Chain transfer — ending one growth history while generating another carrier

Chain transfer is frequently taught as if it were merely “termination with restart.” That description is too vague.

The current 2022 terminology gives a useful general engineering model through the **chain-transfer agent** concept: a substance can react with a chain carrier so that the original chain carrier is deactivated and a new chain carrier is generated. A common result is that the new carrier has lower molar mass. [Gold Book `08947`; S015-004]

Conceptually:

`P_x* + T → P_x–T + new carrier*`

The exact chemistry varies by mechanism. The engineering consequence is that chain transfer can separate:

- the length at which one chain-growth history stops;
- the continued ability of the polymerization system to generate further propagation elsewhere.

This is why transfer can influence the eventual population of chain lengths without being identical to complete termination of polymerization activity.

But the chapter maintains the evidence boundary:

> **Knowing that chain transfer is possible does not establish the magnitude of its effect in a named resin.**

A material-specific claim about hydrogen, transfer agent, monomer, solvent or catalyst effects requires direct evidence at the later primary-literature gate.

## 3.8 Termination versus transfer versus reversible deactivation

| Event | What happens to the current chain carrier? | Is a new carrier generated? | Can the original state return? | Engineering interpretation |
|---|---|---|---|---|
| Propagation | carrier continues on a longer chain | carrier is regenerated through growth | N/A | chain continues growing |
| Chain termination | carrier is irreversibly lost | no | no under the defined mechanism | one propagating history ends |
| Chain transfer | original carrier is deactivated/transferred | yes, in the transfer process | mechanism-dependent | one chain history changes/ends while propagation capacity continues elsewhere |
| Reversible deactivation | carrier becomes dormant | not necessarily a new independent carrier | yes | temporary non-propagating state |

**Table rule:** this is a reaction-state map. It does not predict a commercial resin's MWD.

## 3.9 Why termination and transfer are not mandatory in every chain polymerization

The Gold Book chain-polymerization entry explicitly states that initiation and propagation are fundamental, while termination and chain transfer **may** also occur. [Gold Book `C00958`]

A useful limiting case is **living polymerization**, which IUPAC defines as a chain polymerization from which chain transfer and chain termination are absent. [Gold Book `L03597`]

The teaching point is not to explore living polymerization in depth. It is to prove that this lifecycle diagram is not a mandatory four-step recipe.

Therefore avoid the common textbook sequence:

`initiation → propagation → termination`

when it is presented as though every chain polymerization must end by a classical termination event.

A better framework is:

`initiation → propagation`

with competing/possible pathways whose presence and rates depend on the actual polymerization system.

## 3.10 The competition among events is what creates a chain-building history

At any moment, a propagating chain carrier may have several possible next events.

At engineering-use depth, the possibilities can include:

- another propagation event;
- chain transfer;
- termination;
- reversible deactivation;
- mechanism-specific side reactions;
- depropagation in systems where reverse propagation is relevant.

IUPAC defines **chain depropagation** as the reverse of chain propagation: formation of monomer at the terminal active center while the chain degree of polymerization decreases by one. [Gold Book `15387`]

Chapter 015 does not need to solve the full kinetics of all these competing events. The critical concept is:

> **A polymer population records the statistical history of many competing molecular events, not one idealized reaction arrow.**

This statement sets up the process–structure reasoning needed later in the chapter.

## 3.11 A bounded quantitative notation — useful, but not yet a design calculation

IUPAC recommends `k_p` as the rate coefficient symbol for chain propagation in homopolymerization and `k_t` for chain termination. [Gold Book `08944`; `08946`]

These symbols are introduced only as vocabulary for later mechanism discussion.

Chapter 015 does **not** yet use a propagation/termination rate law to calculate commercial resin architecture, because that would require:

- a defined polymerization mechanism;
- concentrations of relevant species;
- validated kinetic coefficients at the actual conditions;
- transfer/deactivation/side-reaction treatment;
- reactor history;
- proof that the simplified kinetic model applies.

The existence of `k_p` and `k_t` therefore teaches an important engineering distinction:

`reaction pathway identified` is not the same as `reaction history quantified`.

## 3.12 Worked mechanism trace — one chain carrier, several possible outcomes

Consider an abstract propagating chain carrier `P_x*`.

### Path A — propagation

`P_x* + M → P_(x+1)*`

The chain becomes longer and retains/regenerates propagation capability.

### Path B — irreversible termination

`P_x* → P_x(dead)`

The specific chain carrier no longer participates in propagation and no new chain carrier is created by the termination event.

### Path C — transfer

`P_x* + T → P_x–T + carrier*`

The original chain-growth history is interrupted while a new carrier can continue the overall polymerization sequence elsewhere.

### Path D — reversible deactivation

`P_x* ⇌ P_x(dormant)`

The chain temporarily leaves the propagating population but may return under the polymerization conditions.

The exercise demonstrates why a single reaction label cannot determine the final population of chain lengths.

## 3.13 Why this matters to material provenance and change control

Suppose a resin producer changes a process variable that changes the relative frequency of propagation versus transfer.

The correct engineering reasoning chain is:

`process change`

→ `possible change in event competition`

→ `possible change in chain-building history`

→ `architecture hypothesis`

→ `molecular/rheological characterization`

→ `qualification impact assessment`.

It is **not**:

`process change → assumed MWD → assumed pipe performance`.

Likewise, if a change affects termination or reversible-deactivation behavior, the engineer should identify what material-state measurement would reveal the consequence rather than inferring it directly from the mechanism label.

## 3.14 Common mistakes / Failure Lens

### Mistake 1 — treating an initiator as identical to the propagating species

Why it fails: an initiating species may be generated from an initiator before propagation begins.

### Mistake 2 — treating propagation as simply “the chain gets longer”

Why it fails: the controlled definition also requires regeneration of a chain carrier through the growth event.

### Mistake 3 — saying every chain polymerization must terminate

Why it fails: termination and chain transfer are optional in the general definition; living polymerization is the limiting counterexample.

### Mistake 4 — treating reversible deactivation as termination

Why it fails: a dormant chain carrier can be reactivated; termination is irreversible under the defined mechanism.

### Mistake 5 — treating chain transfer as equivalent to stopping all polymerization

Why it fails: transfer deactivates/transfers the original carrier while generating another chain carrier capable of further propagation.

### Mistake 6 — deriving MWD directly from the presence of transfer or termination

Why it fails: the magnitude depends on the rates, concentrations, mechanism, process history and competing events.

### Mistake 7 — treating `k_p` or `k_t` as material constants independent of conditions

Why it fails: kinetic coefficients belong to defined reactions under defined conditions; they are not universal resin-grade labels.

## 3.15 Verification method

Before accepting a description of chain-polymerization growth, ask:

1. What is the chain carrier / propagating species?
2. How is the initiating species formed?
3. What reaction constitutes propagation?
4. Is the chain carrier regenerated during propagation?
5. Is termination actually present in this system, or merely assumed from a generic textbook scheme?
6. Is chain transfer present, and what new carrier is generated?
7. Is a non-propagating state dead or only dormant?
8. Are reversible deactivation and irreversible termination distinguished?
9. Are any kinetic symbols being used without actual validated kinetic data?
10. Has a lifecycle mechanism been converted into a final architecture/property claim without measurement?

## 3.16 Engineering decision from Investigation 3

> **A chain polymerization is governed by the lifecycle of chain carriers. Initiation creates a carrier capable of starting growth; propagation repeatedly grows the chain while regenerating propagation capability; termination irreversibly removes a carrier without creating a new one; chain transfer shifts propagation capability from one chain history to another; and reversible deactivation can temporarily remove a carrier from propagation without killing it. Only initiation and propagation are fundamental to the general chain-polymerization definition.**

This provides the mechanism skeleton required for the next Investigation:

> **How does this lifecycle look when the kinetic-chain carriers are radicals, and which process variables can change the radical chain-building history?**

That is Investigation 4.

---

## Investigation 3 controlled asset disposition

- `FIG-015-002` — chain-polymerization lifecycle scientific specification established.
- Lifecycle comparison table — retained as supporting teaching asset; final numbering to be assigned at integration if required.
- Quantitative notation `k_p` / `k_t` introduced only as controlled terminology, not as a calculation model.
- No named material/process trend introduced; no Class-C primary evidence required.
- Investigation 4 remains subject to a mechanism gate before any named monomer/process trend is retained.