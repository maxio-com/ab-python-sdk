
# Create Product Currency Prices Request

## Structure

`CreateProductCurrencyPricesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_prices` | [`List[CreateProductCurrencyPrice]`](../../doc/models/create-product-currency-price.md) | Required | - |

## Example

```python
from advancedbilling.models.create_product_currency_price import CreateProductCurrencyPrice
from advancedbilling.models.create_product_currency_prices_request import CreateProductCurrencyPricesRequest
from advancedbilling.models.currency_price_role import CurrencyPriceRole

create_product_currency_prices_request = CreateProductCurrencyPricesRequest(
    currency_prices=[
        CreateProductCurrencyPrice(
            currency='currency8',
            price=78,
            role=CurrencyPriceRole.INITIAL
        )
    ]
)
```

