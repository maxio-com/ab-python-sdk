
# Invoice Payment Method

## Structure

`InvoicePaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `details` | `str` | Optional | - |
| `kind` | `str` | Optional | - |
| `memo` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `card_brand` | `str` | Optional | - |
| `card_expiration` | `str` | Optional | - |
| `last_four` | `str` | Optional | - |
| `masked_card_number` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_payment_method import InvoicePaymentMethod

invoice_payment_method = InvoicePaymentMethod(
    details='details2',
    kind='kind0',
    memo='memo6',
    mtype='type2',
    card_brand='card_brand4'
)
```

