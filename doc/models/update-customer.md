
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
| `vat_country` | `str` | Optional | The two-letter ISO 3166-1 country code that qualifies the customer's tax ID. Required when `entity_identifier_kind` is `vat_eu` or `national_tax`, and used to derive the kind when only the legacy `vat_number` is sent. |
| `entity_identifier_kind` | [`EntityIdentifierKind`](../../doc/models/entity-identifier-kind.md) | Optional | The kind of tax or business identifier held by the customer:<br><br>- `vat_eu`: an EU VAT number. Requires `vat_country` to be an EU member state code or `GB`.<br>- `national_tax`: a national tax ID registered outside the EU. Requires `vat_country` to be one of `AL`, `AM`, `AR`, `AU`, `BR`, `CA`, `CH`, `DZ`, `IN`, `MX`, `NO`, `NZ`, or `ZA`.<br>- `company_reg`: a company registration number, such as a French SIREN. No `vat_country` is required.<br>- `gln`: a Global Location Number. The value must be 13 digits.<br>- `duns`: a D-U-N-S Number. The value must be 9 digits.<br>- `lei`: a Legal Entity Identifier. The value must be 20 characters: 18 letters or digits followed by 2 digits.<br><br>A customer holds one identifier at a time. Saving an identifier of a different kind replaces the existing one. |
| `entity_identifier_value` | `str` | Optional | The customer's tax or business identifier, sent together with `entity_identifier_kind`. Advanced Billing trims surrounding whitespace and stores the value in uppercase. |
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

