
# Apple Pay Payment Profile

## Structure

`ApplePayPaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The Chargify-assigned ID of the Apple Pay payment profile. |
| `first_name` | `str` | Optional | The first name of the Apple Pay account holder |
| `last_name` | `str` | Optional | The last name of the Apple Pay account holder |
| `customer_id` | `int` | Optional | The Chargify-assigned ID for the customer record to which the Apple Pay account belongs |
| `current_vault` | [`ApplePayVault`](../../doc/models/apple-pay-vault.md) | Optional | The vault that stores the payment profile with the provided vault_token. |
| `vault_token` | `str` | Optional | The “token” provided by your vault storage for an already stored payment profile |
| `billing_address` | `str` | Optional | The current billing street address for the Apple Pay account |
| `billing_city` | `str` | Optional | The current billing address city for the Apple Pay account |
| `billing_state` | `str` | Optional | The current billing address state for the Apple Pay account |
| `billing_zip` | `str` | Optional | The current billing address zip code for the Apple Pay account |
| `billing_country` | `str` | Optional | The current billing address country for the Apple Pay account |
| `customer_vault_token` | `str` | Optional | - |
| `billing_address_2` | `str` | Optional | The current billing street address, second line, for the Apple Pay account |
| `payment_type` | [`PaymentType`](../../doc/models/payment-type.md) | Required | **Default**: `"apple_pay"` |
| `site_gateway_setting_id` | `int` | Optional | - |
| `gateway_handle` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | A timestamp indicating when this payment profile was created |
| `updated_at` | `datetime` | Optional | A timestamp indicating when this payment profile was last updated |

## Example

```python
from advancedbilling.models.apple_pay_payment_profile import ApplePayPaymentProfile
from advancedbilling.models.apple_pay_vault import ApplePayVault
from advancedbilling.models.payment_type import PaymentType

apple_pay_payment_profile = ApplePayPaymentProfile(
    payment_type=PaymentType.APPLE_PAY,
    id=188,
    first_name='first_name2',
    last_name='last_name0',
    customer_id=226,
    current_vault=ApplePayVault.BRAINTREE_BLUE
)
```

