
# Reactivation Billing

These values are only applicable to subscriptions using calendar billing.

## Structure

`ReactivationBilling`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reactivation_charge` | [`ReactivationCharge`](../../doc/models/reactivation-charge.md) | Optional | You may choose how to handle the reactivation charge for that subscription: 1) `prorated` A prorated charge for the product price will be attempted to complete the period 2) `immediate` A full-price charge for the product price will be attempted immediately 3) `delayed` A full-price charge for the product price will be attempted at the next renewal.<br><br>**Default**: `"prorated"` |

## Example

```python
from advancedbilling.models.reactivation_billing import ReactivationBilling
from advancedbilling.models.reactivation_charge import ReactivationCharge

reactivation_billing = ReactivationBilling(
    reactivation_charge=ReactivationCharge.PRORATED
)
```

