
# Error Array Map Response Exception

## Structure

`ErrorArrayMapResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except ErrorArrayMapResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

