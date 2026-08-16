# Investigation 7 — What Are Crosslinks and Polymer Networks?

## 1. Engineering question

A PE-X datasheet reports a gel content and describes the material as crosslinked.

Can the engineer translate that directly into:

- a crosslink density;
- a complete molecular network drawing;
- weldability;
- pressure rating;
- long-term strength?

No.

Crosslinking changes the connectivity class of the polymer architecture, but the language and measurement must remain controlled.

Investigation 7 separates:

`branch point → crosslink → covalent network / physical network → gel-content evidence → downstream qualification`.

Controlling sources:

- S016-001 / S016-005 for IUPAC network terminology;
- S016-010 for ISO 10147:2011 PE-X gel-content scope.

---

## 2. A branch point is not automatically a crosslink

IUPAC defines a **branch point** as the point on a polymer chain at which a branch is attached.

IUPAC defines **crosslinking** more narrowly as a reaction/interaction involving existing macromolecules that forms a small region from which at least four chains emanate.

The IUPAC crosslinking definition adds a particularly useful boundary:

A reactive chain end attaching to an internal reactive site on another linear macromolecule can create a branch point without being regarded as a crosslinking reaction.

Therefore:

`branch point ≠ crosslink by definition`.

This is the connectivity transition that Chapter 016 needs before discussing PE-X.

---

## 3. Crosslink: a connectivity region, not merely “one bond”

IUPAC defines a **crosslink** as a small region in a macromolecule from which at least four chains emanate, formed through reaction or interaction involving existing macromolecules.

The crosslink can be:

- an atom;
- a group of atoms;
- a set of branch points connected by bonds/groups/oligomeric chains;
- in broader usage, a physical interaction/junction.

Therefore a cartoon showing one simple bond between two lines is only a schematic representation.

The controlled engineering question is:

> **What type of junction exists, how permanent is it over the relevant time/temperature/chemical environment, and how was it characterized?**

---

## 4. Use “covalent crosslink” when permanence matters

The Gold Book notes that most crosslinks are covalent structures, while the term is also used for weaker interactions, crystallite-related junctions and even physical entanglements.

That breadth can create engineering ambiguity.

PPE-BoK therefore applies this language rule:

- use **covalent crosslink** when permanent chemical connectivity is intended;
- use **physical junction / physical network** when reversible/non-covalent connectivity is intended;
- use **entanglement** when topological interpenetration is intended;
- avoid an unqualified `crosslink` where the distinction changes the engineering conclusion.

---

## 5. Network: connectivity extending through the macromolecular structure

IUPAC describes a polymer **network** as a highly ramified macromolecular structure containing many paths through the macromolecule to the macroscopic phase boundary.

If the permanent paths are covalent, the term **covalent network** may be used.

If the network paths rely at least partly on physical interactions that can be removed to leave individual/non-network macromolecules, the term **physical network** may be used.

This gives Chapter 016 a useful hierarchy:

`branched discrete molecule → increasing connectivity → network architecture`

but it is not a one-number continuum.

A branched polymer can remain soluble as discrete macromolecules.

A sufficiently crosslinked covalent network can contain a macroscopic insoluble fraction because individual chains are no longer separable as independent molecules without breaking network bonds.

---

## 6. Physical network is not a weak version of PE-X

IUPAC defines a **physical network** as a polymer network whose junction points/zones are formed by physically interacting chains and need not be permanent.

Possible physical junctions can include:

- hydrogen bonding;
- other intermolecular association;
- crystalline junction regions;
- chain entanglements.

PE-X crosslinking in piping is normally discussed as chemical/covalent network formation, not simply as a physical network.

Therefore physical-network language is retained for conceptual clarity but must not be used to reinterpret a PE-X gel-content test as a physical-junction measurement.

---

## 7. ISO 10147:2011 — what the piping standard actually measures

ISO 10147:2011 is titled:

**Pipes and fittings made of crosslinked polyethylene (PE-X) — Estimation of the degree of crosslinking by determination of the gel content.**

The official ISO scope states that the method assesses the degree of crosslinking in PE-X pipes and fittings through **gel content determined by solvent extraction**.

Status checkpoint:

- Edition 3;
- published 2011-09;
- current / confirmed at stage 90.93 at the 2026-08-16 check.

This is a directly piping-relevant architecture measurement route.

---

## 8. What gel content means conceptually

In a solvent-extraction context, the polymer sample is exposed to a solvent system intended to remove soluble material under the specified method.

The remaining insoluble fraction is used to estimate the gel/network fraction associated with crosslinking.

At Chapter 016 level, the logic is:

`sample → specified solvent extraction → soluble fraction removed → insoluble gel fraction quantified → degree-of-crosslinking estimate in method context`.

The detailed solvent, extraction apparatus, time, specimen preparation and calculation procedure belong to the full ISO method / Part V.

---

## 9. Gel content is not crosslink density

This is one of the most important evidence boundaries in the chapter.

A gel-content percentage tells the engineer about the fraction that remains insoluble under the specified test route.

It does not uniquely tell the engineer:

- number of covalent crosslinks per unit volume;
- molecular weight between crosslinks;
- spatial distribution of crosslinks;
- network defects;
- dangling-chain population;
- loop/ring defects;
- local crosslink heterogeneity;
- elastically active network-chain density.

Two networks can have similar gel fraction and different detailed topology.

Therefore:

`gel content ≠ complete network architecture`.

---

## 10. Gel content is not a universal quality ranking

A larger gel fraction does not automatically mean a universally better PE-X pipe.

The correct engineering chain is:

`gel-content result → method-defined degree-of-crosslinking evidence → relevant product-standard requirement → downstream property/qualification evidence`.

Chapter 016 does not set acceptance limits for PE-X gel content because those values belong to the applicable material/product standard and product type, not to a general architecture chapter.

---

## 11. Crosslinking changes what SEC can represent

A covalent network can create an insoluble fraction that does not enter an SEC solution analysis as independent dissolved macromolecules.

Therefore a combined architecture investigation may need to distinguish:

- soluble fraction available to SEC;
- insoluble gel/network fraction;
- bulk material as manufactured.

An SEC result on the soluble fraction is not automatically the MMD of the complete original crosslinked specimen.

This is a practical example of the chapter-wide rule:

`measurement scope must travel with the result`.

---

## 12. Crosslinking and fusion are different questions

A thermoplastic fusion process relies on melt-state molecular mobility and interdiffusion.

A covalent network can restrict melt flow/molecular rearrangement compared with an uncrosslinked thermoplastic, but Chapter 016 will not convert that mechanism statement into a joining rule or numeric weldability criterion.

Any claim such as:

`crosslink level → fusion performance`

requires direct joining evidence and belongs to the Investigation 9 evidence gate plus the Part VII joining chapters.

For PE-X specifically, applicable joining methods/product-system approvals must come from the relevant system standards/manufacturer qualification, not from gel content alone.

---

## 13. Network imperfections matter, but are not measured by gel fraction alone

Real networks can contain architectural imperfections such as:

- dangling ends;
- loops;
- uneven junction spacing;
- non-uniform crosslink distribution;
- residual soluble molecules.

The existence of such possibilities is enough to explain why one gel-content scalar cannot fully describe the network.

Chapter 016 does not attempt a rubber-elasticity/network-theory derivation; that would exceed the piping-engineer scope and move into downstream mechanical/rheological treatment.

---

## 14. Preliminary network evidence matrix

| Evidence | Direct conclusion | What remains unknown |
|---|---|---|
| supplier says `crosslinked` | provenance/category claim | crosslink type, degree, distribution, qualification |
| IUPAC-defined covalent crosslink evidence | chemical connectivity exists | network distribution / product performance |
| ISO 10147 gel content | method-defined PE-X gel / degree-of-crosslinking evidence | complete topology / crosslink density / local distribution |
| soluble-fraction SEC | MMD of analyzed soluble fraction under method | insoluble network fraction architecture |
| bulk rheology | network/topology-sensitive response | unique covalent topology without model/evidence |
| product qualification test | property/qualification under specified method | does not independently reconstruct molecular network |

---

## 15. Common mistakes

### Mistake 1 — branch point = crosslink

Failure: IUPAC explicitly distinguishes creation of a branch point from crosslinking.

### Mistake 2 — crosslink = one simple covalent bond

Failure: crosslink is a junction region from which multiple chains emanate; it can be more structurally complex.

### Mistake 3 — all crosslinks are automatically covalent

Failure: IUPAC uses the term more broadly; specify `covalent` when permanence matters.

### Mistake 4 — gel content = crosslink density

Failure: gel fraction does not uniquely quantify network-junction density/topology.

### Mistake 5 — higher gel content = stronger/better pipe

Failure: architecture scalar is not a product quality ranking.

### Mistake 6 — SEC of soluble PE-X fraction = complete network MMD

Failure: insoluble network material is outside the dissolved population being separated.

---

## 16. Verification method

When crosslink/network language appears, classify the evidence:

1. Is the junction covalent or physical?
2. Is the material still described as discrete molecules or a network?
3. Was crosslinking directly characterized or inferred?
4. Is gel content available?
5. Does ISO 10147 apply to the exact PE-X pipe/fitting context?
6. Is the reported value gel fraction, degree-of-crosslinking estimate, or a different network metric?
7. What product/engineering conclusion is being proposed, and what separate qualification supports it?

---

## 17. Engineering decision

Use `covalent crosslink`, `physical network`, `gel content` and `network architecture` as distinct concepts.

For PE-X piping, ISO 10147:2011 provides a controlled gel-content route for estimating degree of crosslinking.

Do not translate gel content into complete crosslink density/topology.

Do not set product acceptance or joining rules from Chapter 016 architecture data alone.

---

## 18. Handoff to Investigation 8

The crosslink definition itself acknowledges a difficult boundary: physical interactions and entanglements can function as junctions in a physical network.

The next question is therefore:

> **What is an entanglement, why can it matter to polymer behaviour, and why should it not be confused with a permanent covalent crosslink?**

Investigation 8 develops FIG-016-005 and preserves Chapter 019 ownership of full rheology/viscoelasticity.