
# Refund Prepayment Base Refund Error

## Structure

`RefundPrepaymentBaseRefundError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `refund` | [`BaseRefundError`](../../doc/models/base-refund-error.md) | Optional | - |

## Example

```python
import jsonpickle

from advancedbilling.models.base_refund_error import BaseRefundError
from advancedbilling.models.refund_prepayment_base_refund_error import RefundPrepaymentBaseRefundError

refund_prepayment_base_refund_error = RefundPrepaymentBaseRefundError(
    refund=BaseRefundError(
        base=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ]
    )
)
```

