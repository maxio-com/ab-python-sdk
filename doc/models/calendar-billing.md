
# Calendar Billing

(Optional). Cannot be used when also specifying next_billing_at.

## Structure

`CalendarBilling`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `snap_day` | int \| str \| None | Optional | This is a container for one-of cases. |
| `calendar_billing_first_charge` | [`FirstChargeType`](../../doc/models/first-charge-type.md) | Optional | - |

## Example

```python
from advancedbilling.models.calendar_billing import CalendarBilling
from advancedbilling.models.first_charge_type import FirstChargeType

calendar_billing = CalendarBilling(
    snap_day=170,
    calendar_billing_first_charge=FirstChargeType.PRORATED
)
```

