
# Subscription Group Create Error Response Exception

## Structure

`SubscriptionGroupCreateErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [Subscription Group Members Array Error](../../doc/models/subscription-group-members-array-error.md) \| [Subscription Group Single Error](../../doc/models/subscription-group-single-error.md) \| str | Required | This is a container for one-of cases. |

## Example

```python
try:
    # make the API call
except SubscriptionGroupCreateErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

