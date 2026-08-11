
# Update Currency Price

## Structure

`UpdateCurrencyPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | ID of the currency price record being updated |
| `price` | `float` | Required | New price for the given currency |

## Example

```python
from advancedbilling.models.update_currency_price import UpdateCurrencyPrice

update_currency_price = UpdateCurrencyPrice(
    id=186,
    price=72.26
)
```

