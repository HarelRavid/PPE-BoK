# Chapter 014 — Pre-Integration Editorial / Style Review

**Date:** 2026-08-14  
**PR:** #12  
**Branch:** `chapter-014-engineering-development`  
**Logical manuscript reviewed:** canonical `chapter.md` Investigations 1–8 + approved Investigation 9 and 10 authoring candidates  
**PDS source:** `docs/PDS/Style-Guide.md` Baseline 1.0  
**Disposition:** **CONDITIONAL PASS — NO STRUCTURAL REWRITE REQUIRED**

## 1. Review objective

Determine whether the complete logical Chapter 014 reads as a practical PPE-BoK engineering chapter rather than a general chemistry textbook, and identify bounded editorial actions that should be applied during or after canonical integration without reopening the approved technical scope.

This is a pre-integration review. The final Editorial / Style gate remains open until Investigations 9–10 are integrated into the canonical manuscript and the resulting continuous file is reviewed.

## 2. Overall editorial assessment

**Conditional Pass.**

The chapter has a clear engineering identity despite its foundational-science subject matter.

Its strongest editorial pattern is repeated consistently:

`scientific concept → mechanism value → evidence boundary → engineering decision / common mistake`

The manuscript generally avoids the two failure modes most likely for this topic:

1. becoming a generic introductory chemistry textbook;
2. turning molecular explanation into unsupported materials-design guidance.

No chapter-wide restructure is recommended.

## 3. Style Guide compliance

### 3.1 Language and tone

**PASS.**

The chapter uses professional engineering English, defines specialist chemistry terms before relying on them, and repeatedly distinguishes fact, hypothesis, measured evidence and engineering acceptance.

The tone is direct rather than promotional. Scientific uncertainty and transferability limits are normally stated explicitly.

### 3.2 Heading hierarchy

**PASS SUBJECT TO CANONICAL-INTEGRATION NORMALIZATION.**

The existing canonical file follows the PDS structure:

- chapter-level framing;
- `# Investigation N — Engineering Question`;
- `##` / `###` within Investigations.

The two temporary authoring files intentionally use standalone headings and must be normalized when integrated. This is a mechanical integration task, not an editorial redesign.

### 3.3 Tables

**PASS.**

The important tables serve engineering purposes rather than merely repeating prose. In particular:

- `TAB-014-001` distinguishes bonding/interaction models and invalid direct conclusions;
- final `TAB-014-002` converts molecular observations into mechanism/evidence questions;
- `TAB-014-003` presents controlled teaching cases with explicit prohibited transfers;
- `TAB-014-004` routes downstream questions to the owning PPE-BoK chapters/Parts.

The pre-integration Technical Review finding that the Investigation 6 early table shall become an unnumbered preliminary teaching table is editorially appropriate and prevents duplicate controlled asset identity.

### 3.4 Figures / placeholders

**PASS WITH PUBLISHING NOTE.**

The manuscript specifies what each figure must communicate rather than requesting decorative illustrations.

During final asset production, each figure record should also state its controlled source status explicitly, preferably:

- `Original PPE-BoK scientific schematic` where drawn from first-principles concepts;
- `concept based on cited terminology/recommendation` where appropriate;
- no copying of protected standards graphics unless permission is separately established.

This is a publishing/source-control action, not an authoring blocker.

### 3.5 Workflows, examples and checklist

**PASS.**

`EX-014-001` and `EX-014-002` are appropriate for a chapter with little legitimate numerical calculation. They test interpretation and evidence discipline rather than inventing arithmetic merely to satisfy an example quota.

The final `WF-014-001` and `CL-014-001` materially improve engineering usability and should remain near the end of the chapter.

### 3.6 Standards references

**PASS FOR AUTHORING / FINAL VALIDATION STILL OPEN.**

The text distinguishes terminology authority from design authority and does not reproduce protected standards text. Current edition/lifecycle statements are explicitly treated as authoring records subject to final validation.

## 4. Navigation / five-minute-use test

**PASS FOR LOGICAL MANUSCRIPT.**

The `Engineering Quick Navigation` section gives a reader a direct route to:

- atoms / chemical entities;
- electrons / orbitals / electronegativity;
- primary bonding;
- noncovalent interactions;
- carbon structural versatility;
- hybridization / sigma / pi;
- ethene → PE bridge;
- structure → property hypotheses;
- final evidence / qualification boundary.

After integration, add direct asset references to the quick-navigation layer only if they improve retrieval; do not overload the opening section with a full asset index.

The final `TAB-014-004` is the key exit-navigation asset and should be preserved.

## 5. Bounded editorial findings

### ED-014-01 — Reduce duplicated workflow exposition after final `WF-014-001` exists

**Priority:** medium; post-integration editorial action.

Investigation 1 currently contains a detailed seven-step molecular-inference verification sequence. Investigation 9 develops a related evidence chain, and Investigation 10 contains the final controlled workflow.

The repetition is pedagogically defensible during development, but the final integrated manuscript should avoid presenting three apparently independent workflows.

**Recommended action:**

- retain Investigation 1 as the early conceptual preview;
- retain Investigation 9 as the evidence demonstration using Cases A–C;
- make Investigation 10 the only formally numbered `WF-014-001`;
- where possible, shorten the early Investigation 1 sequence and explicitly state that the final controlled workflow appears in Investigation 10.

Do not remove the early mechanism/evidence warning itself.

### ED-014-02 — Check repeated `chemistry is not design acceptance` warnings for diminishing returns

**Priority:** medium.

The same safety message appropriately recurs across Investigations, but the final continuous manuscript should distinguish purposeful reinforcement from near-verbatim repetition.

**Recommended rule:** retain the warning where it prevents a specific misconception unique to the Investigation; compress it where the paragraph only repeats the generic chapter rule.

This is a tightening pass, not a scope reduction.

### ED-014-03 — Preserve engineering payoff after dense scientific passages

**Priority:** high editorial principle, no current blocker.

Investigations 2–7 contain the densest terminology. Their engineering decision / verification endings are important because they convert chemistry into a practical reader action.

Do not shorten these endings merely to reduce page count. If text must be tightened, prefer removing repeated introductory language before removing the engineering payoff.

### ED-014-04 — Control terminology typography consistently

**Priority:** low/medium.

After integration, perform one consistency pass for:

- `sp`, `sp2`, `sp3` styling;
- `sigma` / `pi` versus `σ` / `π` display conventions;
- `C–C`, `C=C`, `C≡C` bond notation;
- `ethene` / established industrial `ethylene` usage;
- `van der Waals` capitalization;
- `hydrogen bond` / `H-bond` abbreviation after first definition;
- `repeat unit`, `monomeric unit`, `CRU` distinction.

Technical meaning takes precedence over typography.

### ED-014-05 — Keep the evidence ladder visibly non-normative

**Priority:** high; already captured technically as TR-014-03 / E10-01.

The final six-level ladder is one of the chapter's most useful teaching tools, but it must be visually and verbally identified as a **PPE-BoK reasoning framework** rather than an ISO/IUPAC classification.

The required sentence from the technical review should remain adjacent to the ladder, not buried in references.

### ED-014-06 — Figure source-status labels during publishing

**Priority:** later publishing action.

For each `FIG-014-xxx`, add source status to the asset record. The preferred default for Chapter 014 is original PPE-BoK scientific schematic derived from cited concepts, not reproduction of external figures.

### ED-014-07 — Final front-matter synchronization

**Priority:** required after final technical/evidence reviews.

Current front matter correctly says `engineering-development` and has pending review fields. Do not prematurely change those fields now.

After canonical integration and final reviews, synchronize:

- status;
- physics/scientific review;
- standards/evidence review;
- academic/evidence review;
- examples;
- editorial;
- last updated date.

## 6. Engineering-application balance

**PASS FOR SUBJECT TYPE.**

The PDS approximately 60% application / 40% explanation target is non-binding and should not be forced numerically on this foundational chapter.

Chapter 014 earns its engineering identity through:

- repeated `what can/cannot be concluded` boundaries;
- material-specific evidence cases rather than generic chemistry examples only;
- engineering decisions at the end of Investigations;
- the final evidence workflow;
- the checklist;
- downstream chapter routing.

Adding artificial calculations would make the chapter less, not more, engineering-useful.

## 7. Common-mistake architecture

**PASS.**

The recurring `Common mistakes / Failure Lens` sections are useful because each Investigation addresses a distinct failure mode, for example:

- atom/element/molecule category errors;
- planetary-orbit interpretation;
- pure ionic/covalent dichotomy;
- one-dimensional intermolecular-force ranking;
- tetravalency-only carbon explanation;
- literal hybrid-orbital interpretation;
- monomer→polymer arrow treated as mechanism;
- primary paper converted into universal material rule.

Final editorial tightening should preserve these distinct mistakes while removing only truly duplicated generic warnings.

## 8. Chapter opening / closing coherence

**PASS.**

The opening question asks why materials all called `plastics` can behave differently and what an engineer may legitimately infer from atomic/molecular structure.

Investigation 10 answers that same question by closing at the evidence/qualification boundary and handing polymerization/process–structure questions to Working Chapter 015.

The opening and closing therefore form a coherent engineering arc.

## 9. Pre-integration Editorial / Style disposition

**CONDITIONAL PASS — NO STRUCTURAL REWRITE REQUIRED.**

Canonical integration may proceed without reopening chapter architecture.

After integration, the final Editorial / Style Review should focus only on:

1. ED-014-01 — consolidate workflow hierarchy;
2. ED-014-02 — remove redundant generic warnings while preserving mechanism-specific cautions;
3. ED-014-04 — terminology/notation consistency;
4. ED-014-05 — keep PPE-BoK evidence ladder visibly non-normative;
5. asset/source-status and front-matter synchronization;
6. continuous-manuscript flow and cross-references.

No new technical research is required by this editorial review.

## 10. Current gate state

- CDB: approved.
- Engineering Development: Investigations 1–10 authored as controlled candidates.
- Investigation 9 evidence gate: PASS.
- Investigation 9 authoring review: PASS.
- Investigation 10 / chapter-closure review: PASS.
- Pre-integration Technical Review: CONDITIONAL PASS.
- Standards/Evidence Validation for current authoring layer: PASS with publication lifecycle holds.
- Pre-integration Editorial / Style Review: **CONDITIONAL PASS**.
- Canonical integration: OPEN mechanical hold.
- Final full-file Technical Review: pending integration.
- Final Editorial / Style Review: pending integration.
- Human Approval / merge: not authorized.
