
# Segment Price Point Error Details

Price-point validation error details for segment writes.

## Structure

`SegmentPricePointErrorDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | `List[str]` | Required | - |

## Example

```python
from advancedbilling.models.segment_price_point_error_details import SegmentPricePointErrorDetails

segment_price_point_error_details = SegmentPricePointErrorDetails(
    price_point=[
        'price_point8',
        'price_point9',
        'price_point0'
    ]
)
```

