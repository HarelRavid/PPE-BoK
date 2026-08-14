# PPE-BoK Engineering Development Manual

**Baseline:** 1.0

## 1. Knowledge architecture

`Book → Part → Chapter → Investigation → Engineering Assets`

The **chapter** is the primary self-contained knowledge unit. An engineer shall be able to open a chapter without having read the book sequentially and obtain sufficient context, standards navigation and engineering guidance for the chapter scope. Investigations are progressive sections within the chapter and may rely on concepts established earlier in the same chapter.

The current working Part/chapter architecture is controlled by `BOOK_STRUCTURE.md`. Working numbers may remain provisional until final architecture review; the PDS workflow is independent of the final chapter count.

## 2. Chapter development workflow

1. **Chapter Design Brief (CDB)** — define purpose, scope, reader outcomes, Design Basis, standards, required engineering decisions, key assets, exclusions and success criteria.
2. **Technical Outline** — define logical progression of Investigations before drafting prose.
3. **Engineering Development** — write the technical content using the doctrine.
4. **Engineering Assets Integration** — equations, tables, workflows, figures, checklists and worked examples are added where they improve engineering capability.
5. **Technical Review** — verify mechanisms, reasoning, calculations, applicability and decision logic.
6. **Standards Validation** — re-open authoritative standards after authoring is complete and independently verify every standards-derived statement.
7. **Editorial / Style Review** — terminology, consistency, navigation and presentation.
8. **Publication Approval** — chapter enters publication baseline only after all required gates pass.

## 3. Default chapter architecture

A chapter should contain, as appropriate to its subject:

- Metadata and status
- Purpose and scope
- Chapter engineering question
- Why this chapter matters
- Chapter-level Standards Map
- Definitions / terminology where required
- Required Design Basis inputs where relevant
- Progressive Investigations
- Engineering principles and mechanisms
- Governing equations or engineering methods
- Assumptions and validity limits
- Engineering tables / decision tools
- Worked examples (normally 1–2 when useful)
- Common mistakes / Failure Lens
- Design Review Questions / checklist
- Engineering decisions and practical implications
- Chapter summary / closure
- References and controlled cross-references

Not every chapter needs every asset. Do not invent equations or examples merely to satisfy a quota.

## 4. Investigation rule

An Investigation answers one engineering question and advances the chapter. It should not repeatedly restate chapter-level purpose, complete standards lists or definitions already established earlier in the chapter.

A typical Investigation may contain:

- engineering question;
- concise explanation / governing mechanism;
- relevant standards/evidence path where it affects the decision;
- relevant equation, table, figure, workflow or example where needed;
- verification step or practical implication;
- common error / applicability boundary;
- engineering conclusion that advances the chapter.

## 5. Application / explanation balance

Target approximately **60% engineering application / 40% engineering explanation** across the chapter. This is an editorial aim, not a hard numerical acceptance criterion.

Application includes calculations, standards navigation, procedures, checklists, decision logic, verification, design inputs, acceptance criteria and documented worked examples.

Explanation includes physics, material science, context and engineering reasoning.

## 6. Standards integration

Standards shall be integrated as an engineering navigation system, not as vague references or copied text.

Where appropriate, identify:

- standard number and title;
- applicable part;
- relevant clause, table, annex or equation after verification;
- scope of application;
- the engineering input obtained from that source;
- what remains outside that source's scope.

Avoid repeated phrases such as “the applicable standard” where a specific standard can be identified. When applicability genuinely depends on project conditions, state what determines applicability.

During authoring, edition/status information may remain a controlled working reference. Final publication claims about editions, clauses, values and normative meaning require direct authoritative Standards Validation.

## 7. Equation standard

Every important equation shall include:

- unique controlled chapter-based asset ID (for example `EQ-013-004`);
- equation title / engineering purpose;
- definition of all symbols;
- units;
- assumptions;
- validity / applicability limits;
- authoritative source or derivation basis;
- common misuse where relevant.

Numerical examples shall be independently recalculated and dimensionally checked.

## 8. Engineering tables

Tables shall reduce engineering effort. Preferred uses include:

- design inputs;
- standards mapping;
- material / method comparison;
- pressure / temperature / geometry relationships;
- failure modes and indicators;
- inspection requirements;
- decision criteria.

Important engineering tables shall use the controlled chapter asset convention (for example `TAB-013-001`).

## 9. Worked examples

Use normally **1–2 worked examples per chapter** where a worked example adds value. The preferred format is:

`Problem → Design Basis → Applicable standards → Inputs → Method / equations → Calculation → Verification → Engineering decision → What the example does NOT prove`

Examples illustrate a method; they do not establish universal design values.

## 10. Visual assets

During Authoring, visuals are specified using controlled placeholders rather than produced merely for decoration. Final visual production occurs during Publishing or the applicable controlled production stage.

Each placeholder shall state ID, title, type, purpose, required engineering content and intended source status. Visuals must communicate engineering information.

## 11. Navigation

A practicing engineer should be able to identify within a few minutes:

- whether the chapter is relevant;
- the main engineering question;
- the main standards/evidence path;
- required input data;
- the governing engineering method;
- key limitations;
- where to find the relevant example, table, workflow or checklist.

## 12. Production and change control

PDS 1.0 is **released for production**, not limited to the Chapter 13 pilot.

The Chapter 13 pilot remains the reference implementation used to prove and refine application of the PDS. Lessons from Chapter 13 and later chapters may be recorded in review logs or audit records, but they do not become new PDS requirements automatically.

Use the following control boundaries:

- **Book scope, Parts, working chapter numbers and continuation sequence** are controlled by `BOOK_STRUCTURE.md` and architecture change control.
- **Chapter-specific scope and acceptance criteria** are controlled by the approved CDB.
- **Development/review methodology** is controlled by PDS 1.0.
- **Repository locations and configuration rules** are controlled by `governance/`.
- **Superseded guidance** is retained under `archive/` and is non-governing.

A new methodology rule requires a controlled PDS change and explicit approval. Do not silently alter the PDS because one chapter presents an unusual technical challenge; first solve the issue through the CDB, engineering judgement, review package or architecture controls where possible.
