
# Prepayment Prepayments Response

## Structure

`PrepaymentPrepaymentsResponse`

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
  "id": 182.48,
  "subscription_id": 209.18,
  "amount_in_cents": 93.14,
  "remaining_amount_in_cents": 214.64,
  "refunded_amount_in_cents": 239.74,
  "details": "details8",
  "external": false,
  "memo": "memo2",
  "payment_type": "credit_card_on_file",
  "created_at": "created_at6"
}
```

