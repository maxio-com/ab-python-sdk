
# Refund Prepayment Request

## Structure

`RefundPrepaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `refund` | [`RefundPrepayment`](../../doc/models/refund-prepayment.md) | Required | - |

## Example

```python
from advancedbilling.models.refund_prepayment import RefundPrepayment
from advancedbilling.models.refund_prepayment_request import RefundPrepaymentRequest

refund_prepayment_request = RefundPrepaymentRequest(
    refund=RefundPrepayment(
        amount_in_cents=132,
        amount='String1',
        memo='memo2',
        external=False
    )
)
```

