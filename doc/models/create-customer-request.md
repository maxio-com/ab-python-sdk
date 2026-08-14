
# Create Customer Request

## Structure

`CreateCustomerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`CreateCustomer`](../../doc/models/create-customer.md) | Required | - |

## Example

```python
from advancedbilling.models.create_customer import CreateCustomer
from advancedbilling.models.create_customer_request import CreateCustomerRequest

create_customer_request = CreateCustomerRequest(
    customer=CreateCustomer(
        first_name='first_name0',
        last_name='last_name8',
        email='email6',
        cc_emails='cc_emails0',
        organization='organization6',
        reference='reference4',
        address='address6',
        address_2='address_24'
    )
)
```

