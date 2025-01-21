
# Subscription Included Coupon

## Structure

`SubscriptionIncludedCoupon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | - |
| `use_count` | `int` | Optional | - |
| `uses_allowed` | `int` | Optional | - |
| `expires_at` | `str` | Optional | - |
| `recurring` | `bool` | Optional | - |
| `amount_in_cents` | `int` | Optional | **Constraints**: `>= 0` |
| `percentage` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "code": "\"ABCD_10\"",
  "use_count": 2,
  "uses_allowed": 10,
  "expires_at": "\"2023-07-13T05:18:58-04:00\"",
  "amount_in_cents": 1000,
  "percentage": "\"15.0\"",
  "recurring": false
}
```

