
# Consolidated Invoice

## Structure

`ConsolidatedInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoices` | [`List[Invoice]`](../../doc/models/invoice.md) | Optional | - |

## Example

```python
from advancedbilling.models.consolidated_invoice import ConsolidatedInvoice
from advancedbilling.models.invoice import Invoice

consolidated_invoice = ConsolidatedInvoice(
    invoices=[
        Invoice(
            id=196,
            uid='uid6',
            site_id=122,
            customer_id=234,
            subscription_id=50
        )
    ]
)
```

