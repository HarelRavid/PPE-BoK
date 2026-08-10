# Chapter 002 — Review Package

**Chapter:** 002 — The Engineering Decision Process  
**Review framework:** `docs/BOOK-WIDE-REVIEW-PLAN.md`  
**Branch:** `chapter-013-redevelopment`  
**Status:** REVIEW COMPLETE — REVISION APPROVAL PENDING  
**Disposition:** AUGMENT

## 1. Review basis

Reviewed sources:

- `chapters/chapter-002-engineering-decision-process/chapter.md`;
- approved Chapter 001 Rev 1.0 for upstream system-definition and interface boundary;
- `chapters/chapter-003-understanding-industrial-processes/chapter.md` for downstream process-definition handoff;
- `docs/BOOK-WIDE-REVIEW-PLAN.md` for review criteria.

No external source was used to introduce new technical or normative claims. The review assesses the manuscript's decision architecture, internal consistency, scope, practical usefulness, and handoff to adjacent chapters.

---

## 2. Gate A — File and evidence inventory

### Present

- `chapter.md` — complete readable draft.

### Not present before this review

- `review.md`;
- `references.md`;
- `notes.md`;
- figures or decision-workflow assets.

### Evidence dependency

Chapter 002 is methodological rather than calculation-heavy. It contains no equations, design coefficients, standards clauses, or numerical acceptance criteria. The principal evidence burden is therefore internal consistency and disciplined separation between:

- mandatory requirements;
- engineering constraints;
- assumptions;
- uncertainty;
- evidence;
- verification;
- engineering judgement;
- final decision/disposition.

**Gate A result: PASS WITH METHOD-CONTROL GAPS.**

---

## 3. Gate B — Architecture and scope review

### 3.1 What the chapter already does well

The chapter has a strong canonical core:

1. engineering as management of competing constraints;
2. decisions under uncertainty;
3. a six-step practical framework;
4. distinction between data, information and engineering knowledge;
5. standards plus judgement;
6. experience in context;
7. common decision errors;
8. continuation of decisions after commissioning.

This is the correct role for Chapter 002. It should become the book's **canonical decision-process chapter**, not merely one introductory chapter among several.

### 3.2 Boundary with Chapter 001

Chapter 001 now defines the engineering object: the complete piping system, its boundaries, interfaces, life-cycle conditions, and pre-decision system questions.

Chapter 002 should not repeat that system definition. It should answer the next question:

> Given a defined engineering object and context, how is a defensible decision made, documented, verified and reopened when conditions change?

The current draft largely respects this boundary.

### 3.3 Boundary with Chapter 003

Chapter 003 owns detailed process understanding and the conversion of process conditions into piping implications. Chapter 002 should therefore identify “establish requirements” as a formal decision-process step and then hand off to Chapter 003 and later Design Basis chapters for how the required inputs are developed.

The current Step 2 is directionally correct but too compact to make this handoff explicit.

### 3.4 Missing canonical decision-process functions

If Chapter 002 is to govern the rest of the book, the current six steps need several additions or clarifications:

1. **decision statement / scope** — exactly what is being decided and what is outside the decision;
2. **assumptions and unknowns register** — assumptions must be visible and separable from established facts;
3. **evidence status** — distinguish verified input, provisional input, missing input, and controlled hold;
4. **comparison criteria** — alternatives should be assessed against explicit criteria rather than informal preference;
5. **decision disposition** — GO / CONDITIONAL GO / NO-GO (or equivalent) with conditions;
6. **verification ownership** — what must be checked, by whom, and at what stage;
7. **reopen triggers** — changes in Design Basis, standards, product, operation, evidence, failure history, or assumptions should reopen the decision;
8. **decision record** — another competent engineer should be able to reconstruct why the decision was made.

These are not a new framework. They are the missing closure mechanics of the existing framework.

**Gate B result: PASS — AUGMENTATION REQUIRED.**

---

## 4. Gate C — Technical / methodological review

### 4.1 Strong content to retain

The following should remain substantially intact:

- engineering as selection among competing constraints rather than search for a single perfect answer;
- uncertainty cannot be eliminated, only identified and managed;
- problem definition precedes solution selection;
- alternatives should be generated before committing to a preferred solution;
- risk/failure modes belong before final verification;
- verification increases confidence but does not create certainty;
- standards and judgement are complementary;
- experience must be interpreted in context;
- decision errors include confirmation bias, experience bias, specification bias, single-factor optimization, unchallenged assumptions, and false precision;
- decisions continue throughout the life cycle.

### 4.2 Statements requiring sharper boundaries

#### “The engineer must optimize the complete system”

The intent is good, but “optimize” can imply a mathematically global optimum that is rarely demonstrated in engineering practice.

**Recommended action:** use “select a defensible system solution across competing constraints” or “balance and justify competing constraints” unless an actual optimization method is being used.

#### Wall-thickness example

The same example was qualified in Chapter 001. Here it again states that increasing wall thickness may improve pressure capacity while reducing flexibility, increasing fusion time, and raising cost. This is useful, but should remain explicitly context-dependent.

**Recommended action:** align wording with Chapter 001 to avoid presenting the trade-off as universal.

#### “Most problems have more than one technically possible solution”

Generally useful, but not universally true when legal, process, geometric, or qualification constraints are severe.

**Recommended action:** “Many engineering problems…” rather than “Most”.

### 4.3 The six-step framework is incomplete at the decision-output end

Current framework:

1. define the problem;
2. establish requirements;
3. identify constraints;
4. generate alternatives;
5. evaluate risks/failure modes;
6. verify the decision.

The key missing distinction is between **verification** and **decision closure**.

A calculation or standards check verifies evidence or reasoning. It does not itself state the decision.

Recommended canonical chain:

`Define → Requirements → Constraints → Alternatives → Evaluate → Verify → Decide/Document → Monitor/Reopen`

This preserves the existing six steps and adds closure/reopen control rather than replacing the framework.

### 4.4 Assumptions need first-class status

The opening correctly identifies hidden assumptions as a major source of failure, and the summary calls for explicit assumptions, but the framework never creates a formal place to record them.

Recommended rule:

> An assumption is an input with uncertainty attached to it, not a fact.

Each material assumption should have:

- statement;
- basis;
- sensitivity/significance;
- validation owner or action;
- status;
- reopen trigger if invalidated.

The chapter does not need a full project template, but it needs the concept.

### 4.5 Verification should be classified

The current list — calculations, standards checks, independent review, testing, simulation, prototypes, qualification records, operating experience — is good.

It should distinguish at least:

- **input verification** — are the data and assumptions credible?;
- **method verification** — is the chosen method applicable and correctly used?;
- **result verification** — are calculations/results correct?;
- **independent review** — can another competent reviewer reproduce/accept the reasoning?;
- **validation against reality** — testing, inspection, operating evidence, commissioning, or later field evidence where applicable.

This is an important book-wide distinction because later chapters will use the word “verification” frequently.

### 4.6 Risk evaluation should avoid pseudo-quantification

The current questions “How likely is it?” and “What are the consequences?” are appropriate. The chapter should explicitly note that qualitative risk screening is acceptable when numerical probability is not supported, and that false numerical precision is itself a decision error.

This aligns with Section 2.7 and avoids contradiction.

**Gate C result: PASS WITH CANONICAL-METHOD AUGMENTATION.**

---

## 5. Gate D — Standards / evidence review

The chapter should remain largely standards-neutral. It is not the place to reproduce specific codes or risk standards.

However, it should inherit and apply the governance established in Chapter 000:

- mandatory requirements cannot be traded away during alternative comparison;
- standards applicability and edition are inputs to the decision, not afterthoughts;
- missing clause-level evidence remains a controlled hold where it materially affects the decision;
- engineering judgement cannot override mandatory requirements;
- manufacturer guidance and operating experience must be interpreted within their scope.

### 5.1 Constraint hierarchy

Step 3 currently groups laws, standards, client specifications, materials, installation limitations, space, schedule and budget in one list. These are not all equivalent constraints.

Recommended distinction:

- **non-negotiable constraints:** law, regulation, mandatory code, adopted safety requirement;
- **project/design constraints:** owner/project requirements, required service life, access, geometry, interfaces;
- **commercial/execution constraints:** availability, cost, schedule, construction limits.

A commercial constraint cannot justify violating a mandatory requirement.

### 5.2 Evidence treatment

The chapter should add a compact evidence state model:

- verified;
- accepted with bounded uncertainty;
- provisional / assumption;
- missing / hold;
- superseded / invalidated.

That would operationalize Chapter 000's evidence philosophy without duplicating it.

**Gate D result: AUGMENT.**

---

## 6. Gate E — Editorial and academic review

### Strengths

- concise;
- logical progression;
- strong engineering voice;
- practical examples;
- useful bias list;
- no premature technical detail.

### Editorial gaps

1. No explicit reader outcomes.
2. The chapter lacks one visual canonical workflow.
3. The six-step framework has no visible decision-output/disposition.
4. Section 2.4 on data/information/knowledge is useful but currently somewhat detached from the decision workflow; it should connect to evidence quality and input maturity.
5. Section 2.5 should reference the requirement hierarchy established in Chapter 000 rather than restate it generically.
6. Section 2.8 is too short given its importance; it should introduce **reopen triggers** and management of change in principle.
7. No worked micro-example showing how a bad question becomes a defensible decision record.

A full numerical example is unnecessary. A compact qualitative decision example would materially improve teaching value.

**Gate E result: PASS — TARGETED AUGMENTATION.**

---

## 7. Gate F — Gap Register

| Gap ID | Severity | Finding | Required disposition |
|---|---|---|---|
| GAP-002-01 | High | Six-step framework lacks explicit decision closure/disposition | Add decide/document step with GO / CONDITIONAL GO / NO-GO or equivalent |
| GAP-002-02 | High | No assumptions/unknowns register concept despite hidden assumptions being a stated failure source | Add first-class assumption management rule |
| GAP-002-03 | High | No reopen triggers / management-of-change logic | Expand post-commissioning section into monitor/reopen principle |
| GAP-002-04 | High | Mandatory, project and commercial constraints are blended | Add constraint hierarchy and non-negotiable boundary |
| GAP-002-05 | Medium | Verification is broad but not classified | Add input/method/result/independent/field-validation distinction |
| GAP-002-06 | Medium | No evidence maturity/status model | Add verified / bounded uncertainty / provisional / hold / invalidated states |
| GAP-002-07 | Medium | Alternative comparison has no explicit comparison criteria | Require declared criteria tied to requirements and risk |
| GAP-002-08 | Medium | No canonical decision record / traceability requirement | Add minimum decision-record contents |
| GAP-002-09 | Medium | Risk questions can invite unsupported numerical probability | Explicitly permit qualitative risk and warn against false precision |
| GAP-002-10 | Medium | “Optimize complete system” wording implies stronger optimization claim than shown | Replace with defensible balancing/selection language |
| GAP-002-11 | Low | Wall-thickness example needs consistency with Chapter 001 qualification | Normalize wording |
| GAP-002-12 | Low | “Most problems” is too universal | Change to “many engineering problems” |
| GAP-002-13 | Low | No reader outcomes | Add concise outcomes |
| GAP-002-14 | Medium | No canonical decision-process visual | Add `FIG-002-001` workflow placeholder |
| GAP-002-15 | Medium | No compact worked decision example | Add one non-numerical worked example from vague question to disposition/reopen trigger |
| GAP-002-16 | Low | Weak downstream handoff to process-definition chapter | Add handoff to Chapter 003 and subsequent requirements/Design Basis chapters |

---

## 8. Disposition

# AUGMENT

The current chapter is structurally sound and contains the correct core decision logic. It should **not** be rewritten from scratch.

The central improvement is to convert the current six-step sequence from a good introductory framework into the **canonical, traceable decision process used throughout PPE-BoK**.

The revision should preserve the concise character of the chapter while adding closure, evidence state, assumption control and reopen logic.

---

## 9. Proposed Chapter 002 Rev 1.0 scope

Recommended revision package:

1. Retain the opening, constraints/uncertainty framing, data-information-knowledge concept, standards/judgement section, experience section and bias list.
2. Add short reader outcomes.
3. Normalize “optimize” to “balance/select a defensible solution across competing constraints.”
4. Expand the practical framework to the canonical chain:
   - **Step 1 — Define the decision and boundary**;
   - **Step 2 — Establish requirements and success criteria**;
   - **Step 3 — Identify constraints and non-negotiables**;
   - **Step 4 — Record assumptions, unknowns and evidence status**;
   - **Step 5 — Generate credible alternatives**;
   - **Step 6 — Evaluate alternatives, risks and failure modes**;
   - **Step 7 — Verify inputs, methods and results**;
   - **Step 8 — Decide and document disposition**;
   - **Step 9 — Monitor and reopen when triggers occur**.
5. Add `FIG-002-001 — Canonical PPE-BoK Engineering Decision Process` showing the loop rather than a one-way sequence.
6. Add a compact constraint hierarchy: mandatory / project-design / commercial-execution.
7. Add a lightweight evidence-state model.
8. Add an assumption-control rule and minimum assumption metadata.
9. Add a decision record containing at minimum:
   - decision statement;
   - Design Basis / requirements used;
   - governing constraints;
   - assumptions and holds;
   - alternatives considered;
   - key evidence and calculations;
   - risks/failure modes;
   - verification performed;
   - final disposition and conditions;
   - reopen triggers.
10. Use **GO / CONDITIONAL GO / NO-GO** as the default book-level disposition language where appropriate, while allowing domain-specific equivalents in later chapters.
11. Add one short worked qualitative example, such as converting “Which pipe should I buy?” into a traceable material/system selection decision with a controlled hold.
12. Expand Section 2.8 to explain that a decision is reopened when the Design Basis, standards path, product, operating envelope, assumptions, evidence, failure history or modification state changes.
13. Add an explicit handoff to Chapter 003: the decision process requires a valid process definition before requirements can be considered complete.
14. Keep standards content generic; do not turn the chapter into a risk-standard or compliance-code chapter.

---

## 10. Approval gate

No substantive change has been made to `chapter.md` in this review.

If the revision scope above is approved, prepare **Chapter 002 Rev 1.0** as a complete proposed replacement, present the integrated text for review, and only after explicit approval commit the revised manuscript before proceeding to Chapter 003.
