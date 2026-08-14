
# Bulk Create Product Price Points Response

## Structure

`BulkCreateProductPricePointsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_points` | [`List[ProductPricePoint]`](../../doc/models/product-price-point.md) | Optional | - |

## Example

```python
from advancedbilling.models.bulk_create_product_price_points_response import BulkCreateProductPricePointsResponse
from advancedbilling.models.product_price_point import ProductPricePoint

bulk_create_product_price_points_response = BulkCreateProductPricePointsResponse(
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

