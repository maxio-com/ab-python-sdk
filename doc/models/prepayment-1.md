
# Prepayment 1

## Structure

`Prepayment1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `float` | Required | - |
| `subscription_id` | `float` | Required | - |
| `amount_in_cents` | `float` | Required | - |
| `remaining_amount_in_cents` | `float` | Required | - |
| `refunded_amount_in_cents` | `float` | Optional | - |
| `details` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `external` | `bool` | Required | - |
| `memo` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `payment_type` | [`PrepaymentMethod`](../../doc/models/prepayment-method.md) | Optional | The payment type of the prepayment. |
| `created_at` | `str` | Required | **Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "id": 52.0,
  "subscription_id": 78.7,
  "amount_in_cents": 32.38,
  "remaining_amount_in_cents": 84.16,
  "refunded_amount_in_cents": 109.26,
  "details": "details0",
  "external": false,
  "memo": "memo4",
  "payment_type": "ach",
  "created_at": "created_at8"
}
```

