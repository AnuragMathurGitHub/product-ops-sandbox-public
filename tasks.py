"""Task runner for the Product Ops Sandbox.

One place for the development commands, standard library only:

    python tasks.py test        Run the unit tests.
    python tasks.py run         Run the deterministic scripts, then the mock demos.
    python tasks.py demo        Same as run, then list the generated outputs.
    python tasks.py lint        Ruff lint (install requirements-dev.txt first).
    python tasks.py format      Ruff format.
    python tasks.py typecheck   Mypy static type check.
    python tasks.py scan        Repo hygiene scan: ASCII only, wording, secret patterns.
    python tasks.py check       lint + typecheck + scan + test, the full local gate.

Running the sandbox itself needs none of this. The scripts and the agent lane
work with a plain Python install; see START_HERE.md.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

DETERMINISTIC_SCRIPTS = [
    "analyze_feedback.py",
    "score_roadmap.py",
    "summarize_metrics.py",
    "summarize_okrs.py",
    "summarize_releases.py",
]

MOCK_SCRIPTS = [
    "ai_classify_feedback.py",
    "ai_synthesize_research.py",
    "ai_detect_opportunities.py",
    "ai_review_product_planning.py",
    "ai_align_okrs.py",
    "ai_plan_release_measurement.py",
    "ai_weekly_product_insights.py",
]

SCAN_SKIP_DIRS = {
    ".git",
    ".private",
    "__pycache__",
    ".venv",
    "venv",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

# The scanner and its test must spell out the patterns they search for, so they
# would always flag themselves. They are checked by ruff, mypy, and the tests instead.
SCAN_SKIP_FILES = {"tasks.py", "test_tasks.py"}

# Public files must read like a finished product.
WORDING_PATTERN = re.compile(
    r"\b("
    r"coming soon|will be added|being assembled|when available|"
    r"preview|pending|incomplete|TODO|TBD"
    r")\b",
    re.IGNORECASE,
)

# Key-shaped strings and credential assignments. Placeholders in docs must not
# match these, which is why the docs use values like your-anthropic-key.
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]"),
    re.compile(r"OPENAI_API_KEY="),
    re.compile(r"password\s*="),
    re.compile(r"token\s*="),
    re.compile(r"secret\s*="),
]


def iter_scan_files(root: Path) -> list[Path]:
    """Collect the files the hygiene scan should read, honoring the skip lists."""
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in SCAN_SKIP_DIRS for part in relative.parts):
            continue
        if path.name in SCAN_SKIP_FILES:
            continue
        files.append(path)
    return files


def scan_tree(root: Path) -> list[str]:
    """Scan a tree for non-ASCII text, forbidden wording, and secret patterns.

    Returns one finding per line as "path:line: message". An empty list means
    the tree is clean. Binary files (anything that does not decode as UTF-8)
    are skipped.
    """
    findings = []
    for path in iter_scan_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        relative = path.relative_to(root)
        for line_number, line in enumerate(text.splitlines(), start=1):
            where = f"{relative}:{line_number}"
            if not line.isascii():
                findings.append(f"{where}: non-ASCII character")
            match = WORDING_PATTERN.search(line)
            if match:
                findings.append(f"{where}: forbidden wording '{match.group(0)}'")
            for pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    findings.append(f"{where}: secret-shaped text matching '{pattern.pattern}'")
    return findings


def run_command(command: list[str]) -> int:
    """Run one command from the repo root and return its exit code."""
    print(f"$ {' '.join(command)}")
    return subprocess.run(command, cwd=REPO_ROOT).returncode


def task_test() -> int:
    return run_command([sys.executable, "-m", "unittest", "discover", "-s", "tests"])


def task_run() -> int:
    """Run every deterministic script, then every mock demo, in order."""
    for name in DETERMINISTIC_SCRIPTS + MOCK_SCRIPTS:
        code = run_command([sys.executable, str(Path("scripts") / name)])
        if code != 0:
            print(f"{name} failed with exit code {code}.")
            return code
    return 0


def task_demo() -> int:
    code = task_run()
    if code != 0:
        return code
    print("\nGenerated outputs:")
    for path in sorted((REPO_ROOT / "outputs").iterdir()):
        if path.is_file():
            print(f"  outputs/{path.name}")
    return 0


def task_lint() -> int:
    return run_command([sys.executable, "-m", "ruff", "check", "."])


def task_format() -> int:
    return run_command([sys.executable, "-m", "ruff", "format", "."])


def task_typecheck() -> int:
    return run_command([sys.executable, "-m", "mypy"])


def task_scan() -> int:
    findings = scan_tree(REPO_ROOT)
    for finding in findings:
        print(finding)
    if findings:
        print(f"Scan found {len(findings)} problem(s).")
        return 1
    print("Scan clean: ASCII only, no forbidden wording, no secret-shaped text.")
    return 0


def task_check() -> int:
    """The full local gate: lint, typecheck, scan, and tests."""
    gates = [
        ("lint", task_lint),
        ("typecheck", task_typecheck),
        ("scan", task_scan),
        ("test", task_test),
    ]
    failed = []
    for name, gate in gates:
        print(f"\n== {name} ==")
        if gate() != 0:
            failed.append(name)
    if failed:
        print(f"\nFailed gates: {', '.join(failed)}")
        return 1
    print("\nAll gates passed.")
    return 0


TASKS = {
    "test": task_test,
    "run": task_run,
    "demo": task_demo,
    "lint": task_lint,
    "format": task_format,
    "typecheck": task_typecheck,
    "scan": task_scan,
    "check": task_check,
}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="tasks.py",
        description="Development commands for the Product Ops Sandbox.",
    )
    parser.add_argument("task", choices=sorted(TASKS), help="which task to run")
    args = parser.parse_args(argv)
    return TASKS[args.task]()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
