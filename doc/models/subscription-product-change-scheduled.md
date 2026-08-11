
# Subscription Product Change Scheduled

## Structure

`SubscriptionProductChangeScheduled`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `previous_product_id` | `int` | Required | - |
| `new_product_id` | `int` | Required | - |
| `previous_product_price_point_id` | `int` | Optional | - |
| `new_product_price_point_id` | `int` | Optional | - |
| `effective_at` | `datetime` | Optional | When the scheduled product change takes effect (the subscription's next renewal). |

## Example

```python
import dateutil.parser

from advancedbilling.models.subscription_product_change_scheduled import SubscriptionProductChangeScheduled

subscription_product_change_scheduled = SubscriptionProductChangeScheduled(
    previous_product_id=50,
    new_product_id=64,
    previous_product_price_point_id=174,
    new_product_price_point_id=168,
    effective_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

