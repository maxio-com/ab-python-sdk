
# Event Based Billing Segment Error

## Structure

`EventBasedBillingSegmentError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segments` | `Dict[str, Any]` | Required | The key of the object would be a number (an index in the request array) where the error occurred. In the value object, the key represents the field and the value is an array with error messages. In most cases, this object would contain just one key. |

## Example

```python
import jsonpickle

from advancedbilling.models.event_based_billing_segment_error import EventBasedBillingSegmentError

event_based_billing_segment_error = EventBasedBillingSegmentError(
    segments={
        'key0': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        'key1': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

