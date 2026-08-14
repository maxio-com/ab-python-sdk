
# Proforma Invoice Issued

## Structure

`ProformaInvoiceIssued`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Required | - |
| `number` | `str` | Required | - |
| `role` | `str` | Required | - |
| `delivery_date` | `date` | Required | - |
| `created_at` | `datetime` | Required | - |
| `due_amount` | `str` | Required | - |
| `paid_amount` | `str` | Required | - |
| `tax_amount` | `str` | Required | - |
| `total_amount` | `str` | Required | - |
| `product_name` | `str` | Required | - |
| `line_items` | [`List[InvoiceLineItemEventData]`](../../doc/models/invoice-line-item-event-data.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.invoice_line_item_event_data import InvoiceLineItemEventData
from advancedbilling.models.proforma_invoice_issued import ProformaInvoiceIssued

proforma_invoice_issued = ProformaInvoiceIssued(
    uid='uid8',
    number='number4',
    role='role8',
    delivery_date=dateutil.parser.parse('2016-03-13').date(),
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    due_amount='due_amount0',
    paid_amount='paid_amount0',
    tax_amount='tax_amount8',
    total_amount='total_amount4',
    product_name='product_name4',
    line_items=[
        InvoiceLineItemEventData(
            uid='uid8',
            title='title4',
            description='description8',
            quantity=102,
            quantity_delta=204
        )
    ]
)
```

