# Contributing

Thanks for your interest in improving the Product Ops Sandbox. The repo is a learning
sandbox: contributions that make the workflow clearer, safer, or easier to adapt are
welcome, from typo fixes to new sample workflows.

## Ground Rules

- All data stays fictional, synthetic, anonymized, or approved. Never add real customer
  data, real company names, credentials, or personal information.
- Committed files are ASCII only. No smart quotes, em dashes, or emoji.
- Every reference must resolve. If a doc points to a file, that file must exist.
- Structured (JSON) outputs keep a readable Markdown companion.
- The zero-setup path is sacred: the scripts and the agent lane must keep working with a
  plain Python install, no extra packages and no API key.

## Development Setup

The runtime needs nothing beyond Python 3.10 or newer. The dev tools are optional and
only needed for contributing:

```bash
pip install -r requirements-dev.txt
pre-commit install
```

## Everyday Commands

`tasks.py` wraps every development command (standard library only):

| Command | What it does |
| --- | --- |
| `python tasks.py test` | Run the unit tests |
| `python tasks.py run` | Run the deterministic scripts, then the mock demos |
| `python tasks.py lint` | Ruff lint |
| `python tasks.py format` | Ruff format |
| `python tasks.py typecheck` | Mypy static type check |
| `python tasks.py scan` | Hygiene scan: ASCII only, wording, secret patterns |
| `python tasks.py check` | The full local gate: lint + typecheck + scan + test |

Run `python tasks.py check` before opening a pull request. CI runs the same gates plus a
determinism job: rerunning every script must reproduce the committed outputs byte for
byte, so if you change a script or a sample input, run `python tasks.py run` and commit
the regenerated outputs together with your change.

## Making A Change

1. Fork or branch from `main`.
2. Change one thing at a time. The repo's own adaptation rule applies to development too:
   change one input, run, review the output, then change the next thing (see
   `docs/06-adapt-this-sandbox.md`).
3. Add or update tests for behavior changes. The tests are standard library `unittest`.
4. Run `python tasks.py check`.
5. Open a pull request against `main`. The PR template asks for a summary, what changed,
   and how you validated it. CI must pass before merge.

## Reporting Problems

Use the issue templates for bugs and feature ideas. For anything security related, follow
`SECURITY.md` instead of opening a public issue.
