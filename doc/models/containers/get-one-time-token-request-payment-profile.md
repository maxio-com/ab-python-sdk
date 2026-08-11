
# Get One Time Token Request Payment Profile

## Data Type

`GetOneTimeTokenPaymentProfile | GetOneTimeTokenBankAccountPaymentProfile`

## Cases

| Type |
|  --- |
| [`GetOneTimeTokenPaymentProfile`](../../../doc/models/get-one-time-token-payment-profile.md) |
| [`GetOneTimeTokenBankAccountPaymentProfile`](../../../doc/models/get-one-time-token-bank-account-payment-profile.md) |

## GetOneTimeTokenPaymentProfile

### Initialization Code

#### Example

```python
value = GetOneTimeTokenPaymentProfile(
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
    site_gateway_setting_id=232
)
```

## GetOneTimeTokenBankAccountPaymentProfile

### Initialization Code

#### Example

```python
value = GetOneTimeTokenBankAccountPaymentProfile(
    first_name='first_name8',
    last_name='last_name6',
    current_vault=BankAccountVault.MAXP,
    vault_token='vault_token0',
    billing_address='billing_address0',
    billing_city='billing_city4',
    billing_country='billing_country2',
    billing_state='billing_state8',
    billing_zip='billing_zip6',
    bank_name='bank_name6',
    masked_bank_routing_number='masked_bank_routing_number6',
    masked_bank_account_number='masked_bank_account_number0',
    bank_account_type=BankAccountType.CHECKING,
    bank_account_holder_type=BankAccountHolderType.PERSONAL,
    payment_type='payment_type2',
    disabled=False,
    site_gateway_setting_id=254
)
```

