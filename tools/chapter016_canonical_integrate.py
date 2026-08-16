#!/usr/bin/env python3
"""One-shot canonical integration tool for PPE-BoK Chapter 016.

Default mode is DRY RUN: construct and validate the proposed integrated state
without writing files.

Use --apply only under the controlled Chapter 016 canonical integration brief.
This tool performs no Git operations and makes no scientific/editorial choices.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CH_DIR = ROOT / "chapters" / "chapter-016-polymer-chain-architecture"
CHAPTER = CH_DIR / "chapter.md"
REFERENCES = CH_DIR / "references.md"
REVIEW = CH_DIR / "review.md"
ADDENDUM = CH_DIR / "references-addendum-2026-08-16.md"

CANDIDATES = [CH_DIR / f"investigation-{n:03d}-authoring.md" for n in range(2, 11)]

FIG_IDS = [f"FIG-016-{n:03d}" for n in range(1, 7)]
TAB_IDS = [f"TAB-016-{n:03d}" for n in range(1, 6)]
EX_IDS = [f"EX-016-{n:03d}" for n in range(1, 4)]
OTHER_IDS = ["WF-016-001", "CL-016-001"]
SOURCE_IDS = [f"S016-{n:03d}" for n in range(13, 17)]


class IntegrationError(RuntimeError):
    pass


def read(path: Path) -> str:
    if not path.exists():
        raise IntegrationError(f"Required file missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise IntegrationError(message)


def count_top_investigation(text: str, number: int) -> int:
    return len(re.findall(rf"(?m)^# Investigation {number}\s+—", text))


def count_formal_asset_heading(text: str, asset_id: str) -> int:
    return len(re.findall(rf"(?m)^##\s+[^\n]*\b{re.escape(asset_id)}\b[^\n]*$", text))


def build_chapter() -> str:
    chapter = read(CHAPTER)

    require(count_top_investigation(chapter, 1) == 1,
            "Canonical chapter must contain exactly one Investigation 1 before integration")
    for n in range(2, 11):
        require(count_top_investigation(chapter, n) == 0,
                f"Canonical chapter unexpectedly already contains Investigation {n}")

    pieces = [chapter.rstrip()]
    for n, path in enumerate(CANDIDATES, start=2):
        candidate = read(path).strip()
        require(count_top_investigation(candidate, n) == 1,
                f"Candidate {path.name} must contain exactly one Investigation {n} heading")
        for other in range(1, 11):
            if other != n:
                require(count_top_investigation(candidate, other) == 0,
                        f"Candidate {path.name} unexpectedly contains Investigation {other}")
        pieces.append(candidate)

    integrated = "\n\n---\n\n".join(pieces).rstrip() + "\n"

    # Bounded frontmatter status normalization already authorized by TR016-03.
    integrated = integrated.replace(
        "  equations: pending-investigation-3\n  units: pending-investigation-3\n  examples: active",
        "  equations: pass\n  units: pass\n  examples: pass",
        1,
    )

    return integrated


def extract_primary_entries(addendum: str) -> str:
    start_marker = "### S016-013"
    end_marker = "\n---\n\n## Gate rule"
    require(start_marker in addendum, "Primary-evidence addendum missing S016-013 marker")
    start = addendum.index(start_marker)
    if end_marker in addendum[start:]:
        end = addendum.index(end_marker, start)
    else:
        end = len(addendum)
    return addendum[start:end].strip()


def build_references() -> str:
    refs = read(REFERENCES)
    addendum = read(ADDENDUM)

    for sid in SOURCE_IDS:
        require(len(re.findall(rf"(?m)^###\s+{re.escape(sid)}\b", refs)) == 0,
                f"Canonical references already contain {sid}")
        require(len(re.findall(rf"(?m)^###\s+{re.escape(sid)}\b", addendum)) == 1,
                f"Addendum must contain exactly one heading for {sid}")

    entries = extract_primary_entries(addendum)
    insertion_marker = "\n## 5. Investigation-specific evidence plan"
    require(insertion_marker in refs, "references.md missing Investigation-specific evidence-plan marker")
    refs = refs.replace(
        insertion_marker,
        "\n\n" + entries + "\n\n## 5. Investigation-specific evidence plan",
        1,
    )

    old_gate = (
        "No architecture→property case is pre-approved merely because it is common in polymer engineering.\n\n"
        "Before Investigation 9 authoring, each candidate is marked:"
    )
    new_gate = (
        "No architecture→property case is approved merely because it is common in polymer engineering.\n\n"
        "The Investigation 9 direct-primary-evidence gate approved **S016-013 through S016-016 only**. "
        "Any additional named case requires a new gate. The gate checklist remains:"
    )
    require(old_gate in refs, "references.md primary-evidence gate text changed unexpectedly")
    refs = refs.replace(old_gate, new_gate, 1)

    old_dor = (
        "## 10. Definition-of-Ready evidence disposition\n\n"
        "**PASS for entering Engineering Development.**\n\n"
        "The terminology path, method-scope path, quantitative controls and primary-literature gates are sufficiently defined to begin Investigation 1. "
        "Investigations that require named architecture/property claims remain independently gated until the required primary evidence is reviewed."
    )
    new_dor = (
        "## 10. Engineering-development evidence disposition\n\n"
        "**PASS FOR CANONICAL INTEGRATION — PUBLICATION LIFECYCLE HOLDS REMAIN.**\n\n"
        "The terminology, quantitative and method-scope gates passed. The Investigation 9 primary-evidence gate admitted S016-013 through S016-016 only. "
        "Final claim-level source placement and publication-time lifecycle rechecks remain mandatory after canonical integration."
    )
    require(old_dor in refs, "references.md Definition-of-Ready disposition text changed unexpectedly")
    refs = refs.replace(old_dor, new_dor, 1)

    return refs.rstrip() + "\n"


def build_review() -> str:
    review = read(REVIEW)

    replacements = {
        "**Current stage:** Engineering Development complete — canonical integration pending":
            "**Current stage:** Canonical integration complete — final integrated-manuscript review pending",
        "| Canonical integration | **PENDING / AUTHORIZED** | one-shot mechanical integration next |":
            "| Canonical integration | **COMPLETE** | Investigations 1–10 integrated; temporary candidates/addendum removed |",
        "- Investigation 1 is canonical in `chapter.md`.\n- Investigations 2–10 remain controlled temporary authoring candidates until the one-shot canonical integration.":
            "- Investigations 1–10 are canonically integrated in `chapter.md`.\n- Temporary Investigation 2–10 authoring candidates and the evidence addendum are removed after validation.",
    }
    for old, new in replacements.items():
        require(old in review, f"review.md expected text not found: {old[:80]}")
        review = review.replace(old, new, 1)

    section7_start = "## 7. Canonical configuration state"
    section8_start = "## 8. Next controlled action"
    require(section7_start in review and section8_start in review,
            "review.md canonical-state sections not found")
    start = review.index(section7_start)
    end = review.index(section8_start)
    section7 = """## 7. Canonical configuration state

Canonical directory:

`chapters/chapter-016-polymer-chain-architecture/`

Canonical files after integration:

- `chapter.md` — continuous Investigations 1–10;
- `references.md` — S016-001..016 evidence register;
- `technical-outline.md`;
- `review.md`.

Temporary Investigation 2–10 authoring candidates and `references-addendum-2026-08-16.md` are removed after integration validation.

"""
    review = review[:start] + section7 + review[end:]

    next_old = (
        "Perform the one-shot canonical integration under `CANONICAL-INTEGRATION-BRIEF-2026-08-16.md` and its validation script.\n\n"
        "After integration:\n\n"
        "1. Final full-file Technical Review;\n"
        "2. final claim-level Standards/Evidence Validation;\n"
        "3. final Editorial / Style Review + continuous Desk Test;\n"
        "4. synchronize with current `main` if needed;\n"
        "5. Human Approval Gate."
    )
    next_new = (
        "Perform the final integrated-manuscript review cycle:\n\n"
        "1. Final full-file Technical Review;\n"
        "2. final claim-level Standards/Evidence Validation;\n"
        "3. final Editorial / Style Review + continuous Desk Test;\n"
        "4. synchronize with current `main` if needed;\n"
        "5. Human Approval Gate."
    )
    require(next_old in review, "review.md next-action block changed unexpectedly")
    review = review.replace(next_old, next_new, 1)

    return review.rstrip() + "\n"


def validate_integrated(chapter: str, refs: str, review: str) -> None:
    # Investigations exactly once.
    for n in range(1, 11):
        require(count_top_investigation(chapter, n) == 1,
                f"Integrated chapter must contain exactly one Investigation {n}")

    # Primary sources exactly once as source headings.
    for sid in SOURCE_IDS:
        require(len(re.findall(rf"(?m)^###\s+{re.escape(sid)}\b", refs)) == 1,
                f"Integrated references must contain exactly one source heading for {sid}")

    # Formal assets exactly once as chapter headings/specifications.
    for asset_id in FIG_IDS + TAB_IDS + EX_IDS + OTHER_IDS:
        require(count_formal_asset_heading(chapter, asset_id) == 1,
                f"Integrated chapter must contain exactly one formal heading for {asset_id}")

    # Core terminology/evidence controls.
    required_phrases = [
        "relative molecular mass",
        "M_m ≡ M_w",
        "Đ_M",
        "Do not use unqualified `chain length`",
        "ISO 18177:2025",
        "ISO 10147:2011",
        "entanglement ≠ covalent crosslink",
        "supported conclusion",
        "unsupported conclusion",
        "transferability",
        "chain architecture → crystallization/packing possibilities",
    ]
    for phrase in required_phrases:
        require(phrase in chapter, f"Integrated chapter missing required control phrase: {phrase}")

    require("S016-013 through S016-016 only" in refs,
            "Integrated references must record the bounded Investigation 9 source gate")
    require("Canonical integration | **COMPLETE**" in review,
            "review.md must record canonical integration COMPLETE")
    require("Human Approval / merge | PENDING" in review,
            "review.md must retain Human Approval PENDING")

    # Frontmatter quantitative state.
    require("  equations: pass" in chapter, "Chapter frontmatter equations status not normalized to pass")
    require("  units: pass" in chapter, "Chapter frontmatter units status not normalized to pass")
    require("  examples: pass" in chapter, "Chapter frontmatter examples status not normalized to pass")

    # No obvious stale authoring-state markers in the final manuscript.
    forbidden = [
        "canonical-integration-deferred",
        "Investigation 9 BLOCKED",
        "controlled-candidate metadata",
    ]
    for phrase in forbidden:
        require(phrase not in chapter, f"Stale authoring marker remains: {phrase}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Write the validated integrated state")
    args = parser.parse_args()

    # Preconditions.
    for path in [CHAPTER, REFERENCES, REVIEW, ADDENDUM, *CANDIDATES]:
        require(path.exists(), f"Precondition missing: {path.relative_to(ROOT)}")

    chapter = build_chapter()
    refs = build_references()
    review = build_review()
    validate_integrated(chapter, refs, review)

    if not args.apply:
        print("Chapter 016 canonical integration validation: PASS")
        print(f"Planned chapter.md lines: {len(chapter.splitlines())}")
        print(f"Planned references.md lines: {len(refs.splitlines())}")
        print(f"Planned review.md lines: {len(review.splitlines())}")
        print(f"Planned temporary deletions: {len(CANDIDATES) + 1}")
        print("DRY RUN ONLY — no files changed")
        return

    CHAPTER.write_text(chapter, encoding="utf-8")
    REFERENCES.write_text(refs, encoding="utf-8")
    REVIEW.write_text(review, encoding="utf-8")

    for path in CANDIDATES + [ADDENDUM]:
        path.unlink()

    # Re-read and validate written state.
    written_chapter = read(CHAPTER)
    written_refs = read(REFERENCES)
    written_review = read(REVIEW)
    validate_integrated(written_chapter, written_refs, written_review)

    for path in CANDIDATES + [ADDENDUM]:
        require(not path.exists(), f"Temporary file was not removed: {path.relative_to(ROOT)}")

    print("Chapter 016 canonical integration validation: PASS")
    print(f"Applied chapter.md lines: {len(written_chapter.splitlines())}")
    print(f"Applied references.md lines: {len(written_refs.splitlines())}")
    print(f"Applied review.md lines: {len(written_review.splitlines())}")
    print("APPLY COMPLETE — delete tools/chapter016_canonical_integrate.py before the atomic integration commit")


if __name__ == "__main__":
    try:
        main()
    except IntegrationError as exc:
        raise SystemExit(f"Chapter 016 canonical integration validation: FAIL\n{exc}")
