
# Create Invoice Request

## Structure

`CreateInvoiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice` | [`CreateInvoice`](../../doc/models/create-invoice.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.create_invoice import CreateInvoice
from advancedbilling.models.create_invoice_item import CreateInvoiceItem
from advancedbilling.models.create_invoice_request import CreateInvoiceRequest
from advancedbilling.models.create_invoice_status import CreateInvoiceStatus

create_invoice_request = CreateInvoiceRequest(
    invoice=CreateInvoice(
        line_items=[
            CreateInvoiceItem(
                title='title4',
                quantity=56.68,
                unit_price=39.9,
                taxable=False,
                tax_code='tax_code6'
            ),
            CreateInvoiceItem(
                title='title4',
                quantity=56.68,
                unit_price=39.9,
                taxable=False,
                tax_code='tax_code6'
            ),
            CreateInvoiceItem(
                title='title4',
                quantity=56.68,
                unit_price=39.9,
                taxable=False,
                tax_code='tax_code6'
            )
        ],
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        net_terms=144,
        payment_instructions='payment_instructions6',
        memo='memo0',
        status=CreateInvoiceStatus.DRAFT
    )
)
```

