
# Component Allocation Error Exception

## Structure

`ComponentAllocationErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List[ComponentAllocationErrorItem]`](../../doc/models/component-allocation-error-item.md) | Optional | - |

## Example

```python
try:
    # make the API call
except ComponentAllocationErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

