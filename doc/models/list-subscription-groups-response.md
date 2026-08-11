
# List Subscription Groups Response

## Structure

`ListSubscriptionGroupsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_groups` | [`List[ListSubscriptionGroupsItem]`](../../doc/models/list-subscription-groups-item.md) | Optional | - |
| `meta` | [`ListSubscriptionGroupsMeta`](../../doc/models/list-subscription-groups-meta.md) | Optional | - |

## Example

```python
from advancedbilling.models.list_subscription_groups_item import ListSubscriptionGroupsItem
from advancedbilling.models.list_subscription_groups_meta import ListSubscriptionGroupsMeta
from advancedbilling.models.list_subscription_groups_response import ListSubscriptionGroupsResponse

list_subscription_groups_response = ListSubscriptionGroupsResponse(
    subscription_groups=[
        ListSubscriptionGroupsItem(
            uid='uid2',
            scheme=166,
            customer_id=186,
            payment_profile_id=162,
            subscription_ids=[
                40
            ]
        ),
        ListSubscriptionGroupsItem(
            uid='uid2',
            scheme=166,
            customer_id=186,
            payment_profile_id=162,
            subscription_ids=[
                40
            ]
        )
    ],
    meta=ListSubscriptionGroupsMeta(
        current_page=126,
        total_count=150
    )
)
```

