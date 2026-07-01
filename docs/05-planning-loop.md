# Planning Loop

This doc explains how insights, opportunities, roadmap candidates, OKRs, release communication, and measurement connect in this sandbox.

## The Core Flow

```text
Signals explain what is happening.
Insights explain why it may matter.
Opportunities define what could improve.
Prioritization compares what deserves attention.
Roadmap candidates show what the team may build.
OKR alignment connects work to measurable outcomes.
Release planning prepares teams for launch.
Measurement checks whether the change worked.
```

The flow is a loop, not a straight line. Measurement after a release creates new evidence for the next planning cycle.

## What Each Layer Means

| Layer | Meaning | Repo Example |
| --- | --- | --- |
| Signal | A raw or structured data point | Support notes, event counts, research notes |
| Insight | A reason the signal may matter | Users lose confidence when the gym visit fails |
| Opportunity | A problem worth exploring | Improve check in recovery |
| Prioritization | A way to compare candidates | Roadmap score based on reach, impact, confidence, effort, and strategic fit |
| Roadmap candidate | Work the team may consider | Improve check in fallback |
| OKR alignment | Outcome the work may support | Reduce failed check ins |
| Release planning | Launch message, owner, audience, risk | Prepare support and customer success before launch |
| Measurement | How the team checks impact | Review failed check ins two weeks after release |

## How OKRs Fit

OKRs are not created only from customer feedback. They usually come from strategy, company priorities, and product outcomes.

In this repo, OKRs are used to answer:

```text
If we do this work, which measurable outcome might it support?
```

That is why the repo uses the term `OKR alignment`. The output is a draft that connects evidence and roadmap candidates to objectives and key results. A human product leader still approves the OKR decision.

## How Release Communication Fits

Release communication is not only a launch note. It answers:

- who needs to know
- what changed
- why it matters
- what internal teams need before launch
- what risk should be watched
- which metric should move

In this repo, release planning lives in `sample-data/releases.csv` and `outputs/ai_release_measurement_plan.md`.

## How Measurement Fits

Measurement closes the loop.

Before launch, the team should know:

- the linked metric
- the baseline
- the expected signal
- the review window
- the owner
- what decision will be made after results are reviewed

If the metric does not move, the team should ask whether the issue is product flow, partner operations, communication, eligibility, or data quality.

## What Product Ops Owns

Product Ops does not replace product judgment. It makes the operating system clearer.

In this sandbox, Product Ops helps:

- collect signals from multiple teams
- standardize how evidence is summarized
- connect opportunities to metrics
- make prioritization assumptions visible
- show whether roadmap candidates support current OKRs
- prepare release communication and measurement
- keep a review loop after launch

The final decision still belongs to accountable humans.
