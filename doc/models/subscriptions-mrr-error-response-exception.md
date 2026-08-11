
# Subscriptions Mrr Error Response Exception

## Structure

`SubscriptionsMrrErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`AttributeError`](../../doc/models/attribute-error.md) | Required | - |

## Example

```python
try:
    # make the API call
except SubscriptionsMrrErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

