
# Single Error Response Exception

## Structure

`SingleErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `str` | Required | - |

## Example

```python
try:
    # make the API call
except SingleErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

