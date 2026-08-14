
# Create Segment Request

## Structure

`CreateSegmentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segment` | [`CreateSegment`](../../doc/models/create-segment.md) | Required | - |

## Example

```python
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice
from advancedbilling.models.create_segment import CreateSegment
from advancedbilling.models.create_segment_request import CreateSegmentRequest
from advancedbilling.models.pricing_scheme import PricingScheme

create_segment_request = CreateSegmentRequest(
    segment=CreateSegment(
        pricing_scheme=PricingScheme.STAIRSTEP,
        segment_property_1_value='String1',
        segment_property_2_value='String3',
        segment_property_3_value='String1',
        segment_property_4_value='String5',
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
)
```

