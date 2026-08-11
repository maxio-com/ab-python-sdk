
# Create Subscription Component

## Structure

`CreateSubscriptionComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | int \| str \| None | Optional | This is a container for one-of cases. |
| `enabled` | `bool` | Optional | Used for on/off components only. |
| `unit_balance` | int \| str \| None | Optional | This is a container for one-of cases. |
| `allocated_quantity` | int \| str \| None | Optional | This is a container for one-of cases. |
| `quantity` | `int` | Optional | Deprecated. Use `allocated_quantity` instead. |
| `price_point_id` | int \| str \| None | Optional | This is a container for one-of cases. |
| `custom_price` | [`ComponentCustomPrice`](../../doc/models/component-custom-price.md) | Optional | Create or update custom pricing unique to the subscription. Used in place of `price_point_id`. |

## Example

```python
from advancedbilling.models.create_subscription_component import CreateSubscriptionComponent

create_subscription_component = CreateSubscriptionComponent(
    component_id=66,
    enabled=False,
    unit_balance=124,
    allocated_quantity=160,
    quantity=246
)
```

