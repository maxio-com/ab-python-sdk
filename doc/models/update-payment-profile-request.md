
# Update Payment Profile Request

## Structure

`UpdatePaymentProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_profile` | [`UpdatePaymentProfile`](../../doc/models/update-payment-profile.md) | Required | - |

## Example

```python
from advancedbilling.models.card_type import CardType
from advancedbilling.models.update_payment_profile import UpdatePaymentProfile
from advancedbilling.models.update_payment_profile_request import UpdatePaymentProfileRequest

update_payment_profile_request = UpdatePaymentProfileRequest(
    payment_profile=UpdatePaymentProfile(
        first_name='first_name4',
        last_name='last_name2',
        full_number='5424000000000015',
        card_type=CardType.BOGUS,
        expiration_month='expiration_month0'
    )
)
```

