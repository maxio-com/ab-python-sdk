
# Create Subscription

## Structure

`CreateSubscription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_handle` | `str` | Optional | The API Handle of the product for which you are creating a subscription. Required, unless a `product_id` is given instead. |
| `product_id` | `int` | Optional | The Product ID of the product for which you are creating a subscription. The product ID is not currently published, so we recommend using the API Handle instead. |
| `product_price_point_handle` | `str` | Optional | The user-friendly API handle of a product's particular price point. |
| `product_price_point_id` | `int` | Optional | The ID of the particular price point on the product. |
| `custom_price` | [`SubscriptionCustomPrice`](../../doc/models/subscription-custom-price.md) | Optional | (Optional) Used in place of `product_price_point_id` to define a custom price point unique to the subscription |
| `coupon_code` | `str` | Optional | (deprecated) The coupon code of the single coupon currently applied to the subscription. See coupon_codes instead as subscriptions can now have more than one coupon. |
| `coupon_codes` | `List[str]` | Optional | An array for all the coupons attached to the subscription. |
| `payment_collection_method` | [`CollectionMethod`](../../doc/models/collection-method.md) | Optional | The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing Architecture valid options are - `remittance`, `automatic`, `prepaid`.<br>**Default**: `'automatic'` |
| `receives_invoice_emails` | `str` | Optional | (Optional) Default: True - Whether or not this subscription is set to receive emails related to this subscription. |
| `net_terms` | `str` | Optional | (Optional) Default: null The number of days after renewal (on invoice billing) that a subscription is due. A value between 0 (due immediately) and 180. |
| `customer_id` | `int` | Optional | The ID of an existing customer within Chargify. Required, unless a `customer_reference` or a set of `customer_attributes` is given. |
| `next_billing_at` | `datetime` | Optional | (Optional) Set this attribute to a future date/time to sync imported subscriptions to your existing renewal schedule. See the notes on “Date/Time Format” in our [subscription import documentation](https://maxio-chargify.zendesk.com/hc/en-us/articles/5404863655821#date-format). If you provide a next_billing_at timestamp that is in the future, no trial or initial charges will be applied when you create the subscription. In fact, no payment will be captured at all. The first payment will be captured, according to the prices defined by the product, near the time specified by next_billing_at. If you do not provide a value for next_billing_at, any trial and/or initial charges will be assessed and charged at the time of subscription creation. If the card cannot be successfully charged, the subscription will not be created. See further notes in the section on Importing Subscriptions. |
| `initial_billing_at` | `str` | Optional | (Optional) Set this attribute to a future date/time to create a subscription in the "Awaiting Signup" state, rather than "Active" or "Trialing". See the notes on “Date/Time Format” in our [subscription import documentation](https://maxio-chargify.zendesk.com/hc/en-us/articles/5404863655821#date-format). In the "Awaiting Signup" state, a subscription behaves like any other. It can be canceled, allocated to, had its billing date changed. etc. When the initial_billing_at date hits, the subscription will transition to the expected state. If the product has a trial, the subscription will enter a trial, otherwise it will go active. Setup fees will be respected either before or after the trial, as configured on the price point. If the payment is due at the initial_billing_at and it fails the subscription will be immediately canceled. See further notes in the section on Delayed Signups. |
| `stored_credential_transaction_id` | `int` | Optional | For European sites subject to PSD2 and using 3D Secure, this can be used to reference a previous transaction for the customer. This will ensure the card will be charged successfully at renewal. |
| `sales_rep_id` | `int` | Optional | - |
| `payment_profile_id` | `int` | Optional | The Payment Profile ID of an existing card or bank account, which belongs to an existing customer to use for payment for this subscription. If the card, bank account, or customer does not exist already, or if you want to use a new (unstored) card or bank account for the subscription, use `payment_profile_attributes` instead to create a new payment profile along with the subscription. (This value is available on an existing subscription via the API as `credit_card` > id or `bank_account` > id) |
| `reference` | `str` | Optional | The reference value (provided by your app) for the subscription itelf. |
| `customer_attributes` | [`CustomerAttributes`](../../doc/models/customer-attributes.md) | Optional | - |
| `payment_profile_attributes` | [`PaymentProfileAttributes`](../../doc/models/payment-profile-attributes.md) | Optional | alias to credit_card_attributes |
| `credit_card_attributes` | [`PaymentProfileAttributes`](../../doc/models/payment-profile-attributes.md) | Optional | Credit Card data to create a new Subscription. Interchangeable with `payment_profile_attributes` property. |
| `bank_account_attributes` | [`BankAccountAttributes`](../../doc/models/bank-account-attributes.md) | Optional | - |
| `components` | [`List[CreateSubscriptionComponent]`](../../doc/models/create-subscription-component.md) | Optional | (Optional) An array of component ids and quantities to be added to the subscription. See [Components](https://maxio-chargify.zendesk.com/hc/en-us/articles/5405020625677) for more information. |
| `calendar_billing` | [`CalendarBilling`](../../doc/models/calendar-billing.md) | Optional | (Optional). Cannot be used when also specifying next_billing_at |
| `metafields` | `Dict[str, str]` | Optional | (Optional) A set of key/value pairs representing custom fields and their values. Metafields will be created “on-the-fly” in your site for a given key, if they have not been created yet. |
| `customer_reference` | `str` | Optional | The reference value (provided by your app) of an existing customer within Chargify. Required, unless a `customer_id` or a set of `customer_attributes` is given. |
| `group` | [`GroupSettings`](../../doc/models/group-settings.md) | Optional | - |
| `ref` | `str` | Optional | A valid referral code. (optional, see [Referrals](https://maxio-chargify.zendesk.com/hc/en-us/articles/5405420204045-Referrals-Reference#how-to-obtain-referral-codes) for more details). If supplied, must be valid, or else subscription creation will fail. |
| `cancellation_message` | `str` | Optional | (Optional) Can be used when canceling a subscription (via the HTTP DELETE method) to make a note about the reason for cancellation. |
| `cancellation_method` | `str` | Optional | (Optional) Can be used when canceling a subscription (via the HTTP DELETE method) to make a note about how the subscription was canceled. |
| `currency` | `str` | Optional | (Optional) If Multi-Currency is enabled and the currency is configured in Chargify, pass it at signup to create a subscription on a non-default currency. Note that you cannot update the currency of an existing subscription. |
| `expires_at` | `datetime` | Optional | Timestamp giving the expiration date of this subscription (if any). You may manually change the expiration date at any point during a subscription period. |
| `expiration_tracks_next_billing_change` | `str` | Optional | (Optional, default false) When set to true, and when next_billing_at is present, if the subscription expires, the expires_at will be shifted by the same amount of time as the difference between the old and new “next billing” dates. |
| `agreement_terms` | `str` | Optional | (Optional) The ACH authorization agreement terms. If enabled, an email will be sent to the customer with a copy of the terms. |
| `authorizer_first_name` | `str` | Optional | (Optional) The first name of the person authorizing the ACH agreement. |
| `authorizer_last_name` | `str` | Optional | (Optional) The last name of the person authorizing the ACH agreement. |
| `calendar_billing_first_charge` | `str` | Optional | (Optional) One of “prorated” (the default – the prorated product price will be charged immediately), “immediate” (the full product price will be charged immediately), or “delayed” (the full product price will be charged with the first scheduled renewal). |
| `reason_code` | `str` | Optional | (Optional) Can be used when canceling a subscription (via the HTTP DELETE method) to indicate why a subscription was canceled. |
| `product_change_delayed` | `bool` | Optional | (Optional, used only for Delayed Product Change When set to true, indicates that a changed value for product_handle should schedule the product change to the next subscription renewal. |
| `offer_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `prepaid_configuration` | [`UpsertPrepaidConfiguration`](../../doc/models/upsert-prepaid-configuration.md) | Optional | - |
| `previous_billing_at` | `datetime` | Optional | Providing a previous_billing_at that is in the past will set the current_period_starts_at when the subscription is created. It will also set activated_at if not explicitly passed during the subscription import. Can only be used if next_billing_at is also passed. Using this option will allow you to set the period start for the subscription so mid period component allocations have the correct prorated amount. |
| `import_mrr` | `bool` | Optional | Setting this attribute to true will cause the subscription's MRR to be added to your MRR analytics immediately. For this value to be honored, a next_billing_at must be present and set to a future date. This key/value will not be returned in the subscription response body. |
| `canceled_at` | `str` | Optional | - |
| `activated_at` | `datetime` | Optional | - |
| `agreement_acceptance` | [`AgreementAcceptance`](../../doc/models/agreement-acceptance.md) | Optional | Required when creating a subscription with Maxio Payments. |
| `ach_agreement` | [`ACHAgreement`](../../doc/models/ach-agreement.md) | Optional | (Optional) If passed, the proof of the authorized ACH agreement terms will be persisted. |
| `dunning_communication_delay_enabled` | `bool` | Optional | Enable Communication Delay feature, making sure no communication (email or SMS) is sent to the Customer between 9PM and 8AM in time zone set by the `dunning_communication_delay_time_zone` attribute.<br>**Default**: `False` |
| `dunning_communication_delay_time_zone` | `str` | Optional | Time zone for the Dunning Communication Delay feature. |
| `skip_billing_manifest_taxes` | `bool` | Optional | Valid only for the Subscription Preview endpoint. When set to `true` it skips calculating taxes for the current and next billing manifests.<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "payment_collection_method": "automatic",
  "metafields": {
    "custom_field_name_1": "custom_field_value_1",
    "custom_field_name_2": "custom_field_value_2"
  },
  "dunning_communication_delay_enabled": false,
  "dunning_communication_delay_time_zone": "\"Eastern Time (US & Canada)\"",
  "skip_billing_manifest_taxes": false,
  "product_handle": "product_handle6",
  "product_id": 212,
  "product_price_point_handle": "product_price_point_handle0",
  "product_price_point_id": 136,
  "custom_price": {
    "name": "name4",
    "handle": "handle0",
    "price_in_cents": "String3",
    "interval": "String3",
    "interval_unit": "day",
    "trial_price_in_cents": "String3",
    "trial_interval": "String5",
    "trial_interval_unit": "day"
  }
}
```

