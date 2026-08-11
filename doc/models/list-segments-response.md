
# List Segments Response

## Structure

`ListSegmentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segments` | [`List[Segment]`](../../doc/models/segment.md) | Optional | - |

## Example

```python
from advancedbilling.models.list_segments_response import ListSegmentsResponse
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.segment import Segment

list_segments_response = ListSegmentsResponse(
    segments=[
        Segment(
            id=50,
            component_id=160,
            price_point_id=184,
            event_based_billing_metric_id=244,
            pricing_scheme=PricingScheme.STAIRSTEP
        )
    ]
)
```

