
# Credit Card Attributes

## Structure

`CreditCardAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_number` | `str` | Optional | - |
| `expiration_month` | `str` | Optional | - |
| `expiration_year` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.credit_card_attributes import CreditCardAttributes

credit_card_attributes = CreditCardAttributes(
    full_number='full_number2',
    expiration_month='expiration_month6',
    expiration_year='expiration_year2'
)
```

