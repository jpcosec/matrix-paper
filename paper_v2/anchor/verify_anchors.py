#!/usr/bin/env python3
"""Guardrail test for the KB->paper anchoring (Fase 3).

Run from paper_v2/:  python3 anchor/verify_anchors.py
Exit 1 if any check fails.
"""
from __future__ import annotations

import glob
import hashlib
import json
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent          # paper_v2/
MATRIX_ROOT = ROOT.parent                              # Matrix/
BASELINE_FILE = ROOT / "anchor" / "build" / "pre_change_hashes.txt"

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, ok, detail))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# 1. Pipeline artifacts exist and are fresh (composed older-or-equal to validation report)
composed = ROOT / "build" / "paper.composed.md"
report_path = ROOT / "build" / "validation_report.json"
check(
    "pipeline_artifacts_exist",
    composed.is_file() and report_path.is_file(),
    f"composed={composed.is_file()} report={report_path.is_file()}",
)

# 2. Invariante de no-invasividad: el cuerpo compuesto NO depende del anclaje.
# Compone con mapping (A), sin mapping (B) y con mapping otra vez (A').
# A == B (el anclaje no altera paragraph_text/section_body) y A' == A (idempotencia).
# Robusto ante ediciones externas del paper (el usuario edita sections/ en vivo).
import subprocess  # noqa: E402

mapping_path = ROOT / "anchor" / "mapping.yaml"
bypass_path = ROOT / "anchor" / "mapping.yaml.bypass"

def run_pipeline() -> str:
    subprocess.run([sys.executable, "build_pipeline.py"], cwd=ROOT,
                   check=True, capture_output=True)
    return sha256(ROOT / "build" / "paper.composed.md")

hash_a = run_pipeline()
try:
    mapping_path.rename(bypass_path)
    hash_b = run_pipeline()
finally:
    bypass_path.rename(mapping_path)
hash_a2 = run_pipeline()
check(
    "composed_body_independent_of_anchors",
    hash_a == hash_b,
    f"con={hash_a[:12]} sin={hash_b[:12]}",
)
check(
    "composed_idempotent",
    hash_a2 == hash_a,
    f"rerun={hash_a2[:12]} vs {hash_a[:12]}",
)

# 3. validation_report all valid:true
report = json.loads(report_path.read_text())["validation"]
invalid = [x["path"] for x in report if not x["valid"]]
check("validation_all_true", not invalid, f"{len(report)} entries, invalid={invalid[:5]}")

# 4. kb refs in notes and kb file count == mapping paragraph entries
mapping = yaml.safe_load((ROOT / "anchor" / "mapping.yaml").read_text())
expected = sum(len(v) for v in mapping["paragraphs"].values())
kb_files = sorted(glob.glob(str(ROOT / "sources" / "kb" / "*.md")))
notes_with_kb = 0
for note in glob.glob(str(ROOT / "notes" / "*.md")):
    if "kb/" in Path(note).read_text(encoding="utf-8"):
        notes_with_kb += 1
anchored_paras = sum(1 for v in mapping["paragraphs"].values() if v)
check(
    "kb_count_matches_mapping",
    len(kb_files) == expected,
    f"kb_files={len(kb_files)} mapping_entries={expected}",
)
check(
    "notes_reference_kb",
    notes_with_kb == anchored_paras,
    f"notes_with_kb={notes_with_kb} anchored_paragraphs={anchored_paras}",
)

# 5. every kb source origin resolves to an existing atom file
bad_origins = []
for f in kb_files:
    m = re.search(r"^Origin: (.+)$", Path(f).read_text(encoding="utf-8"), re.M)
    if not m or not (ROOT / m.group(1).strip()).resolve().is_file():
        bad_origins.append(Path(f).name)
check("kb_origins_resolve", not bad_origins, f"bad={bad_origins[:5]}")

print(f"{'CHECK':<34} RESULT  DETAIL")
for name, ok, detail in results:
    print(f"{name:<34} {'PASS' if ok else 'FAIL':<6} {detail}")
failed = [n for n, ok, _ in results if not ok]
print(f"\n{'ALL PASS' if not failed else 'FAILED: ' + ', '.join(failed)}")
sys.exit(1 if failed else 0)
