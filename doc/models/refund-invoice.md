
# Refund Invoice

Refund an invoice or a segment of a consolidated invoice.

## Structure

`RefundInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `str` | Required | The amount to be refunded in decimal format as a string. Example: "10.50". Must not exceed the remaining refundable balance of the payment. |
| `memo` | `str` | Required | A description that will be attached to the refund |
| `payment_id` | `int` | Required | The ID of the payment to be refunded |
| `external` | `bool` | Optional | Flag that marks refund as external (no money is returned to the customer). Defaults to `false`. |
| `apply_credit` | `bool` | Optional | If set to true, creates credit and applies it to an invoice. Defaults to `false`. |
| `void_invoice` | `bool` | Optional | If `apply_credit` is set to false and refunding full amount, if `void_invoice` is set to true, invoice will be voided after refund. Defaults to `false`. |

## Example

```python
from advancedbilling.models.refund_invoice import RefundInvoice

refund_invoice = RefundInvoice(
    amount='amount6',
    memo='memo8',
    payment_id=74,
    external=False,
    apply_credit=False,
    void_invoice=False
)
```

