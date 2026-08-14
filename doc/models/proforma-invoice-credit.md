
# Proforma Invoice Credit

## Structure

`ProformaInvoiceCredit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `memo` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `original_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `applied_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |

## Example

```python
from advancedbilling.models.proforma_invoice_credit import ProformaInvoiceCredit

proforma_invoice_credit = ProformaInvoiceCredit(
    uid='uid0',
    memo='memo4',
    original_amount='original_amount4',
    applied_amount='applied_amount8'
)
```

