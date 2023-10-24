
# Event

## Structure

`Event`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `float` | Required | - |
| `key` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `message` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `subscription_id` | `float` | Required | - |
| `created_at` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `event_specific_data` | [Subscription Product Change](../../doc/models/subscription-product-change.md) \| [Subscription State Change](../../doc/models/subscription-state-change.md) \| [Payment Related Events](../../doc/models/payment-related-events.md) \| [Refund Success](../../doc/models/refund-success.md) \| [Component Allocation Change](../../doc/models/component-allocation-change.md) \| [Metered Usage](../../doc/models/metered-usage.md) \| [Prepaid Usage](../../doc/models/prepaid-usage.md) \| [Dunning Step Reached](../../doc/models/dunning-step-reached.md) \| [Invoice Issued](../../doc/models/invoice-issued.md) \| [Pending Cancellation Change](../../doc/models/pending-cancellation-change.md) \| [Prepaid Subscription Balance Changed](../../doc/models/prepaid-subscription-balance-changed.md) \| [Proforma Invoice Issued](../../doc/models/proforma-invoice-issued.md) \| [Subscription Group Signup Success](../../doc/models/subscription-group-signup-success.md) \| [Subscription Group Signup Failure](../../doc/models/subscription-group-signup-failure.md) \| [Credit Account Balance Changed](../../doc/models/credit-account-balance-changed.md) \| [Prepayment Account Balance Changed](../../doc/models/prepayment-account-balance-changed.md) \| [Payment Collection Method Changed](../../doc/models/payment-collection-method-changed.md) \| [Item Price Point Changed](../../doc/models/item-price-point-changed.md) \| [Custom Field Value Change](../../doc/models/custom-field-value-change.md) | Required | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "id": 159.12,
  "key": "key2",
  "message": "message8",
  "subscription_id": 185.82,
  "created_at": "created_at0",
  "event_specific_data": {
    "previous_unit_balance": null,
    "previous_overage_unit_balance": null,
    "new_unit_balance": null,
    "new_overage_unit_balance": null,
    "usage_quantity": null,
    "overage_usage_quantity": null,
    "component_id": null,
    "component_handle": null,
    "memo": null,
    "allocation_details": [
      null
    ],
    "previous_product_id": 126,
    "new_product_id": 12
  }
}
```

