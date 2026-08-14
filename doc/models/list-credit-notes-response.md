
# List Credit Notes Response

## Structure

`ListCreditNotesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credit_notes` | [`List[CreditNote]`](../../doc/models/credit-note.md) | Required | - |

## Example

```python
from advancedbilling.models.credit_note import CreditNote
from advancedbilling.models.list_credit_notes_response import ListCreditNotesResponse

list_credit_notes_response = ListCreditNotesResponse(
    credit_notes=[
        CreditNote(
            uid='uid2',
            site_id=112,
            customer_id=224,
            subscription_id=40,
            number='number0'
        )
    ]
)
```

