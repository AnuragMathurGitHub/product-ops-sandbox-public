# Product Ops Signal Triage Taxonomy

Use this taxonomy so feedback is classified consistently. It matches the allowed values in
`ai-workflows/prompts/classify_feedback.md`.

## Product Areas

- Activation
- Search
- Booking
- Check-in
- Employer reporting
- Partner data
- Notifications
- Habit
- Other

## Severity

| Severity | Use When |
| --- | --- |
| Critical | User is blocked at scale, or revenue/trust risk is immediate |
| High | User is blocked in an important journey, or buyer confidence is affected |
| Medium | User can continue but friction may reduce conversion, engagement, or satisfaction |
| Low | Minor confusion, polish, or low-impact improvement |

## Confidence

| Confidence | Use When |
| --- | --- |
| High | Multiple signals agree, or the source is clear and specific |
| Medium | The signal is plausible but needs more evidence |
| Low | The signal is ambiguous, one-off, or missing context |

## Common Linked Metrics

These are examples seen in the sample data. Use the metric closest to the signal, or `Unknown`.

- Membership Activation Rate
- First Successful Visit Rate
- Search Result Click Rate
- Class Booking Completion Rate
- Booking Cancellation Rate
- Check-in Failed Count
- Weekly Active Users
- Support Contact Rate
- Unknown
