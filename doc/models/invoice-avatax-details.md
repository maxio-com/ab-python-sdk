
# Invoice Avatax Details

## Structure

`InvoiceAvataxDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `status` | `str` | Optional | - |
| `document_code` | `str` | Optional | - |
| `commit_date` | `datetime` | Optional | - |
| `modify_date` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.invoice_avatax_details import InvoiceAvataxDetails

invoice_avatax_details = InvoiceAvataxDetails(
    id=18,
    status='status2',
    document_code='document_code0',
    commit_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    modify_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

