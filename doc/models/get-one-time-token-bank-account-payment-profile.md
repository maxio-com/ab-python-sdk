
# Get One Time Token Bank Account Payment Profile

## Structure

`GetOneTimeTokenBankAccountPaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `first_name` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `last_name` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `customer_id` | `str` | Optional | - |
| `current_vault` | [`BankAccountVault`](../../doc/models/bank-account-vault.md) | Required | The vault that stores the payment profile with the provided vault_token. Use `bogus` for testing. |
| `vault_token` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `billing_address` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `billing_address_2` | `str` | Optional | - |
| `billing_city` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `billing_country` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `billing_state` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `billing_zip` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `bank_name` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `masked_bank_routing_number` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `masked_bank_account_number` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `bank_account_type` | [`BankAccountType`](../../doc/models/bank-account-type.md) | Required | Defaults to checking |
| `bank_account_holder_type` | [`BankAccountHolderType`](../../doc/models/bank-account-holder-type.md) | Required | Defaults to personal |
| `payment_type` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `disabled` | `bool` | Required | - |
| `site_gateway_setting_id` | `int` | Required | - |
| `customer_vault_token` | `str` | Optional | - |
| `gateway_handle` | `str` | Optional | - |
| `verified` | `bool` | Optional | - |

## Example

```python
from advancedbilling.models.bank_account_holder_type import BankAccountHolderType
from advancedbilling.models.bank_account_type import BankAccountType
from advancedbilling.models.bank_account_vault import BankAccountVault
from advancedbilling.models.get_one_time_token_bank_account_payment_profile import GetOneTimeTokenBankAccountPaymentProfile

get_one_time_token_bank_account_payment_profile = GetOneTimeTokenBankAccountPaymentProfile(
    first_name='first_name6',
    last_name='last_name4',
    current_vault=BankAccountVault.AUTHORIZENET,
    vault_token='vault_token8',
    billing_address='billing_address8',
    billing_city='billing_city4',
    billing_country='billing_country0',
    billing_state='billing_state0',
    billing_zip='billing_zip4',
    bank_name='bank_name8',
    masked_bank_routing_number='masked_bank_routing_number8',
    masked_bank_account_number='masked_bank_account_number8',
    bank_account_type=BankAccountType.CHECKING,
    bank_account_holder_type=BankAccountHolderType.PERSONAL,
    payment_type='payment_type4',
    disabled=False,
    site_gateway_setting_id=128,
    id='id6',
    customer_id='customer_id4',
    billing_address_2='billing_address_28',
    customer_vault_token='customer_vault_token4',
    gateway_handle='gateway_handle8'
)
```

