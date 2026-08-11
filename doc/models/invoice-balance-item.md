
# Invoice Balance Item

## Structure

`InvoiceBalanceItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `number` | `str` | Optional | - |
| `outstanding_amount` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_balance_item import InvoiceBalanceItem

invoice_balance_item = InvoiceBalanceItem(
    uid='uid4',
    number='number2',
    outstanding_amount='outstanding_amount0'
)
```

