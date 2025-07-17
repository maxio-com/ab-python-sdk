
# Bank Account Payment Profile

## Structure

`BankAccountPaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The Chargify-assigned ID of the stored bank account. This value can be used as an input to payment_profile_id when creating a subscription, in order to re-use a stored payment profile for the same customer |
| `first_name` | `str` | Optional | The first name of the bank account holder |
| `last_name` | `str` | Optional | The last name of the bank account holder |
| `customer_id` | `int` | Optional | The Chargify-assigned id for the customer record to which the bank account belongs |
| `current_vault` | [`BankAccountVault`](../../doc/models/bank-account-vault.md) | Optional | The vault that stores the payment profile with the provided vault_token. Use `bogus` for testing. |
| `vault_token` | `str` | Optional | The “token” provided by your vault storage for an already stored payment profile |
| `billing_address` | `str` | Optional | The current billing street address for the bank account |
| `billing_city` | `str` | Optional | The current billing address city for the bank account |
| `billing_state` | `str` | Optional | The current billing address state for the bank account |
| `billing_zip` | `str` | Optional | The current billing address zip code for the bank account |
| `billing_country` | `str` | Optional | The current billing address country for the bank account |
| `customer_vault_token` | `str` | Optional | (only for Authorize.Net CIM storage): the customerProfileId for the owner of the customerPaymentProfileId provided as the vault_token. |
| `billing_address_2` | `str` | Optional | The current billing street address, second line, for the bank account |
| `bank_name` | `str` | Optional | The bank where the account resides |
| `masked_bank_routing_number` | `str` | Optional | A string representation of the stored bank routing number with all but the last 4 digits marked with X’s (i.e. ‘XXXXXXX1111’). payment_type will be bank_account |
| `masked_bank_account_number` | `str` | Required | A string representation of the stored bank account number with all but the last 4 digits marked with X’s (i.e. ‘XXXXXXX1111’) |
| `bank_account_type` | [`BankAccountType`](../../doc/models/bank-account-type.md) | Optional | Defaults to checking |
| `bank_account_holder_type` | [`BankAccountHolderType`](../../doc/models/bank-account-holder-type.md) | Optional | Defaults to personal |
| `payment_type` | [`PaymentType`](../../doc/models/payment-type.md) | Required | **Default**: `'bank_account'` |
| `verified` | `bool` | Optional | denotes whether a bank account has been verified by providing the amounts of two small deposits made into the account<br><br>**Default**: `False` |
| `site_gateway_setting_id` | `int` | Optional | - |
| `gateway_handle` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | A timestamp indicating when this payment profile was created |
| `updated_at` | `datetime` | Optional | A timestamp indicating when this payment profile was last updated |

## Example (as JSON)

```json
{
  "masked_bank_account_number": "masked_bank_account_number8",
  "payment_type": "bank_account",
  "verified": false,
  "id": 188,
  "first_name": "first_name6",
  "last_name": "last_name4",
  "customer_id": 226,
  "current_vault": "authorizenet"
}
```

