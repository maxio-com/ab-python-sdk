
# Product Price Point Response

## Structure

`ProductPricePointResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | [`ProductPricePoint`](../../doc/models/product-price-point.md) | Required | - |

## Example

```python
from advancedbilling.models.product_price_point import ProductPricePoint
from advancedbilling.models.product_price_point_response import ProductPricePointResponse

product_price_point_response = ProductPricePointResponse(
    price_point=ProductPricePoint(
        id=248,
        name='name0',
        handle='handle6',
        price_in_cents=196,
        interval=44
    )
)
```

