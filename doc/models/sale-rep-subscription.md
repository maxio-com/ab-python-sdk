
# Sale Rep Subscription

## Structure

`SaleRepSubscription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `site_name` | `str` | Optional | - |
| `subscription_url` | `str` | Optional | - |
| `customer_name` | `str` | Optional | - |
| `created_at` | `str` | Optional | - |
| `mrr` | `str` | Optional | - |
| `usage` | `str` | Optional | - |
| `recurring` | `str` | Optional | - |
| `last_payment` | `str` | Optional | - |
| `churn_date` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.sale_rep_subscription import SaleRepSubscription

sale_rep_subscription = SaleRepSubscription(
    id=126,
    site_name='site_name2',
    subscription_url='subscription_url6',
    customer_name='customer_name2',
    created_at='created_at8'
)
```

