
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
| `amount_in_cents` | `int` | Optional | - |
| `product_family_id` | `int` | Optional | - |
| `product_family_name` | `str` | Optional | - |
| `start_date` | `datetime` | Optional | - |
| `end_date` | `datetime` | Optional | - |
| `percentage` | `str` | Optional | - |
| `recurring` | `bool` | Optional | - |
| `recurring_scheme` | [`RecurringScheme`](../../doc/models/recurring-scheme.md) | Optional | - |
| `duration_period_count` | `int` | Optional | - |
| `duration_interval` | `int` | Optional | - |
| `duration_interval_unit` | `str` | Optional | - |
| `duration_interval_span` | `str` | Optional | - |
| `allow_negative_balance` | `bool` | Optional | - |
| `archived_at` | `datetime` | Optional | - |
| `conversion_limit` | `str` | Optional | - |
| `stackable` | `bool` | Optional | - |
| `compounding_strategy` | [Compounding Strategy](../../doc/models/compounding-strategy.md) \| None | Optional | This is a container for any-of cases. |
| `use_site_exchange_rate` | `bool` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `discount_type` | [`DiscountType`](../../doc/models/discount-type.md) | Optional | - |
| `exclude_mid_period_allocations` | `bool` | Optional | - |
| `apply_on_cancel_at_end_of_period` | `bool` | Optional | - |
| `apply_on_subscription_expiration` | `bool` | Optional | - |
| `coupon_restrictions` | [`List[CouponRestriction]`](../../doc/models/coupon-restriction.md) | Optional | - |

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

