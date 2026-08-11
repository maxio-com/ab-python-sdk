
# Payment Profile Response

## Structure

`PaymentProfileResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_profile` | [ApplePay Payment Profile](../../doc/models/apple-pay-payment-profile.md) \| [Bank Account Payment Profile](../../doc/models/bank-account-payment-profile.md) \| [Credit Card Payment Profile](../../doc/models/credit-card-payment-profile.md) \| [Paypal Payment Profile](../../doc/models/paypal-payment-profile.md) | Required | - |

## Example

```python
from advancedbilling.models.apple_pay_payment_profile import ApplePayPaymentProfile
from advancedbilling.models.apple_pay_vault import ApplePayVault
from advancedbilling.models.payment_profile_response import PaymentProfileResponse
from advancedbilling.models.payment_type import PaymentType

payment_profile_response = PaymentProfileResponse(
    payment_profile=ApplePayPaymentProfile(
        payment_type=PaymentType.APPLE_PAY,
        id=60,
        first_name='first_name2',
        last_name='last_name0',
        customer_id=98,
        current_vault=ApplePayVault.BRAINTREE_BLUE
    )
)
```

