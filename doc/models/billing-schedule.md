
# Billing Schedule

Billing schedule settings for component allocations or usages on multi-frequency subscriptions. Use this to start a component's billing period on a custom date instead of aligning with the product charge schedule.

## Structure

`BillingSchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `initial_billing_at` | `date` | Optional | Custom start date (ISO 8601 date, YYYY-MM-DD) for the component's first billing period. If omitted or null, billing aligns with the product schedule. If provided, date must be on or after the minimum allowed date for the subscription or component. |

## Example

```python
import dateutil.parser

from advancedbilling.models.billing_schedule import BillingSchedule

billing_schedule = BillingSchedule(
    initial_billing_at=dateutil.parser.parse('2026-01-01').date()
)
```

