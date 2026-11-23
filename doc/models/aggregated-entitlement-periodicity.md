
# Aggregated Entitlement Periodicity

## Structure

`AggregatedEntitlementPeriodicity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `interval` | `int` | Optional | - |
| `unit` | [`EntitlementPeriodicityUnit`](../../doc/models/entitlement-periodicity-unit.md) | Optional | The recurring window over which a `usage_limit` feature's allowance resets. |

## Example

```python
from advancedbilling.models.aggregated_entitlement_periodicity import AggregatedEntitlementPeriodicity
from advancedbilling.models.entitlement_periodicity_unit import EntitlementPeriodicityUnit

aggregated_entitlement_periodicity = AggregatedEntitlementPeriodicity(
    interval=186,
    unit=EntitlementPeriodicityUnit.MONTH
)
```

