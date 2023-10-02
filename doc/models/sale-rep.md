
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

## Example (as JSON)

```json
{
  "id": 18,
  "full_name": "full_name0",
  "subscriptions_count": 162,
  "test_mode": false,
  "subscriptions": [
    {
      "id": 202,
      "site_name": "site_name8",
      "subscription_url": "subscription_url2",
      "customer_name": "customer_name8",
      "created_at": "created_at4"
    },
    {
      "id": 202,
      "site_name": "site_name8",
      "subscription_url": "subscription_url2",
      "customer_name": "customer_name8",
      "created_at": "created_at4"
    }
  ]
}
```

