# Investigation 10 — What Can Chemistry Tell Us, and Where Must the Engineer Stop?

> **Controlled authoring file.** This temporary development artifact is authorized by the Investigation 9 Authoring Review. Its approved content shall be integrated into `chapter.md` and this file removed before PR #12 is eligible for Ready-for-Review.

**Scope boundary:** chapter-closing evidence discipline only. No new named-material property claim and no new numerical design value are introduced.

---

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

# 10.5 WF-014-001 — Chemical structure to engineering decision boundary — final chapter version

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

# 10.6 CL-014-001 — Before inferring engineering behaviour from a chemical structure

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

# 10.7 TAB-014-004 — Downstream chapter ownership crosswalk

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

# 10.8 What “first principles” should mean in engineering practice

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

# 10.9 Common mistakes / Failure Lens

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

# 10.10 Verification — the chapter desk test

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

# 10.11 Engineering decision from Investigation 10

> **Use chemistry to identify mechanisms, variables, evidence needs and plausible failure hypotheses. Do not promote molecular reasoning into engineering acceptance until the relevant property has been measured, transferability has been justified, the actual material/product state is qualified and the application Design Basis has been checked.**

This closes the first-principles scope of Chapter 014.

The reader now has the bridge:

`atom → electron structure → bonding → intermolecular interactions → carbon chemistry → local geometry / σπ → ethene → idealized PE backbone → structure-property hypothesis → measured evidence → qualification boundary`

The next chapter begins where this one intentionally stops:

> **How does polymerization transform monomers into real macromolecular architectures, and how do catalysts and process history shape the material that the engineer ultimately receives?**

That question belongs to Working Chapter 015.

---

# Chapter 014 engineering closure — candidate text

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
