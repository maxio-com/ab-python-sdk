
# Invoice Custom Field

## Structure

`InvoiceCustomField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `owner_id` | `int` | Optional | - |
| `owner_type` | [`CustomFieldOwner`](../../doc/models/custom-field-owner.md) | Optional | - |
| `name` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `value` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `metadatum_id` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.custom_field_owner import CustomFieldOwner
from advancedbilling.models.invoice_custom_field import InvoiceCustomField

invoice_custom_field = InvoiceCustomField(
    owner_id=238,
    owner_type=CustomFieldOwner.CUSTOMER,
    name='name4',
    value='value6',
    metadatum_id=238
)
```

