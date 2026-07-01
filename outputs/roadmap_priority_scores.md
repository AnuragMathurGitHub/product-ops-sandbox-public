# Roadmap Priority Scores

These scores rank roadmap candidates with a transparent, RICE inspired formula.

```text
score = (reach * impact * confidence * strategic_fit) / effort
```

## What Each Factor Means

| Factor | Meaning | Scale in the sample data |
| --- | --- | --- |
| reach | How many users or accounts the change affects in a period | 1 to 10 |
| impact | How much it moves the linked metric when it lands | 1 to 10 |
| confidence | How sure we are about the reach and impact estimates | 0 to 1 |
| strategic_fit | How well it supports strategy, employer value, and renewal | 1 to 10 |
| effort | Rough delivery cost; larger effort lowers the score | 1 to 10 |

Standard RICE is `(reach * impact * confidence) / effort`. This repo adds `strategic_fit`
so business importance stays visible in the math instead of hidden in a side conversation.
Learn more about RICE: https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/

## The Score Is A Decision Input, Not The Decision

The ranking starts the conversation; product judgment finishes it. If a lower ranked item
matters more to the business, that usually means an input assumption needs a second look.
For example, `Launch activation reminder kit` ranks third here, but activation is central to
employer value and renewal, so a team might raise its `strategic_fit` or revisit the impact
estimate and re-run. The goal is to make assumptions explicit, not to trust the number blindly.

| Rank | Item | Product Area | Status | Linked Metric | Score |
| ---: | --- | --- | --- | --- | ---: |
| 1 | Improve check in fallback | Check In | Discovery | Check In Failed Count | 129.6 |
| 2 | Clarify booking confirmation | Booking | Ready for shaping | Class Booking Completion Rate | 119.5 |
| 3 | Launch activation reminder kit | Activation | Ready for delivery | Membership Activation Rate | 117.6 |
| 4 | Explain cancellation policy before booking | Booking | Backlog | Booking Cancellation Rate | 60.0 |
| 5 | Improve location aware search ranking | Search | Discovery | Search Result Click Rate | 47.0 |

## Product Ops Readout

- High scoring items combine reach, expected impact, confidence, and reasonable effort.
- Lower scoring items may still matter when they reduce trust, renewal, or operational risk.
- The useful conversation is often about the assumptions behind the score.
