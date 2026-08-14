
# Subscription Group Item

## Structure

`SubscriptionGroupItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `reference` | `str` | Optional | - |
| `product_id` | `int` | Optional | - |
| `product_handle` | `str` | Optional | - |
| `product_price_point_id` | `int` | Optional | - |
| `product_price_point_handle` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `coupon_code` | `str` | Optional | - |
| `total_revenue_in_cents` | `int` | Optional | - |
| `balance_in_cents` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.subscription_group_item import SubscriptionGroupItem

subscription_group_item = SubscriptionGroupItem(
    id=214,
    reference='reference2',
    product_id=156,
    product_handle='product_handle6',
    product_price_point_id=80
)
```

