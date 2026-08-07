# PPE-BoK Development System (PDS)

**Baseline:** 1.0
**Status:** Design Freeze Candidate / Approved for pilot implementation
**Branch:** `pds-baseline-1.0`

The PPE-BoK Development System governs how the book is engineered, authored, reviewed, validated and maintained.

## Governing documents

1. [Engineering Doctrine](Engineering-Doctrine.md) — why PPE-BoK exists and the principles that govern engineering content.
2. [Engineering Development Manual](Engineering-Development-Manual.md) — how chapters are designed and developed.
3. [Quality & Validation Manual](Quality-and-Validation-Manual.md) — how technical content and standards-derived statements are verified.
4. [Style Guide](Style-Guide.md) — presentation and consistency rules.

## Core baseline decisions

- The **chapter** is the primary self-contained knowledge unit. Investigations are progressive sections inside the chapter and shall not repeatedly restate chapter-level context.
- Target balance is approximately **60% engineering application / 40% engineering explanation**, adjusted to what is required to communicate the engineering point correctly.
- Standards are the authoritative technical framework. PPE-BoK explains, navigates and applies them; it does not replace them.
- Every standards-derived statement must be checked again against the authoritative standard during the final Standards Validation pass after authoring is complete.
- Engineering assets (equations, tables, workflows, worked examples, figures, checklists) are included when they increase engineering capability; they are not decorative quotas.
- A practicing engineer should be able to open a chapter and quickly locate the standards path, engineering method, limits, calculations or decision tools required for the subject.
- No new process rule is added during chapter writing unless a demonstrated gap cannot be solved within PDS 1.0. Proposed improvements are recorded for controlled revision.

## Development workflow

`Chapter Design Brief → Technical Outline → Engineering Development → Engineering Assets Integration → Technical Review → Standards Validation → Editorial/Style Review → Publication Approval`

## Relationship to legacy guidance

`docs/PPE-BoK_LLM_WIKI.md` and existing templates remain valuable legacy inputs. During the PDS 1.0 pilot they shall be reconciled with these documents rather than silently discarded. Where a material conflict is identified, it must be resolved explicitly before publication baseline.

## Pilot

Chapter 13 — Polyethylene (PE) is the first PDS pilot/reference chapter. Its approved design brief is maintained under `docs/PDS/Chapter-Design-Briefs/`.
