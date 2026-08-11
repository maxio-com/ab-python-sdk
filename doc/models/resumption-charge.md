
# Resumption Charge

(For calendar billing subscriptions only) The way that the resumed subscription's charge should be handled

## Enumeration

`ResumptionCharge`

## Fields

| Name |
|  --- |
| `PRORATED` |
| `IMMEDIATE` |
| `DELAYED` |

## Example

```python
from advancedbilling.models.resumption_charge import ResumptionCharge

resumption_charge = ResumptionCharge.PRORATED
```

