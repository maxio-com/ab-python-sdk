
# Coupon Usage

## Structure

`CouponUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The Chargify id of the product |
| `name` | `str` | Optional | Name of the product |
| `signups` | `int` | Optional | Number of times the coupon has been applied |
| `savings` | `int` | Optional | Dollar amount of customer savings as a result of the coupon. |
| `savings_in_cents` | `long\|int` | Optional | Dollar amount of customer savings as a result of the coupon. |
| `revenue` | `int` | Optional | Total revenue of the all subscriptions that have received a discount from this coupon. |
| `revenue_in_cents` | `long\|int` | Optional | Total revenue of the all subscriptions that have received a discount from this coupon. |

## Example (as JSON)

```json
{
  "id": 14,
  "name": "name0",
  "signups": 34,
  "savings": 52,
  "savings_in_cents": 138
}
```

