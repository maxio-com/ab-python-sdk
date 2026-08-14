
# Bulk Create Segments

## Structure

`BulkCreateSegments`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segments` | [`List[CreateSegment]`](../../doc/models/create-segment.md) | Optional | **Constraints**: *Maximum Items*: `2000` |

## Example

```python
from advancedbilling.models.bulk_create_segments import BulkCreateSegments
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice
from advancedbilling.models.create_segment import CreateSegment
from advancedbilling.models.pricing_scheme import PricingScheme

bulk_create_segments = BulkCreateSegments(
    segments=[
        CreateSegment(
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
        ),
        CreateSegment(
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
        ),
        CreateSegment(
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
    ]
)
```

