
# Calendar Billing

(Optional). Cannot be used when also specifying next_billing_at

## Structure

`CalendarBilling`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `snap_day` | int \| str \| None | Optional | This is a container for one-of cases. |
| `calendar_billing_first_charge` | [`FirstChargeTypeEnum`](../../doc/models/first-charge-type-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "snap_day": 210,
  "calendar_billing_first_charge": "prorated"
}
```

