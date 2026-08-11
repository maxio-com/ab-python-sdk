
# Subscription Group Prepayment Response

## Structure

`SubscriptionGroupPrepaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `amount_in_cents` | `int` | Optional | The amount in cents of the entry. |
| `ending_balance_in_cents` | `int` | Optional | The ending balance in cents of the account. |
| `entry_type` | [`ServiceCreditType`](../../doc/models/service-credit-type.md) | Optional | The type of entry |
| `memo` | `str` | Optional | A memo attached to the entry. |

## Example

```python
from advancedbilling.models.service_credit_type import ServiceCreditType
from advancedbilling.models.subscription_group_prepayment_response import SubscriptionGroupPrepaymentResponse

subscription_group_prepayment_response = SubscriptionGroupPrepaymentResponse(
    id=28,
    amount_in_cents=114,
    ending_balance_in_cents=154,
    entry_type=ServiceCreditType.CREDIT,
    memo='memo2'
)
```

