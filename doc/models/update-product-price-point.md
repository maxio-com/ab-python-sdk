
# Update Product Price Point

## Structure

`UpdateProductPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `handle` | `str` | Optional | - |
| `price_in_cents` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.update_product_price_point import UpdateProductPricePoint

update_product_price_point = UpdateProductPricePoint(
    handle='handle2',
    price_in_cents=190
)
```

