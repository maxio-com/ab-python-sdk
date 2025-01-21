
# Refund Prepayment

## Structure

`RefundPrepayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_in_cents` | `int` | Required | `amount` is not required if you pass `amount_in_cents`. |
| `amount` | str \| float | Required | This is a container for one-of cases. |
| `memo` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `external` | `bool` | Optional | Specify the type of refund you wish to initiate. When the prepayment is external, the `external` flag is optional. But if the prepayment was made through a payment profile, the `external` flag is required. |

## Example (as JSON)

```json
{
  "amount_in_cents": 110,
  "amount": "String3",
  "memo": "memo4",
  "external": false
}
```

