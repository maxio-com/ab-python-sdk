
# Error List Response Exception

Error which contains list of messages.

## Structure

`ErrorListResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | `List[str]` | Required | - |

## Example

```python
try:
    # make the API call
except ErrorListResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

