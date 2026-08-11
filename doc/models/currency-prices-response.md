
# Currency Prices Response

## Structure

`CurrencyPricesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_prices` | [`List[CurrencyPrice]`](../../doc/models/currency-price.md) | Required | - |

## Example

```python
from advancedbilling.models.currency_price import CurrencyPrice
from advancedbilling.models.currency_prices_response import CurrencyPricesResponse

currency_prices_response = CurrencyPricesResponse(
    currency_prices=[
        CurrencyPrice(
            id=50,
            currency='currency8',
            price=233.74,
            formatted_price='formatted_price6',
            price_id=116
        )
    ]
)
```

