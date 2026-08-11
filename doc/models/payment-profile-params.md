
# Payment Profile Params

PCI-safe cardholder fields only. Full card numbers, CVV, and billing address are never included.

## Structure

`PaymentProfileParams`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `card_type` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.payment_profile_params import PaymentProfileParams

payment_profile_params = PaymentProfileParams(
    first_name='first_name2',
    last_name='last_name0',
    card_type='card_type2'
)
```

