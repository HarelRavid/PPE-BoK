#!/usr/bin/env python3
"""One-shot controlled canonical integration for PPE-BoK Working Chapter 014.

Default mode is dry-run: build and validate the proposed integrated manuscript
in memory, print a summary, and write nothing.

Use --apply only from the controlled branch after reviewing this script and the
Canonical Integration Brief. In apply mode it writes the canonical files,
removes the two temporary Investigation 9/10 authoring files, and removes this
script. It does NOT commit, push, merge, rebase, or touch main.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

BRANCH = "chapter-014-engineering-development"
ROOT = Path("chapters/chapter-014-atomic-structure-chemical-bonding-carbon-chemistry")
CHAPTER = ROOT / "chapter.md"
INV9 = ROOT / "investigation-009-authoring.md"
INV10 = ROOT / "investigation-010-authoring.md"
REVIEW = ROOT / "review.md"
OUTLINE = ROOT / "technical-outline.md"
CDB = Path("docs/PDS/Chapter-Design-Briefs/CDB-014-Atomic-Structure-Chemical-Bonding-Carbon-Chemistry.md")
SELF = Path("tools/chapter014_canonical_integrate.py")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def require_repo_state() -> None:
    branch = git("branch", "--show-current")
    if branch != BRANCH:
        raise RuntimeError(f"Wrong branch: {branch!r}; expected {BRANCH!r}")

    status = git("status", "--short")
    if status:
        raise RuntimeError("Working tree is not clean before integration:\n" + status)

    for path in (CHAPTER, INV9, INV10, REVIEW, OUTLINE, CDB, SELF):
        if not path.exists():
            raise RuntimeError(f"Missing controlled file: {path}")


def clean_authoring(path: Path, heading: str, number: str) -> str:
    text = path.read_text(encoding="utf-8")
    start = text.index(heading)
    text = text[start:]
    sep = text.find("\n---\n")
    if not (0 < sep < 1500):
        raise RuntimeError(f"Controlled preamble separator not found in {path}")

    text = heading + "\n\n" + text[sep + len("\n---\n"):].lstrip()

    # Temporary authoring files use one heading level too high after the
    # Investigation heading. Normalize them for canonical chapter nesting.
    text = re.sub(rf"(?m)^## ({number}\.\d+\.\d+.*?)$", r"### \1", text)
    text = re.sub(rf"(?m)^# ({number}\.\d+.*?)$", r"## \1", text)
    return text.strip() + "\n"


def build() -> tuple[str, str, str, str, dict[str, int]]:
    original = CHAPTER.read_text(encoding="utf-8")
    if original.count("# Investigation 9") != 1 or original.count("# Investigation 10") != 1:
        raise RuntimeError("Canonical chapter does not contain exactly one Investigation 9/10 stub pair")
    if "**Authoring state:** BLOCKED" not in original:
        raise RuntimeError("Expected controlled Investigation 9 BLOCKED stub not found")

    prefix = original.split("# Investigation 9", 1)[0].rstrip() + "\n\n"

    inv9 = clean_authoring(
        INV9,
        "# Investigation 9 — How Do Molecular Features Become Engineering-Property Hypotheses?",
        "9",
    )
    inv10 = clean_authoring(
        INV10,
        "# Investigation 10 — What Can Chemistry Tell Us, and Where Must the Engineer Stop?",
        "10",
    )

    # TR-014-01 — reserve Level 1–6 for the final evidence ladder.
    prefix = prefix.replace(
        "After Investigation 1, the engineer should be able to classify a statement into one of three levels:",
        "After Investigation 1, the engineer should be able to classify a statement into one of three claim classes:",
    )
    prefix = prefix.replace("### Level 1 — Chemistry fact", "### Claim Class A — Chemistry fact")
    prefix = prefix.replace("### Level 2 — Mechanism hypothesis", "### Claim Class B — Mechanism hypothesis")
    prefix = prefix.replace("### Level 3 — Engineering conclusion", "### Claim Class C — Engineering conclusion")
    prefix = prefix.replace(
        "**Never jump directly from Level 1 to Level 3.**",
        "**Never jump directly from Claim Class A to Claim Class C.**",
    )
    prefix = prefix.replace(
        "make Level 1 accurate and Level 2 useful",
        "make Claim Class A accurate and Claim Class B useful",
    )
    prefix = prefix.replace("needed to reach Level 3", "needed to reach Claim Class C")

    # Final TAB-014-002 belongs to Investigation 9.
    prefix = prefix.replace(
        "## 6.9 TAB-014-002 — Carbon feature → mechanism → evidence boundary",
        "## 6.9 Carbon feature → mechanism → evidence boundary — preliminary teaching table",
    )

    # TR-014-04 — bounded wording controls from the Investigation 9 review.
    inv9 = inv9.replace(
        "morphology, free volume, crystallinity, copolymer structure and processing.",
        "morphology, packing/free-volume effects, crystallinity, copolymer structure and processing.",
    )
    inv9 = inv9.replace(
        "- amorphous free volume;",
        "- packing / morphology-related free-volume effects;",
    )
    inv9 = inv9.replace(
        "crystallinity, density/free volume, copolymer structure, film/test configuration",
        "crystallinity, density/packing/free-volume interpretation, copolymer structure, film/test configuration",
    )

    # Investigation 9 defines development requirements; Investigation 10 owns
    # the final controlled FIG-014-006 specification.
    inv9 = inv9.replace(
        "## 9.9 FIG-014-006 — Molecular feature to engineering evidence chain — scientific specification",
        "## 9.9 Evidence-chain design requirements for FIG-014-006",
    )

    # Keep only one final WF-014-001, owned by Investigation 10.
    wf_start = inv9.index("## 9.10 WF-014-001")
    ver_start = inv9.index("## 9.11 Verification")
    inv9 = (
        inv9[:wf_start]
        + "## 9.10 Workflow checkpoint before the final chapter decision tool\n\n"
        + "Cases A–C have now validated the reasoning sequence used throughout this Investigation:\n\n"
        + "`observe structure → state mechanism hypothesis → define measurable property → obtain direct evidence → identify confounders → set transferability boundary → qualify → decide`\n\n"
        + "The final controlled `WF-014-001` is intentionally placed in Investigation 10, where the scientific reasoning track is joined to product/application qualification and the chapter stop-rule.\n\n"
        + "---\n\n"
        + inv9[ver_start:]
    )

    # TR-014-03 / E10-01 — the ladder is PPE-BoK reasoning architecture, not
    # a normative external taxonomy.
    ladder_needle = "A useful way to prevent overclaiming is to separate evidence into levels.\n"
    ladder_note = (
        "\n> **PPE-BoK framework:** The following levels are a PPE-BoK reasoning framework for controlling evidence transfer; "
        "they are not a normative classification defined by ISO, IUPAC or another single standards body.\n"
    )
    if ladder_needle not in inv10:
        raise RuntimeError("Investigation 10 evidence-ladder insertion point not found")
    inv10 = inv10.replace(ladder_needle, ladder_needle + ladder_note, 1)
    inv10 = inv10.replace("# Chapter 014 engineering closure — candidate text", "# Chapter engineering closure")

    asset_tail = """# Chapter engineering assets — current register

| ID | Asset | Status |
|---|---|---|
| FIG-014-001 | Atom-to-material hierarchy | Placeholder integrated; graphic production pending |
| FIG-014-002 | Primary Bonding and Noncovalent Interaction Map | Scientific specification complete; graphic production pending |
| FIG-014-003 | Carbon hybridization and geometry | Scientific specification complete; graphic production pending |
| FIG-014-004 | Sigma and pi bonding in ethene | Scientific specification complete; graphic production pending |
| FIG-014-005 | Ethene to polyethylene bridge | Scientific specification complete; graphic production pending |
| FIG-014-006 | Molecular feature to engineering evidence chain | Final scientific specification integrated; graphic production pending |
| TAB-014-001 | Bonding types and engineering relevance | Integrated |
| TAB-014-002 | Molecular feature / likely mechanism / invalid direct conclusion | Integrated in Investigation 9 |
| TAB-014-003 | Controlled structure–property teaching cases | Integrated; Investigation 9 authoring review PASS |
| TAB-014-004 | Downstream chapter ownership crosswalk | Integrated in Investigation 10 |
| EX-014-001 | Reading ethene and PE repeat unit | Integrated; final full-chapter review pending |
| EX-014-002 | Comparing two simple polymer hypotheses | Integrated; Investigation 9 authoring review PASS |
| WF-014-001 | Chemical structure → evidence → engineering decision boundary | Final chapter version integrated |
| CL-014-001 | Before inferring engineering behaviour from chemical structure | Integrated |

---

# Publication hold points

Chapter 014 has completed its approved Engineering Development arc, but publication closure is not implied.

Before publication, the chapter still requires:

- final full-file Technical Review after canonical integration;
- final claim-level Standards/Evidence publication pass;
- final Editorial / Style Review;
- continuous-manuscript Desk Test;
- final figure production where required for Publishing;
- explicit author review / Human Approval Gate;
- synchronization with current `main` and controlled merge.

No chemistry, vocabulary source or primary-study result in this chapter independently authorizes a piping material, pressure, temperature, chemical service, permeability allowance, lifetime or joining condition.

# References

See `references.md` for the controlled Chapter 014 source and evidence register.
"""

    assembled = (
        prefix.rstrip()
        + "\n\n"
        + inv9.strip()
        + "\n\n---\n\n"
        + inv10.strip()
        + "\n\n---\n\n"
        + asset_tail
    )

    # TR-014-02 — use the clearer terminology across controlled architecture.
    assembled = assembled.replace(
        "Primary and secondary bonding map",
        "Primary Bonding and Noncovalent Interaction Map",
    )
    assembled = assembled.replace(
        "Primary and secondary bonding",
        "Primary Bonding and Noncovalent Interaction",
    )

    outline = OUTLINE.read_text(encoding="utf-8")
    cdb = CDB.read_text(encoding="utf-8")
    for name, value in (("outline", outline), ("cdb", cdb)):
        value = value.replace(
            "Primary and secondary bonding map",
            "Primary Bonding and Noncovalent Interaction Map",
        )
        value = value.replace(
            "Primary and secondary bonding",
            "Primary Bonding and Noncovalent Interaction",
        )
        if name == "outline":
            outline = value
        else:
            cdb = value

    outline = outline.replace(
        "Investigation 1 may be authored now under the current evidence plan. Later Investigations shall not be authored ahead of their required evidence research merely to accelerate chapter completion.",
        "Investigations 1–10 have now been authored through their required evidence checkpoints. Canonical integration has been completed; final full-chapter Technical Review and downstream validation gates remain required before Ready-for-Review.",
    )
    checkpoint = """

## 8. Engineering Development completion checkpoint — 2026-08-15

- Investigations 1–8: authored controlled candidates.
- Investigation 9: primary-literature gate PASS; authoring review PASS; canonical integration complete.
- Investigation 10 / chapter closure: authoring review PASS; canonical integration complete.
- Pre-integration Technical Review: CONDITIONAL PASS; TR-014-01 through TR-014-04 applied during integration.
- Logical-manuscript Technical/Evidence Review: PASS FOR CANONICAL INTEGRATION.
- Logical-manuscript Editorial/Desk Review: CONDITIONAL PASS.
- Next gate: final full-file Technical Review of the integrated manuscript.

This checkpoint does not imply final Standards/Evidence publication validation, final Editorial/Style Review, Human Approval or publication readiness.
"""
    if "## 8. Engineering Development completion checkpoint" not in outline:
        outline = outline.rstrip() + checkpoint

    review = REVIEW.read_text(encoding="utf-8")
    review_checkpoint = """

## 11. Canonical-integration checkpoint — 2026-08-15

Investigations 9–10 were integrated into `chapter.md` only after their controlled authoring reviews, the pre-integration Technical Review, the logical-manuscript Technical/Evidence Review and the logical-manuscript Editorial/Desk Review. The integration applied TR-014-01 through TR-014-04, including claim-class/evidence-level disambiguation, noncovalent-interaction terminology for FIG-014-002, explicit non-normative labeling of the PPE-BoK evidence ladder, and Investigation 9 transferability wording controls.

**Current disposition:** Engineering Development arc integrated; final full-file Technical Review is the next gate. Final claim-level Standards/Evidence publication pass, final Editorial/Style Review, final Desk Test, Human Approval and merge remain open.
"""
    if "## 11. Canonical-integration checkpoint" not in review:
        review = review.rstrip() + review_checkpoint

    counts = {
        "lines": len(assembled.splitlines()),
        "investigation9": assembled.count("# Investigation 9 —"),
        "investigation10": assembled.count("# Investigation 10 —"),
        "tab014002_final": assembled.count("TAB-014-002 — Molecular feature"),
        "wf014001_final": assembled.count("WF-014-001 — Chemical structure to engineering decision boundary"),
    }

    # Safety assertions.
    assert counts["investigation9"] == 1
    assert counts["investigation10"] == 1
    assert "**Authoring state:** BLOCKED" not in assembled
    assert "**Authoring state:** planned" not in assembled
    assert "Claim Class A — Chemistry fact" in assembled
    assert "Never jump directly from Claim Class A to Claim Class C" in assembled
    assert "PPE-BoK reasoning framework for controlling evidence transfer" in assembled
    assert "## 6.9 TAB-014-002" not in assembled
    assert "## 9.3 TAB-014-002" in assembled
    assert "## 9.10 WF-014-001" not in assembled
    assert "## 10.5 WF-014-001" in assembled
    assert "Primary Bonding and Noncovalent Interaction Map" in assembled
    assert "Controlled authoring file" not in assembled
    assert counts["lines"] > 2200

    return assembled, outline, review, cdb, counts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the validated integration to the working tree",
    )
    args = parser.parse_args()

    require_repo_state()
    assembled, outline, review, cdb, counts = build()

    print("Chapter 014 canonical integration validation: PASS")
    for key, value in counts.items():
        print(f"  {key}: {value}")

    if not args.apply:
        print("DRY RUN ONLY — no files changed. Re-run with --apply after review.")
        return 0

    CHAPTER.write_text(assembled, encoding="utf-8")
    OUTLINE.write_text(outline, encoding="utf-8")
    REVIEW.write_text(review, encoding="utf-8")
    CDB.write_text(cdb, encoding="utf-8")

    INV9.unlink()
    INV10.unlink()
    SELF.unlink()

    print("APPLIED. No commit or push was performed.")
    print("Next required checks:")
    print("  git diff --check")
    print("  git status --short")
    print("  inspect the diff, then commit/push only if clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
