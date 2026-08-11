
# Base Refund Error

## Structure

`BaseRefundError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `base` | `List[Any]` | Optional | - |

## Example

```python
import jsonpickle

from advancedbilling.models.base_refund_error import BaseRefundError

base_refund_error = BaseRefundError(
    base=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

