
# Create Currency Prices Request

## Structure

`CreateCurrencyPricesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_prices` | [`List[CreateCurrencyPrice]`](../../doc/models/create-currency-price.md) | Required | - |

## Example

```python
from advancedbilling.models.create_currency_price import CreateCurrencyPrice
from advancedbilling.models.create_currency_prices_request import CreateCurrencyPricesRequest

create_currency_prices_request = CreateCurrencyPricesRequest(
    currency_prices=[
        CreateCurrencyPrice(
            currency='currency8',
            price=233.74,
            price_id=116
        )
    ]
)
```

