
# Change Invoice Status Event Data

Example schema for an `change_invoice_status` event

## Structure

`ChangeInvoiceStatusEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gateway_trans_id` | `str` | Optional | Identifier for the transaction within the payment gateway. |
| `amount` | `str` | Optional | The monetary value associated with the linked payment, expressed in dollars. |
| `from_status` | [`InvoiceStatus`](../../doc/models/invoice-status.md) | Required | The status of the invoice before any changes occurred. See [Invoice Statuses](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses) for more. |
| `to_status` | [`InvoiceStatus`](../../doc/models/invoice-status.md) | Required | The updated status of the invoice after changes have been made. See [Invoice Statuses](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses) for more. |
| `consolidation_level` | [`InvoiceConsolidationLevel`](../../doc/models/invoice-consolidation-level.md) | Optional | - |

## Example

```python
from advancedbilling.models.change_invoice_status_event_data import ChangeInvoiceStatusEventData
from advancedbilling.models.invoice_consolidation_level import InvoiceConsolidationLevel
from advancedbilling.models.invoice_status import InvoiceStatus

change_invoice_status_event_data = ChangeInvoiceStatusEventData(
    from_status=InvoiceStatus.VOIDED,
    to_status=InvoiceStatus.DRAFT,
    gateway_trans_id='gateway_trans_id6',
    amount='amount4',
    consolidation_level=InvoiceConsolidationLevel.NONE
)
```

