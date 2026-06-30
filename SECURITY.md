# Security And Data Handling

This repo is designed for public learning with fictional data. It is also structured so teams can
adapt it privately with approved data, but public sharing and private analysis have different rules.

## Core Rule

```text
Public repo = fictional, synthetic, anonymized, or approved examples.
Private company copy = real data only with permission, access controls, and review.
```

The risk is not that real customer data can never be analyzed. The risk is committing, publishing,
or sending sensitive data somewhere it should not go.

## Do Not Commit Or Publish

Do not commit or publish:

- raw customer data
- personal information
- private company notes
- confidential interview transcripts
- commercial or contractual details
- API keys
- access tokens
- passwords
- `.env` files
- model credentials
- confidential business information

## Safe Data Types

For public examples, use one of these:

| Data Type | Safe To Commit Publicly? | Notes |
| --- | --- | --- |
| Fictional data | Yes | Best for public examples |
| Synthetic data | Yes | Useful for demos and tests |
| Fully anonymized data | Maybe | Use only when approved and reviewed |
| Real customer data | No | Use only in a private, approved environment |

## If You Adapt This For Real Work

Use a private repo, private branch, or local copy. Keep sensitive files out of Git.

The `.gitignore` file includes local-only patterns such as:

```text
local-inputs/
private-data/
sensitive-data/
input-notes/local-*
input-notes/private-*
sample-data/local-*
sample-data/private-*
outputs/local-*
outputs/private-*
.env
.env.*
```

Recommended naming pattern:

```text
input-notes/private-support-notes.md
sample-data/private-product-events.csv
outputs/private-feedback-classification.json
```

These files are ignored by Git in this repo. Still, check `git status` before every commit.

## AI Usage

Use approved AI tools only. Before sending any note to an AI assistant, check:

- Is this tool approved for this data?
- Does the note contain personal information?
- Does it include confidential company, customer, pricing, legal, or contract details?
- Does the output create a new sensitive summary that should also stay private?

If the answer is unclear, do not send the data. Use fictional or anonymized examples instead.

AI output should be reviewed against the source notes before it influences product decisions.

## Git Hygiene

Before sharing or publishing changes:

```bash
git status
git diff --stat
```

If sensitive data was committed by mistake, deleting the file in a later commit may not be enough
because Git history can still contain it. Treat that as an incident and rotate any exposed
credentials.

## Local Files

The `.private/` folder is ignored by Git. Use it only for local working notes, task lists, or private
planning context.
