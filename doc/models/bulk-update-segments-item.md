
# Bulk Update Segments Item

## Structure

`BulkUpdateSegmentsItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | The ID of the segment you want to update. |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Required | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `prices` | [`List[CreateOrUpdateSegmentPrice]`](../../doc/models/create-or-update-segment-price.md) | Required | - |

## Example

```python
from advancedbilling.models.bulk_update_segments_item import BulkUpdateSegmentsItem
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice
from advancedbilling.models.pricing_scheme import PricingScheme

bulk_update_segments_item = BulkUpdateSegmentsItem(
    id=156,
    pricing_scheme=PricingScheme.PER_UNIT,
    prices=[
        CreateOrUpdateSegmentPrice(
            unit_price='String3',
            starting_quantity=64,
            ending_quantity=38
        )
    ]
)
```

