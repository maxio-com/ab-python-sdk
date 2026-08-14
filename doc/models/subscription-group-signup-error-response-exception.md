
# Subscription Group Signup Error Response Exception

## Structure

`SubscriptionGroupSignupErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`SubscriptionGroupSignupError`](../../doc/models/subscription-group-signup-error.md) | Required | - |

## Example

```python
try:
    # make the API call
except SubscriptionGroupSignupErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

