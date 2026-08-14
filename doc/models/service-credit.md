
# Service Credit

## Structure

`ServiceCredit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `amount_in_cents` | `int` | Optional | The amount in cents of the entry |
| `ending_balance_in_cents` | `int` | Optional | The new balance for the credit account |
| `entry_type` | [`ServiceCreditType`](../../doc/models/service-credit-type.md) | Optional | The type of entry |
| `memo` | `str` | Optional | The memo attached to the entry |

## Example

```python
from advancedbilling.models.service_credit import ServiceCredit
from advancedbilling.models.service_credit_type import ServiceCreditType

service_credit = ServiceCredit(
    id=38,
    amount_in_cents=124,
    ending_balance_in_cents=164,
    entry_type=ServiceCreditType.CREDIT,
    memo='memo0'
)
```

