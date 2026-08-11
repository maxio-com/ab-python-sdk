
# Product Price Point Error Response Exception

## Structure

`ProductPricePointErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`ProductPricePointErrors`](../../doc/models/product-price-point-errors.md) | Required | - |

## Example

```python
try:
    # make the API call
except ProductPricePointErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

