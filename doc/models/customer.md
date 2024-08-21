
# Customer

## Structure

`Customer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | The first name of the customer |
| `last_name` | `str` | Optional | The last name of the customer |
| `email` | `str` | Optional | The email address of the customer |
| `cc_emails` | `str` | Optional | A comma-separated list of emails that should be cc’d on all customer communications (i.e. “joe@example.com, sue@example.com”) |
| `organization` | `str` | Optional | The organization of the customer. If no value, `null` or empty string is provided, `organization` will be populated with the customer's first and last name, separated with a space. |
| `reference` | `str` | Optional | The unique identifier used within your own application for this customer |
| `id` | `int` | Optional | The customer ID in Chargify |
| `created_at` | `datetime` | Optional | The timestamp in which the customer object was created in Chargify |
| `updated_at` | `datetime` | Optional | The timestamp in which the customer object was last edited |
| `address` | `str` | Optional | The customer’s shipping street address (i.e. “123 Main St.”) |
| `address_2` | `str` | Optional | Second line of the customer’s shipping address i.e. “Apt. 100” |
| `city` | `str` | Optional | The customer’s shipping address city (i.e. “Boston”) |
| `state` | `str` | Optional | The customer’s shipping address state (i.e. “MA”) |
| `state_name` | `str` | Optional | The customer's full name of state |
| `zip` | `str` | Optional | The customer’s shipping address zip code (i.e. “12345”) |
| `country` | `str` | Optional | The customer shipping address country |
| `country_name` | `str` | Optional | The customer's full name of country |
| `phone` | `str` | Optional | The phone number of the customer |
| `verified` | `bool` | Optional | Is the customer verified to use ACH as a payment method. Available only on Authorize.Net gateway |
| `portal_customer_created_at` | `datetime` | Optional | The timestamp of when the Billing Portal entry was created at for the customer |
| `portal_invite_last_sent_at` | `datetime` | Optional | The timestamp of when the Billing Portal invite was last sent at |
| `portal_invite_last_accepted_at` | `datetime` | Optional | The timestamp of when the Billing Portal invite was last accepted |
| `tax_exempt` | `bool` | Optional | The tax exempt status for the customer. Acceptable values are true or 1 for true and false or 0 for false. |
| `vat_number` | `str` | Optional | The VAT business identification number for the customer. This number is used to determine VAT tax opt out rules. It is not validated when added or updated on a customer record. Instead, it is validated via VIES before calculating taxes. Only valid business identification numbers will allow for VAT opt out. |
| `parent_id` | `int` | Optional | The parent ID in Chargify if applicable. Parent is another Customer object. |
| `locale` | `str` | Optional | The locale for the customer to identify language-region |
| `default_subscription_group_uid` | `str` | Optional | - |
| `salesforce_id` | `str` | Optional | The Salesforce ID for the customer |

## Example (as JSON)

```json
{
  "first_name": "first_name8",
  "last_name": "last_name6",
  "email": "email8",
  "cc_emails": "cc_emails2",
  "organization": "organization8"
}
```

