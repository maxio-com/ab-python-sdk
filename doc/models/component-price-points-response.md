
# Component Price Points Response

## Structure

`ComponentPricePointsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_points` | [`List[ComponentPricePoint]`](../../doc/models/component-price-point.md) | Optional | - |
| `meta` | [`ListPublicKeysMeta`](../../doc/models/list-public-keys-meta.md) | Optional | - |

## Example

```python
from advancedbilling.models.component_price_point import ComponentPricePoint
from advancedbilling.models.component_price_points_response import ComponentPricePointsResponse
from advancedbilling.models.list_public_keys_meta import ListPublicKeysMeta
from advancedbilling.models.price_point_type import PricePointType
from advancedbilling.models.pricing_scheme import PricingScheme

component_price_points_response = ComponentPricePointsResponse(
    price_points=[
        ComponentPricePoint(
            id=40,
            mtype=PricePointType.DEFAULT,
            default=False,
            name='name2',
            pricing_scheme=PricingScheme.PER_UNIT
        ),
        ComponentPricePoint(
            id=40,
            mtype=PricePointType.DEFAULT,
            default=False,
            name='name2',
            pricing_scheme=PricingScheme.PER_UNIT
        )
    ],
    meta=ListPublicKeysMeta(
        total_count=150,
        current_page=126,
        total_pages=138,
        per_page=152
    )
)
```

