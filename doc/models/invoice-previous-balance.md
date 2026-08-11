
# Invoice Previous Balance

## Structure

`InvoicePreviousBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `captured_at` | `datetime` | Optional | - |
| `invoices` | [`List[InvoiceBalanceItem]`](../../doc/models/invoice-balance-item.md) | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.invoice_balance_item import InvoiceBalanceItem
from advancedbilling.models.invoice_previous_balance import InvoicePreviousBalance

invoice_previous_balance = InvoicePreviousBalance(
    captured_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoices=[
        InvoiceBalanceItem(
            uid='uid6',
            number='number6',
            outstanding_amount='outstanding_amount8'
        ),
        InvoiceBalanceItem(
            uid='uid6',
            number='number6',
            outstanding_amount='outstanding_amount8'
        ),
        InvoiceBalanceItem(
            uid='uid6',
            number='number6',
            outstanding_amount='outstanding_amount8'
        )
    ]
)
```

