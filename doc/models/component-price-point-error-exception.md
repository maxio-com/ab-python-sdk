
# Component Price Point Error Exception

## Structure

`ComponentPricePointErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List[ComponentPricePointErrorItem]`](../../doc/models/component-price-point-error-item.md) | Optional | - |

## Example

```python
try:
    # make the API call
except ComponentPricePointErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

