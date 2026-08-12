# PPE-BoK Configuration Management

**Version:** 1.1  
**Status:** Released for Production

## Configuration items

The following are controlled configuration items (CIs):

- PDS governance documents;
- `BOOK_STRUCTURE.md` and book-architecture controls;
- chapters and Chapter Design Briefs;
- equations;
- figures;
- tables;
- workflows;
- worked examples;
- decision trees;
- checklists;
- active templates;
- standards-register entries;
- formal review packages and closure records where they support a baselined chapter.

Archived material is preserved for traceability but is not an active CI unless it is intentionally restored through change control.

## Human Approval Gate

No technical chapter content shall become part of the repository baseline without explicit author approval.

Working sequence:

`Draft → Internal Review → Joint Review → Author Approval → Commit/PR → Merge → Baseline`

A branch or pull request may contain approved working material, but only merged content on `main` is an official baseline.

## Versioning

Use `1.0`, `1.1`, `1.2`, `2.0` where a controlled document/chapter revision requires versioning.

A baselined chapter is never silently overwritten. A material technical change creates a controlled revision and is recorded in the relevant changelog / repository history.

## Change classes

- **A — Editorial:** no engineering meaning changed.
- **B — Structural:** architecture/navigation changed without changing engineering meaning.
- **C — Technical:** engineering meaning, calculation, limit or recommendation changed; technical re-review required.
- **D — PDS:** methodology/governance changed; explicit author approval required.

Repository hygiene that only relocates identical content, updates navigation, or archives superseded files is normally Class B unless the move changes which technical statement is treated as authoritative.

## No silent improvements

All material changes are disclosed during review. Technical changes are not inserted into `main` merely because they appear obvious or beneficial.

A cleanup or migration shall preserve technical content exactly unless a separate approved technical work package authorizes a change.

## Standards revalidation trigger

Any change to a standards-derived requirement, coefficient, equation, table value, scope statement, terminology or normative interpretation reopens Standards Validation for the affected content.

Updating navigation or recording an edition already documented in a chapter source register does not itself constitute final Standards Validation.

## Archive control

Superseded files are moved under `archive/` rather than left in active locations where they could be mistaken for current guidance.

Archived files:

- remain available for provenance and historical recovery;
- shall be identified as archived when cited;
- do not override current `BOOK_STRUCTURE.md`, PDS, governance, active templates, chapter sources or the central Standards Register.

Restoring archived guidance to active status requires review against the current PDS and an explicit controlled change.

## Development sequence

Chapter 013 remains the PDS pilot/reference implementation and must complete its remaining publication gates before the next new working chapter is baselined.

After Chapter 013 closure, development follows the active `BOOK_STRUCTURE.md`, beginning with the approved CDB for Working Chapter 014 unless an explicit author-approved sequencing exception is recorded.

The book remains topic-driven. Working numbers may be reorganized during the final architecture/editorial review, but chapters are not baselined out of the controlled development sequence without explicit approval.
