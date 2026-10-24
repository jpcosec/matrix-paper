#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path


ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,]+),", re.MULTILINE)
FIELD_RE = re.compile(r"(\w+)\s*=\s*(\{.*?\}|\".*?\")\s*,?", re.DOTALL)


@dataclass
class BibEntry:
    entry_type: str
    key: str
    fields: dict[str, str]


def parse_bibtex(path: Path) -> list[BibEntry]:
    text = path.read_text(encoding="utf-8")
    matches = list(ENTRY_RE.finditer(text))
    entries: list[BibEntry] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[start:end]
        fields: dict[str, str] = {}
        for field_match in FIELD_RE.finditer(block):
            name = field_match.group(1).lower()
            raw_value = field_match.group(2).strip()
            if raw_value.startswith("{") and raw_value.endswith("}"):
                value = raw_value[1:-1]
            elif raw_value.startswith('"') and raw_value.endswith('"'):
                value = raw_value[1:-1]
            else:
                value = raw_value
            fields[name] = " ".join(value.split())
        entries.append(BibEntry(match.group(1).lower(), match.group(2).strip(), fields))
    return entries


def candidate_url(entry: BibEntry) -> str | None:
    if entry.fields.get("url"):
        return entry.fields["url"]
    if entry.fields.get("doi"):
        doi = (
            entry.fields["doi"]
            .removeprefix("https://doi.org/")
            .removeprefix("http://doi.org/")
        )
        return f"https://doi.org/{doi}"
    return None


def fetch_status(url: str, timeout: float = 8.0) -> tuple[bool, int | None, str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "tractatusBIt-reference-check/1.0"},
        method="HEAD",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return True, getattr(response, "status", None), response.geturl()
    except urllib.error.HTTPError as exc:
        if exc.code in {405, 403}:
            fallback = urllib.request.Request(
                url,
                headers={"User-Agent": "tractatusBIt-reference-check/1.0"},
                method="GET",
            )
            try:
                with urllib.request.urlopen(fallback, timeout=timeout) as response:
                    return True, getattr(response, "status", None), response.geturl()
            except Exception as inner_exc:  # pragma: no cover - network dependent
                return False, getattr(inner_exc, "code", None), str(inner_exc)
        return False, exc.code, url
    except Exception as exc:  # pragma: no cover - network dependent
        return False, None, str(exc)


def build_report(entries: list[BibEntry]) -> tuple[str, int]:
    lines = ["# Reference URL report", ""]
    failures = 0
    for entry in entries:
        url = candidate_url(entry)
        if not url:
            lines.append(f"- `{entry.key}`: warning - no `url` or `doi` field")
            continue
        ok, status, resolved = fetch_status(url)
        if ok:
            if resolved != url:
                lines.append(
                    f"- `{entry.key}`: ok ({status}), redirected from `{url}` to `{resolved}`"
                )
            else:
                lines.append(f"- `{entry.key}`: ok ({status}) `{url}`")
            continue
        failures += 1
        lines.append(f"- `{entry.key}`: broken ({status}) `{url}` -> `{resolved}`")
    lines.append("")
    return "\n".join(lines), failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check BibTeX URLs and DOIs")
    parser.add_argument("bibtex", type=Path)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    entries = parse_bibtex(args.bibtex)
    report, failures = build_report(entries)

    if args.output:
        args.output.write_text(report, encoding="utf-8")
    print(report)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
