
# Customer Response

## Structure

`CustomerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`Customer`](../../doc/models/customer.md) | Required | - |

## Example

```python
from advancedbilling.models.customer import Customer
from advancedbilling.models.customer_response import CustomerResponse

customer_response = CustomerResponse(
    customer=Customer(
        first_name='first_name0',
        last_name='last_name8',
        email='email6',
        cc_emails='cc_emails0',
        organization='organization6'
    )
)
```

