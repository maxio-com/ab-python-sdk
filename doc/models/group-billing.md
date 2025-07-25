
# Group Billing

Optional attributes related to billing date and accrual. Note: Only applicable for new subscriptions.

## Structure

`GroupBilling`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accrue` | `bool` | Optional | A flag indicating whether or not to accrue charges on the new subscription.<br><br>**Default**: `False` |
| `align_date` | `bool` | Optional | A flag indicating whether or not to align the billing date of the new subscription with the billing date of the primary subscription of the hierarchy's default subscription group. Required to be true if prorate is also true.<br><br>**Default**: `False` |
| `prorate` | `bool` | Optional | A flag indicating whether or not to prorate billing of the new subscription for the current period. A value of true is ignored unless align_date is also true.<br><br>**Default**: `False` |

## Example (as JSON)

```json
{
  "accrue": false,
  "align_date": false,
  "prorate": false
}
```

