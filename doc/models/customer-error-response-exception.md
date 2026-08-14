
# Customer Error Response Exception

## Structure

`CustomerErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [Customer Error](../../doc/models/customer-error.md) \| List[str] \| None | Optional | This is a container for one-of cases. |

## Example

```python
try:
    # make the API call
except CustomerErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

