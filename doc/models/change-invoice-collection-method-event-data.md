
# Change Invoice Collection Method Event Data

Example schema for an `change_invoice_collection_method` event

## Structure

`ChangeInvoiceCollectionMethodEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_collection_method` | `str` | Required | The previous collection method of the invoice. |
| `to_collection_method` | `str` | Required | The new collection method of the invoice. |

## Example

```python
from advancedbilling.models.change_invoice_collection_method_event_data import ChangeInvoiceCollectionMethodEventData

change_invoice_collection_method_event_data = ChangeInvoiceCollectionMethodEventData(
    from_collection_method='from_collection_method2',
    to_collection_method='to_collection_method0'
)
```

