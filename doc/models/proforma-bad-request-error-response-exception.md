
# Proforma Bad Request Error Response Exception

## Structure

`ProformaBadRequestErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`ProformaError`](../../doc/models/proforma-error.md) | Optional | - |

## Example

```python
try:
    # make the API call
except ProformaBadRequestErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

