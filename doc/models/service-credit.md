
# Service Credit

## Structure

`ServiceCredit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `amount_in_cents` | `int` | Optional | The amount in cents of the entry |
| `ending_balance_in_cents` | `int` | Optional | The new balance for the credit account |
| `entry_type` | [`ServiceCreditType`](../../doc/models/service-credit-type.md) | Optional | The type of entry |
| `memo` | `str` | Optional | The memo attached to the entry |

## Example (as JSON)

```json
{
  "id": 216,
  "amount_in_cents": 210,
  "ending_balance_in_cents": 86,
  "entry_type": "Credit",
  "memo": "memo2"
}
```

