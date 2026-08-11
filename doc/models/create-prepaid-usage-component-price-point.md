
# Create Prepaid Usage Component Price Point

## Structure

`CreatePrepaidUsageComponentPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `handle` | `str` | Optional | - |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Required | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Required | - |
| `overage_pricing` | [`OveragePricing`](../../doc/models/overage-pricing.md) | Required | - |
| `use_site_exchange_rate` | `bool` | Optional | Whether to use the site level exchange rate or define your own prices for each currency if you have multiple currencies defined on the site.<br><br>**Default**: `True` |
| `rollover_prepaid_remainder` | `bool` | Optional | (only for prepaid usage components) Boolean which controls whether or not remaining units should be rolled over to the next period. |
| `renew_prepaid_allocation` | `bool` | Optional | (only for prepaid usage components) Boolean which controls whether or not the allocated quantity should be renewed at the beginning of each period. |
| `expiration_interval` | `float` | Optional | (only for prepaid usage components where rollover_prepaid_remainder is true) The number of `expiration_interval_unit`s after which rollover amounts should expire. |
| `expiration_interval_unit` | [`ExpirationIntervalUnit`](../../doc/models/expiration-interval-unit.md) | Optional | (only for prepaid usage components where rollover_prepaid_remainder is true) A string representing the expiration interval unit for this component, either month or day. |

## Example

```python
from advancedbilling.models.create_prepaid_usage_component_price_point import CreatePrepaidUsageComponentPricePoint
from advancedbilling.models.overage_pricing import OveragePricing
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme

create_prepaid_usage_component_price_point = CreatePrepaidUsageComponentPricePoint(
    name='name6',
    pricing_scheme=PricingScheme.PER_UNIT,
    prices=[
        Price(
            starting_quantity=242,
            unit_price=23.26,
            ending_quantity=40
        )
    ],
    overage_pricing=OveragePricing(
        pricing_scheme=PricingScheme.STAIRSTEP,
        prices=[
            Price(
                starting_quantity=242,
                unit_price=23.26,
                ending_quantity=40
            )
        ]
    ),
    handle='handle2',
    use_site_exchange_rate=True,
    rollover_prepaid_remainder=False,
    renew_prepaid_allocation=False,
    expiration_interval=117.54
)
```

