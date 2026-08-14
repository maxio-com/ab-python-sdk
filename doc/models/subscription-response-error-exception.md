
# Subscription Response Error Exception

## Structure

`SubscriptionResponseErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription` | [`Subscription`](../../doc/models/subscription.md) | Optional | - |

## Example

```python
try:
    # make the API call
except SubscriptionResponseErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

