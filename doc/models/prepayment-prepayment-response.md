
# Prepayment Prepayment Response

## Structure

`PrepaymentPrepaymentResponse`

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
  "id": 233.44,
  "subscription_id": 4.14,
  "amount_in_cents": 42.18,
  "remaining_amount_in_cents": 9.6,
  "refunded_amount_in_cents": 34.7,
  "details": "details4",
  "external": false,
  "memo": "memo8",
  "payment_type": "paypal_account",
  "created_at": "created_at2"
}
```

