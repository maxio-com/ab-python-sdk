
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

## Example (as JSON)

```json
{
  "item_id": 66,
  "item_type": "item_type6",
  "item_handle": "item_handle4",
  "item_name": "item_name8",
  "previous_price_point": {
    "id": 216,
    "handle": "handle6",
    "name": "name0"
  },
  "current_price_point": {
    "id": 218,
    "handle": "handle6",
    "name": "name0"
  }
}
```

