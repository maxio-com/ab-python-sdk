
# Entitlement Periodicity Unit

The recurring window over which a `usage_limit` feature's allowance resets.

## Enumeration

`EntitlementPeriodicityUnit`

## Fields

| Name |
|  --- |
| `HOUR` |
| `DAY` |
| `WEEK` |
| `MONTH` |
| `YEAR` |

## Example

```python
from advancedbilling.models.entitlement_periodicity_unit import EntitlementPeriodicityUnit

entitlement_periodicity_unit = EntitlementPeriodicityUnit.MONTH
```

