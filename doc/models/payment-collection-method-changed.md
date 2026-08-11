
# Payment Collection Method Changed

## Structure

`PaymentCollectionMethodChanged`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `previous_value` | `str` | Required | - |
| `current_value` | `str` | Required | - |

## Example

```python
from advancedbilling.models.payment_collection_method_changed import PaymentCollectionMethodChanged

payment_collection_method_changed = PaymentCollectionMethodChanged(
    previous_value='previous_value2',
    current_value='current_value0'
)
```

