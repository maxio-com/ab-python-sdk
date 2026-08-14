
# Update Segment

## Structure

`UpdateSegment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Required | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `prices` | [`List[CreateOrUpdateSegmentPrice]`](../../doc/models/create-or-update-segment-price.md) | Optional | - |

## Example

```python
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.update_segment import UpdateSegment

update_segment = UpdateSegment(
    pricing_scheme=PricingScheme.STAIRSTEP,
    prices=[
        CreateOrUpdateSegmentPrice(
            unit_price='String3',
            starting_quantity=64,
            ending_quantity=38
        ),
        CreateOrUpdateSegmentPrice(
            unit_price='String3',
            starting_quantity=64,
            ending_quantity=38
        )
    ]
)
```

