
# Service Credit 1

## Structure

`ServiceCredit1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `amount_in_cents` | `int` | Optional | The amount in cents of the entry |
| `ending_balance_in_cents` | `int` | Optional | The new balance for the credit account |
| `entry_type` | [`ServiceCreditType`](../../doc/models/service-credit-type.md) | Optional | The type of entry |
| `memo` | `str` | Optional | The memo attached to the entry |
| `invoice_uid` | `str` | Optional | The invoice uid associated with the entry. Only present for debit entries. |
| `remaining_balance_in_cents` | `int` | Optional | The remaining balance for the entry |
| `created_at` | `datetime` | Optional | The date and time the entry was created |

## Example

```python
from advancedbilling.models.service_credit_1 import ServiceCredit1
from advancedbilling.models.service_credit_type import ServiceCreditType

service_credit_1 = ServiceCredit1(
    id=40,
    amount_in_cents=126,
    ending_balance_in_cents=166,
    entry_type=ServiceCreditType.CREDIT,
    memo='memo2'
)
```

