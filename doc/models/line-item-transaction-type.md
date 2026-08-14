
# Line Item Transaction Type

A handle for the line item transaction type

## Enumeration

`LineItemTransactionType`

## Fields

| Name |
|  --- |
| `CHARGE` |
| `CREDIT` |
| `ADJUSTMENT` |
| `PAYMENT` |
| `REFUND` |
| `INFO_TRANSACTION` |
| `PAYMENT_AUTHORIZATION` |

## Example

```python
from advancedbilling.models.line_item_transaction_type import LineItemTransactionType

line_item_transaction_type = LineItemTransactionType.REFUND
```

