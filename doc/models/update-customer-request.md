
# Update Customer Request

## Structure

`UpdateCustomerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`UpdateCustomer`](../../doc/models/update-customer.md) | Required | - |

## Example

```python
from advancedbilling.models.update_customer import UpdateCustomer
from advancedbilling.models.update_customer_request import UpdateCustomerRequest

update_customer_request = UpdateCustomerRequest(
    customer=UpdateCustomer(
        first_name='first_name0',
        last_name='last_name8',
        email='email6',
        cc_emails='cc_emails0',
        organization='organization6'
    )
)
```

