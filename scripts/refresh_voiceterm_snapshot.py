#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "_data" / "voiceterm_snapshot.json"
DEFAULT_LOCAL_REPO = Path("/Users/jguida941/testing_upgrade/codex-voice")
DEFAULT_REPO_URL = "https://github.com/jguida941/voiceterm.git"

WORKFLOW_FAMILIES = [
    (
        "Core product quality workflows",
        "core-quality",
        "Core product quality",
        "Runtime quality, latency, parser, memory, security, coverage, and mutation lanes.",
    ),
    (
        "Docs, process, and policy workflows",
        "docs-process-policy",
        "Docs, process, and policy",
        "Documentation linting, workflow policy, supply-chain review, tooling governance, and watchdog checks.",
    ),
    (
        "AI triage and autonomy workflows",
        "ai-triage-autonomy",
        "AI triage and autonomy",
        "Triage ingestion, bounded remediation loops, failure capture, and autonomous controller or swarm runs.",
    ),
    (
        "Release and publish workflows",
        "release-publish",
        "Release and publish",
        "Release preflight, package publishing, binary distribution, and provenance attestation.",
    ),
]


def run(args: list[str], cwd: Path) -> str:
    result = subprocess.run(
        args,
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def pretty_date(value: str) -> str:
    return datetime.strptime(value, "%Y-%m-%d").strftime("%B %d, %Y").replace(" 0", " ")


def format_int(value: int) -> str:
    return f"{value:,}"


def count_lines(paths: list[Path]) -> int:
    total = 0
    for path in paths:
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            total += sum(1 for _ in handle)
    return total


def parse_runtime_bundle_commands(agents_text: str) -> int:
    match = re.search(
        r"### `bundle\.runtime`\n\n```bash\n(.*?)\n```",
        agents_text,
        re.DOTALL,
    )
    if not match:
        raise RuntimeError("Could not locate bundle.runtime in AGENTS.md")
    return sum(1 for line in match.group(1).splitlines() if line.strip())


def parse_bundle_count(agents_text: str) -> int:
    names = re.findall(r"^### `(bundle\.(?:runtime|docs|tooling|release))`$", agents_text, re.MULTILINE)
    return len(set(names))


def parse_workflow_families(readme_text: str) -> list[dict[str, object]]:
    families: list[dict[str, object]] = []
    for heading, slug, name, summary in WORKFLOW_FAMILIES:
        pattern = re.compile(
            rf"^## {re.escape(heading)}\n\n\| Workflow file \| What it does \| When it runs \| Main checks/actions \| First local command \|\n\|---\|---\|---\|---\|---\|\n(.*?)(?=^## |\Z)",
            re.MULTILINE | re.DOTALL,
        )
        match = pattern.search(readme_text)
        if not match:
            raise RuntimeError(f"Could not parse workflow section: {heading}")
        count = sum(1 for line in match.group(1).splitlines() if line.startswith("| `"))
        families.append(
            {
                "slug": slug,
                "name": name,
                "count": count,
                "count_display": format_int(count),
                "summary": summary,
            }
        )
    return families


def prepare_repo(repo_path: str | None, repo_url: str) -> tuple[Path, str, tempfile.TemporaryDirectory[str] | None]:
    if repo_path:
        path = Path(repo_path).expanduser().resolve()
        return path, "local-path", None
    if DEFAULT_LOCAL_REPO.exists():
        return DEFAULT_LOCAL_REPO.resolve(), "local-default", None

    tempdir = tempfile.TemporaryDirectory(prefix="voiceterm-snapshot-")
    path = Path(tempdir.name)
    subprocess.run(
        ["git", "clone", "--quiet", "--filter=blob:none", repo_url, str(path)],
        check=True,
    )
    return path, "cloned", tempdir


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh the VoiceTerm snapshot used by the paper site.")
    parser.add_argument("--repo-path", help="Use an existing local VoiceTerm checkout.")
    parser.add_argument("--repo-url", default=DEFAULT_REPO_URL, help="Clone URL to use when no local repo path is available.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Path to the generated JSON snapshot.")
    args = parser.parse_args()

    repo, source_mode, tempdir = prepare_repo(args.repo_path, args.repo_url)
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    agents_text = (repo / "AGENTS.md").read_text(encoding="utf-8")
    workflows_readme = (repo / ".github/workflows/README.md").read_text(encoding="utf-8")

    guard_scripts = sorted((repo / "dev/scripts/checks").glob("check_*.py"))
    workflow_files = sorted((repo / ".github/workflows").glob("*.yml"))
    rust_files = [path for path in (repo / "rust/src/bin/voiceterm").rglob("*") if path.is_file()]
    devctl_files = [
        path
        for path in (repo / "dev/scripts/devctl").rglob("*")
        if path.is_file() and path.suffix in {".py", ".sh", ".md"}
    ]

    first_commit = run(["git", "log", "--reverse", "--format=%cs"], repo).splitlines()[0]
    head_date = run(["git", "log", "-1", "--format=%cs"], repo)

    workflow_families = parse_workflow_families(workflows_readme)
    commit_count = int(run(["git", "rev-list", "--count", "HEAD"], repo))
    tag_count = len(run(["git", "tag"], repo).splitlines())
    bundle_count = parse_bundle_count(agents_text)
    runtime_bundle_commands = parse_runtime_bundle_commands(agents_text)
    rust_runtime_lines = count_lines(rust_files)
    devctl_lines = count_lines(devctl_files)

    snapshot = {
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "snapshot_date": head_date,
        "snapshot_label": pretty_date(head_date),
        "first_commit_date": first_commit,
        "first_commit_label": pretty_date(first_commit),
        "repo_url": args.repo_url,
        "repo_web_url": args.repo_url.removesuffix(".git"),
        "source_mode": source_mode,
        "head_sha": run(["git", "rev-parse", "--short=12", "HEAD"], repo),
        "workflow_family_count": len(workflow_families),
        "workflow_families": workflow_families,
        "stats": {
            "commits": {
                "value": commit_count,
                "display": format_int(commit_count),
            },
            "tags": {
                "value": tag_count,
                "display": format_int(tag_count),
            },
            "guard_scripts": {
                "value": len(guard_scripts),
                "display": format_int(len(guard_scripts)),
            },
            "workflows": {
                "value": len(workflow_files),
                "display": format_int(len(workflow_files)),
            },
            "bundle_classes": {
                "value": bundle_count,
                "display": format_int(bundle_count),
            },
            "runtime_bundle_commands": {
                "value": runtime_bundle_commands,
                "display": format_int(runtime_bundle_commands),
            },
            "rust_runtime_lines": {
                "value": rust_runtime_lines,
                "display": format_int(rust_runtime_lines),
            },
            "devctl_lines": {
                "value": devctl_lines,
                "display": format_int(devctl_lines),
            },
        },
    }

    output_path.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    if tempdir is not None:
        tempdir.cleanup()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
