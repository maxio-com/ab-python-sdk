
# Subscription Group Customer

## Structure

`SubscriptionGroupCustomer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `organization` | `str` | Optional | - |
| `email` | `str` | Optional | - |
| `reference` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.subscription_group_customer import SubscriptionGroupCustomer

subscription_group_customer = SubscriptionGroupCustomer(
    first_name='first_name2',
    last_name='last_name0',
    organization='organization4',
    email='email4',
    reference='reference2'
)
```

