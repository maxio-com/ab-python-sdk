
# Create Invoice

## Structure

`CreateInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `line_items` | [`List[CreateInvoiceItem]`](../../doc/models/create-invoice-item.md) | Optional | - |
| `issue_date` | `date` | Optional | Date on which the invoice will be issued (format YYYY-MM-DD). This date is interpreted and validated in your site's time zone. It must be today or a date in the past — future dates are not accepted. If omitted, defaults to today in your site's time zone. |
| `net_terms` | `int` | Optional | By default, invoices will be created with a due date matching the date of invoice creation. If a different due date is desired, the net_terms parameter can be sent indicating the number of days in advance the due date should be. |
| `payment_instructions` | `str` | Optional | - |
| `memo` | `str` | Optional | A custom memo can be sent to override the site's default. |
| `seller_address` | [`CreateInvoiceAddress`](../../doc/models/create-invoice-address.md) | Optional | Overrides the defaults for the site. |
| `billing_address` | [`CreateInvoiceAddress`](../../doc/models/create-invoice-address.md) | Optional | Overrides the default for the customer. |
| `shipping_address` | [`CreateInvoiceAddress`](../../doc/models/create-invoice-address.md) | Optional | Overrides the default for the customer. |
| `coupons` | [`List[CreateInvoiceCoupon]`](../../doc/models/create-invoice-coupon.md) | Optional | - |
| `status` | [`CreateInvoiceStatus`](../../doc/models/create-invoice-status.md) | Optional | **Default**: `"open"` |

## Example

```python
import dateutil.parser

from advancedbilling.models.create_invoice import CreateInvoice
from advancedbilling.models.create_invoice_item import CreateInvoiceItem
from advancedbilling.models.create_invoice_status import CreateInvoiceStatus

create_invoice = CreateInvoice(
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
        )
    ],
    issue_date=dateutil.parser.parse('2024-01-01').date(),
    net_terms=100,
    payment_instructions='payment_instructions4',
    memo='memo0',
    status=CreateInvoiceStatus.DRAFT
)
```

