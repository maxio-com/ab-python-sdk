
# Prepayment

## Structure

`Prepayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `subscription_id` | `int` | Required | - |
| `amount_in_cents` | `long\|int` | Required | - |
| `remaining_amount_in_cents` | `long\|int` | Required | - |
| `refunded_amount_in_cents` | `long\|int` | Optional | - |
| `details` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `external` | `bool` | Required | - |
| `memo` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `payment_type` | [`PrepaymentMethod`](../../doc/models/prepayment-method.md) | Optional | The payment type of the prepayment. |
| `created_at` | `str` | Required | **Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "id": 50,
  "subscription_id": 160,
  "amount_in_cents": 120,
  "remaining_amount_in_cents": 194,
  "refunded_amount_in_cents": 144,
  "details": "details4",
  "external": false,
  "memo": "memo8",
  "payment_type": "cash",
  "created_at": "created_at8"
}
```

