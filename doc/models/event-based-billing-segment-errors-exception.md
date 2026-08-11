
# Event Based Billing Segment Errors Exception

## Structure

`EventBasedBillingSegmentErrorsException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | `Dict[str, Any]` | Optional | The key of the object would be a number (an index in the request array) where the error occurred. In the value object, the key represents the field and the value is an array with error messages. In most cases, this object would contain just one key. |

## Example

```python
try:
    # make the API call
except EventBasedBillingSegmentErrorsException as e:
    print(e)
except APIException as e:
    print(e)
```

