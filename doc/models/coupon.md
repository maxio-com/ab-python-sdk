
# Coupon

## Structure

`Coupon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `float` | Optional | - |
| `name` | `str` | Optional | - |
| `code` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `amount` | `float` | Optional | - |
| `amount_in_cents` | `int` | Optional | - |
| `product_family_id` | `int` | Optional | - |
| `product_family_name` | `str` | Optional | - |
| `start_date` | `str` | Optional | - |
| `end_date` | `str` | Optional | - |
| `percentage` | `float` | Optional | - |
| `recurring` | `bool` | Optional | - |
| `recurring_scheme` | [`RecurringSchemeEnum`](../../doc/models/recurring-scheme-enum.md) | Optional | - |
| `duration_period_count` | `int` | Optional | - |
| `duration_interval` | `int` | Optional | - |
| `duration_interval_unit` | `str` | Optional | - |
| `duration_interval_span` | `str` | Optional | - |
| `allow_negative_balance` | `bool` | Optional | - |
| `archived_at` | `str` | Optional | - |
| `conversion_limit` | `str` | Optional | - |
| `stackable` | `bool` | Optional | - |
| `compounding_strategy` | [Compounding Strategy](../../doc/models/compounding-strategy-enum.md) \| None | Optional | This is a container for any-of cases. |
| `use_site_exchange_rate` | `bool` | Optional | - |
| `created_at` | `str` | Optional | - |
| `updated_at` | `str` | Optional | - |
| `discount_type` | [`DiscountTypeEnum`](../../doc/models/discount-type-enum.md) | Optional | - |
| `exclude_mid_period_allocations` | `bool` | Optional | - |
| `apply_on_cancel_at_end_of_period` | `bool` | Optional | - |
| `coupon_restrictions` | [`List[CouponRestriction]`](../../doc/models/coupon-restriction.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": 179.42,
  "name": "name2",
  "code": "code0",
  "description": "description2",
  "amount": 62.64
}
```

