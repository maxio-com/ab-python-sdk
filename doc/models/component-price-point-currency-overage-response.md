
# Component Price Point Currency Overage Response

## Structure

`ComponentPricePointCurrencyOverageResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | [`CurrencyOveragePrices`](../../doc/models/currency-overage-prices.md) | Required | Extends a component price point with currency overage prices. |

## Example

```python
from advancedbilling.models.component_price_point_currency_overage_response import ComponentPricePointCurrencyOverageResponse
from advancedbilling.models.currency_overage_prices import CurrencyOveragePrices
from advancedbilling.models.price_point_type import PricePointType
from advancedbilling.models.pricing_scheme import PricingScheme

component_price_point_currency_overage_response = ComponentPricePointCurrencyOverageResponse(
    price_point=CurrencyOveragePrices(
        id=248,
        mtype=PricePointType.DEFAULT,
        default=False,
        name='name0',
        pricing_scheme=PricingScheme.PER_UNIT
    )
)
```

