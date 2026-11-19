
# Event Based Billing List Segments Errors Exception

## Structure

`EventBasedBillingListSegmentsErrorsException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`Errors1`](../../doc/models/errors-1.md) | Optional | - |

## Example

```python
try:
    # make the API call
except EventBasedBillingListSegmentsErrorsException as e:
    print(e)
except APIException as e:
    print(e)
```

