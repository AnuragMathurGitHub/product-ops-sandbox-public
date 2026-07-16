# Changelog

All notable changes to the Product Ops Sandbox are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-07-16

The first tagged release of the sandbox.

### Added

- The Product Ops loop for the fictional FitPass Demo product: product context, success
  metrics, sample data, and docs that walk from signals to insights, opportunities,
  prioritization, roadmap candidates, OKR alignment, release measurement, and learning.
- Four ways to run it: read only, the agent lane (your own assistant, no API key), the
  mock demo scripts, and an optional provider-neutral API pipeline (`scripts/ai_real.py`).
- Seven AI workflows, each with a prompt, a JSON schema where structured, sample outputs,
  and a readable Markdown companion for every JSON draft.
- A schema gate (`scripts/harness.py`): every real AI reply is parsed, validated against
  its schema, retried a fixed number of times, and failed closed, with a command line
  check any lane can run.
- Deterministic Python scripts for metrics, feedback themes, roadmap scoring, OKR and
  release snapshots, with tests that prove the committed outputs are reproduced byte for
  byte.
- Agent entry points: `AGENTS.md`, Claude Code commands and skills, Cursor rules, GitHub
  Copilot prompts, and portable skill packages in `agent-skills/`.
- A guided onboarding flow (`docs/07-customer-onboarding-user-flow.md`) with persona
  paths and Mermaid diagrams across the entry docs.
- Engineering tooling: `pyproject.toml`, ruff lint and format, mypy type checking,
  pre-commit hooks, a stdlib task runner (`tasks.py`) with a repo hygiene scan, a CI
  matrix across Python 3.10 to 3.13 with lint, type, scan, and determinism jobs, and
  community health files.
