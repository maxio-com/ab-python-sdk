
# Create Invoice Coupon

## Structure

`CreateInvoiceCoupon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | - |
| `percentage` | str \| float \| None | Optional | This is a container for one-of cases. |
| `amount` | str \| float \| None | Optional | This is a container for one-of cases. |
| `description` | `str` | Optional | **Constraints**: *Maximum Length*: `255` |
| `product_family_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `compounding_strategy` | [`CompoundingStrategy`](../../doc/models/compounding-strategy.md) | Optional | Applicable only to stackable coupons. For `compound`, Percentage-based discounts will be calculated against the remaining price, after prior discounts have been calculated. For `full-price`, Percentage-based discounts will always be calculated against the original item price, before other discounts are applied. |

## Example (as JSON)

```json
{
  "percentage": 50.0,
  "code": "code4",
  "amount": "String9",
  "description": "description4",
  "product_family_id": "String3"
}
```

