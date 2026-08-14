
# Update Invoice Request

Request payload for updating a draft ad hoc invoice.

## Structure

`UpdateInvoiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice` | [`UpdateInvoice`](../../doc/models/update-invoice.md) | Required | Attributes of a draft ad hoc invoice which can be updated. Only the submitted attributes are changed. |

## Example

```python
import dateutil.parser

from advancedbilling.models.update_invoice import UpdateInvoice
from advancedbilling.models.update_invoice_item import UpdateInvoiceItem
from advancedbilling.models.update_invoice_request import UpdateInvoiceRequest

update_invoice_request = UpdateInvoiceRequest(
    invoice=UpdateInvoice(
        line_items=[
            UpdateInvoiceItem(
                title='title4',
                quantity=56.68,
                unit_price=39.9,
                taxable=False,
                tax_code='tax_code6'
            ),
            UpdateInvoiceItem(
                title='title4',
                quantity=56.68,
                unit_price=39.9,
                taxable=False,
                tax_code='tax_code6'
            ),
            UpdateInvoiceItem(
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
        memo='memo0'
    )
)
```

