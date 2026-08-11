
# Update Segment Request

## Structure

`UpdateSegmentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segment` | [`UpdateSegment`](../../doc/models/update-segment.md) | Required | - |

## Example

```python
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.update_segment import UpdateSegment
from advancedbilling.models.update_segment_request import UpdateSegmentRequest

update_segment_request = UpdateSegmentRequest(
    segment=UpdateSegment(
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

