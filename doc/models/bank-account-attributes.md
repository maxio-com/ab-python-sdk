
# Bank Account Attributes

## Structure

`BankAccountAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chargify_token` | `str` | Optional | - |
| `bank_name` | `str` | Optional | (Required when creating a subscription with ACH or GoCardless) The name of the bank where the customer’s account resides |
| `bank_routing_number` | `str` | Optional | (Required when creating a subscription with ACH. Optional when creating a subscription with GoCardless). The routing number of the bank. It becomes bank_code while passing via GoCardless API |
| `bank_account_number` | `str` | Optional | (Required when creating a subscription with ACH. Required when creating a subscription with GoCardless and bank_iban is blank) The customerʼs bank account number |
| `bank_account_type` | `str` | Optional | - |
| `bank_branch_code` | `str` | Optional | (Optional when creating a subscription with GoCardless) Branch code. Alternatively, an IBAN can be provided |
| `bank_iban` | `str` | Optional | (Optional when creating a subscription with GoCardless). International Bank Account Number. Alternatively, local bank details can be provided |
| `bank_account_holder_type` | `str` | Optional | - |
| `payment_type` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "chargify_token": "chargify_token0",
  "bank_name": "bank_name2",
  "bank_routing_number": "bank_routing_number8",
  "bank_account_number": "bank_account_number4",
  "bank_account_type": "bank_account_type0"
}
```

