
# Subscription Group Prepayment Response

## Structure

`SubscriptionGroupPrepaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `amount_in_cents` | `int` | Optional | The amount in cents of the entry. |
| `ending_balance_in_cents` | `int` | Optional | The ending balance in cents of the account. |
| `entry_type` | [`ServiceCreditType`](../../doc/models/service-credit-type.md) | Optional | The type of entry |
| `memo` | `str` | Optional | A memo attached to the entry. |

## Example (as JSON)

```json
{
  "id": 110,
  "amount_in_cents": 196,
  "ending_balance_in_cents": 236,
  "entry_type": "Credit",
  "memo": "memo2"
}
```

