
# Chjs Tokenization Failure

## Structure

`ChjsTokenizationFailure`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | `str` | Required | - |
| `payment_profile_params` | [`PaymentProfileParams`](../../doc/models/payment-profile-params.md) | Optional | PCI-safe cardholder fields only. Full card numbers, CVV, and billing address are never included. |

## Example

```python
from advancedbilling.models.chjs_tokenization_failure import ChjsTokenizationFailure
from advancedbilling.models.payment_profile_params import PaymentProfileParams

chjs_tokenization_failure = ChjsTokenizationFailure(
    errors='errors4',
    payment_profile_params=PaymentProfileParams(
        first_name='first_name2',
        last_name='last_name0',
        card_type='card_type2'
    )
)
```

