# Investigation 10 — What Architecture Information Should the Engineer Request, and Where Must Inference Stop?

## 1. Engineering question

A project specification asks whether two thermoplastic pipe compounds are “molecularly equivalent.”

One supplier provides:

- resin family;
- MFR;
- density;
- the phrase `high molecular weight`.

Another provides:

- `M_n`, `M_m/M_w` and the full MMD;
- SEC method/calibration information;
- branching characterization;
- relevant morphology and product-qualification data.

Which dataset is configuration-ready engineering evidence?

The second is stronger not because more numbers are always better, but because each claim is tied to a defined quantity, measurement route and downstream evidence boundary.

Investigation 10 converts Chapter 016 into a reusable workflow for supplier evaluation, laboratory requests, root-cause investigation and design evidence review.

---

## 2. The Chapter 016 stop rule

The governing chapter rule is:

> **Stop the inference when the next conclusion requires a quantity that has not been measured or qualified.**

Examples:

- catalyst label available, architecture not measured → stop at architecture hypothesis;
- `M_w` available, full MMD required by the hypothesis → stop and request MMD;
- MMD available, branching unknown → do not infer branch topology;
- branching measured, morphology unknown → do not claim crystallinity/tie-molecule state;
- architecture/morphology characterized, SCG not tested → do not claim SCG qualification;
- resin characterization available, pipe product not qualified → do not claim system suitability.

The stop rule protects the project from both under-testing and over-interpreting sophisticated laboratory data.

---

## 3. WF-016-001 — Architecture claim to engineering decision

**Final workflow.**

`Step 1 — Identify the claim`

→ What is being asserted: family, provenance, architecture, property, product qualification or application suitability?

`Step 2 — Name the controlled quantity`

→ DP, `M_n`, `M_m/M_w`, MMD, `Đ_M`, SCB descriptor, LCB descriptor, gel content, physical/covalent network descriptor, MFR/MVR, or another defined quantity?

`Step 3 — Identify the measurement and calibration basis`

→ SEC route, detector/calibration, NMR, SSA-DSC, gel extraction, rheology, product test, etc.

`Step 4 — Separate direct measurement from inference`

→ Was the architecture variable measured directly, estimated by a calibrated method, inferred from a correlated property or merely predicted from process provenance?

`Step 5 — State the downstream hypothesis`

→ What mechanism/property is architecture expected to influence?

`Step 6 — Obtain the downstream measurement`

→ Morphology, rheology, permeability, creep, fracture/SCG, joining or product qualification as appropriate.

`Step 7 — Check transferability`

→ Same material family, composition, morphology/process history, method and application conditions?

`Step 8 — Apply product/application requirements`

→ Applicable material, pipe, fitting, joining, design and service requirements.

`Step 9 — Make the engineering decision`

→ Accept, reject, request more evidence, or classify the conclusion as mechanism-level only.

**Control:** A downstream step cannot be waived merely because an upstream architecture descriptor appears favourable.

---

## 4. Supplier architecture-data request

When architecture is technically relevant, the request should be targeted rather than asking for “all molecular data.”

### 4.1 Material identity and provenance

Request:

- polymer family and grade/compound designation;
- resin versus final compound distinction;
- comonomer type where relevant;
- additives/fillers/carbon black where relevant to the comparison;
- lot/batch and production state;
- known polymerization/process provenance only as contextual information.

Do not treat process provenance as measured architecture.

### 4.2 Molar-mass population

Where relevant request:

- `M_n`;
- `M_m/M_w`;
- `Đ_M`;
- complete MMD, not only one average;
- statement of whether the distribution is unimodal/multimodal only when supported by the measured distribution;
- SEC/GPC method;
- solvent and test temperature;
- detector configuration;
- conventional/universal/SEC-LS calibration basis;
- calibration standards;
- dissolution/insoluble-fraction note;
- whether values are relative, absolute within method scope, or apparent/calibration dependent.

### 4.3 Branching

Where relevant request:

- SCB versus LCB explicitly;
- branch quantity and normalization basis;
- branch chemistry/comonomer basis;
- branch distribution where the engineering hypothesis depends on distribution;
- measurement method;
- direct versus inferred status;
- material/method scope.

### 4.4 Crosslink/network state

For crosslinked systems request, as applicable:

- crosslinking route/provenance;
- gel-content result and standard/method;
- specimen/product state tested;
- any independent network/crosslink-density measurement if the engineering conclusion genuinely requires it;
- soluble/insoluble fraction distinction where MMD is also reported.

Do not ask gel content to answer a question about complete network topology.

### 4.5 Correlated/QC variables

Request MFR/MVR, density, rheology or other production-QC data when useful, but label them correctly:

`architecture-sensitive / downstream / QC evidence`

rather than:

`direct MMD / branching topology measurement`.

---

## 5. EX-016-002 — Converting “high molecular weight” into an evidence request

Supplier statement:

> “Our pipe resin has very high molecular weight and therefore excellent long-term crack resistance.”

### 5.1 Uncontrolled interpretation

A weak engineering response is:

> High molecular weight is good for SCG, so the claim is acceptable.

This skips multiple evidence layers.

### 5.2 Controlled interpretation

Break the claim into two statements.

**Architecture statement:**

> `high molecular weight`.

Questions:

1. Which quantity — `M_n`, `M_m/M_w`, viscosity-average or other?
2. Units?
3. SEC/GPC or another method?
4. Calibration/detector basis?
5. Full MMD available?
6. SCB/LCB/comonomer architecture available?
7. Final resin or final compounded pipe material?

**Performance statement:**

> `excellent long-term crack resistance`.

Questions:

1. Which SCG/product test?
2. Specimen taken from resin plaque or actual pipe?
3. Standard and edition?
4. Test temperature/stress/environment?
5. Pass/failure criterion?
6. Product qualification evidence?

### 5.3 Engineering disposition

Until both layers are supported:

`high molecular weight → plausible architecture clue`

and:

`excellent SCG → unverified performance claim`.

After both layers are supplied, architecture can help interpret the SCG evidence but does not replace it.

---

## 6. EX-016-003 — MFR is not molecular architecture

Two PE pipe compounds are tested at the same applicable MFR condition and both report:

`MFR = 0.25 g/10 min`.

Can the engineer conclude that the materials have the same `M_n`, `M_w`, MMD and branching architecture?

No.

### 6.1 What the equal MFR legitimately supports

Within the stated method/test conditions, the two materials produced the same reported melt mass-flow rate.

That can be useful for:

- QC comparison;
- process consistency checks;
- screening of significant batch changes when the product specification uses the metric.

### 6.2 What the equal MFR does not establish

It does not uniquely establish:

- `M_n`;
- `M_m/M_w`;
- `Đ_M`;
- distribution shape/modes;
- SCB;
- LCB;
- entanglement topology;
- crystallinity;
- SCG;
- fusion performance.

Different molecular architectures can produce similar scalar melt-flow results.

### 6.3 Controlled next action

If the engineering question is molecular equivalence, request architecture measurements.

If the engineering question is process/product conformity and the applicable standard specifies MFR, use MFR for that defined conformity question.

Do not make one test answer a different question simply because the value is convenient.

---

## 7. TAB-016-004 — Architecture feature → hypothesis → required verification

| Architecture information | Plausible downstream hypothesis | Direct architecture evidence needed | Downstream verification needed before engineering conclusion |
|---|---|---|---|
| different `M_n` / `M_m` / MMD | different mobility, entanglement/interdiffusion or rheological response | validated molar-mass measurement with method/calibration | rheology, joining, creep/fracture or other property relevant to claim |
| different SCB content/distribution | different packing/crystallization opportunity | SCB measurement within method/material scope | morphology + property/transport/fracture test relevant to claim |
| measured LCB | altered long-time/extensional rheological response | LCB-sensitive direct/combined characterization | rheology/processing test under relevant conditions |
| higher gel fraction in PE-X | greater method-defined insoluble/network fraction | ISO 10147 or applicable gel-content method | applicable PE-X product/property requirement; network details if specifically needed |
| entanglement-sensitive model parameter | different transient network dynamics | method/model with stated assumptions | rheology/creep/fracture/joining evidence depending on decision |
| same MFR | similar specified melt-flow result | ISO 1133 applicable test | architecture measurement if molecular equivalence is claimed |
| same density | similar bulk density under stated method | density measurement | architecture/morphology measurements if branch/crystal equivalence is claimed |

**Rule:** The final column cannot be deleted merely because the architecture hypothesis is mechanistically convincing.

---

## 8. TAB-016-005 — Downstream ownership crosswalk

| Question created by Chapter 016 | Primary downstream owner | Why Chapter 016 stops |
|---|---|---|
| How did branching change crystallinity, lamellae or tie-molecule state? | Chapter 017 | morphology must be measured; architecture is not morphology |
| How do architecture and morphology interact with `T_g`, `T_m`, thermal expansion or thermal mobility? | Chapter 018 | thermal transitions/thermophysical response need their own measurements/models |
| How do MMD/LCB/entanglements change creep, relaxation or melt rheology? | Chapter 019 | time-dependent constitutive behaviour exceeds architecture-definition scope |
| How does architecture affect SCG/RCP/fatigue/ESC/fracture? | Chapter 020 | fracture/failure metrics and lifetime evidence are downstream |
| How should a particular resin/compound be qualified? | Chapters 021 onward / product standards | family/compound requirements are material-specific |
| How should SEC/DSC/other methods be executed and validated? | Part V | detailed laboratory procedure/uncertainty/instrument control |
| How does architecture influence butt/electrofusion interdiffusion and weld qualification? | Part VII | joining process physics and acceptance require process-specific evidence |
| How is pipe wall/design pressure calculated? | Part VIII | architecture is not a design allowable |

---

## 9. FIG-016-006 — Architecture evidence chain

**Final figure specification.**

Create a horizontal evidence-chain figure with seven boxes:

1. `Provenance / label`
2. `Controlled architecture quantity`
3. `Measurement + calibration`
4. `Measured architecture state`
5. `Downstream hypothesis`
6. `Downstream property / product qualification`
7. `Engineering decision`

Between boxes 4 and 5 place a visible warning gate:

`NO DIRECT PERFORMANCE INFERENCE`.

Under boxes 2–4 add examples:

`M_n / M_m / MMD / Đ_M / SCB / LCB / gel / network`.

Under box 6 add:

`morphology / rheology / transport / creep / fracture / joining / product standard`.

Footer:

`Evidence strength is limited by the weakest unsupported transition.`

No material ranking or acceptance value shall be drawn into the figure.

---

## 10. CL-016-001 — Before using chain-architecture information in a piping decision

**Final checklist.**

Before an architecture statement enters a calculation, specification, RCA conclusion, material-selection decision or supplier acceptance, confirm:

- [ ] The material/grade/lot/product state is identified.
- [ ] The statement is classified as provenance, architecture, property or qualification evidence.
- [ ] The controlled quantity is named.
- [ ] Symbol and units/dimensionless status are correct.
- [ ] For polymer populations, the averaging basis/distribution is identified.
- [ ] `M_n`, `M_m/M_w`, MMD and `Đ_M` are not treated as synonyms.
- [ ] `PDI` is mapped to the actual defined quantity before use.
- [ ] SEC/GPC method, temperature, solvent, detector and calibration basis are known when relevant.
- [ ] Relative/apparent versus SEC-LS/absolute-within-method status is understood.
- [ ] Sample dissolution/insoluble fraction is considered.
- [ ] SCB and LCB are distinguished.
- [ ] Branch quantity includes a normalization basis and method.
- [ ] Branch amount is not treated as branch distribution.
- [ ] Branch point, covalent crosslink, physical junction and entanglement are distinguished.
- [ ] Gel content is not treated as complete crosslink density/topology.
- [ ] MFR/MVR is not treated as a direct MMD measurement.
- [ ] Density is not treated as a direct branch-distribution measurement.
- [ ] Any named architecture→property claim has direct primary evidence.
- [ ] Confounders/co-varying architecture/morphology variables are listed.
- [ ] Transferability to the current material/state/method/application is stated.
- [ ] The required downstream property/product test has been identified.
- [ ] No architecture descriptor has been converted directly into pressure rating, lifetime, SCG, permeability or joining acceptance.
- [ ] The applicable product/design/service standard remains controlling.

If any critical item is `no`, the engineering action is normally:

`REQUEST EVIDENCE / QUALIFY INFERENCE / STOP`.

---

## 11. Failure lens — how architecture data misleads good engineers

### Failure mode 1 — sophisticated number, undefined quantity

A six-significant-digit SEC value is not strong evidence if the averaging/calibration basis is unknown.

### Failure mode 2 — correct quantity, wrong material state

Resin-pellet architecture may not fully describe the final extruded/aged/processed compound state relevant to a failure investigation.

### Failure mode 3 — correct architecture, missing morphology

Branching and MMD create possibilities; processing and crystallization create actual semicrystalline morphology.

### Failure mode 4 — correlation treated as qualification

A molecular trend is not an applicable product test.

### Failure mode 5 — one supplier metric used because competitors do not disclose more

Information availability is not a scientific reason to promote MFR/density into architecture measurements.

### Failure mode 6 — architecture data used to rationalize a decision already made

Evidence review should test competing hypotheses, not merely decorate a preferred supplier/material selection.

---

## 12. Supplier-data maturity levels

For practical procurement/engineering review, classify the package:

### Level A — descriptive only

Family/trade-name/process labels, MFR/density only.

Use: routine identification/QC context; weak architecture evidence.

### Level B — architecture averages

Defined `M_n` / `M_m` / `Đ_M`, method stated.

Use: stronger population comparison; still incomplete if shape/branching matters.

### Level C — distribution/topology characterization

Full MMD plus appropriate branching/network data with method/calibration.

Use: architecture comparison and mechanism hypotheses.

### Level D — linked downstream evidence

Architecture characterization plus morphology/rheology/transport/fracture/joining data for the same or demonstrably comparable material state.

Use: bounded structure-property interpretation.

### Level E — product/application qualification

Applicable pipe/fitting/joint/design/service evidence added.

Use: engineering acceptance within the governing standard/application.

The maturity levels are a PPE-BoK evidence-routing framework, **not an ISO classification**.

---

## 13. Chapter engineering closure

Chapter 016 began with a simple-sounding question: what is the architecture of a polymer chain?

The answer is not one molecular-weight number.

An engineering description can require:

- degree of polymerization;
- molar-mass averages;
- full MMD;
- dispersity;
- branch presence/count/length/distribution/topology;
- crosslink/network state;
- entanglement/physical connectivity;
- measurement method and calibration.

More importantly, Chapter 016 established what those descriptors **cannot** prove by themselves.

The final reasoning chain is:

`polymerization provenance`

→ `measured chain architecture`

→ `morphology / mobility / physical-state hypothesis`

→ `direct downstream property measurement`

→ `product qualification`

→ `engineering decision`.

That chain is the handoff to Chapter 017.

---

## 14. Handoff to Chapter 017

Chapter 016 defined the molecular population and connectivity.

Chapter 017 asks what happens when those chains organize in the bulk polymer:

- amorphous versus semicrystalline material;
- crystallinity;
- lamellae;
- spherulites;
- amorphous regions;
- tie molecules where applicable;
- molecular mobility within morphology;
- morphology effects on downstream behaviour.

The controlled handoff is:

`chain architecture → crystallization/packing possibilities`

not:

`chain architecture → guaranteed morphology`.

Chapter 017 must measure and reason about the morphology that was actually produced.