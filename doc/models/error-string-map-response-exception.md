
# Error String Map Response Exception

## Structure

`ErrorStringMapResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | `Dict[str, str]` | Optional | - |

## Example

```python
try:
    # make the API call
except ErrorStringMapResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

