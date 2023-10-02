
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
| `details` | `object` | Optional | - |
| `external` | `bool` | Required | - |
| `memo` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `payment_type` | `object` | Optional | - |
| `created_at` | `str` | Required | **Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "id": 52.0,
  "subscription_id": 78.7,
  "amount_in_cents": 32.38,
  "remaining_amount_in_cents": 84.16,
  "details": {
    "key1": "val1",
    "key2": "val2"
  },
  "external": false,
  "memo": "memo4",
  "payment_type": {
    "key1": "val1",
    "key2": "val2"
  },
  "created_at": "created_at8"
}
```

