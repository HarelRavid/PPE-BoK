# PPE-BoK Configuration Management

**Version:** 1.0  
**Status:** Released for Production

## Configuration items

The following are controlled configuration items (CIs):

- PDS governance documents;
- chapters;
- equations;
- figures;
- tables;
- workflows;
- worked examples;
- decision trees;
- checklists;
- templates;
- standards-register entries.

## Human Approval Gate

No technical chapter content shall become part of the repository baseline without explicit author approval.

Working sequence:

`Draft → Internal Review → Joint Review → Author Approval → Commit/PR → Merge → Baseline`

A branch or pull request may contain approved working material, but only merged content on `main` is an official baseline.

## Versioning

Use `1.0`, `1.1`, `1.2`, `2.0`.

A baselined chapter is never silently overwritten. A material technical change creates a new controlled revision and is recorded in the relevant changelog / repository history.

## Change classes

- **A — Editorial:** no engineering meaning changed.
- **B — Structural:** architecture/navigation changed.
- **C — Technical:** engineering meaning, calculation, limit or recommendation changed; technical re-review required.
- **D — PDS:** methodology/governance changed; explicit author approval required.

## No silent improvements

All material changes are disclosed during review. Technical changes are not inserted into `main` merely because they appear obvious or beneficial.

## Standards revalidation trigger

Any change to a standards-derived requirement, coefficient, equation, table value, scope statement, terminology or normative interpretation reopens Standards Validation for the affected content.

## One chapter at a time

After the Chapter 13 pilot, full-book redevelopment proceeds sequentially from Chapter 001 onward. No chapter is baselined out of sequence unless explicitly approved.
