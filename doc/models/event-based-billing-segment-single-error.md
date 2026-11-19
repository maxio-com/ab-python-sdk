
# Event Based Billing Segment Single Error

The key of the object would be a number (an index in the request array) where the error occurred. In the value object, the key represents the field and the value is an array with error messages. In most cases, this object would contain just one key.

## Structure

`EventBasedBillingSegmentSingleError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | `List[str]` | Required | - |

## Example

```python
from advancedbilling.models.event_based_billing_segment_single_error import EventBasedBillingSegmentSingleError

event_based_billing_segment_single_error = EventBasedBillingSegmentSingleError(
    price_point=[
        'price_point8',
        'price_point9'
    ]
)
```

