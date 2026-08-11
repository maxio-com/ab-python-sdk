
# Create Payment Profile

## Structure

`CreatePaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chargify_token` | `str` | Optional | Token received after sending billing information using Maxio.js (formerly Chargify.js). |
| `id` | `int` | Optional | - |
| `payment_type` | [`PaymentType`](../../doc/models/payment-type.md) | Optional | - |
| `first_name` | `str` | Optional | First name on card or bank account. If omitted, the first_name from customer attributes will be used. |
| `last_name` | `str` | Optional | Last name on card or bank account. If omitted, the last_name from customer attributes will be used. |
| `masked_card_number` | `str` | Optional | - |
| `full_number` | `str` | Optional | The full credit card number |
| `card_type` | [`CardType`](../../doc/models/card-type.md) | Optional | The type of card used. |
| `expiration_month` | int \| str \| None | Optional | This is a container for one-of cases. |
| `expiration_year` | int \| str \| None | Optional | This is a container for one-of cases. |
| `billing_address` | `str` | Optional | The credit card or bank account billing street address (e.g., 123 Main St.). This value is merely passed through to the payment gateway. |
| `billing_address_2` | `str` | Optional | Second line of the customer’s billing address e.g., Apt. 100 |
| `billing_city` | `str` | Optional | The credit card or bank account billing address city (e.g., “Boston”). This value is merely passed through to the payment gateway. |
| `billing_state` | `str` | Optional | The credit card or bank account billing address state (e.g., MA). This value is merely passed through to the payment gateway. This must conform to the [ISO_3166-1](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes) in order to be valid for tax locale purposes. |
| `billing_country` | `str` | Optional | “The credit card or bank account billing address country, required in [ISO_3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format (e.g., “US”). This value is merely passed through to the payment gateway. Some gateways require country codes in a specific format. Check your gateway’s documentation. If creating an ACH subscription, only US is supported at this time.” |
| `billing_zip` | `str` | Optional | The credit card or bank account billing address zip code (e.g., 12345). This value is merely passed through to the payment gateway. |
| `current_vault` | [`AllVaults`](../../doc/models/all-vaults.md) | Optional | The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for testing. |
| `vault_token` | `str` | Optional | The “token” provided by your vault storage for an already stored payment profile |
| `customer_vault_token` | `str` | Optional | (only for Authorize.Net CIM storage or Square) The customerProfileId for the owner of the customerPaymentProfileId provided as the vault_token |
| `customer_id` | `int` | Optional | (Required when creating a new payment profile) The Chargify customer id. |
| `paypal_email` | `str` | Optional | used by merchants that implemented BraintreeBlue javaScript libraries on their own. We recommend using Maxio.js (formerly Chargify.js) instead. |
| `payment_method_nonce` | `str` | Optional | used by merchants that implemented BraintreeBlue javaScript libraries on their own. We recommend using Maxio.js (formerly Chargify.js) instead. |
| `gateway_handle` | `str` | Optional | This attribute is only available if MultiGateway feature is enabled for your Site. This feature is in the Private Beta currently. gateway_handle is used to directly select a gateway where a payment profile will be stored in. Every connected gateway must have a unique gateway handle specified. Read [Multigateway description](https://chargify.zendesk.com/hc/en-us/articles/4407761759643#connecting-with-multiple-gateways) to learn more about new concepts that MultiGateway introduces and the default behavior when this attribute is not passed. |
| `cvv` | `str` | Optional | The 3- or 4-digit Card Verification Value. This value is merely passed through to the payment gateway. |
| `bank_name` | `str` | Optional | (Required when creating with ACH or GoCardless, optional with Stripe Direct Debit). The name of the bank where the customerʼs account resides |
| `bank_iban` | `str` | Optional | (Optional when creating with GoCardless, required with Stripe Direct Debit). International Bank Account Number. Alternatively, local bank details can be provided. |
| `bank_routing_number` | `str` | Optional | (Required when creating with ACH. Optional when creating a subscription with GoCardless). The routing number of the bank. It becomes bank_code while passing via GoCardless API. |
| `bank_account_number` | `str` | Optional | (Required when creating with ACH, GoCardless, Stripe BECS or BACS Direct Debit, and bank_iban is blank) The customerʼs bank account number |
| `bank_branch_code` | `str` | Optional | (Optional when creating with GoCardless, required with Stripe BECS or BACS Direct Debit) Branch/Sort code. Alternatively, an IBAN can be provided. |
| `bank_account_type` | [`BankAccountType`](../../doc/models/bank-account-type.md) | Optional | Defaults to checking |
| `bank_account_holder_type` | [`BankAccountHolderType`](../../doc/models/bank-account-holder-type.md) | Optional | Defaults to personal |
| `last_four` | `str` | Optional | (Optional) Used for creating subscription with payment profile imported using vault_token, for proper display in Advanced Billing UI |

## Example

```python
from advancedbilling.models.create_payment_profile import CreatePaymentProfile
from advancedbilling.models.payment_type import PaymentType

create_payment_profile = CreatePaymentProfile(
    chargify_token='tok_9g6hw85pnpt6knmskpwp4ttt',
    id=32,
    payment_type=PaymentType.CREDIT_CARD,
    first_name='first_name4',
    last_name='last_name2',
    full_number='5424000000000015'
)
```

