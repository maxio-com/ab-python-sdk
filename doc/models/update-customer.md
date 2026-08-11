
# Update Customer

## Structure

`UpdateCustomer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `email` | `str` | Optional | - |
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
| `surcharging` | `bool` | Optional | Whether surcharging is enabled for the customer. Only applied on sites where surcharging control is enabled. |
| `tax_exempt_reason` | `str` | Optional | - |
| `parent_id` | `int` | Optional | - |
| `verified` | `bool` | Optional | Is the customer verified to use ACH as a payment method. Available only on the Authorize.Net gateway. |
| `salesforce_id` | `str` | Optional | The Salesforce ID of the customer |
| `branding_theme_id` | `int` | Optional | The ID of the Branding Theme assigned to this customer as the customer's default Branding Theme. This customer-level Branding Theme is used when a subscription does not have its own subscription-level Branding Theme. Available only when Branding Themes are enabled for the site. |

## Example

```python
from advancedbilling.models.update_customer import UpdateCustomer

update_customer = UpdateCustomer(
    first_name='first_name4',
    last_name='last_name2',
    email='email2',
    cc_emails='cc_emails6',
    organization='organization8'
)
```

