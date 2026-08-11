
# Void Remainder Event Data

Example schema for an `void_remainder` event

## Structure

`VoidRemainderEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credit_note_attributes` | [`CreditNote`](../../doc/models/credit-note.md) | Required | - |
| `memo` | `str` | Required | The memo provided during invoice remainder voiding. |
| `applied_amount` | `str` | Required | The amount of the void. |
| `transaction_time` | `datetime` | Required | The time the refund was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" |

## Example

```python
import dateutil.parser

from advancedbilling.models.credit_note import CreditNote
from advancedbilling.models.void_remainder_event_data import VoidRemainderEventData

void_remainder_event_data = VoidRemainderEventData(
    credit_note_attributes=CreditNote(
        uid='uid2',
        site_id=72,
        customer_id=184,
        subscription_id=0,
        number='number0'
    ),
    memo='memo0',
    applied_amount='applied_amount2',
    transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

