
# Event Based Billing List Segments Errors Exception

## Structure

`EventBasedBillingListSegmentsErrorsException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`Errors`](../../doc/models/errors.md) | Optional | Validation error details for listing segments. |

## Example

```python
try:
    # make the API call
except EventBasedBillingListSegmentsErrorsException as e:
    print(e)
except APIException as e:
    print(e)
```

