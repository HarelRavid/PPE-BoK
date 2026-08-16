# Chapter 016 — Standards and Evidence Plan

**Working chapter:** 016 — Polymer Chain Architecture: Molar Mass, Distribution, Branching and Crosslinking  
**PDS baseline:** 1.0  
**Status:** Active Engineering-Development Evidence Plan  
**Research checkpoint:** 2026-08-16

## 1. Evidence objective

Chapter 016 converts polymer-chain architecture from informal supplier/industry language into controlled quantities, measurement routes and bounded engineering hypotheses.

The evidence system must separate:

1. controlled terminology;
2. measurement-method scope;
3. measured architecture state;
4. architecture→downstream-property evidence;
5. product/application qualification.

No architecture descriptor is a piping acceptance criterion by itself.

## 2. Evidence classes

| Class | Meaning | Permitted use |
|---|---|---|
| A | Current authoritative standard / official terminology source | controlled term, method scope, status |
| B | IUPAC Recommendation / recognized scientific recommendation | definitions, quantitative conventions, network terminology |
| C | Directly reviewed primary research | named architecture/material/property claims |
| D | Established academic reference / review | teaching context and navigation |
| E | Manufacturer / secondary source | provenance lead only unless independently verified |

## 3. Authoritative terminology path

### S016-001 — IUPAC Gold Book, 5th ed., online v5.0.0

Role: current controlled terminology source. Terms to verify at authoring/final validation include:

- molar mass — Gold Book 12214;
- molar-mass average — 12215;
- number-average molar mass — 12216;
- mass-average molar mass — 12217;
- molar-mass dispersity — 12224;
- dispersity — 12226;
- branch / branched polymer / branch point;
- crosslink / crosslinking;
- network / network polymer / physical network.

Controlled quantitative convention:

`M_m ≡ M_w`

and

`Đ_M = M_m / M_n`.

The term `polydispersity index` is not preferred controlled terminology.

### S016-002 — IUPAC Recommendations 2014, published 2015

**Definitions of terms relating to individual macromolecules, macromolecular assemblies, polymer solutions, and amorphous bulk polymers.**  
DOI: `10.1515/pac-2013-0201`.

Role: primary source for molar-mass averages/distributions and related macromolecular quantities.

### S016-003 — IUPAC Recommendations 2009

**Dispersity in polymer science.**  
DOI: `10.1351/PAC-REC-08-05-02`.

Role: terminology basis for dispersity and replacement of the misleading `polydispersity index` expression.

### S016-004 — IUPAC Glossary of Basic Terms in Polymer Science, Recommendations 1996

Role: foundational architecture terminology.

### S016-005 — IUPAC Recommendations on sols, gels and networks, 2007

Role: network/physical-network/crosslinking terminology where applicable.

## 4. ISO characterization path

### S016-006 — ISO 472:2013 + Amd 1:2018

Role: plastics vocabulary cross-check only. Publication-time lifecycle recheck required because the current ISO lifecycle remains under revision/replacement activity.

### S016-007 — ISO 16014-1:2019

**Plastics — Determination of average molecular weight and molecular weight distribution of polymers using size-exclusion chromatography — Part 1: General principles.**

Status checkpoint 2026-08-16: Published / Confirmed, stage 90.93.

Scope use:

- establishes SEC as a route for average molecular weight/molar-mass distribution determination;
- distinguishes polymer-standard calibration routes from SEC-LS using absolute molecular-weight data;
- does not authorize treating all SEC outputs as method-independent absolute quantities.

### S016-008 — ISO 16014-2:2019 through ISO 16014-5:2019

Role: controlled SEC family supporting universal-calibration, low/high-temperature and light-scattering contexts. Exact part scope shall be checked before each authoring claim; detailed procedure is deferred to Part V.

### S016-009 — ISO 18177:2025

**Plastics — Test method for estimation of the short chain branching distribution of semicrystalline ethylene 1-olefin copolymers — Differential scanning calorimetry (DSC).**

Status checkpoint: Published, stage 60.60.

Scope control:

- applicable to estimation of short-chain branching distribution of semicrystalline ethylene/1-olefin copolymers;
- quantitative calculation stated for ethylene/1-butene, ethylene/1-hexene and ethylene/1-octene copolymers;
- do not generalize to long-chain branching or unrelated polymer families.

### S016-010 — ISO 10147:2011

**Pipes and fittings made of crosslinked polyethylene (PE-X) — Estimation of the degree of crosslinking by determination of the gel content.**

Status checkpoint 2026-08-16: Published / Confirmed, stage 90.93.

Controlled use:

- establishes gel-content-by-solvent-extraction logic for PE-X pipes/fittings;
- does not establish complete network topology or a universal crosslink-density quantity.

### S016-011 — ISO 1133-1:2022

**Plastics — Determination of the melt mass-flow rate (MFR) and melt volume-flow rate (MVR) of thermoplastics — Part 1: Standard method.**

Status checkpoint: Published, stage 60.60.

Controlled use:

- MFR/MVR are determined under specified temperature/load conditions;
- ISO notes these methods are used primarily in quality control and may not correlate directly with normal processing behaviour;
- MFR/MVR are not direct measurements of `M_n`, `M_m`, full MMD or branching topology.

### S016-012 — ISO 1133-2:2011

Role: MFR/MVR route for materials sensitive to time-temperature history and/or moisture. Current ISO page states the version remains current after review; lifecycle should be rechecked at final validation.

## 5. Investigation-specific evidence plan

### Investigation 1

Evidence level: A/B + stable explanatory science.

Permitted claims:

- polymerization provenance is upstream of architecture;
- architecture is a measurable material state, not a catalyst/process label;
- architecture descriptors route the engineer toward characterization and downstream verification.

No named architecture→property trend is authorized here.

### Investigation 2

Evidence level: A/B.

Mandatory controls:

- molar mass versus relative molecular mass/molecular-weight language;
- units for molar mass;
- degree-of-polymerization boundary;
- polymer population rather than one unique scalar for non-uniform polymers.

### Investigation 3

Evidence level: A/B; quantitative review mandatory.

Required source checks:

- S016-001 through S016-003.

Required equations:

- `M_n`;
- `M_m ≡ M_w`;
- `Đ_M = M_m/M_n`.

Every equation must identify weighting and units.

### Investigation 4

Evidence level: A/B plus ISO method scope.

Required source checks:

- S016-007/S016-008.

Authoring boundary:

- explain measurement principle/calibration logic;
- do not reproduce procedural details that belong to lab-method chapters;
- distinguish relative calibration from SEC-LS logic.

### Investigation 5

Evidence level: B/D for generic architecture definitions; C for named resin-specific claims.

No `branching → property` directional rule yet.

### Investigation 6

Evidence level: A/B for terminology; ISO scope for S016-009; C for named PE/PP architecture claims.

Primary-evidence gate triggers for statements about:

- specific SCB/LCB level in a named resin;
- catalyst/process route producing a measured branching distribution;
- architecture differences between named pipe grades.

### Investigation 7

Evidence level: A/B + S016-010.

PE-X claims must distinguish:

- gel content;
- inferred degree of crosslinking in the standard context;
- crosslink density/topology claims requiring other evidence.

### Investigation 8

Evidence level: B/D stable polymer physics.

If a named polymer/system is claimed to have a specified entanglement density or architecture-driven rheological response, direct evidence is required.

### Investigation 9

Evidence level: C mandatory for every retained named architecture→behaviour case.

Candidate case domains:

- architecture → morphology/crystallization;
- architecture → melt/rheology;
- architecture → diffusion/permeation;
- architecture → creep;
- architecture → SCG;
- architecture → fusion/interdiffusion.

Each case must record:

`system | architecture variable | measurement | downstream measurement | confounders | supported conclusion | unsupported conclusion | transferability`.

### Investigation 10

Evidence level: synthesis of already validated evidence. No new named technical case by default.

## 6. Primary-literature gate register

No architecture→property case is pre-approved merely because it is common in polymer engineering.

Before Investigation 9 authoring, each candidate is marked:

- `CANDIDATE`;
- `DIRECT SOURCE LOCATED`;
- `DIRECT SOURCE REVIEWED`;
- `ARCHITECTURE VARIABLE ACTUALLY MEASURED`;
- `DOWNSTREAM OUTPUT ACTUALLY MEASURED`;
- `CONFOUNDERS DISPOSITIONED`;
- `SUPPORTED CLAIM BOUNDED`;
- `TRANSFERABILITY DISPOSITIONED`;
- `APPROVED FOR AUTHORING`.

## 7. Quantitative evidence policy

Authorized definitions are not design equations.

For every numerical example:

- source or synthetic-data status must be explicit;
- units must be explicit;
- weighting basis must be explicit;
- `M_m`, `M_n` and dispersity must not be treated as complete distribution descriptors;
- no numerical threshold may be converted into pipe acceptance without an applicable product/material standard or direct qualification evidence.

## 8. Prohibited shortcuts

Do not author any of the following as universal rules:

- `higher molar mass = better pipe`;
- `broader MWD = easier processing`;
- `more branching = tougher`;
- `lower density proves more branching`;
- `metallocene implies narrow MWD`;
- `high gel content = ideal crosslink network`;
- `low MFR uniquely means high molecular weight`;
- `architecture metric = SCG/lifetime/fusion acceptance`.

## 9. Current source-status checkpoint — 2026-08-16

- IUPAC 2014/2015 macromolecule terminology remains the direct source behind current Gold Book molar-mass entries.
- IUPAC 2009 dispersity Recommendation remains the terminology source replacing `polydispersity index` with dispersity language.
- ISO 16014-1:2019 is current and confirmed at stage 90.93; the 2019 SEC family is the active method path.
- ISO 18177:2025 is published at stage 60.60.
- ISO 10147:2011 is current/confirmed at stage 90.93.
- ISO 1133-1:2022 is published; ISO 1133-2:2011 remains current on the ISO catalogue and carries a lifecycle recheck hold for final publication validation.

## 10. Definition-of-Ready evidence disposition

**PASS for entering Engineering Development.**

The terminology path, method-scope path, quantitative controls and primary-literature gates are sufficiently defined to begin Investigation 1. Investigations that require named architecture/property claims remain independently gated until the required primary evidence is reviewed.
