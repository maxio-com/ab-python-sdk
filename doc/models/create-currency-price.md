
# Create Currency Price

## Structure

`CreateCurrencyPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | ISO code for a currency defined on the site level |
| `price` | `float` | Optional | Price for the price level in this currency |
| `price_id` | `int` | Optional | ID of the price that this corresponds with |

## Example

```python
from advancedbilling.models.create_currency_price import CreateCurrencyPrice

create_currency_price = CreateCurrencyPrice(
    currency='currency8',
    price=24.44,
    price_id=178
)
```

