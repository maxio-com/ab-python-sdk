
# Update Subscription

## Structure

`UpdateSubscription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credit_card_attributes` | [`CreditCardAttributes`](../../doc/models/credit-card-attributes.md) | Optional | - |
| `product_handle` | `str` | Optional | Set to the handle of a different product to change the subscription's product |
| `product_id` | `int` | Optional | Set to the id of a different product to change the subscription's product |
| `product_change_delayed` | `bool` | Optional | - |
| `next_product_id` | `str` | Optional | Set to an empty string to cancel a delayed product change. |
| `next_product_price_point_id` | `str` | Optional | - |
| `snap_day` | [SnapDay](../../doc/models/snap-day.md) \| int \| None | Optional | This is a container for one-of cases. |
| `next_billing_at` | `datetime` | Optional | - |
| `payment_collection_method` | `str` | Optional | - |
| `receives_invoice_emails` | `bool` | Optional | - |
| `net_terms` | str \| int \| None | Optional | This is a container for one-of cases. |
| `stored_credential_transaction_id` | `int` | Optional | - |
| `reference` | `str` | Optional | - |
| `custom_price` | [`SubscriptionCustomPrice`](../../doc/models/subscription-custom-price.md) | Optional | (Optional) Used in place of `product_price_point_id` to define a custom price point unique to the subscription |
| `components` | [`List[UpdateSubscriptionComponent]`](../../doc/models/update-subscription-component.md) | Optional | (Optional) An array of component ids and custom prices to be added to the subscription. |
| `dunning_communication_delay_enabled` | `bool` | Optional | Enable Communication Delay feature, making sure no communication (email or SMS) is sent to the Customer between 9PM and 8AM in time zone set by the `dunning_communication_delay_time_zone` attribute. |
| `dunning_communication_delay_time_zone` | `str` | Optional | Time zone for the Dunning Communication Delay feature. |
| `product_price_point_id` | `int` | Optional | Set to change the current product's price point. |
| `product_price_point_handle` | `str` | Optional | Set to change the current product's price point. |

## Example (as JSON)

```json
{
  "dunning_communication_delay_time_zone": "\"Eastern Time (US & Canada)\"",
  "credit_card_attributes": {
    "full_number": "full_number2",
    "expiration_month": "expiration_month6",
    "expiration_year": "expiration_year2"
  },
  "product_handle": "product_handle2",
  "product_id": 114,
  "product_change_delayed": false,
  "next_product_id": "next_product_id8"
}
```

