
# Bulk Update Segments

## Structure

`BulkUpdateSegments`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segments` | [`List[BulkUpdateSegmentsItem]`](../../doc/models/bulk-update-segments-item.md) | Optional | **Constraints**: *Maximum Items*: `1000` |

## Example

```python
from advancedbilling.models.bulk_update_segments import BulkUpdateSegments
from advancedbilling.models.bulk_update_segments_item import BulkUpdateSegmentsItem
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice
from advancedbilling.models.pricing_scheme import PricingScheme

bulk_update_segments = BulkUpdateSegments(
    segments=[
        BulkUpdateSegmentsItem(
            id=50,
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
        ),
        BulkUpdateSegmentsItem(
            id=50,
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
    ]
)
```

