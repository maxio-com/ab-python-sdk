
# Update Invoice Item

A line item change for a draft ad hoc invoice. Supports the same attributes as line items on invoice creation, plus `uid` and `_destroy` for updating or removing existing line items.

## Structure

`UpdateInvoiceItem`

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
| `uid` | `str` | Optional | Unique identifier of an existing line item on the invoice. When provided, the matching line item is updated with the submitted attributes. When omitted, a new line item is added to the invoice. |
| `destroy` | `bool` | Optional | Set to `true` together with `uid` to remove the matching line item from the invoice. Line items not referenced in the request remain unchanged. |

## Example

```python
from advancedbilling.models.update_invoice_item import UpdateInvoiceItem

update_invoice_item = UpdateInvoiceItem(
    title='title4',
    quantity=29.28,
    unit_price=12.5,
    taxable=False,
    tax_code='tax_code6'
)
```

