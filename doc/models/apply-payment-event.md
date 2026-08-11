
# Apply Payment Event

## Structure

`ApplyPaymentEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"apply_payment"` |
| `event_data` | [`ApplyPaymentEventData`](../../doc/models/apply-payment-event-data.md) | Required | Example schema for an `apply_payment` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.apply_payment_event import ApplyPaymentEvent
from advancedbilling.models.apply_payment_event_data import ApplyPaymentEventData
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_consolidation_level import InvoiceConsolidationLevel
from advancedbilling.models.invoice_event_payment_method import InvoiceEventPaymentMethod
from advancedbilling.models.invoice_event_type import InvoiceEventType
from advancedbilling.models.payment_method_apple_pay import PaymentMethodApplePay

apply_payment_event = ApplyPaymentEvent(
    id=244,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        id=166,
        uid='uid6',
        site_id=92,
        customer_id=204,
        subscription_id=20,
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.APPLY_PAYMENT,
    event_data=ApplyPaymentEventData(
        consolidation_level=InvoiceConsolidationLevel.CHILD,
        memo='memo0',
        original_amount='original_amount0',
        applied_amount='applied_amount2',
        transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        payment_method=PaymentMethodApplePay(
            mtype=InvoiceEventPaymentMethod.APPLE_PAY
        ),
        transaction_id=78,
        parent_invoice_number=36,
        remaining_prepayment_amount='remaining_prepayment_amount6',
        prepayment=False,
        external=False
    )
)
```

