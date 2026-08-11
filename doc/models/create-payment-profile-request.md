
# Create Payment Profile Request

## Structure

`CreatePaymentProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_profile` | [`CreatePaymentProfile`](../../doc/models/create-payment-profile.md) | Required | - |

## Example

```python
from advancedbilling.models.create_payment_profile import CreatePaymentProfile
from advancedbilling.models.create_payment_profile_request import CreatePaymentProfileRequest
from advancedbilling.models.payment_type import PaymentType

create_payment_profile_request = CreatePaymentProfileRequest(
    payment_profile=CreatePaymentProfile(
        chargify_token='tok_9g6hw85pnpt6knmskpwp4ttt',
        id=44,
        payment_type=PaymentType.CREDIT_CARD,
        first_name='first_name4',
        last_name='last_name2',
        full_number='5424000000000015'
    )
)
```

