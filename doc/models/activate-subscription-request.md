
# Activate Subscription Request

## Structure

`ActivateSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `revert_on_failure` | `bool` | Optional | You may choose how to handle the activation failure. `true` means do not change the subscription’s state and billing period. `false` means to continue through with the activation and enter an end-of-life state. If this parameter is omitted or `null` is passed it will default to the value set in the site settings (default: `true`). |

## Example

```python
from advancedbilling.models.activate_subscription_request import ActivateSubscriptionRequest

activate_subscription_request = ActivateSubscriptionRequest(
    revert_on_failure=False
)
```

