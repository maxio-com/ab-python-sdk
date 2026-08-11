
# Create Product Currency Price

## Structure

`CreateProductCurrencyPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | ISO code for one of the site level currencies. |
| `price` | `int` | Required | Price for the given role. |
| `role` | [`CurrencyPriceRole`](../../doc/models/currency-price-role.md) | Required | Role for the price. |

## Example

```python
from advancedbilling.models.create_product_currency_price import CreateProductCurrencyPrice
from advancedbilling.models.currency_price_role import CurrencyPriceRole

create_product_currency_price = CreateProductCurrencyPrice(
    currency='currency6',
    price=34,
    role=CurrencyPriceRole.BASELINE
)
```

