
# Subscription Group Update Error Response Exception

## Structure

`SubscriptionGroupUpdateErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`SubscriptionGroupUpdateError`](../../doc/models/subscription-group-update-error.md) | Optional | - |

## Example

```python
try:
    # make the API call
except SubscriptionGroupUpdateErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

