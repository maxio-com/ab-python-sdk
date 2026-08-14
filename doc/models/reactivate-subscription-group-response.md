
# Reactivate Subscription Group Response

## Structure

`ReactivateSubscriptionGroupResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `scheme` | `int` | Optional | - |
| `customer_id` | `int` | Optional | - |
| `payment_profile_id` | `int` | Optional | - |
| `subscription_ids` | `List[int]` | Optional | - |
| `primary_subscription_id` | `int` | Optional | - |
| `next_assessment_at` | `datetime` | Optional | - |
| `state` | `str` | Optional | - |
| `cancel_at_end_of_period` | `bool` | Optional | - |

## Example

```python
from advancedbilling.models.reactivate_subscription_group_response import ReactivateSubscriptionGroupResponse

reactivate_subscription_group_response = ReactivateSubscriptionGroupResponse(
    uid='uid8',
    scheme=220,
    customer_id=240,
    payment_profile_id=148,
    subscription_ids=[
        94,
        95,
        96
    ]
)
```

