
# Component Currency Prices Response

## Structure

`ComponentCurrencyPricesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_prices` | [`List[ComponentCurrencyPrice]`](../../doc/models/component-currency-price.md) | Required | - |

## Example

```python
from advancedbilling.models.component_currency_price import ComponentCurrencyPrice
from advancedbilling.models.component_currency_prices_response import ComponentCurrencyPricesResponse

component_currency_prices_response = ComponentCurrencyPricesResponse(
    currency_prices=[
        ComponentCurrencyPrice(
            id=50,
            currency='currency8',
            price='price4',
            formatted_price='formatted_price6',
            price_id=116
        )
    ]
)
```

