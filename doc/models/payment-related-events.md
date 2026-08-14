
# Payment Related Events

## Structure

`PaymentRelatedEvents`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Required | - |
| `account_transaction_id` | `int` | Required | - |

## Example

```python
from advancedbilling.models.payment_related_events import PaymentRelatedEvents

payment_related_events = PaymentRelatedEvents(
    product_id=208,
    account_transaction_id=52
)
```

