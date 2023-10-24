
# List Subcription Group Prepayment Item

## Structure

`ListSubcriptionGroupPrepaymentItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `float` | Optional | - |
| `subscription_group_uid` | `str` | Optional | - |
| `amount_in_cents` | `float` | Optional | - |
| `remaining_amount_in_cents` | `float` | Optional | - |
| `details` | `str` | Optional | - |
| `external` | `bool` | Optional | - |
| `memo` | `str` | Optional | - |
| `payment_type` | [`PrepaymentMethod`](../../doc/models/prepayment-method.md) | Optional | :- When the `method` specified is `"credit_card_on_file"`, the prepayment amount will be collected using the default credit card payment profile and applied to the prepayment account balance. This is especially useful for manual replenishment of prepaid subscriptions. |
| `created_at` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "id": 138.22,
  "subscription_group_uid": "subscription_group_uid6",
  "amount_in_cents": 137.4,
  "remaining_amount_in_cents": 170.38,
  "details": "details2"
}
```

