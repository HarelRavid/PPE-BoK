# PPE-BoK Style Guide

**Baseline:** 1.0

## 1. Purpose

This guide defines presentation rules that support technical clarity and long-term consistency. Technical correctness always takes precedence over visual uniformity.

## 2. Language

- Use clear professional engineering English in publication chapters unless a project-wide language decision states otherwise.
- Introduce uncommon abbreviations and specialist terms before relying on them.
- Prefer direct engineering statements over rhetorical or promotional language.
- Avoid unnecessary repetition and filler.
- Preserve internationally recognised symbols and notation.

## 3. Headings

Use a stable hierarchy:

- `# Chapter NNN — Title`
- chapter-level sections such as `## Chapter purpose`, `## Chapter standards map`, etc.;
- `# Investigation N — Engineering Question` or the chapter-approved equivalent when the chapter uses Investigation-led structure;
- `##` / `###` for subsections within an Investigation as required by the chapter structure.

Investigations are progressive; do not repeat chapter-level introductions within every Investigation.

## 4. Equations

Important equations use the controlled asset convention:

- `EQ-NNN-001`
- `EQ-NNN-002`
- etc.

Present the asset ID with an engineering-purpose title, for example:

`EQ-013-004 — SDR pressure relationship`

For every important equation:

- define every symbol and unit immediately after first use or in an adjacent symbol table;
- state assumptions and validity/applicability limits;
- state source / derivation basis;
- identify common misuse where relevant;
- use consistent SI units unless a referenced standard or worked example requires another system; conversions must be explicit.

Do not maintain a second parallel equation-numbering system such as `Eq. 13-1` unless a final publishing layer intentionally renders the controlled ID differently without changing the underlying asset identity.

## 5. Tables

Important engineering tables use controlled IDs such as:

- `TAB-013-001`
- `TAB-013-002`

Give every table an engineering-purpose title.

- Put units in headings where practical.
- Do not use a table merely to restate prose.
- Identify source basis for standards-derived or externally derived values.
- A publishing format may display a reader-friendly caption, but the controlled asset ID remains the source identity.

## 6. Figures and visual placeholders

During Authoring, use controlled visual placeholders. Final production occurs during Publishing or the applicable controlled production phase.

Placeholder identity follows the engineering-asset convention, for example:

`FIG-013-003 — Long-term hydrostatic regression concept [PLACEHOLDER]`

A placeholder should state, as needed:

- controlled ID;
- title;
- type;
- engineering purpose;
- required engineering content;
- source status: Original / standards-derived concept / permission required / TBD.

Final figures must communicate an engineering message. Decorative figures are excluded.

## 7. Workflows, examples, decision trees and checklists

Use the controlled chapter-based IDs:

- Workflow: `WF-NNN-001`
- Worked Example: `EX-NNN-001`
- Decision Tree: `DT-NNN-001`
- Checklist: `CL-NNN-001`

### Worked examples

Use a consistent visual structure:

- Problem
- Design Basis
- Applicable standards / evidence
- Inputs
- Method
- Calculation
- Verification
- Engineering decision
- Limitations / What this example does not prove

Normally use 1–2 substantial examples per chapter where examples add value.

## 8. Standards references

Prefer explicit references such as `ISO 12162, Clause X / Table Y` **after authoritative validation** rather than vague wording such as “the applicable standard”.

Where exact applicability is project-dependent, state what determines applicability.

Do not reproduce copyrighted standards text beyond permitted quotation. Prefer paraphrase, engineering interpretation and precise navigation references.

During authoring, unvalidated clause/edition details shall be treated as working references or explicit Standards Validation hold points rather than publication-final facts.

## 9. Knowledge callouts

Use sparingly and consistently. Approved callout purposes include:

- Engineering Insight
- Engineering Mistake
- Reality Check
- Think Like an Engineer
- Source and Validity Range
- Engineering Inference
- Knowledge Gap

Callouts are not substitutes for equations, standards requirements or evidence.

## 10. Tone

- Accurate before elegant.
- Clear before clever.
- Professional without sounding bureaucratic.
- Accessible without oversimplifying.
- State uncertainty directly.
- Distinguish mandatory requirements from recommendations and interpretation.

## 11. Cross-references

Use stable chapter / section / engineering-asset identifiers. Cross-reference rather than repeating substantial technical explanations already established elsewhere in the same chapter or book.

Working chapter numbers may change before final architecture freeze; avoid unnecessary prose that hard-codes a final TOC assumption when a controlled asset, topic or working chapter reference is sufficient.

Archived material shall not be used as an active cross-reference target unless the text explicitly discusses historical recovery.

## 12. Visual production rule

**No visual is produced merely to satisfy a chapter quota. Every necessary visual is specified during Authoring and produced during the controlled Publishing stage.**

The absence of a finished visual shall not interrupt technically correct manuscript development when a complete engineering placeholder is sufficient for the current gate.
