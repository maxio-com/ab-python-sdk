
# Update Currency Prices Request

## Structure

`UpdateCurrencyPricesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_prices` | [`List[UpdateCurrencyPrice]`](../../doc/models/update-currency-price.md) | Required | - |

## Example

```python
from advancedbilling.models.update_currency_price import UpdateCurrencyPrice
from advancedbilling.models.update_currency_prices_request import UpdateCurrencyPricesRequest

update_currency_prices_request = UpdateCurrencyPricesRequest(
    currency_prices=[
        UpdateCurrencyPrice(
            id=50,
            price=233.74
        )
    ]
)
```

