
# Segment Response

## Structure

`SegmentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segment` | [`Segment`](../../doc/models/segment.md) | Optional | - |

## Example

```python
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.segment import Segment
from advancedbilling.models.segment_response import SegmentResponse

segment_response = SegmentResponse(
    segment=Segment(
        id=118,
        component_id=228,
        price_point_id=4,
        event_based_billing_metric_id=56,
        pricing_scheme=PricingScheme.STAIRSTEP
    )
)
```

