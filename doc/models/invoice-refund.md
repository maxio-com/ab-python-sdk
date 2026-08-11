
# Invoice Refund

## Structure

`InvoiceRefund`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `int` | Optional | - |
| `payment_id` | `int` | Optional | - |
| `memo` | `str` | Optional | - |
| `original_amount` | `str` | Optional | - |
| `applied_amount` | `str` | Optional | - |
| `gateway_transaction_id` | `str` | Optional | The transaction ID for the refund as returned from the payment gateway |
| `gateway_used` | `str` | Optional | - |
| `gateway_handle` | `str` | Optional | - |
| `ach_late_reject` | `bool` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_refund import InvoiceRefund

invoice_refund = InvoiceRefund(
    transaction_id=0,
    payment_id=126,
    memo='memo0',
    original_amount='original_amount0',
    applied_amount='applied_amount2'
)
```

