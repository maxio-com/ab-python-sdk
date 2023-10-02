
# Create Invoice Item

## Structure

`CreateInvoiceItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | - |
| `quantity` | float \| str \| None | Optional | This is a container for one-of cases. |
| `unit_price` | float \| str \| None | Optional | This is a container for one-of cases. |
| `taxable` | `bool` | Optional | Set to true to automatically calculate taxes. Site must be configured to use and calculate taxes.<br><br>If using Avalara, a tax_code parameter must also be sent. |
| `tax_code` | `str` | Optional | - |
| `period_range_start` | `str` | Optional | YYYY-MM-DD |
| `period_range_end` | `str` | Optional | YYYY-MM-DD |
| `product_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `component_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `price_point_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `product_price_point_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `description` | `str` | Optional | **Constraints**: *Maximum Length*: `255` |

## Example (as JSON)

```json
{
  "title": "title2",
  "quantity": 154.86,
  "unit_price": 138.08,
  "taxable": false,
  "tax_code": "tax_code4"
}
```

