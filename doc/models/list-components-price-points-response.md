
# List Components Price Points Response

## Structure

`ListComponentsPricePointsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_points` | [`List[ComponentPricePoint]`](../../doc/models/component-price-point.md) | Required | - |

## Example

```python
from advancedbilling.models.component_price_point import ComponentPricePoint
from advancedbilling.models.list_components_price_points_response import ListComponentsPricePointsResponse
from advancedbilling.models.price_point_type import PricePointType
from advancedbilling.models.pricing_scheme import PricingScheme

list_components_price_points_response = ListComponentsPricePointsResponse(
    price_points=[
        ComponentPricePoint(
            id=40,
            mtype=PricePointType.DEFAULT,
            default=False,
            name='name2',
            pricing_scheme=PricingScheme.PER_UNIT
        )
    ]
)
```

