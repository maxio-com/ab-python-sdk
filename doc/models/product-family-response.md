
# Product Family Response

## Structure

`ProductFamilyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_family` | [`ProductFamily`](../../doc/models/product-family.md) | Optional | - |

## Example

```python
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.product_family_response import ProductFamilyResponse

product_family_response = ProductFamilyResponse(
    product_family=ProductFamily(
        id=14,
        name='name0',
        handle='handle6',
        accounting_code='accounting_code6',
        description='description0'
    )
)
```

