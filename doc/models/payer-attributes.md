
# Payer Attributes

## Structure

`PayerAttributes`

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
| `locale` | `str` | Optional | - |
| `vat_number` | `str` | Optional | - |
| `tax_exempt` | `bool` | Optional | - |
| `tax_exempt_reason` | `str` | Optional | - |
| `metafields` | `Dict[str, str]` | Optional | (Optional) A set of key/value pairs representing custom fields and their values. Metafields will be created “on-the-fly” in your site for a given key, if they have not been created yet. |

## Example (as JSON)

```json
{
  "metafields": {
    "custom_field_name_1": "custom_field_value_1",
    "custom_field_name_2": "custom_field_value_2"
  },
  "first_name": "first_name4",
  "last_name": "last_name2",
  "email": "email2",
  "cc_emails": "cc_emails4",
  "organization": "organization8"
}
```

