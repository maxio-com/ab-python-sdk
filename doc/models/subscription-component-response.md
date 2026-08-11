
# Subscription Component Response

## Structure

`SubscriptionComponentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component` | [`SubscriptionComponent`](../../doc/models/subscription-component.md) | Optional | - |

## Example

```python
from advancedbilling.models.component_kind import ComponentKind
from advancedbilling.models.subscription_component import SubscriptionComponent
from advancedbilling.models.subscription_component_response import SubscriptionComponentResponse

subscription_component_response = SubscriptionComponentResponse(
    component=SubscriptionComponent(
        id=80,
        name='name8',
        kind=ComponentKind.QUANTITY_BASED_COMPONENT,
        unit_name='unit_name0',
        enabled=False
    )
)
```

