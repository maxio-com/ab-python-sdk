
# Get One Time Token Request

## Structure

`GetOneTimeTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_profile` | [Get One Time Token Payment Profile](../../doc/models/get-one-time-token-payment-profile.md) \| [Get One Time Token Bank Account Payment Profile](../../doc/models/get-one-time-token-bank-account-payment-profile.md) | Required | This is a container for any-of cases. |

## Example

```python
from advancedbilling.models.card_type import CardType
from advancedbilling.models.credit_card_vault import CreditCardVault
from advancedbilling.models.get_one_time_token_payment_profile import GetOneTimeTokenPaymentProfile
from advancedbilling.models.get_one_time_token_request import GetOneTimeTokenRequest

get_one_time_token_request = GetOneTimeTokenRequest(
    payment_profile=GetOneTimeTokenPaymentProfile(
        first_name='first_name2',
        last_name='last_name0',
        masked_card_number='masked_card_number0',
        card_type=CardType.ROUTEX,
        expiration_month=187.78,
        expiration_year=164.44,
        current_vault=CreditCardVault.BRAINTREE_BLUE,
        vault_token='vault_token4',
        billing_address='billing_address4',
        billing_city='billing_city0',
        billing_country='billing_country6',
        billing_state='billing_state6',
        billing_zip='billing_zip0',
        payment_type='payment_type2',
        disabled=False,
        site_gateway_setting_id=232,
        id='id2',
        customer_id='customer_id0',
        billing_address_2='billing_address_24',
        customer_vault_token='customer_vault_token0',
        gateway_handle='gateway_handle4'
    )
)
```

