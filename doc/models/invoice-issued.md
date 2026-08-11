
# Invoice Issued

## Structure

`InvoiceIssued`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Required | - |
| `number` | `str` | Required | - |
| `role` | `str` | Required | - |
| `due_date` | `date` | Required | - |
| `issue_date` | `str` | Required | Invoice issue date. Can be an empty string if value is missing. |
| `paid_date` | `str` | Required | Paid date. Can be an empty string if value is missing. |
| `due_amount` | `str` | Required | - |
| `paid_amount` | `str` | Required | - |
| `tax_amount` | `str` | Required | - |
| `refund_amount` | `str` | Required | - |
| `total_amount` | `str` | Required | - |
| `status_amount` | `str` | Required | - |
| `product_name` | `str` | Required | - |
| `consolidation_level` | `str` | Required | - |
| `line_items` | [`List[InvoiceLineItemEventData]`](../../doc/models/invoice-line-item-event-data.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.invoice_issued import InvoiceIssued
from advancedbilling.models.invoice_line_item_event_data import InvoiceLineItemEventData

invoice_issued = InvoiceIssued(
    uid='uid0',
    number='number8',
    role='role4',
    due_date=dateutil.parser.parse('2016-03-13').date(),
    issue_date='issue_date6',
    paid_date='paid_date0',
    due_amount='due_amount2',
    paid_amount='paid_amount2',
    tax_amount='tax_amount4',
    refund_amount='refund_amount6',
    total_amount='total_amount6',
    status_amount='status_amount0',
    product_name='product_name6',
    consolidation_level='consolidation_level2',
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

