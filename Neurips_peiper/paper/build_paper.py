#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PAPER_DIR = PROJECT_ROOT / "paper"
BUILD_DIR = PAPER_DIR / "build"


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def ensure_dirs() -> None:
    PAPER_DIR.mkdir(exist_ok=True)
    BUILD_DIR.mkdir(exist_ok=True)


def require_binary(name: str) -> str:
    resolved = shutil.which(name)
    if not resolved:
        raise FileNotFoundError(f"Required binary not found on PATH: {name}")
    return resolved


def sync_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_front_matter(config: dict, abstract: str) -> str:
    lines = [
        "---",
        f'title: "{config["title"]}"',
        "author:",
        '  - "Anonymous Author(s)"',
    ]
    lines.append("bibliography:")
    lines.append('  - "references.bib"')
    lines.append(f'bibliographystyle: "{config.get("bibliography_style", "plainnat")}"')
    lines.append("abstract: |")
    for line in abstract.splitlines() or [""]:
        lines.append(f"  {line}")
    lines.append("---")
    return "\n".join(lines)


def build_main_markdown(config: dict) -> Path:
    abstract_file = (PAPER_DIR / config["abstract_file"]).resolve()
    abstract = read_text(abstract_file)
    front_matter = build_front_matter(config, abstract)
    section_paths = [(PAPER_DIR / section).resolve() for section in config["sections"]]
    body_parts = [read_text(path) for path in section_paths]
    main_md = f"{front_matter}\n\n" + "\n\n".join(body_parts) + "\n"
    output = PAPER_DIR / "main.md"
    write_text(output, main_md)
    return output


def generate_checklist(config: dict) -> Path:
    formatting_dir = (PAPER_DIR / config["formatting_dir"]).resolve()
    source = formatting_dir / "checklist.tex"
    answers_file = (PAPER_DIR / config["checklist_answers"]).resolve()
    answers = load_yaml(answers_file)["answers"]

    lines = source.read_text(encoding="utf-8").splitlines()
    cleaned: list[str] = []
    skip = False
    answer_index = 0
    macro_map = {"yes": r"\answerYes{}", "no": r"\answerNo{}", "na": r"\answerNA{}"}

    def normalize_answer(value: object) -> str:
        if isinstance(value, bool):
            return "yes" if value else "no"
        return str(value).strip().lower()

    for line in lines:
        if line.strip() == "%%% BEGIN INSTRUCTIONS %%%":
            skip = True
            continue
        if line.strip() == "%%% END INSTRUCTIONS %%%":
            skip = False
            continue
        if skip:
            continue
        if "Answer: \\answerTODO{}" in line:
            answer = answers[answer_index]
            normalized = normalize_answer(answer["answer"])
            cleaned.append(f"    \\item[] Answer: {macro_map[normalized]}")
            continue
        if "Justification: \\justificationTODO{}" in line:
            answer = answers[answer_index]
            cleaned.append(f"    \\item[] Justification: {answer['justification']}")
            answer_index += 1
            continue
        cleaned.append(line)

    output = PAPER_DIR / "checklist.tex"
    write_text(output, "\n".join(cleaned) + "\n")
    return output


def sync_assets(config: dict) -> None:
    formatting_dir = (PAPER_DIR / config["formatting_dir"]).resolve()
    sync_file(formatting_dir / "neurips_2026.sty", PAPER_DIR / "neurips_2026.sty")
    bibliography_source = (PAPER_DIR / config["bibliography"]).resolve()
    sync_file(bibliography_source, PAPER_DIR / "references.bib")


def render_tex(config: dict, main_md: Path) -> Path:
    pandoc = require_binary("pandoc")
    output_basename = config.get("output_basename", "neurips_2026")
    tex_output = PAPER_DIR / f"{output_basename}.tex"
    template = PAPER_DIR / "template.tex"
    command = [
        pandoc,
        str(main_md),
        "--from",
        "markdown+tex_math_dollars",
        "--to",
        "latex",
        "--standalone",
        "--template",
        str(template),
        "--natbib",
        "--output",
        str(tex_output),
        "--resource-path",
        f"{PAPER_DIR}:{PROJECT_ROOT}",
    ]
    subprocess.run(command, check=True, cwd=PAPER_DIR)
    return tex_output


def compile_pdf(tex_path: Path) -> Path:
    pdflatex = require_binary("pdflatex")
    bibtex = require_binary("bibtex")
    stem = tex_path.stem
    for command in (
        [pdflatex, "-interaction=nonstopmode", stem + ".tex"],
        [bibtex, stem],
        [pdflatex, "-interaction=nonstopmode", stem + ".tex"],
        [pdflatex, "-interaction=nonstopmode", stem + ".tex"],
    ):
        subprocess.run(command, check=True, cwd=PAPER_DIR)
    return PAPER_DIR / f"{stem}.pdf"


def run_reference_check() -> None:
    report = PAPER_DIR / "reference_report.md"
    script = Path(__file__).resolve().parent / "check_references.py"
    subprocess.run(
        [
            sys.executable,
            str(script),
            str(PAPER_DIR / "references.bib"),
            "--output",
            str(report),
        ],
        check=False,
        cwd=PAPER_DIR,
    )


def main() -> int:
    global PAPER_DIR, BUILD_DIR
    parser = argparse.ArgumentParser(description="Build the NeurIPS 2026 paper")
    parser.add_argument(
        "--config",
        type=Path,
        default=PAPER_DIR / "paper.yaml",
        help="Path to the build configuration file",
    )
    args = parser.parse_args()

    PAPER_DIR = args.config.resolve().parent
    BUILD_DIR = PAPER_DIR / "build"
    ensure_dirs()
    config = load_yaml(args.config)
    sync_assets(config)
    main_md = build_main_markdown(config)
    tex_path = render_tex(config, main_md)
    pdf_path = compile_pdf(tex_path)
    run_reference_check()
    print(pdf_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
