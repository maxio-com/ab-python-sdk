
# Sale Rep

## Structure

`SaleRep`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `full_name` | `str` | Optional | - |
| `subscriptions_count` | `int` | Optional | - |
| `test_mode` | `bool` | Optional | - |
| `subscriptions` | [`List[SaleRepSubscription]`](../../doc/models/sale-rep-subscription.md) | Optional | - |

## Example

```python
from advancedbilling.models.sale_rep import SaleRep
from advancedbilling.models.sale_rep_subscription import SaleRepSubscription

sale_rep = SaleRep(
    id=214,
    full_name='full_name0',
    subscriptions_count=34,
    test_mode=False,
    subscriptions=[
        SaleRepSubscription(
            id=202,
            site_name='site_name8',
            subscription_url='subscription_url2',
            customer_name='customer_name8',
            created_at='created_at4'
        ),
        SaleRepSubscription(
            id=202,
            site_name='site_name8',
            subscription_url='subscription_url2',
            customer_name='customer_name8',
            created_at='created_at4'
        )
    ]
)
```

