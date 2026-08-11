
# Create Invoice Item

## Structure

`CreateInvoiceItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | - |
| `quantity` | float \| str \| None | Optional | This is a container for one-of cases. |
| `unit_price` | float \| str \| None | Optional | This is a container for one-of cases. |
| `taxable` | `bool` | Optional | Set to true to automatically calculate taxes. Site must be configured to use and calculate taxes. If using AvaTax, a tax_code parameter must also be sent. |
| `tax_code` | `str` | Optional | A string representing the tax code related to the product type. This is especially important when using AvaTax to tax based on locale. This attribute has a max length of 25 characters. |
| `period_range_start` | `str` | Optional | YYYY-MM-DD |
| `period_range_end` | `str` | Optional | YYYY-MM-DD |
| `product_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `component_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `price_point_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `product_price_point_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `description` | `str` | Optional | **Constraints**: *Maximum Length*: `255` |

## Example

```python
from advancedbilling.models.create_invoice_item import CreateInvoiceItem

create_invoice_item = CreateInvoiceItem(
    title='title2',
    quantity=163.26,
    unit_price=146.48,
    taxable=False,
    tax_code='tax_code4'
)
```

