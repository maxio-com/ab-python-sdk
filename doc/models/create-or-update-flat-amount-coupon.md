
# Create or Update Flat Amount Coupon

## Structure

`CreateOrUpdateFlatAmountCoupon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | the name of the coupon |
| `code` | `str` | Required | may contain uppercase alphanumeric characters and these special characters (which allow for email addresses to be used): “%”, “@”, “+”, “-”, “_”, and “.” |
| `description` | `str` | Optional | - |
| `amount_in_cents` | `long\|int` | Required | - |
| `allow_negative_balance` | `bool` | Optional | - |
| `recurring` | `bool` | Optional | - |
| `end_date` | `datetime` | Optional | - |
| `product_family_id` | `str` | Optional | - |
| `stackable` | `bool` | Optional | - |
| `compounding_strategy` | [`CompoundingStrategy`](../../doc/models/compounding-strategy.md) | Optional | - |
| `exclude_mid_period_allocations` | `bool` | Optional | - |
| `apply_on_cancel_at_end_of_period` | `bool` | Optional | - |
| `apply_on_subscription_expiration` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name0",
  "code": "code8",
  "description": "description0",
  "amount_in_cents": 120,
  "allow_negative_balance": false,
  "recurring": false,
  "end_date": "2016-03-13T12:52:32.123Z",
  "product_family_id": "product_family_id4"
}
```

