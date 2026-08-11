
# List Sale Rep Item

## Structure

`ListSaleRepItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `full_name` | `str` | Optional | - |
| `subscriptions_count` | `int` | Optional | - |
| `mrr_data` | [`Dict[str, SaleRepItemMrr]`](../../doc/models/sale-rep-item-mrr.md) | Optional | - |
| `test_mode` | `bool` | Optional | - |

## Example

```python
from advancedbilling.models.list_sale_rep_item import ListSaleRepItem
from advancedbilling.models.sale_rep_item_mrr import SaleRepItemMrr

list_sale_rep_item = ListSaleRepItem(
    id=124,
    full_name='full_name8',
    subscriptions_count=56,
    mrr_data={
        'november_2019': SaleRepItemMrr(
            mrr='$0.00',
            usage='$0.00',
            recurring='$0.00'
        ),
        'december_2019': SaleRepItemMrr(
            mrr='$0.00',
            usage='$0.00',
            recurring='$0.00'
        ),
        'january_2020': SaleRepItemMrr(
            mrr='$400.00',
            usage='$0.00',
            recurring='$400.00'
        )
    },
    test_mode=False
)
```

