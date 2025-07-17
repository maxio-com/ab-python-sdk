
# Tax Configuration

## Structure

`TaxConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kind` | [`TaxConfigurationKind`](../../doc/models/tax-configuration-kind.md) | Optional | **Default**: `'custom'` |
| `destination_address` | [`TaxDestinationAddress`](../../doc/models/tax-destination-address.md) | Optional | - |
| `fully_configured` | `bool` | Optional | Returns `true` when Chargify has been properly configured to charge tax using the specified tax system. More details about taxes: https://maxio.zendesk.com/hc/en-us/articles/24287012608909-Taxes-Overview<br><br>**Default**: `False` |

## Example (as JSON)

```json
{
  "kind": "custom",
  "fully_configured": false,
  "destination_address": "shipping_only"
}
```

