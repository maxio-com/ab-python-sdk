
# Feature 3

## Structure

`Feature3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Optional | - |
| `periodicity_interval` | `int` | Optional | - |
| `periodicity_unit` | [`EntitlementPeriodicityUnit`](../../doc/models/entitlement-periodicity-unit.md) | Optional | - |
| `propagate_to_subscriptions` | `bool` | Optional | When `true`, existing subscriptions on the item's price point are updated with the new `value`/periodicity by a background job shortly after. Has no effect on a product/component-level item. When `false` (default) and the item's price point already has subscribers, the update is made on a clone of the price point instead, and existing subscribers are unaffected.<br><br>**Default**: `False` |

## Example

```python
from advancedbilling.models.entitlement_periodicity_unit import EntitlementPeriodicityUnit
from advancedbilling.models.feature_3 import Feature3

feature_3 = Feature3(
    value='value2',
    periodicity_interval=160,
    periodicity_unit=EntitlementPeriodicityUnit.MONTH,
    propagate_to_subscriptions=False
)
```

