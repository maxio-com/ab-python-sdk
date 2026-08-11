
# List Subscription Components Response

## Structure

`ListSubscriptionComponentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscriptions_components` | [`List[SubscriptionComponent]`](../../doc/models/subscription-component.md) | Required | - |

## Example

```python
from advancedbilling.models.component_kind import ComponentKind
from advancedbilling.models.list_subscription_components_response import ListSubscriptionComponentsResponse
from advancedbilling.models.subscription_component import SubscriptionComponent

list_subscription_components_response = ListSubscriptionComponentsResponse(
    subscriptions_components=[
        SubscriptionComponent(
            id=138,
            name='name2',
            kind=ComponentKind.METERED_COMPONENT,
            unit_name='unit_name4',
            enabled=False
        )
    ]
)
```

