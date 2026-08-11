
# Invoice Payment

## Structure

`InvoicePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_time` | `datetime` | Optional | - |
| `memo` | `str` | Optional | - |
| `original_amount` | `str` | Optional | - |
| `applied_amount` | `str` | Optional | - |
| `payment_method` | [`InvoicePaymentMethod`](../../doc/models/invoice-payment-method.md) | Optional | - |
| `transaction_id` | `int` | Optional | - |
| `prepayment` | `bool` | Optional | - |
| `gateway_handle` | `str` | Optional | - |
| `gateway_used` | `str` | Optional | - |
| `gateway_transaction_id` | `str` | Optional | The transaction ID for the payment as returned from the payment gateway |
| `received_on` | `date` | Optional | Date reflecting when the payment was received from a customer. Must be in the past. Applicable only to<br>`external` payments. |
| `uid` | `str` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.invoice_payment import InvoicePayment
from advancedbilling.models.invoice_payment_method import InvoicePaymentMethod

invoice_payment = InvoicePayment(
    transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    memo='memo4',
    original_amount='original_amount4',
    applied_amount='applied_amount8',
    payment_method=InvoicePaymentMethod(
        details='details0',
        kind='kind8',
        memo='memo4',
        mtype='type0',
        card_brand='card_brand6'
    )
)
```

