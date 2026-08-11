
# Single String Error Response Exception

## Structure

`SingleStringErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | `str` | Optional | - |

## Example

```python
try:
    # make the API call
except SingleStringErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

