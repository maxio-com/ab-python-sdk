
# Subscription State Change

## Structure

`SubscriptionStateChange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `previous_subscription_state` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `new_subscription_state` | `str` | Required | **Constraints**: *Minimum Length*: `1` |

## Example

```python
from advancedbilling.models.subscription_state_change import SubscriptionStateChange

subscription_state_change = SubscriptionStateChange(
    previous_subscription_state='previous_subscription_state4',
    new_subscription_state='new_subscription_state8'
)
```

