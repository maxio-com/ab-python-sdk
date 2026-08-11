
# Prepaid Subscription Balance Changed

## Structure

`PrepaidSubscriptionBalanceChanged`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Required | - |
| `current_account_balance_in_cents` | `int` | Required | - |
| `prepayment_account_balance_in_cents` | `int` | Required | - |
| `current_usage_amount_in_cents` | `int` | Required | - |

## Example

```python
from advancedbilling.models.prepaid_subscription_balance_changed import PrepaidSubscriptionBalanceChanged

prepaid_subscription_balance_changed = PrepaidSubscriptionBalanceChanged(
    reason='reason4',
    current_account_balance_in_cents=24,
    prepayment_account_balance_in_cents=242,
    current_usage_amount_in_cents=16
)
```

