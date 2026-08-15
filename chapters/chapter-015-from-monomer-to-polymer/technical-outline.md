# Chapter 015 — Technical Outline

**Working title:** From Monomer to Polymer: Polymerization, Catalysts and Process–Structure Relationships  
**PDS baseline:** 1.0  
**CDB:** `docs/PDS/Chapter-Design-Briefs/CDB-015-Polymerization-Catalysts-Process-Structure.md`  
**CDB status:** Approved  
**Outline status:** Approved implementation path for Definition-of-Ready verification  
**Date:** 2026-08-15

## 1. Chapter engineering question

> How does the route from monomer to polymer create the molecular-architecture possibilities that later control real engineering behaviour, and what can a piping engineer legitimately infer from catalyst/process information before material-specific evidence is required?

The chapter must connect Chapter 014 chemistry to Chapter 016 architecture without turning polymerization provenance into an unsupported material-property prediction.

## 2. Governing reasoning chain

Use this chain throughout the manuscript:

`monomer / feed → polymerization class → active species / catalyst environment → chain-building events → process history → architecture hypothesis → characterization → qualification → piping decision`

The chapter owns the first six blocks only to the depth needed to explain how architecture can be created. Chapter 016 owns detailed architecture; Chapter 017 owns morphology; Chapters 018–020 own downstream behaviour.

## 3. Terminology controls

1. Use **polymerization** as the broad process term.
2. Use **chain polymerization** only for the IUPAC chain-reaction concept in which propagation occurs by reaction of monomer with reactive site(s) on the growing chain and the active site is regenerated.
3. Explicitly state that the adjective `chain` refers to the chain reaction, not simply to the existence of a polymer chain.
4. Use **polyaddition** for growth by addition reactions between molecules of all degrees of polymerization.
5. Use **polycondensation** for growth by condensation reactions between molecules of all degrees of polymerization.
6. Treat the older expression **addition polymerization** as historical classroom terminology; explain that IUPAC notes that it previously covered both present-day polyaddition and chain polymerization.
7. Use `step-growth` only as explanatory language when useful; do not present it as the controlling formal IUPAC classification unless mapped to the actual chemistry.
8. Use **radical polymerization** as a chain polymerization whose kinetic-chain carriers are radicals.
9. Use **coordination polymerization** as a chain polymerization involving preliminary coordination of monomer with a chain carrier.
10. Use **heterogeneous catalysis coordination polymerization** / **heterogeneous coordination polymerization** as the controlled term; note that polyolefin routes of this type are sometimes called Ziegler–Natta polymerization and that current IUPAC terminology deprecates named reactions as the technical definition.
11. Use **homogeneous catalysis coordination polymerization** / **homogeneous coordination polymerization** for coordination polymerization using a homogeneous catalyst.
12. Treat **metallocene polymerization** as one form of homogeneous coordination polymerization, not as a synonym for every homogeneous coordination route.

## 4. Evidence controls

### 4.1 Stable mechanism layer

May rely on current IUPAC terminology/recommendations plus established academic references for mechanism explanation. No commercial-grade property conclusion is permitted from this layer.

### 4.2 Named material / catalyst / process layer

Any retained statement of the form `named route/process variable → measured architecture/property change` requires a directly reviewed primary source and a case record containing:

- exact monomer/feed;
- catalyst/initiator/active-system identity at the level reported;
- process variable(s);
- measured chain/structural output;
- measured property if discussed;
- confounders;
- supported conclusion;
- unsupported conclusion;
- transferability to real piping compounds/products.

### 4.3 Prohibited direct transfers

Do not infer directly from catalyst/process route:

- MWD or branching magnitude;
- density/crystallinity;
- modulus/toughness;
- SCG/RCP/fatigue performance;
- permeability;
- fusion parameters;
- pressure rating;
- service temperature;
- lifetime;
- chemical compatibility.

## 5. Investigation implementation sequence

### Investigation 1 — Why should a piping engineer care how the polymer was made?

**Purpose:** Establish polymerization history as material provenance.

Required content:
- bridge from Chapter 014: repeat-unit chemistry is not the finished material state;
- family name versus chain-building history;
- why process/catalyst provenance can change what must be characterized;
- mechanism evidence versus qualification evidence;
- initial `process provenance` concept;
- no named catalyst/property claims yet.

Assets introduced:
- conceptual precursor to `FIG-015-006`;
- preliminary evidence-boundary table.

Exit capability:
- reader can explain why a resin family/monomer label does not erase polymerization history.

### Investigation 2 — What does “polymerization” actually mean, and how should the reactions be classified?

**Purpose:** Build the controlled classification map.

Required content:
- monomer, polymerization;
- chain polymerization;
- polyaddition;
- polycondensation;
- condensative chain polymerization as the key counterexample to the simplistic classroom split;
- explanatory `step-growth` mapping;
- `TAB-015-001`;
- `FIG-015-001`;
- `EX-015-002`.

Exit capability:
- reader can classify simplified descriptions without relying on `addition vs condensation` alone.

### Investigation 3 — How does chain polymerization build a macromolecule?

**Purpose:** Explain the chain-reaction lifecycle at engineering-use depth.

Required content:
- reactive site / chain carrier;
- chain initiation;
- chain propagation;
- chain termination;
- chain transfer;
- not all chain polymerizations contain termination/transfer in the same way;
- distinguish kinetic chain from polymer chain when needed;
- `FIG-015-002`.

Exit capability:
- reader can separate growth chemistry from the final architecture it may generate.

### Investigation 4 — How does radical polymerization work, and what process variables matter?

**Purpose:** Provide one complete chain-polymerization mechanism family before coordination routes.

Required content:
- radical chain carrier;
- initiator versus radical species;
- propagation;
- termination and transfer concepts;
- temperature/concentration/transfer-agent variables as mechanism hypotheses;
- no commercial-grade trends without primary evidence;
- `FIG-015-003`.

Quantitative candidate:
- only bounded rate-law concepts if they materially improve understanding; otherwise omit.

### Investigation 5 — How does growth by reactions between molecules of different chain lengths differ from chain polymerization?

**Purpose:** Explain polyaddition/polycondensation without creating a synthesis textbook.

Required content:
- all-degrees-of-polymerization growth concept;
- condensation versus addition reaction distinction;
- functional-group conversion;
- stoichiometric balance as a qualitative engineering concern;
- Carothers-type ideal relationship only if assumptions are explicit and evidence review approves its teaching value;
- transfer ownership of molar-mass consequences to Chapter 016.

### Investigation 6 — What is coordination polymerization?

**Purpose:** Build the controlled coordination-polymerization model.

Required content:
- preliminary monomer coordination;
- chain carrier / coordination complex;
- catalyst precursor, activator/cocatalyst language where needed;
- insertion/polyiinsertion concepts only at useful depth;
- avoid full organometallic catalytic cycles;
- `TAB-015-002`.

### Investigation 7 — What does “Ziegler–Natta” mean in modern engineering language?

**Purpose:** Reconcile industrial language with controlled terminology.

Required content:
- heterogeneous catalysis coordination polymerization;
- industrial/historical `Ziegler–Natta` usage;
- heterogeneous catalyst environment as a source of possible site diversity, only as a hypothesis until measured;
- no claim that a named catalyst family uniquely fixes MWD, branching or pipe properties;
- primary-evidence gate before named PE/PP outcome examples.

### Investigation 8 — What changes with homogeneous / metallocene coordination polymerization?

**Purpose:** Explain homogeneous coordination routes without a superiority narrative.

Required content:
- homogeneous catalysis coordination polymerization;
- metallocene polymerization as a subset;
- defined-site / site-environment concepts only where source-supported;
- stereoregularity/comonomer-placement hypotheses;
- comparison with heterogeneous routes must remain bounded and non-ranking;
- `FIG-015-004`.

### Investigation 9 — How do process variables become molecular-architecture hypotheses?

**Purpose:** Execute the main primary-literature evidence gate.

Candidate variables requiring direct evidence before named claims:
- temperature;
- monomer/comonomer feed;
- pressure/concentration context;
- hydrogen / chain transfer;
- residence/reaction history;
- reactor/process configuration when materially relevant.

Mandatory case matrix columns:
`system | variable | measured architecture output | property if measured | confounders | supported conclusion | unsupported conclusion | transferability`.

Assets:
- `TAB-015-003`;
- `TAB-015-004`;
- `FIG-015-005`;
- `EX-015-001`.

### Investigation 10 — What may the engineer infer from polymerization provenance, and where must the inference stop?

**Purpose:** Close the engineering decision boundary.

Required content:
- final `FIG-015-006`;
- final chapter workflow `WF-015-001`;
- checklist `CL-015-001`;
- supplier/process-provenance evidence request `EX-015-003`;
- `TAB-015-005` downstream chapter ownership crosswalk;
- explicit stop-rule;
- clean handoff to Chapter 016.

## 6. Quantitative-treatment decision rules

The chapter is not equation-driven. Include a quantitative relationship only if all are true:

1. it explains a mechanism or process-to-architecture bridge;
2. assumptions are short enough to state explicitly;
3. the equation does not duplicate Chapter 016;
4. symbols and units can be controlled;
5. the result is not presented as a commercial-grade property prediction.

Potential candidates:
- chain-polymerization rate notation / propagation coefficient only where needed;
- idealized Carothers relationship for balanced difunctional polycondensation/polyaddition teaching, subject to review;
- chain-transfer relationship only if an authoritative/primary source and a clear engineering use justify it.

## 7. Required assets register

| ID | Asset | Owning Investigation | Development rule |
|---|---|---:|---|
| FIG-015-001 | Polymerization classification map | 2 | Must show historical terminology warning |
| FIG-015-002 | Chain-polymerization lifecycle | 3 | Must show optional termination/transfer branches |
| FIG-015-003 | Radical polymerization at engineering-use depth | 4 | Conceptual, not a complete mechanistic scheme |
| FIG-015-004 | Coordination catalyst environment map | 6–8 | Finalized after Inv. 8 |
| FIG-015-005 | Same monomer, different chain-building histories | 9 | Requires evidence-bounded examples |
| FIG-015-006 | Process provenance to engineering evidence chain | 10 | Final chapter decision figure |
| TAB-015-001 | Controlled terminology/common misuse | 2 | IUPAC-controlled |
| TAB-015-002 | Route/active species/output/evidence limit | 6 | No performance ranking |
| TAB-015-003 | Process variable → hypothesis → characterization | 9 | Primary-evidence gated |
| TAB-015-004 | Controlled polymer-family examples | 9 | No commercial-grade ranking |
| TAB-015-005 | Downstream ownership crosswalk | 10 | Match BOOK_STRUCTURE working architecture |
| EX-015-001 | Same ethene, different PE outcome hypotheses | 9 | Direct evidence required for retained specifics |
| EX-015-002 | Why “addition polymer” is insufficient | 2 | Terminology exercise |
| EX-015-003 | Supplier process-history evidence request | 10 | Evidence workflow exercise |
| WF-015-001 | Polymerization provenance → engineering decision | 10 | Final workflow |
| CL-015-001 | Before inferring behaviour from polymerization route | 10 | Final checklist |

## 8. Review gates

1. **Definition of Ready:** CDB + this outline + Standards/Evidence Plan complete.
2. **Investigation 2 terminology gate:** IUPAC classification wording checked before canonical use.
3. **Investigation 4 mechanism gate:** radical mechanism reviewed before advancing.
4. **Investigation 6–8 coordination terminology gate:** current IUPAC chain-polymerization terminology checked.
5. **Investigation 9 primary-literature gate:** named process/catalyst effects cannot enter without direct evidence matrix.
6. **Pre-integration Technical Review.**
7. **Final full-file Technical Review.**
8. **Final claim-level Standards/Evidence Review.**
9. **Editorial/Style + Desk Test.**
10. **Human Approval Gate before merge.**

## 9. Definition-of-Ready conclusion

This outline fully instantiates the approved CDB into a sequential engineering-development path. Together with the active `references.md` Evidence Plan and the CDB, it supplies the required purpose, outcomes, inputs, standards/evidence path, Investigation structure, assets, exclusions and acceptance criteria required by `governance/Definition-of-Ready.md`.
