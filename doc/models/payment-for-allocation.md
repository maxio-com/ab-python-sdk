
# Payment for Allocation

Information for captured payment, if applicable

## Structure

`PaymentForAllocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `amount_in_cents` | `int` | Optional | - |
| `success` | `bool` | Optional | - |
| `memo` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.payment_for_allocation import PaymentForAllocation

payment_for_allocation = PaymentForAllocation(
    id=232,
    amount_in_cents=194,
    success=False,
    memo='memo6'
)
```

