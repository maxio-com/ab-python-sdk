
# Create Segment

## Structure

`CreateSegment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segment_property_1_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `segment_property_2_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `segment_property_3_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `segment_property_4_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Required | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `prices` | [`List[CreateOrUpdateSegmentPrice]`](../../doc/models/create-or-update-segment-price.md) | Optional | - |

## Example

```python
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice
from advancedbilling.models.create_segment import CreateSegment
from advancedbilling.models.pricing_scheme import PricingScheme

create_segment = CreateSegment(
    pricing_scheme=PricingScheme.STAIRSTEP,
    segment_property_1_value='String3',
    segment_property_2_value='String5',
    segment_property_3_value='String3',
    segment_property_4_value='String7',
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
        ),
        CreateOrUpdateSegmentPrice(
            unit_price='String3',
            starting_quantity=64,
            ending_quantity=38
        )
    ]
)
```

