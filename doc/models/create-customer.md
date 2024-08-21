
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
| `tax_exempt_reason` | `str` | Optional | - |
| `parent_id` | `int` | Optional | The parent ID in Chargify if applicable. Parent is another Customer object. |
| `salesforce_id` | `str` | Optional | The Salesforce ID of the customer |

## Example (as JSON)

```json
{
  "first_name": "first_name8",
  "last_name": "last_name6",
  "email": "email8",
  "cc_emails": "cc_emails8",
  "organization": "organization2",
  "reference": "reference4",
  "address": "address4",
  "address_2": "address_22"
}
```

