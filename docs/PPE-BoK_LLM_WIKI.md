# PPE-BoK – LLM Wiki, Writing Charter and Knowledge Architecture

> **Purpose:** This document is the master operating guide for writing, reviewing, organizing and maintaining the *Plastic Piping Engineering Body of Knowledge (PPE-BoK)*. It is intended for human authors, reviewers and AI/LLM collaborators. When any other note, template or chapter conflicts with this document, this document governs until explicitly revised.

---

# 1. Mission of the Book

The PPE-BoK is not only a book about pipes. It is a systems-engineering reference that teaches engineering thinking through thermoplastic piping and process systems.

The book shall connect:

- polymer science;
- pressure piping design;
- mechanics, creep, fatigue and fracture;
- hydraulics and heat/mass transfer;
- single-, two- and three-phase flow;
- slurries, suspensions and solids transport;
- process safety, operability and maintainability;
- inspection, QA/QC, failure investigation and remaining life;
- standards, industrial practice and academic research.

The primary objective is not to impress by volume of information, but to make the reader say:

> **“Now I understand why this happens, how to analyse it, and when the model may fail.”**

---

# 2. Core Writing Philosophy

## 2.1 Physics before formulas

Every technical topic should normally be developed in this order:

1. What is physically occurring?
2. Why does it occur?
3. What forces, transport mechanisms or material behaviours govern it?
4. What is observable in a laboratory or plant?
5. How is it measured?
6. Which models and correlations exist?
7. Under which assumptions are they valid?
8. What engineering decisions follow?
9. What happens if the effect is ignored?

A formula must never appear as an unexplained recipe.

## 2.2 Systems, not isolated components

Each topic must be connected to the complete system:

\[
Material + Geometry + Joints + Supports + Process + Environment + Operation + Maintenance
\]

A pipe is simultaneously:

- a pressure boundary;
- a structural beam or shell;
- a thermally expanding body;
- a hydraulic flow path;
- part of a safety system;
- an inspectable and maintainable asset.

## 2.3 Teach engineering judgement

The book must teach the reader to ask:

- What do I know?
- What do I not know?
- Which assumption am I making?
- Is that assumption justified?
- Which mechanism dominates?
- Is the selected model inside its validated range?
- How could I independently verify the result?

## 2.4 Examples are illustrations, not the theory

Alkaline electrolysers, KOH, Ni(OH)₂ and H₂/O₂ are important recurring examples because they demonstrate complex multiphase behaviour. They are **case examples**, not the sole subject of the book.

Whenever the electrolyser example is used, the text should make clear that the underlying physics can apply to other systems with similar boundary conditions, such as bubble columns, reactors, fermentation, hydrometallurgy, mining slurries, wastewater and other gas–liquid–solid processes.

---

# 3. Scientific Integrity and Evidence Rules

## 3.1 No unsupported certainty

The book shall not present assumptions, plausible inferences or engineering intuition as experimentally proven conclusions.

## 3.2 Two-source rule

Every material technical claim that is not elementary physics or mathematics should, where reasonably possible, be verified against at least two independent sources.

Preferred combinations:

- standard + peer-reviewed paper;
- standard + recognised engineering handbook;
- two independent peer-reviewed papers;
- handbook + professional organisation guidance;
- two leading manufacturer design manuals, clearly labelled as manufacturer guidance.

## 3.3 Source hierarchy

Use the following order of authority, while recognising that relevance and scope still matter:

1. International/national standards and regulatory documents.
2. Fundamental physical laws and recognised engineering textbooks.
3. Peer-reviewed academic papers and authoritative review articles.
4. Professional organisations and industry guidance.
5. Manufacturer engineering manuals and validated product data.
6. Conference papers, theses and technical reports.
7. Informal or secondary sources only as navigation aids, never as the sole support for a critical claim.

## 3.4 Evidence classification

Every significant statement should be mentally or explicitly classified as one of the following:

### A — Established Knowledge
Supported by standards, fundamental theory or strong multi-source consensus.

### B — Engineering Consensus
Widely accepted in industry and professional literature, but not necessarily a mandatory standard requirement.

### C — Evidence-Based Hypothesis
Supported by relevant studies or analogous systems, but not fully established for the exact system discussed.

### D — Knowledge Gap
Direct evidence was not found, is insufficient or is contradictory.

### E — Engineering Inference
A transparent inference derived from established principles and cited evidence. It must be labelled as an inference, not a conclusion.

## 3.5 Standard requirement versus recommendation

Never present:

- a manufacturer recommendation as a standard requirement;
- a common practice as a legal obligation;
- a correlation as a physical law;
- a laboratory result as universally transferable to an industrial plant.

Use explicit labels such as:

- **Standard requirement**
- **Regulatory requirement**
- **Industry recommendation**
- **Manufacturer guidance**
- **Empirical correlation**
- **Mechanistic model**
- **Engineering inference**

---

# 4. Applicability and Transferability Review

Whenever a study or model is cited, record or discuss:

- where the study was performed: electrode surface, flow channel, pipe, vessel, pilot or plant;
- geometry and characteristic dimensions;
- fluid and material properties;
- pressure and temperature range;
- phase fractions and concentrations;
- steady or transient operation;
- laboratory, pilot or industrial scale;
- whether the result is directly applicable, conditionally transferable or only qualitatively informative.

A result measured in a 2 mm electrochemical channel must not be applied directly to a DN50 process pipe without an explicit scale and applicability discussion.

---

# 5. Standard Chapter Architecture

Not every chapter must contain every section, but this is the default structure.

## 5.1 Metadata block

```yaml
chapter: 000
title_he: ""
title_en: ""
part: ""
status: draft
language: he
technical_level: foundational | intermediate | advanced
primary_domains: []
review:
  physics: pending
  standards: pending
  academic: pending
  equations: pending
  units: pending
  examples: pending
  editorial: pending
last_updated: YYYY-MM-DD
```

## 5.2 Recommended chapter sequence

1. Purpose and scope.
2. Why the topic matters.
3. Physical phenomenon.
4. Fundamental mechanisms and forces.
5. Definitions and terminology.
6. Governing equations and models.
7. Assumptions and validity range.
8. Measurement and test methods.
9. Industrial design implications.
10. Operation, maintenance and safety implications.
11. Worked examples.
12. Common mistakes and failure modes.
13. Design review questions.
14. Evidence and uncertainty review.
15. References and cross-references.

---

# 6. Mandatory Formula Rules

Every equation must include:

- equation in a clear standard form;
- definition of every symbol;
- units for every dimensional variable;
- assumptions;
- scope of validity;
- source or derivation basis;
- warning about common misuse where relevant.

Each important equation should answer four questions:

1. Where does it come from?
2. When may it be used?
3. When should it not be used?
4. What is the most common error when applying it?

Numerical examples must be recalculated independently and checked for dimensional consistency and order of magnitude.

---

# 7. Standard Knowledge Boxes

Use these boxes consistently and sparingly.

## Engineering Insight
A deep practical interpretation grounded in established engineering principles.

## Think Like an Engineer
Questions that guide reasoning before calculation.

## Field Note
A concise plant or inspection observation. It must not replace evidence.

## Engineering Mistake
A realistic misuse of a model, design practice or assumption.

## Reality Check
What an operator, inspector or engineer would observe in the field.

## If You Remember Only One Thing
The core concept of the chapter in one short statement.

## What We Know / What We Do Not Know
Separates established knowledge, probable interpretation, active research and gaps.

## Engineering Inference
A clearly labelled inference based on cited principles but not directly proven in the exact application.

## Source and Validity Range
Origin, test conditions and limits of a commonly used value, threshold or correlation.

## The Next Question
The logical question that leads to the next topic or chapter.

## Engineer’s Challenge
A scenario that asks what information is missing or whether a model is applicable, rather than merely requesting substitution into a formula.

---

# 8. Reviews Required for Every Chapter

## 8.1 Physics review

- Are the mechanisms described correctly?
- Are analogies explicitly identified as analogies?
- Are conservation laws respected?
- Are simplifications visible?

## 8.2 Standards review

- Are the correct editions used?
- Is the standard relevant to the material, service and geography?
- Is the wording a requirement, recommendation or informative note?
- Are quotation and copyright limits respected?

## 8.3 Academic review

- Are at least two relevant independent sources used for major claims?
- Are contradictory findings acknowledged?
- Is the experimental scale documented?
- Are review papers supported by primary studies where necessary?

## 8.4 Equation and units review

- Symbols defined?
- Units consistent?
- Mathematical transcription correct?
- Calculation independently repeated?
- Validity range stated?

## 8.5 Industrial applicability review

- Can the result guide an actual decision?
- Does it address normal, start-up, shutdown and abnormal cases where relevant?
- Are inspection and maintenance implications included?
- Does it distinguish component behaviour from system behaviour?

## 8.6 Objectivity review

- Are facts separated from interpretations?
- Are uncertainty and gaps visible?
- Is the tone free from exaggerated certainty?
- Is one industry example dominating the general theory?

---

# 9. Multiphase and Slurry Writing Protocol

This subject receives enhanced scrutiny.

## 9.1 Required distinctions

Always distinguish between:

- single-phase liquid or gas;
- gas–liquid flow;
- liquid–solid suspension/slurry;
- gas–liquid–solid flow;
- homogeneous versus heterogeneous suspension;
- local versus averaged void fraction;
- superficial versus actual phase velocity;
- steady-state versus transient behaviour;
- cell/channel findings versus process-piping findings.

## 9.2 Model hierarchy

When relevant, compare:

- homogeneous/no-slip model;
- slip-ratio model;
- drift-flux model;
- separated-flow model;
- Euler–Euler/two-fluid model;
- Euler–Lagrange model;
- population-balance model;
- CFD models and their closure assumptions.

Do not imply that the most complex model is automatically the most reliable. Input-data quality and validation govern usefulness.

## 9.3 Required transient cases

For multiphase and slurry systems, consider:

- normal continuous operation;
- load increase/decrease;
- start-up;
- normal shutdown;
- prolonged shutdown;
- settled-bed restart;
- gas-pocket release;
- loss of circulation;
- loss of agitation;
- flushing and drain-down;
- blocked or partially blocked line;
- emergency isolation.

## 9.4 Representative example

The recurring representative case may be written as:

\[
KOH + Ni(OH)_2 + H_2/O_2
\]

It must be used to illustrate general gas–liquid–solid principles. Where no direct published data exist for the exact mixture and geometry, this must be stated explicitly.

---

# 10. Dimensionless-Number Protocol

Each dimensionless-number chapter should include:

1. The physical mechanisms being compared.
2. Intuitive but qualified explanation.
3. Formal definition.
4. Characteristic length/velocity selection.
5. Derivation or origin through non-dimensionalisation where appropriate.
6. Validity and limitations.
7. Interaction with other dimensionless groups.
8. Common misuse.
9. Industrial observation.
10. Scale-up implications.

Never define Reynolds number as “the turbulence number,” Weber number as “the bubble-breakup number,” or any dimensionless group as a universal predictor. It is a ratio of mechanisms; outcomes depend on the entire system.

---

# 11. Scale-Up Protocol

Scale-up chapters must distinguish:

- geometric similarity;
- kinematic similarity;
- dynamic similarity;
- thermal similarity;
- mass-transfer similarity;
- electrochemical similarity where relevant.

The central question is:

> Which governing physics must be preserved, and which cannot be preserved simultaneously?

Never assume that geometric enlargement preserves performance. Explicitly examine how area, volume, residence time, phase distribution, bubble/particle population and heat/mass transfer change with scale.

---

# 12. Case Study Rules

Case studies must be used in good taste and only where they add understanding.

For every real case:

- verify the event with at least two reliable sources where possible;
- separate confirmed facts from reported allegations or interpretations;
- state the exact equipment/system involved;
- avoid invented details;
- explain the mechanism and lesson, not merely the story;
- state whether the lesson is transferable to thermoplastic piping.

Hypothetical cases must be labelled **Worked Scenario** or **Illustrative Example**, never presented as real incidents.

---

# 13. Language and Style

## 13.1 Working language

The development edition is written in Hebrew, with professional English terms in parentheses on first use where helpful.

Examples:

- תחזוקתיות (Maintainability)
- שבר נפחי גז (Void Fraction)
- מהירות שטחית (Superficial Velocity)

Equations and internationally recognised symbols remain in Latin/Greek notation.

## 13.2 Tone

- Professional and readable.
- Detailed without unnecessary repetition.
- Avoid promotional or absolute language.
- Avoid rhetorical overstatement.
- Use complete sentences.
- Explain jargon before relying on it.

## 13.3 Analogies

Analogies are permitted to build intuition but must be labelled as simplified illustrations and followed by the precise engineering interpretation.

---

# 14. Index and Taxonomy Definitions

Each chapter should be tagged against one or more controlled indexes.

## 14.1 Material index

- PE80 / PE100 / PE100-RC
- PP-H / PP-R / PP-RCT
- PVC-U / PVC-C / CPVC
- PVDF
- ECTFE
- PTFE / PFA / FEP
- GRP/FRP where comparative context is required
- Elastomers, liners and metallic transition components

## 14.2 Mechanism index

- pressure stress;
- creep;
- fatigue;
- fracture;
- buckling;
- thermal expansion;
- permeation;
- chemical ageing;
- UV/weathering;
- erosion/abrasion;
- vibration;
- electrostatics;
- fire;
- fluid transients;
- phase separation;
- settling/deposition;
- plugging.

## 14.3 Lifecycle index

- concept;
- design basis;
- detailed design;
- procurement;
- fabrication;
- joining;
- installation;
- inspection;
- pressure testing;
- commissioning;
- operation;
- shutdown/restart;
- maintenance;
- modification/MOC;
- failure investigation;
- remaining life;
- decommissioning.

## 14.4 Evidence index

- standard;
- regulation;
- handbook;
- peer-reviewed paper;
- review paper;
- manufacturer manual;
- field data;
- case study;
- engineering inference;
- knowledge gap.

## 14.5 Application index

- water and wastewater;
- chemical processing;
- hydrogen and electrolysis;
- chlor-alkali;
- mining and hydrometallurgy;
- semiconductor chemicals;
- pharmaceutical/bioprocess;
- food and beverage;
- energy and utilities;
- gas service;
- corrosive and hazardous fluids;
- slurry and multiphase systems.

---

# 15. Repository Structure and File Naming

Recommended chapter folder:

```text
chapters/chapter-078-maintainability/
├── README.md          # chapter text
├── references.md      # standards, papers, books, DOI and applicability
├── review.md          # technical review checklist and decisions
├── notes.md           # unresolved questions and future additions
└── figures/           # original figures and source notes
```

File naming:

- `chapter-NNN-short-title`
- figures: `fig-NNN-XX-short-description.svg`
- equations: `eq-NNN-XX`
- tables: `table-NNN-XX`
- case studies: `case-NNN-XX`

PDF is a release output, not the source of truth. Markdown is the source format.

---

# 16. Review Status Vocabulary

Use only these statuses unless this guide is revised:

- `idea`
- `outline`
- `draft`
- `technical-review`
- `source-review`
- `editorial-review`
- `ready-for-release`
- `released`
- `revision-required`

A chapter is not `ready-for-release` until all critical review fields are complete.

---

# 17. Definition of Done for a Chapter

A chapter is complete only when:

- scope is clear;
- core physics is correct;
- major factual claims are sourced;
- formulas and units are checked;
- assumptions and limits are stated;
- examples are recalculated;
- industrial relevance is explained;
- common errors are included;
- uncertainty and knowledge gaps are visible;
- cross-references are added;
- references and review files are updated;
- language and numbering are consistent.

---

# 18. Instructions for an LLM Continuing the Book

Before drafting or revising a chapter, the LLM must:

1. Read this document.
2. Read the chapter template and technical-review template.
3. Read the current `BOOK_STRUCTURE.md`.
4. Read adjacent chapters for terminology and continuity.
5. Search standards and academic literature when the claim is not stable or is technically specialised.
6. Avoid relying on conversational memory when the repository contains the authoritative text.
7. Preserve Hebrew writing with English technical terminology where useful.
8. Never manufacture citations, standards clauses, experimental values or case details.
9. Mark uncertainty explicitly.
10. Update `references.md`, `review.md` and `notes.md` together with the chapter.

When asked to continue writing, write the actual content rather than repeatedly proposing new structural ideas, unless a genuine technical gap prevents correct continuation.

---

# 19. Governance and Change Control

Changes to this master guide should be deliberate and documented.

When changing a major rule:

- describe the reason;
- identify affected chapters/templates;
- create an issue or review note;
- update templates if necessary;
- avoid silently changing terminology or evidence standards.

This document will evolve, but it should remain the stable “constitution” of the PPE-BoK project.

---

# 20. Master Principle

> **Understand the phenomenon, verify the evidence, expose the assumptions, define the model limits, and only then convert the knowledge into an engineering decision.**
