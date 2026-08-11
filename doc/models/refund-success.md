
# Refund Success

## Structure

`RefundSuccess`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `refund_id` | `int` | Required | - |
| `gateway_transaction_id` | `int` | Required | - |
| `product_id` | `int` | Required | - |

## Example

```python
from advancedbilling.models.refund_success import RefundSuccess

refund_success = RefundSuccess(
    refund_id=194,
    gateway_transaction_id=0,
    product_id=162
)
```

