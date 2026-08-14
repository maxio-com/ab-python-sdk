
# Create Product Family Request

## Structure

`CreateProductFamilyRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_family` | [`CreateProductFamily`](../../doc/models/create-product-family.md) | Required | - |

## Example

```python
from advancedbilling.models.create_product_family import CreateProductFamily
from advancedbilling.models.create_product_family_request import CreateProductFamilyRequest

create_product_family_request = CreateProductFamilyRequest(
    product_family=CreateProductFamily(
        name='name0',
        handle='handle6',
        description='description0',
        surcharging=False
    )
)
```

