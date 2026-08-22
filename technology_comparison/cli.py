"""Command-line report generator covering every discovered technology family."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .baselines import BASELINES
from .catalog import discover_technologies
from .models import DEFAULT_SCENARIOS, calculate, headline


def _load_overrides(path: str | None) -> dict[str, dict[str, float]]:
    if not path:
        return {}
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("assumptions file must contain an object keyed by technology path")
    return data


def _markdown(root: Path, overrides: dict[str, dict[str, float]]) -> str:
    technologies = discover_technologies(root)
    lines = [
        "# Theoretical Technology Comparison",
        "",
        "> **Screening output, not predicted performance.** Every row uses an illustrative default scenario unless its path has explicit overrides. Replace defaults with measured or design-controlled inputs before drawing conclusions.",
        "",
        f"Technology families covered: **{len(technologies)}**.",
        "",
        "| Technology family | Domain | Model | Illustrative result | Why this model |",
        "|---|---|---|---|---|",
    ]
    for technology in technologies:
        result = calculate(technology.model, overrides.get(technology.path))
        cells = (technology.path, technology.domain, technology.model, headline(result), technology.rationale)
        lines.append("| " + " | ".join(cell.replace("|", "\\|") for cell in cells) + " |")
    lines.extend(["", "## Present-day reference points", "", "| Key | Value | Reference |", "|---|---|---|"])
    for key, benchmark in BASELINES.items():
        lines.append(f"| {key} | {benchmark.value:g} {benchmark.unit} | [{benchmark.label}]({benchmark.source}) |")
    lines.extend(["", "## Default scenarios", "", "```json", json.dumps(DEFAULT_SCENARIOS, indent=2, sort_keys=True), "```", ""])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="archive root")
    parser.add_argument("--assumptions", help="JSON overrides keyed by technology path")
    parser.add_argument("--output", help="write Markdown report to this path; stdout if omitted")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON instead of Markdown")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    overrides = _load_overrides(args.assumptions)
    if args.json:
        payload = []
        for technology in discover_technologies(root):
            payload.append({**technology.__dict__, "calculation": calculate(technology.model, overrides.get(technology.path))})
        content = json.dumps(payload, indent=2, ensure_ascii=False)
    else:
        content = _markdown(root, overrides)
    if args.output:
        Path(args.output).write_text(content + "\n", encoding="utf-8")
    else:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        print(content)
    return 0
