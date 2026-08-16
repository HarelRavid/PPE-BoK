#!/usr/bin/env python3
"""Controlled one-shot canonical integration for PPE-BoK Chapter 016.

Default = dry run. --apply writes only the already-reviewed canonical integration.
No Git operations. No research. No scientific/editorial decision-making.
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

SOURCE_IDS = [f"S016-{n:03d}" for n in range(13, 17)]
FIG_IDS = [f"FIG-016-{n:03d}" for n in range(1, 7)]
TAB_IDS = [f"TAB-016-{n:03d}" for n in range(1, 6)]
EX_IDS = [f"EX-016-{n:03d}" for n in range(1, 4)]
OTHER_IDS = ["WF-016-001", "CL-016-001"]


class IntegrationError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise IntegrationError(message)


def read(path: Path) -> str:
    require(path.exists(), f"Required file missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def inv_count(text: str, n: int) -> int:
    return len(re.findall(rf"(?m)^# Investigation {n}\s+—", text))


def asset_heading_count(text: str, asset_id: str) -> int:
    return len(re.findall(rf"(?m)^##\s+[^\n]*{re.escape(asset_id)}[^\n]*$", text))


def build_chapter() -> str:
    chapter = read(CHAPTER)
    require(inv_count(chapter, 1) == 1, "Canonical chapter must contain exactly one Investigation 1")
    for n in range(2, 11):
        require(inv_count(chapter, n) == 0, f"Canonical chapter already contains Investigation {n}")

    parts = [chapter.rstrip()]
    for n, path in enumerate(CANDIDATES, start=2):
        candidate = read(path).strip()
        require(inv_count(candidate, n) == 1, f"{path.name} must contain exactly one Investigation {n}")
        for other in range(1, 11):
            if other != n:
                require(inv_count(candidate, other) == 0, f"{path.name} unexpectedly contains Investigation {other}")
        parts.append(candidate)

    integrated = "\n\n---\n\n".join(parts).rstrip() + "\n"

    old_frontmatter = "  equations: pending-investigation-3\n  units: pending-investigation-3\n  examples: active"
    new_frontmatter = "  equations: pass\n  units: pass\n  examples: pass"
    require(old_frontmatter in integrated, "Expected Chapter 016 frontmatter quantitative status not found")
    integrated = integrated.replace(old_frontmatter, new_frontmatter, 1)
    return integrated


def primary_entries(addendum: str) -> str:
    start_marker = "### S016-013"
    end_marker = "\n---\n\n## Gate rule"
    require(start_marker in addendum, "Addendum missing S016-013")
    start = addendum.index(start_marker)
    end = addendum.index(end_marker, start) if end_marker in addendum[start:] else len(addendum)
    return addendum[start:end].strip()


def build_references() -> str:
    refs = read(REFERENCES)
    addendum = read(ADDENDUM)

    for sid in SOURCE_IDS:
        require(len(re.findall(rf"(?m)^###\s+{sid}\b", refs)) == 0, f"references.md already contains {sid}")
        require(len(re.findall(rf"(?m)^###\s+{sid}\b", addendum)) == 1, f"addendum must contain exactly one {sid}")

    marker = "\n## 5. Investigation-specific evidence plan"
    require(marker in refs, "references.md insertion marker missing")
    refs = refs.replace(marker, "\n\n" + primary_entries(addendum) + "\n\n## 5. Investigation-specific evidence plan", 1)

    old_status = "**PASS FOR CANONICAL INTEGRATION — S016-013..016 PENDING MECHANICAL ABSORPTION INTO THIS REGISTER.**"
    new_status = "**PASS FOR CANONICAL INTEGRATION — S016-013..016 INTEGRATED; FINAL CLAIM-LEVEL REVIEW PENDING.**"
    require(old_status in refs, "references.md pre-integration disposition changed unexpectedly")
    refs = refs.replace(old_status, new_status, 1)
    return refs.rstrip() + "\n"


def build_review() -> str:
    review = read(REVIEW)

    replacements = [
        (
            "**Current stage:** Engineering Development complete — canonical integration pending",
            "**Current stage:** Canonical integration complete — final integrated-manuscript review pending",
        ),
        (
            "| Canonical integration | **PENDING / AUTHORIZED** | one-shot mechanical integration next |",
            "| Canonical integration | **COMPLETE** | Investigations 1–10 integrated; temporary candidates/addendum removed |",
        ),
        (
            "- Investigation 1 is canonical in `chapter.md`.\n- Investigations 2–10 remain controlled temporary authoring candidates until the one-shot canonical integration.",
            "- Investigations 1–10 are canonically integrated in `chapter.md`.\n- Temporary Investigation 2–10 authoring candidates and the evidence addendum are removed after validation.",
        ),
    ]
    for old, new in replacements:
        require(old in review, f"review.md expected integration text missing: {old[:70]}")
        review = review.replace(old, new, 1)

    s7 = "## 7. Canonical configuration state"
    s8 = "## 8. Next controlled action"
    require(s7 in review and s8 in review, "review.md section markers missing")
    start = review.index(s7)
    end = review.index(s8)
    new_s7 = """## 7. Canonical configuration state

Canonical directory:

`chapters/chapter-016-polymer-chain-architecture/`

Canonical files after integration:

- `chapter.md` — continuous Investigations 1–10;
- `references.md` — S016-001..016 evidence register;
- `technical-outline.md`;
- `review.md`.

Temporary Investigation 2–10 authoring candidates and `references-addendum-2026-08-16.md` are removed after validation.

"""
    review = review[:start] + new_s7 + review[end:]

    old_next = """Perform the one-shot canonical integration under `CANONICAL-INTEGRATION-BRIEF-2026-08-16.md` and its validation script.

After integration:

1. Final full-file Technical Review;
2. final claim-level Standards/Evidence Validation;
3. final Editorial / Style Review + continuous Desk Test;
4. synchronize with current `main` if needed;
5. Human Approval Gate."""
    new_next = """Perform the final integrated-manuscript review cycle:

1. Final full-file Technical Review;
2. final claim-level Standards/Evidence Validation;
3. final Editorial / Style Review + continuous Desk Test;
4. synchronize with current `main` if needed;
5. Human Approval Gate."""
    require(old_next in review, "review.md next-action block changed unexpectedly")
    review = review.replace(old_next, new_next, 1)
    return review.rstrip() + "\n"


def validate(chapter: str, refs: str, review: str) -> None:
    for n in range(1, 11):
        require(inv_count(chapter, n) == 1, f"Integrated chapter must contain exactly one Investigation {n}")

    for sid in SOURCE_IDS:
        require(len(re.findall(rf"(?m)^###\s+{sid}\b", refs)) == 1, f"Integrated references must contain exactly one {sid} heading")

    for aid in FIG_IDS + TAB_IDS + EX_IDS + OTHER_IDS:
        require(asset_heading_count(chapter, aid) == 1, f"Integrated chapter must contain exactly one formal heading for {aid}")

    for phrase in [
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
    ]:
        require(phrase in chapter, f"Integrated chapter missing control phrase: {phrase}")

    require("PASS FOR S016-013 THROUGH S016-016 ONLY" in refs, "Bounded Investigation 9 source gate missing from references")
    require("S016-013..016 INTEGRATED" in refs, "Integrated source disposition missing from references")
    require("Canonical integration | **COMPLETE**" in review, "review.md must record integration COMPLETE")
    require("Human Approval / merge | PENDING" in review, "review.md must retain Human Approval PENDING")

    require("  equations: pass" in chapter, "equations frontmatter not PASS")
    require("  units: pass" in chapter, "units frontmatter not PASS")
    require("  examples: pass" in chapter, "examples frontmatter not PASS")

    for stale in ["canonical-integration-deferred", "Investigation 9 BLOCKED", "controlled-candidate metadata"]:
        require(stale not in chapter, f"Stale authoring marker remains: {stale}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    for path in [CHAPTER, REFERENCES, REVIEW, ADDENDUM, *CANDIDATES]:
        require(path.exists(), f"Precondition missing: {path.relative_to(ROOT)}")

    chapter = build_chapter()
    refs = build_references()
    review = build_review()
    validate(chapter, refs, review)

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

    validate(read(CHAPTER), read(REFERENCES), read(REVIEW))
    for path in CANDIDATES + [ADDENDUM]:
        require(not path.exists(), f"Temporary file was not removed: {path.relative_to(ROOT)}")

    print("Chapter 016 canonical integration validation: PASS")
    print(f"Applied chapter.md lines: {len(read(CHAPTER).splitlines())}")
    print(f"Applied references.md lines: {len(read(REFERENCES).splitlines())}")
    print(f"Applied review.md lines: {len(read(REVIEW).splitlines())}")
    print("APPLY COMPLETE — delete tools/chapter016_canonical_integrate.py before the atomic integration commit")


if __name__ == "__main__":
    try:
        main()
    except IntegrationError as exc:
        raise SystemExit(f"Chapter 016 canonical integration validation: FAIL\n{exc}")
