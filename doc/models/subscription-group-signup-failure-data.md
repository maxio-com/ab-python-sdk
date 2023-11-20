
# Subscription Group Signup Failure Data

## Structure

`SubscriptionGroupSignupFailureData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `int` | Optional | - |
| `payer_reference` | `str` | Optional | - |
| `payment_profile_id` | `int` | Optional | - |
| `payment_collection_method` | `str` | Optional | - |
| `payer_attributes` | [`PayerAttributes`](../../doc/models/payer-attributes.md) | Optional | - |
| `credit_card_attributes` | [`SubscriptionGroupCreditCard`](../../doc/models/subscription-group-credit-card.md) | Optional | - |
| `bank_account_attributes` | [`SubscriptionGroupBankAccount`](../../doc/models/subscription-group-bank-account.md) | Optional | - |
| `subscriptions` | [`List[SubscriptionGroupSignupItem]`](../../doc/models/subscription-group-signup-item.md) | Optional | - |

## Example (as JSON)

```json
{
  "payer_id": 16,
  "payer_reference": "payer_reference8",
  "payment_profile_id": 6,
  "payment_collection_method": "payment_collection_method0",
  "payer_attributes": {
    "first_name": "first_name2",
    "last_name": "last_name0",
    "email": "email4",
    "cc_emails": "cc_emails2",
    "organization": "organization6"
  }
}
```

