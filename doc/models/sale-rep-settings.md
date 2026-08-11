
# Sale Rep Settings

## Structure

`SaleRepSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_name` | `str` | Optional | - |
| `subscription_id` | `int` | Optional | - |
| `site_link` | `str` | Optional | - |
| `site_name` | `str` | Optional | - |
| `subscription_mrr` | `str` | Optional | - |
| `sales_rep_id` | `int` | Optional | - |
| `sales_rep_name` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.sale_rep_settings import SaleRepSettings

sale_rep_settings = SaleRepSettings(
    customer_name='customer_name4',
    subscription_id=168,
    site_link='site_link0',
    site_name='site_name6',
    subscription_mrr='subscription_mrr2'
)
```

