
# Item Price Point Changed

## Structure

`ItemPricePointChanged`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `int` | Required | - |
| `item_type` | `str` | Required | - |
| `item_handle` | `str` | Required | - |
| `item_name` | `str` | Required | - |
| `previous_price_point` | [`ItemPricePointData`](../../doc/models/item-price-point-data.md) | Required | - |
| `current_price_point` | [`ItemPricePointData`](../../doc/models/item-price-point-data.md) | Required | - |

## Example

```python
from advancedbilling.models.item_price_point_changed import ItemPricePointChanged
from advancedbilling.models.item_price_point_data import ItemPricePointData

item_price_point_changed = ItemPricePointChanged(
    item_id=66,
    item_type='item_type2',
    item_handle='item_handle0',
    item_name='item_name4',
    previous_price_point=ItemPricePointData(
        id=216,
        handle='handle6',
        name='name0'
    ),
    current_price_point=ItemPricePointData(
        id=218,
        handle='handle6',
        name='name0'
    )
)
```

