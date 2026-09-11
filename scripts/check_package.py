#!/usr/bin/env python3
"""Offline package completeness and privacy-ish scans. Not a behavior proof."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "herdr-orchestration"

REQUIRED = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    ".gitignore",
    "SOURCE-REVISION.md",
    "skills/herdr-orchestration/SKILL.md",
    "skills/herdr-orchestration/CONTRACT-SNIPPET.md",
    "skills/herdr-orchestration/references/mode.md",
    "skills/herdr-orchestration/references/profiles.md",
    "skills/herdr-orchestration/references/packets.md",
    "skills/herdr-orchestration/references/claims.md",
    "skills/herdr-orchestration/references/runbooks.md",
    "skills/herdr-orchestration/references/adapters/herdr.md",
    "skills/herdr-orchestration/references/install.md",
    "skills/herdr-orchestration/scripts/claims.py",
    "skills/herdr-orchestration/examples/config.example.json",
    "skills/herdr-orchestration/examples/early-packet.md",
    "skills/herdr-orchestration/examples/task-packet.md",
    "skills/herdr-orchestration/examples/closing-packet.json",
    "skills/herdr-orchestration/examples/receipts.json",
    "tests/test_claims.py",
    "tests/policy-scenarios.md",
    "tests/traceability.md",
    "scripts/check_package.py",
    ".github/workflows/check.yml",
]

PRIVATE_PATTERNS = [
    re.compile(r"notion\.so|notion\.com", re.I),
    re.compile(r"vmi\d+", re.I),
    re.compile(r"Dropbox/Projects"),
    re.compile(r"contabo", re.I),
    re.compile(r"--dangerously-bypass"),
    re.compile(r"op://"),
    re.compile(r"sk-[a-zA-Z0-9]{20,}"),
]


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing:{rel}")

    skill_md = SKILL / "SKILL.md"
    if skill_md.is_file():
        text = skill_md.read_text(encoding="utf-8")
        if not text.startswith("---"):
            errors.append("frontmatter:missing")
        elif "name: herdr-orchestration" not in text.split("---", 2)[1]:
            errors.append("frontmatter:name")
        if "description:" not in text.split("---", 2)[1]:
            errors.append("frontmatter:description")

    skip_scan = {
        Path("scripts/check_package.py"),
    }
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        if rel in skip_scan:
            continue
        if path.suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico"}:
            continue
        try:
            body = path.read_text(encoding="utf-8")
        except UnicodeError:
            continue
        for pat in PRIVATE_PATTERNS:
            if pat.search(body):
                errors.append(f"private:{rel}:{pat.pattern}")

    if errors:
        for e in errors:
            print(e)
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
