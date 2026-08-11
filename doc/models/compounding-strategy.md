
# Compounding Strategy

Applicable only to stackable coupons. For `compound`, Percentage-based discounts will be calculated against the remaining price, after prior discounts have been calculated. For `full-price`, Percentage-based discounts will always be calculated against the original item price, before other discounts are applied.

## Enumeration

`CompoundingStrategy`

## Fields

| Name |
|  --- |
| `COMPOUND` |
| `FULLPRICE` |

## Example

```python
from advancedbilling.models.compounding_strategy import CompoundingStrategy

compounding_strategy = CompoundingStrategy.COMPOUND
```

