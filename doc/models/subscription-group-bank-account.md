
# Subscription Group Bank Account

## Structure

`SubscriptionGroupBankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_name` | `str` | Optional | (Required when creating a subscription with ACH or GoCardless) The name of the bank where the customer’s account resides |
| `bank_account_number` | `str` | Optional | (Required when creating a subscription with ACH. Required when creating a subscription with GoCardless and bank_iban is blank) The customerʼs bank account number |
| `bank_routing_number` | `str` | Optional | (Required when creating a subscription with ACH. Optional when creating a subscription with GoCardless). The routing number of the bank. It becomes bank_code while passing via GoCardless API |
| `bank_iban` | `str` | Optional | (Optional when creating a subscription with GoCardless). International Bank Account Number. Alternatively, local bank details can be provided |
| `bank_branch_code` | `str` | Optional | (Optional when creating a subscription with GoCardless) Branch code. Alternatively, an IBAN can be provided |
| `bank_account_type` | [`BankAccountType`](../../doc/models/bank-account-type.md) | Optional | Defaults to checking<br>**Default**: `'checking'` |
| `bank_account_holder_type` | [`BankAccountHolderType`](../../doc/models/bank-account-holder-type.md) | Optional | Defaults to personal |
| `payment_type` | [`PaymentType`](../../doc/models/payment-type.md) | Optional | **Default**: `'credit_card'` |
| `billing_address` | `str` | Optional | - |
| `billing_city` | `str` | Optional | - |
| `billing_state` | `str` | Optional | - |
| `billing_zip` | `str` | Optional | - |
| `billing_country` | `str` | Optional | - |
| `chargify_token` | `str` | Optional | - |
| `current_vault` | [`BankAccountVault`](../../doc/models/bank-account-vault.md) | Optional | The vault that stores the payment profile with the provided vault_token. |
| `gateway_handle` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "bank_account_type": "checking",
  "payment_type": "credit_card",
  "bank_name": "bank_name2",
  "bank_account_number": "bank_account_number4",
  "bank_routing_number": "bank_routing_number8",
  "bank_iban": "bank_iban6",
  "bank_branch_code": "bank_branch_code6"
}
```

