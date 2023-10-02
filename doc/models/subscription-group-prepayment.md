
# Subscription Group Prepayment

## Structure

`SubscriptionGroupPrepayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | - |
| `details` | `str` | Required | - |
| `memo` | `str` | Required | - |
| `method` | [`SubscriptionGroupPrepaymentMethodEnum`](../../doc/models/subscription-group-prepayment-method-enum.md) | Required | - |

## Example (as JSON)

```json
{
  "amount": 96,
  "details": "details2",
  "memo": "memo6",
  "method": "money_order"
}
```

