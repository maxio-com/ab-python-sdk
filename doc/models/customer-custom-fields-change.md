
# Customer Custom Fields Change

## Structure

`CustomerCustomFieldsChange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `before` | [`List[InvoiceCustomField]`](../../doc/models/invoice-custom-field.md) | Required | - |
| `after` | [`List[InvoiceCustomField]`](../../doc/models/invoice-custom-field.md) | Required | - |

## Example

```python
from advancedbilling.models.custom_field_owner import CustomFieldOwner
from advancedbilling.models.customer_custom_fields_change import CustomerCustomFieldsChange
from advancedbilling.models.invoice_custom_field import InvoiceCustomField

customer_custom_fields_change = CustomerCustomFieldsChange(
    before=[
        InvoiceCustomField(
            owner_id=26,
            owner_type=CustomFieldOwner.CUSTOMER,
            name='name0',
            value='value2',
            metadatum_id=26
        )
    ],
    after=[
        InvoiceCustomField(
            owner_id=130,
            owner_type=CustomFieldOwner.CUSTOMER,
            name='name2',
            value='value4',
            metadatum_id=130
        )
    ]
)
```

