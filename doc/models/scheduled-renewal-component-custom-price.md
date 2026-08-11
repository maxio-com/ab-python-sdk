
# Scheduled Renewal Component Custom Price

Custom pricing for a component within a scheduled renewal.

## Structure

`ScheduledRenewalComponentCustomPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_included` | `bool` | Optional | Whether or not the price point includes tax |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Required | Omit for On/Off components. |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Required | On/off components only need one price bracket starting at 1. |

## Example

```python
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.scheduled_renewal_component_custom_price import ScheduledRenewalComponentCustomPrice

scheduled_renewal_component_custom_price = ScheduledRenewalComponentCustomPrice(
    pricing_scheme=PricingScheme.PER_UNIT,
    prices=[
        Price(
            starting_quantity=242,
            unit_price=23.26,
            ending_quantity=40
        )
    ],
    tax_included=False
)
```

