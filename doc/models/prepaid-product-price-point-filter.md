
# Prepaid Product Price Point Filter

## Structure

`PrepaidProductPricePointFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_price_point_id` | `str` | Required, Constant | Passed as a parameter to list methods to return only non null values.<br><br>**Value**: `"not_null"` |

## Example

```python
from advancedbilling.models.prepaid_product_price_point_filter import PrepaidProductPricePointFilter

prepaid_product_price_point_filter = PrepaidProductPricePointFilter()
```

