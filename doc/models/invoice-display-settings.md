
# Invoice Display Settings

## Structure

`InvoiceDisplaySettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hide_zero_subtotal_lines` | `bool` | Optional | - |
| `include_discounts_on_lines` | `bool` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_display_settings import InvoiceDisplaySettings

invoice_display_settings = InvoiceDisplaySettings(
    hide_zero_subtotal_lines=False,
    include_discounts_on_lines=False
)
```

