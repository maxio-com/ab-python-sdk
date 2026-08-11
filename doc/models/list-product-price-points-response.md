
# List Product Price Points Response

## Structure

`ListProductPricePointsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_points` | [`List[ProductPricePoint]`](../../doc/models/product-price-point.md) | Required | - |

## Example

```python
from advancedbilling.models.list_product_price_points_response import ListProductPricePointsResponse
from advancedbilling.models.product_price_point import ProductPricePoint

list_product_price_points_response = ListProductPricePointsResponse(
    price_points=[
        ProductPricePoint(
            id=40,
            name='name2',
            handle='handle8',
            price_in_cents=108,
            interval=92
        )
    ]
)
```

