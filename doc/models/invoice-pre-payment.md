
# Invoice Pre Payment

## Structure

`InvoicePrePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Optional | The subscription id for the prepayment account |
| `amount_in_cents` | `int` | Optional | The amount in cents of the prepayment that was created as a result of this payment. |
| `ending_balance_in_cents` | `int` | Optional | The total balance of the prepayment account for this subscription including any prior prepayments |

## Example

```python
from advancedbilling.models.invoice_pre_payment import InvoicePrePayment

invoice_pre_payment = InvoicePrePayment(
    subscription_id=40,
    amount_in_cents=240,
    ending_balance_in_cents=56
)
```

