
# Invoice Response

## Structure

`InvoiceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_response import InvoiceResponse

invoice_response = InvoiceResponse(
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
    )
)
```

