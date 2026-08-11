
# Customer Changes Preview Response

## Structure

`CustomerChangesPreviewResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `changes` | [`CustomerChange`](../../doc/models/customer-change.md) | Required | - |

## Example

```python
from advancedbilling.models.address_change import AddressChange
from advancedbilling.models.custom_field_owner import CustomFieldOwner
from advancedbilling.models.customer_change import CustomerChange
from advancedbilling.models.customer_changes_preview_response import CustomerChangesPreviewResponse
from advancedbilling.models.customer_custom_fields_change import CustomerCustomFieldsChange
from advancedbilling.models.customer_payer_change import CustomerPayerChange
from advancedbilling.models.invoice_address import InvoiceAddress
from advancedbilling.models.invoice_custom_field import InvoiceCustomField
from advancedbilling.models.invoice_payer_change import InvoicePayerChange

customer_changes_preview_response = CustomerChangesPreviewResponse(
    changes=CustomerChange(
        payer=CustomerPayerChange(
            before=InvoicePayerChange(
                first_name='first_name0',
                last_name='last_name8',
                organization='organization4',
                email='email6'
            ),
            after=InvoicePayerChange(
                first_name='first_name2',
                last_name='last_name0',
                organization='organization4',
                email='email4'
            )
        ),
        shipping_address=AddressChange(
            before=InvoiceAddress(
                street='street0',
                line_2='line24',
                city='city0',
                state='state6',
                zip='zip4'
            ),
            after=InvoiceAddress(
                street='street2',
                line_2='line26',
                city='city8',
                state='state2',
                zip='zip4'
            )
        ),
        billing_address=AddressChange(
            before=InvoiceAddress(
                street='street0',
                line_2='line24',
                city='city0',
                state='state6',
                zip='zip4'
            ),
            after=InvoiceAddress(
                street='street2',
                line_2='line26',
                city='city8',
                state='state2',
                zip='zip4'
            )
        ),
        custom_fields=CustomerCustomFieldsChange(
            before=[
                InvoiceCustomField(
                    owner_id=26,
                    owner_type=CustomFieldOwner.CUSTOMER,
                    name='name0',
                    value='value2',
                    metadatum_id=26
                ),
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
                ),
                InvoiceCustomField(
                    owner_id=130,
                    owner_type=CustomFieldOwner.CUSTOMER,
                    name='name2',
                    value='value4',
                    metadatum_id=130
                ),
                InvoiceCustomField(
                    owner_id=130,
                    owner_type=CustomFieldOwner.CUSTOMER,
                    name='name2',
                    value='value4',
                    metadatum_id=130
                )
            ]
        )
    )
)
```

