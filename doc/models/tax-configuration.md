
# Tax Configuration

## Structure

`TaxConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kind` | [`TaxConfigurationKind`](../../doc/models/tax-configuration-kind.md) | Optional | **Default**: `"custom"` |
| `destination_address` | [`TaxDestinationAddress`](../../doc/models/tax-destination-address.md) | Optional | - |
| `fully_configured` | `bool` | Optional | Returns `true` when Chargify has been properly configured to charge tax using the specified tax system. More details about taxes: https://maxio.zendesk.com/hc/en-us/articles/24287012608909-Taxes-Overview<br><br>**Default**: `False` |

## Example

```python
from advancedbilling.models.tax_configuration import TaxConfiguration
from advancedbilling.models.tax_configuration_kind import TaxConfigurationKind
from advancedbilling.models.tax_destination_address import TaxDestinationAddress

tax_configuration = TaxConfiguration(
    kind=TaxConfigurationKind.CUSTOM,
    destination_address=TaxDestinationAddress.SHIPPING_THEN_BILLING,
    fully_configured=False
)
```

