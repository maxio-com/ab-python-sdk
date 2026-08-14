
# Tax Destination Address

## Enumeration

`TaxDestinationAddress`

## Fields

| Name |
|  --- |
| `SHIPPING_THEN_BILLING` |
| `BILLING_THEN_SHIPPING` |
| `SHIPPING_ONLY` |
| `BILLING_ONLY` |

## Example

```python
from advancedbilling.models.tax_destination_address import TaxDestinationAddress

tax_destination_address = TaxDestinationAddress.SHIPPING_ONLY
```

