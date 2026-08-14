
# Component Price Point Response

## Structure

`ComponentPricePointResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | [`ComponentPricePoint`](../../doc/models/component-price-point.md) | Required | - |

## Example

```python
from advancedbilling.models.component_price_point import ComponentPricePoint
from advancedbilling.models.component_price_point_response import ComponentPricePointResponse
from advancedbilling.models.price_point_type import PricePointType
from advancedbilling.models.pricing_scheme import PricingScheme

component_price_point_response = ComponentPricePointResponse(
    price_point=ComponentPricePoint(
        id=248,
        mtype=PricePointType.DEFAULT,
        default=False,
        name='name0',
        pricing_scheme=PricingScheme.PER_UNIT
    )
)
```

