
# Bulk Create Product Price Points Request

## Structure

`BulkCreateProductPricePointsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_points` | [`List[CreateProductPricePoint]`](../../doc/models/create-product-price-point.md) | Required | - |

## Example

```python
from advancedbilling.models.bulk_create_product_price_points_request import BulkCreateProductPricePointsRequest
from advancedbilling.models.create_product_price_point import CreateProductPricePoint
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.trial_type import TrialType

bulk_create_product_price_points_request = BulkCreateProductPricePointsRequest(
    price_points=[
        CreateProductPricePoint(
            name='name2',
            price_in_cents=108,
            interval=92,
            interval_unit=IntervalUnit.DAY,
            handle='handle8',
            trial_price_in_cents=196,
            trial_interval=250,
            trial_interval_unit=IntervalUnit.DAY,
            trial_type=TrialType.NO_OBLIGATION,
            use_site_exchange_rate=True
        )
    ]
)
```

