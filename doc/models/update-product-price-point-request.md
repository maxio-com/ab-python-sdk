
# Update Product Price Point Request

## Structure

`UpdateProductPricePointRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | [`UpdateProductPricePoint`](../../doc/models/update-product-price-point.md) | Required | - |

## Example

```python
from advancedbilling.models.update_product_price_point import UpdateProductPricePoint
from advancedbilling.models.update_product_price_point_request import UpdateProductPricePointRequest

update_product_price_point_request = UpdateProductPricePointRequest(
    price_point=UpdateProductPricePoint(
        handle='handle6',
        price_in_cents=196
    )
)
```

