
# List Invoices Response

## Structure

`ListInvoicesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoices` | [`List[Invoice]`](../../doc/models/invoice.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.invoice import Invoice
from advancedbilling.models.list_invoices_response import ListInvoicesResponse

list_invoices_response = ListInvoicesResponse(
    invoices=[
        Invoice(
            id=196,
            uid='uid6',
            site_id=122,
            customer_id=234,
            subscription_id=50,
            issue_date=dateutil.parser.parse('2024-01-01').date(),
            due_date=dateutil.parser.parse('2024-01-01').date(),
            paid_date=dateutil.parser.parse('2024-01-01').date(),
            public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
        )
    ]
)
```

