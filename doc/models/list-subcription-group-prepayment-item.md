
# List Subcription Group Prepayment Item

## Structure

`ListSubcriptionGroupPrepaymentItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `subscription_group_uid` | `str` | Optional | - |
| `amount_in_cents` | `long\|int` | Optional | - |
| `remaining_amount_in_cents` | `long\|int` | Optional | - |
| `details` | `str` | Optional | - |
| `external` | `bool` | Optional | - |
| `memo` | `str` | Optional | - |
| `payment_type` | [`PrepaymentMethod`](../../doc/models/prepayment-method.md) | Optional | - |
| `created_at` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "id": 254,
  "subscription_group_uid": "subscription_group_uid6",
  "amount_in_cents": 172,
  "remaining_amount_in_cents": 142,
  "details": "details2"
}
```

