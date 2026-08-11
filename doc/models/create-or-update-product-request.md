
# Create or Update Product Request

## Structure

`CreateOrUpdateProductRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product` | [`CreateOrUpdateProduct`](../../doc/models/create-or-update-product.md) | Required | - |

## Example

```python
from advancedbilling.models.create_or_update_product import CreateOrUpdateProduct
from advancedbilling.models.create_or_update_product_request import CreateOrUpdateProductRequest
from advancedbilling.models.interval_unit import IntervalUnit

create_or_update_product_request = CreateOrUpdateProductRequest(
    product=CreateOrUpdateProduct(
        name='name0',
        description='description0',
        price_in_cents=54,
        interval=186,
        interval_unit=IntervalUnit.DAY,
        handle='handle6',
        accounting_code='accounting_code6',
        require_credit_card=False,
        trial_price_in_cents=34,
        trial_interval=88
    )
)
```

