#!/usr/bin/env python3
"""Basic public-document consistency check; not a mathematical proof checker."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DOCS = (
    "README.md",
    "RESEARCH_STATUS.md",
    "TECHNICAL_BRIEF.md",
    "EXTERNAL_RECONCILIATION.md",
    "TARGET_SCOPE.md",
    "REVIEW_ERRATA_20261026.md",
    "CONTRIBUTING.md",
    "RIGHTS_AND_ATTRIBUTION.md",
    "DOCUMENTATION_STOP_ADVISORY.md",
)
LINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")
REPO_RESEARCH_HEAD = "ym/checkpoints/YM_HEAD_R108_20261026.json"


def check() -> list[str]:
    errors: list[str] = []
    checkpoint_path = ROOT / REPO_RESEARCH_HEAD
    if not checkpoint_path.exists():
        return [f"missing canonical checkpoint: {REPO_RESEARCH_HEAD}"]
    try:
        head = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read canonical checkpoint: {exc}"]
    if head.get("passes_completed_through") != "YM-R108":
        errors.append("canonical head no longer R108: update public status review")
    if head.get("live_cursor") != "YM-R109" or head.get("live_cursor_consumed") is not False:
        errors.append("native cursor changed: documentation snapshot must be revisited")
    if head.get("claim_status") != "UNPROVED_RESEARCH_PROGRAM":
        errors.append("canonical research status changed: documentation must be reviewed")
    for rel in PUBLIC_DOCS:
        doc = ROOT / rel
        if not doc.exists():
            errors.append(f"missing public document: {rel}")
            continue
        content = doc.read_text(encoding="utf-8")
        if "YM-R109" not in content and rel in (
            "README.md",
            "RESEARCH_STATUS.md",
            "TECHNICAL_BRIEF.md",
            "EXTERNAL_RECONCILIATION.md",
            "TARGET_SCOPE.md",
        ):
            errors.append(f"missing native-cursor reference: {rel}")
        for target in LINK.findall(content):
            dest = target.split(" ", 1)[0].strip("<>")
            parsed = urlsplit(dest)
            if parsed.scheme or dest.startswith(("#", "mailto:", "//")):
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            local = (doc.parent / path).resolve()
            if not local.is_relative_to(ROOT.resolve()):
                errors.append(f"link escapes repository: {rel} -> {target}")
            elif not local.exists():
                errors.append(f"broken local link: {rel} -> {target}")
    return errors


if __name__ == "__main__":
    failures = check()
    if failures:
        print("Documentation consistency FAIL:")
        for error in failures:
            print(" -", error)
        sys.exit(1)
    print("Documentation consistency PASS (paths and snapshot labels only).")
    print("This check does not validate equations, source fidelity, or external URLs.")
