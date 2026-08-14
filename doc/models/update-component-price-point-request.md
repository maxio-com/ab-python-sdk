
# Update Component Price Point Request

## Structure

`UpdateComponentPricePointRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | [`UpdateComponentPricePoint`](../../doc/models/update-component-price-point.md) | Optional | - |

## Example

```python
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.update_component_price_point import UpdateComponentPricePoint
from advancedbilling.models.update_component_price_point_request import UpdateComponentPricePointRequest

update_component_price_point_request = UpdateComponentPricePointRequest(
    price_point=UpdateComponentPricePoint(
        name='name0',
        handle='handle6',
        pricing_scheme=PricingScheme.PER_UNIT,
        use_site_exchange_rate=False,
        tax_included=False
    )
)
```

