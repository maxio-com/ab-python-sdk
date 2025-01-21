
# Coupon Payload

## Structure

`CouponPayload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Required when creating a new coupon. This name is not displayed to customers and is limited to 255 characters. |
| `code` | `str` | Optional | Required when creating a new coupon. The code is limited to 255 characters. May contain uppercase alphanumeric characters and these special characters (which allow for email addresses to be used): “%”, “@”, “+”, “-”, “_”, and “.” |
| `description` | `str` | Optional | Required when creating a new coupon. A description of the coupon that can be displayed to customers in transactions and on statements. The description is limited to 255 characters. |
| `percentage` | str \| float \| None | Optional | This is a container for one-of cases. |
| `amount_in_cents` | `int` | Optional | Required when creating a new flat amount coupon. Can't be used together with percentage. Flat USD discount |
| `allow_negative_balance` | `bool` | Optional | If set to true, discount is not limited (credits will carry forward to next billing). Can't be used together with restrictions. |
| `recurring` | `bool` | Optional | - |
| `end_date` | `date` | Optional | After the end of the given day, this coupon code will be invalid for new signups. Recurring discounts started before this date will continue to recur even after this date. |
| `product_family_id` | `str` | Optional | - |
| `stackable` | `bool` | Optional | A stackable coupon can be combined with other coupons on a Subscription. |
| `compounding_strategy` | [`CompoundingStrategy`](../../doc/models/compounding-strategy.md) | Optional | Applicable only to stackable coupons. For `compound`, Percentage-based discounts will be calculated against the remaining price, after prior discounts have been calculated. For `full-price`, Percentage-based discounts will always be calculated against the original item price, before other discounts are applied. |
| `exclude_mid_period_allocations` | `bool` | Optional | - |
| `apply_on_cancel_at_end_of_period` | `bool` | Optional | - |
| `apply_on_subscription_expiration` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name8",
  "code": "code6",
  "description": "description8",
  "percentage": "String7",
  "amount_in_cents": 110
}
```

