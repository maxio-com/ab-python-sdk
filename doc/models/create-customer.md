
# Create Customer

## Structure

`CreateCustomer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | - |
| `last_name` | `str` | Required | - |
| `email` | `str` | Required | - |
| `cc_emails` | `str` | Optional | - |
| `organization` | `str` | Optional | - |
| `reference` | `str` | Optional | - |
| `address` | `str` | Optional | - |
| `address_2` | `str` | Optional | - |
| `city` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `zip` | `str` | Optional | - |
| `country` | `str` | Optional | - |
| `phone` | `str` | Optional | - |
| `locale` | `str` | Optional | Set a specific language on a customer record. |
| `vat_number` | `str` | Optional | - |
| `tax_exempt` | `bool` | Optional | - |
| `surcharging` | `bool` | Optional | Whether surcharging is enabled for the customer. Defaults to `true` when omitted. Only applied on sites where surcharging control is enabled. |
| `tax_exempt_reason` | `str` | Optional | - |
| `parent_id` | `int` | Optional | The parent ID in Chargify if applicable. Parent is another Customer object. |
| `salesforce_id` | `str` | Optional | The Salesforce ID of the customer |
| `branding_theme_id` | `int` | Optional | The ID of the Branding Theme assigned to this customer as the customer's default Branding Theme. This customer-level Branding Theme is used when a subscription does not have its own subscription-level Branding Theme. Available only when Branding Themes are enabled for the site. |

## Example

```python
from advancedbilling.models.create_customer import CreateCustomer

create_customer = CreateCustomer(
    first_name='first_name0',
    last_name='last_name8',
    email='email6',
    cc_emails='cc_emails0',
    organization='organization6',
    reference='reference4',
    address='address6',
    address_2='address_24'
)
```

