#!/usr/bin/env python3
"""One-shot canonical integration for PPE-BoK Chapter 015.

Default mode is dry-run. Use --apply only after the controlled pre-integration
reviews have been read and the branch/working-tree preconditions are satisfied.

This script performs mechanical integration only. It does not add research,
new examples, new claims, or Chapter 016 content.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "chapters/chapter-015-from-monomer-to-polymer"
CHAPTER = CHAPTER_DIR / "chapter.md"
REFERENCES = CHAPTER_DIR / "references.md"
ADDENDUM = CHAPTER_DIR / "references-addendum-2026-08-15.md"
OUTLINE = CHAPTER_DIR / "technical-outline.md"
REVIEW = CHAPTER_DIR / "review.md"
CDB = ROOT / "docs/PDS/Chapter-Design-Briefs/CDB-015-Polymerization-Catalysts-Process-Structure.md"
SCRIPT = Path(__file__).resolve()

CANDIDATES = [CHAPTER_DIR / f"investigation-{n:03d}-authoring.md" for n in range(2, 11)]

CHAPTER_MARKER = "# Investigation 2 — What Does “Polymerization” Actually Mean, and How Should the Reactions Be Classified?"
ADD_START = "<!-- CANONICAL-APPEND-START -->"
ADD_END = "<!-- CANONICAL-APPEND-END -->"


def read(path: Path) -> str:
    if not path.exists():
        raise RuntimeError(f"required file missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def clean_candidate(text: str, n: int) -> str:
    lines = text.splitlines()
    if not lines or not lines[0].startswith(f"# Investigation {n} —"):
        raise RuntimeError(f"Investigation {n}: unexpected first heading")

    # Strip the temporary candidate metadata block immediately below the title.
    i = 1
    while i < len(lines):
        s = lines[i].strip()
        if s == "" or s.startswith("**"):
            i += 1
            continue
        break
    cleaned = lines[0] + "\n\n" + "\n".join(lines[i:]).lstrip()

    # Investigations 2–9 contain development-only terminal asset-disposition
    # blocks. Final asset ownership is consolidated in Investigation 10.
    if n < 10:
        cleaned = re.sub(
            rf"\n---\n\n## Investigation {n} controlled asset disposition\n.*\Z",
            "",
            cleaned,
            flags=re.DOTALL | re.IGNORECASE,
        ).rstrip()

    return cleaned.rstrip() + "\n"


def integrate_chapter() -> str:
    current = read(CHAPTER)
    pos = current.find(CHAPTER_MARKER)
    if pos < 0:
        raise RuntimeError("canonical Chapter 015 placeholder marker not found")

    prefix = current[:pos].rstrip()
    parts = [clean_candidate(read(path), n) for n, path in zip(range(2, 11), CANDIDATES)]
    combined = prefix + "\n\n---\n\n" + "\n\n---\n\n".join(p.rstrip() for p in parts) + "\n"

    # Investigation 10 was authored before integration and therefore contains
    # a now-stale pre-integration closure checklist. Replace only that terminal
    # development-status section; retain all technical content and final assets.
    closure_marker = "## Closure holds before canonical integration"
    pos2 = combined.find(closure_marker)
    if pos2 < 0:
        raise RuntimeError("Investigation 10 pre-integration closure marker not found")

    post = """## Post-integration closure state

Canonical integration of Investigations 1–10 is complete.

The remaining controlled gates before merge are:

1. final full-file Technical Review;
2. final claim-level Standards/Evidence Validation;
3. final Editorial / Style Review and continuous-manuscript Desk Test;
4. explicit Human Approval Gate;
5. merge to `main` with the final manuscript remaining under the canonical `chapters/` directory.

Publishing remains separately subject to final figure production and publication-time source/lifecycle rechecks.

No Chapter 016 Engineering Development is authorized before Chapter 015 reaches its controlled baseline.

# References

See `references.md`.
"""
    return combined[:pos2].rstrip() + "\n\n" + post


def integrate_references() -> str:
    refs = read(REFERENCES).rstrip()
    if "### S015-008 —" in refs:
        raise RuntimeError("canonical references already contain S015-008; refusing duplicate integration")
    add = read(ADDENDUM)
    if ADD_START not in add or ADD_END not in add:
        raise RuntimeError("evidence addendum canonical markers missing")
    block = add.split(ADD_START, 1)[1].split(ADD_END, 1)[0].strip()
    return refs + "\n\n---\n\n" + block + "\n"


def integrate_outline() -> str:
    text = read(OUTLINE)

    old = """4. Use **polyaddition** for growth by addition reactions between molecules of all degrees of polymerization.
5. Use **polycondensation** for growth by condensation reactions between molecules of all degrees of polymerization.
6. Treat the older expression **addition polymerization** as historical classroom terminology; explain that IUPAC notes that it previously covered both present-day polyaddition and chain polymerization.
7. Use `step-growth` only as explanatory language when useful; do not present it as the controlling formal IUPAC classification unless mapped to the actual chemistry."""
    new = """4. Use **step polymerization** as the current IUPAC top-level class for growth by reactions between monomer, oligomer or polymer molecules of any length.
5. Within step polymerization, use **additive step polymerization (polyaddition)** and **condensative step polymerization (polycondensation)**.
6. Within chain polymerization, retain the current **additive chain polymerization** / **condensative chain polymerization** distinction where it matters to classification.
7. Treat the older expression **addition polymerization** as historical/ambiguous classroom terminology; do not use `addition polymerization / condensation polymerization` as the controlling top-level taxonomy."""
    text = replace_once(text, old, new, "outline terminology block")

    old = """Required content:
- monomer, polymerization;
- chain polymerization;
- polyaddition;
- polycondensation;
- condensative chain polymerization as the key counterexample to the simplistic classroom split;
- explanatory `step-growth` mapping;
- `TAB-015-001`;
- `FIG-015-001`;
- `EX-015-002`."""
    new = """Required content:
- monomer, polymerization;
- current `step polymerization` / `chain polymerization` top-level hierarchy;
- additive step polymerization = polyaddition;
- condensative step polymerization = polycondensation;
- additive and condensative chain-polymerization qualifiers where applicable;
- condensative chain polymerization as the key counterexample to the simplistic historical split;
- `TAB-015-001`;
- `FIG-015-001`;
- `EX-015-002`."""
    text = replace_once(text, old, new, "outline Investigation 2 block")

    text = replace_once(
        text,
        "### Investigation 5 — How does growth by reactions between molecules of different chain lengths differ from chain polymerization?",
        "### Investigation 5 — How does step polymerization build macromolecules, and what distinguishes additive from condensative step growth?",
        "outline Investigation 5 title",
    )

    old = """Required content:
- all-degrees-of-polymerization growth concept;
- condensation versus addition reaction distinction;
- functional-group conversion;
- stoichiometric balance as a qualitative engineering concern;
- Carothers-type ideal relationship only if assumptions are explicit and evidence review approves its teaching value;
- transfer ownership of molar-mass consequences to Chapter 016."""
    new = """Required content:
- formal step-polymerization growth among monomer/oligomer/polymer molecules of different lengths;
- additive step polymerization = polyaddition;
- condensative step polymerization = polycondensation;
- monomer functionality and possible connectivity;
- stoichiometric balance / reaction extent as qualitative provenance concerns;
- no Carothers-type equation retained in Chapter 015;
- transfer detailed molar-mass/topology consequences to Chapter 016."""
    text = replace_once(text, old, new, "outline Investigation 5 content")

    text = text.replace(
        "- ideal Carothers relationship for balanced difunctional polycondensation/polyaddition teaching, subject to review;",
        "- Carothers-type relation reviewed and intentionally excluded to preserve the Chapter 016 architecture boundary;",
    )

    return text


def integrate_cdb() -> str:
    text = read(CDB)

    status_anchor = "**Author approval:** 2026-08-15  \n"
    update_line = "**Post-approval authoritative-source update:** 2026-08-15 — S015-008 published 2026 IUPAC step/chain classification incorporated without scope change  \n"
    if update_line not in text:
        text = replace_once(text, status_anchor, status_anchor + update_line, "CDB source-update status")

    text = replace_once(
        text,
        "1. Distinguish monomer, polymerization, chain polymerization, polyaddition and polycondensation using controlled modern terminology.",
        "1. Distinguish monomer, polymerization, step polymerization, chain polymerization, additive step polymerization/polyaddition and condensative step polymerization/polycondensation using the current controlled terminology.",
        "CDB reader outcome 1",
    )
    text = replace_once(
        text,
        "3. Explain the difference between chain-growth-style behaviour and growth by reactions between molecules of multiple degrees of polymerization without oversimplifying IUPAC terminology.",
        "3. Explain the difference between chain polymerization and step polymerization, including additive/condensative qualifiers, without reducing classification to the historical addition/condensation split.",
        "CDB reader outcome 3",
    )

    text = replace_once(
        text,
        "6. **ISO 472 and ISO 1043-1** only where plastics terminology or polymer abbreviations need controlled cross-reference; neither is to be treated as polymerization-design authority.\n7. **Directly reviewed primary literature** for every retained claim that links a named catalyst/process route to a real material-specific architecture/property tendency.",
        "6. **Basic classification and definitions of polymerization reactions (IUPAC Recommendations 2025), published in Pure and Applied Chemistry 98(7) (2026), 1105–1117, DOI `10.1515/pac-2025-0490`** — controlling current top-level `step polymerization / chain polymerization` classification.\n7. **ISO 472 and ISO 1043-1** only where plastics terminology or polymer abbreviations need controlled cross-reference; neither is to be treated as polymerization-design authority.\n8. **Directly reviewed primary literature** for every retained claim that links a named catalyst/process route to a real material-specific architecture/property tendency.",
        "CDB authoritative path",
    )

    old = """Formal chapter language shall prefer the mechanism-based IUPAC categories rather than the oversimplified historical pair `addition polymerization / condensation polymerization`.

The chapter may introduce **step-growth** as a widely used explanatory concept, but when formal classification is required it shall map the actual process to the appropriate controlled terminology such as `polyaddition` or `polycondensation` rather than silently treating `step-growth polymerization` as a universal normative category."""
    new = """Formal chapter language shall use the current IUPAC top-level hierarchy: **step polymerization** and **chain polymerization**.

Within step polymerization, use **additive step polymerization (polyaddition)** and **condensative step polymerization (polycondensation)**. Within chain polymerization, use additive/condensative qualifiers where they are needed to avoid the historical `addition polymerization / condensation polymerization` ambiguity. `Step-growth` may remain as explanatory legacy/common language, but the reader-facing controlled taxonomy shall use the published IUPAC `step polymerization` term."""
    text = replace_once(text, old, new, "CDB terminology-control block")

    text = replace_once(
        text,
        "2. Simple degree-of-polymerization / conversion relationships for idealized step-growth systems only if assumptions and limitations are explicit and Chapter 016 ownership is preserved.",
        "2. Carothers-type degree-of-polymerization relationships were evaluated during Engineering Development and are intentionally not retained; functionality, stoichiometric balance and reaction extent remain qualitative provenance concepts, with detailed molar-mass treatment owned by Chapter 016.",
        "CDB quantitative item 2",
    )

    text = replace_once(
        text,
        "1. **FIG-015-001 — Polymerization classification map** — controlled map of polymerization → chain polymerization / polyaddition / polycondensation, with a warning showing why the historical `addition vs condensation` split is incomplete.",
        "1. **FIG-015-001 — Polymerization classification map** — controlled map of polymerization → step polymerization / chain polymerization, with additive/condensative subclasses and a warning showing why the historical `addition vs condensation` split is incomplete.",
        "CDB FIG-015-001",
    )

    text = replace_once(
        text,
        "### Investigation 5 — How does growth by reactions between molecules of different chain lengths differ from chain polymerization?\nPolyaddition/polycondensation concepts, functional-group conversion, stoichiometric sensitivity where relevant, and the bridge to material architecture without turning the chapter into a polymer-synthesis textbook.",
        "### Investigation 5 — How does step polymerization build macromolecules, and what distinguishes additive from condensative step growth?\nFormal step-polymerization growth, additive step/polyaddition, condensative step/polycondensation, functionality and stoichiometric/reaction-extent provenance, with detailed molar-mass/topology consequences deferred to Chapter 016.",
        "CDB Investigation 5",
    )

    return text


REVIEW_AFTER = """# Chapter 015 — Review Record

**Chapter:** From Monomer to Polymer: Polymerization, Catalysts and Process–Structure Relationships  
**PDS baseline:** 1.0  
**Current stage:** Canonical integration complete — final integrated-manuscript review pending  
**CDB author approval:** 2026-08-15  
**Development checkpoint:** Investigations 1–10 integrated; pre-integration Technical / Standards-Evidence / Editorial-Desk reviews passed with bounded integration findings applied

## 1. Gate status

| Gate | Status | Current disposition |
|---|---|---|
| CDB / Definition of Ready | PASS | CDB-015 author-approved and DoR passed |
| Technical Outline | PASS / UPDATED | 2026 IUPAC step/chain classification update integrated |
| Standards / Evidence Plan | PASS / UPDATED | S015-008 through S015-016 integrated with evidence limits |
| Engineering Development | COMPLETE | Investigations 1–10 canonically integrated |
| Investigation authoring reviews | PASS | Investigation 1–10 authoring gates closed |
| Named primary-evidence gates | PASS | Controlled cases for Investigations 7–9 only |
| Pre-integration Technical Review | CONDITIONAL PASS → FINDINGS APPLIED | TR015-01 through TR015-07 applied during canonical integration |
| Pre-integration Standards/Evidence Validation | PASS | Publication lifecycle holds retained |
| Pre-integration Editorial / Desk Review | CONDITIONAL PASS → FINDINGS APPLIED | ED015-01 through ED015-06 applied during integration |
| Final full-file Technical Review | PENDING | must review continuous canonical manuscript |
| Final claim-level Standards/Evidence Review | PENDING | must validate final integrated wording/source placement |
| Final Editorial / Style / Desk Test | PENDING | continuous manuscript required |
| Human Approval / merge | PENDING | explicit author approval required after final reviews |
| Publishing / Design Freeze | BLOCKED | final figures + publication-time source/lifecycle checks remain |

## 2. Definition-of-Ready record

Definition of Ready passed before Engineering Development. The approved planning package defined chapter purpose/scope, reader outcomes, scientific/process inputs, evidence path, ten-Investigation structure, engineering assets, exclusions/cross-references and acceptance criteria.

## 3. Controlled terminology update

A new final IUPAC Recommendation published in 2026 was identified during Investigation 2 and superseded one planning-era classification assumption without changing chapter scope.

Canonical Chapter 015 now uses:

- `step polymerization`;
  - additive step polymerization = polyaddition;
  - condensative step polymerization = polycondensation;
- `chain polymerization`;
  - additive chain polymerization;
  - condensative chain polymerization.

The change record remains in `reviews/chapter-015/TERMINOLOGY-CLASSIFICATION-UPDATE-2026-08-15.md`.

## 4. Primary-evidence boundaries

Named catalyst/process outcome claims are limited to the directly reviewed systems recorded as S015-009 through S015-016. No source is treated as a universal catalyst-family rule or as piping-design authority.

## 5. Quantitative disposition

No Chapter 015 design equation is retained.

- `P_x + P_y` notation is mechanistic.
- `k_p` / `k_t` are terminology only.
- a Carothers-type equation was evaluated and intentionally excluded to preserve the Chapter 016 boundary.

## 6. Canonical manuscript / configuration state

Canonical manuscript:

`chapters/chapter-015-from-monomer-to-polymer/chapter.md`

Supporting canonical files:

- `references.md`;
- `technical-outline.md`;
- `review.md`.

Temporary Investigation 2–10 authoring candidates and the temporary references addendum are removed by the canonical integration.

## 7. Next controlled action

Perform the final integrated-manuscript review cycle:

1. full-file Technical Review;
2. final claim-level Standards/Evidence Validation;
3. final Editorial / Style Review + continuous Desk Test;
4. branch synchronization with current `main` if needed;
5. Human Approval Gate.

Do not merge PR #15 or start Chapter 016 before those gates close.
"""


def integrate_review() -> str:
    return REVIEW_AFTER


def transform_all() -> dict[Path, str]:
    return {
        CHAPTER: integrate_chapter(),
        REFERENCES: integrate_references(),
        OUTLINE: integrate_outline(),
        CDB: integrate_cdb(),
        REVIEW: integrate_review(),
    }


def validate(outputs: dict[Path, str], after_apply: bool) -> None:
    chapter = outputs[CHAPTER]
    refs = outputs[REFERENCES]
    outline = outputs[OUTLINE]
    cdb = outputs[CDB]
    review = outputs[REVIEW]

    for n in range(1, 11):
        count = len(re.findall(rf"^# Investigation {n} —", chapter, flags=re.MULTILINE))
        if count != 1:
            raise RuntimeError(f"chapter: Investigation {n} heading count = {count}, expected 1")

    forbidden = [
        "**Authoring state:** planned",
        "**Authoring status:** controlled candidate",
        "Canonical integration: deferred to end-of-chapter integration",
        "BLOCKED pending controlled primary-literature case gate",
        "## Closure holds before canonical integration",
    ]
    for token in forbidden:
        if token in chapter:
            raise RuntimeError(f"chapter contains stale development token: {token}")

    required_chapter = [
        "step polymerization",
        "additive step polymerization",
        "condensative step polymerization",
        "WF-015-001",
        "CL-015-001",
        "# Chapter engineering closure",
        "## Post-integration closure state",
    ]
    for token in required_chapter:
        if token not in chapter:
            raise RuntimeError(f"chapter required token missing: {token}")

    for prefix, end in [("FIG-015-", 6), ("TAB-015-", 5)]:
        for i in range(1, end + 1):
            token = f"{prefix}{i:03d}"
            if token not in chapter:
                raise RuntimeError(f"chapter asset token missing: {token}")
    for i in range(1, 4):
        if f"EX-015-{i:03d}" not in chapter:
            raise RuntimeError(f"chapter example token missing: EX-015-{i:03d}")

    for i in range(8, 17):
        if f"S015-{i:03d}" not in refs:
            raise RuntimeError(f"references missing S015-{i:03d}")

    stale_outline = "Use `step-growth` only as explanatory language"
    stale_cdb = "The chapter may introduce **step-growth** as a widely used explanatory concept"
    if stale_outline in outline:
        raise RuntimeError("outline retains stale pre-2026 step-growth wording")
    if stale_cdb in cdb:
        raise RuntimeError("CDB retains stale pre-2026 step-growth wording")
    if "Basic classification and definitions of polymerization reactions" not in cdb:
        raise RuntimeError("CDB missing 2026 IUPAC classification source")
    if "Engineering Development | COMPLETE" not in review:
        raise RuntimeError("review gate table not updated to Engineering Development COMPLETE")
    if "Human Approval / merge | PENDING" not in review:
        raise RuntimeError("review does not retain Human Approval hold")

    if after_apply:
        for path in CANDIDATES + [ADDENDUM]:
            if path.exists():
                raise RuntimeError(f"temporary file still exists: {path.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write validated integration and delete temporary authoring files")
    args = parser.parse_args()

    outputs = transform_all()
    validate(outputs, after_apply=False)

    print("Chapter 015 canonical integration validation: PASS")
    print("Planned canonical writes:")
    for path, text in outputs.items():
        print(f"  {path.relative_to(ROOT)}: {len(text.splitlines())} lines")
    print("Temporary files to delete:")
    for path in CANDIDATES + [ADDENDUM, SCRIPT]:
        print(f"  {path.relative_to(ROOT)}")

    if not args.apply:
        print("DRY RUN ONLY — no files changed. Re-run with --apply after repository preconditions are confirmed.")
        return

    for path, text in outputs.items():
        path.write_text(text, encoding="utf-8", newline="\n")

    for path in CANDIDATES + [ADDENDUM]:
        path.unlink()

    # Validate the written state before deleting this one-shot tool.
    written = {path: read(path) for path in outputs}
    validate(written, after_apply=True)
    print("Applied Chapter 015 canonical integration: PASS")

    try:
        SCRIPT.unlink()
        print("Deleted one-shot integration script.")
    except OSError as exc:
        print(f"WARNING: could not self-delete integration script: {exc}")
        print("Delete tools/chapter015_canonical_integrate.py manually before committing.")


if __name__ == "__main__":
    main()
