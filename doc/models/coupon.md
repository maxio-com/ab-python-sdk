
# Coupon

## Structure

`Coupon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `code` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `amount` | `float` | Optional | - |
| `amount_in_cents` | `long\|int` | Optional | - |
| `product_family_id` | `int` | Optional | - |
| `product_family_name` | `str` | Optional | - |
| `start_date` | `datetime` | Optional | - |
| `end_date` | `datetime` | Optional | After the given time, this coupon code will be invalid for new signups. Recurring discounts started before this date will continue to recur even after this date. |
| `percentage` | `str` | Optional | - |
| `recurring` | `bool` | Optional | - |
| `recurring_scheme` | [`RecurringScheme`](../../doc/models/recurring-scheme.md) | Optional | - |
| `duration_period_count` | `int` | Optional | - |
| `duration_interval` | `int` | Optional | - |
| `duration_interval_unit` | `str` | Optional | - |
| `duration_interval_span` | `str` | Optional | - |
| `allow_negative_balance` | `bool` | Optional | If set to true, discount is not limited (credits will carry forward to next billing). |
| `archived_at` | `datetime` | Optional | - |
| `conversion_limit` | `str` | Optional | - |
| `stackable` | `bool` | Optional | A stackable coupon can be combined with other coupons on a Subscription. |
| `compounding_strategy` | [`CompoundingStrategy`](../../doc/models/compounding-strategy.md) | Optional | Applicable only to stackable coupons. For `compound`, Percentage-based discounts will be calculated against the remaining price, after prior discounts have been calculated. For `full-price`, Percentage-based discounts will always be calculated against the original item price, before other discounts are applied. |
| `use_site_exchange_rate` | `bool` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `discount_type` | [`DiscountType`](../../doc/models/discount-type.md) | Optional | - |
| `exclude_mid_period_allocations` | `bool` | Optional | - |
| `apply_on_cancel_at_end_of_period` | `bool` | Optional | - |
| `apply_on_subscription_expiration` | `bool` | Optional | - |
| `coupon_restrictions` | [`List[CouponRestriction]`](../../doc/models/coupon-restriction.md) | Optional | - |
| `currency_prices` | [`List[CouponCurrency]`](../../doc/models/coupon-currency.md) | Optional | Returned in read, find, and list endpoints if the query parameter is provided. |

## Example (as JSON)

```json
{
  "id": 22,
  "name": "name2",
  "code": "code0",
  "description": "description2",
  "amount": 62.64
}
```

