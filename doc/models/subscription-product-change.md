
# Subscription Product Change

## Structure

`SubscriptionProductChange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `previous_product_id` | `int` | Required | - |
| `new_product_id` | `int` | Required | - |

## Example

```python
from advancedbilling.models.subscription_product_change import SubscriptionProductChange

subscription_product_change = SubscriptionProductChange(
    previous_product_id=250,
    new_product_id=120
)
```

