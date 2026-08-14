
# Proforma Invoice Payment

## Structure

`ProformaInvoicePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `memo` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `original_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `applied_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `prepayment` | `bool` | Optional | - |

## Example

```python
from advancedbilling.models.proforma_invoice_payment import ProformaInvoicePayment

proforma_invoice_payment = ProformaInvoicePayment(
    memo='memo2',
    original_amount='original_amount2',
    applied_amount='applied_amount0',
    prepayment=False
)
```

