
# Product Response

## Structure

`ProductResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product` | [`Product`](../../doc/models/product.md) | Required | - |

## Example

```python
from advancedbilling.models.product import Product
from advancedbilling.models.product_response import ProductResponse

product_response = ProductResponse(
    product=Product(
        id=134,
        name='name0',
        handle='handle6',
        description='description0',
        accounting_code='accounting_code6'
    )
)
```

