
# Void Invoice

## Structure

`VoidInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Required | **Constraints**: *Minimum Length*: `1` |

## Example

```python
from advancedbilling.models.void_invoice import VoidInvoice

void_invoice = VoidInvoice(
    reason='reason6'
)
```

