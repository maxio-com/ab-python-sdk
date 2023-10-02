
# Create or Update Product

## Structure

`CreateOrUpdateProduct`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `handle` | `str` | Optional | - |
| `description` | `str` | Required | - |
| `accounting_code` | `str` | Optional | - |
| `require_credit_card` | `bool` | Optional | - |
| `price_in_cents` | `int` | Required | - |
| `interval` | `int` | Required | - |
| `interval_unit` | `str` | Required | - |
| `auto_create_signup_page` | `bool` | Optional | - |
| `tax_code` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name8",
  "handle": "handle4",
  "description": "description8",
  "accounting_code": "accounting_code4",
  "require_credit_card": false,
  "price_in_cents": 190,
  "interval": 174,
  "interval_unit": "interval_unit8",
  "auto_create_signup_page": false,
  "tax_code": "tax_code6"
}
```

