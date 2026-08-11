
# Subscription Migration Preview

## Structure

`SubscriptionMigrationPreview`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `prorated_adjustment_in_cents` | `int` | Optional | The amount of the prorated adjustment that would be issued for the current subscription. |
| `charge_in_cents` | `int` | Optional | The amount of the charge that would be created for the new product. |
| `payment_due_in_cents` | `int` | Optional | The amount of the payment due in the case of an upgrade. |
| `credit_applied_in_cents` | `int` | Optional | Represents a credit in cents that is applied to your subscription as part of a migration process for a specific product, which reduces the amount owed for the subscription. |

## Example

```python
from advancedbilling.models.subscription_migration_preview import SubscriptionMigrationPreview

subscription_migration_preview = SubscriptionMigrationPreview(
    prorated_adjustment_in_cents=176,
    charge_in_cents=58,
    payment_due_in_cents=230,
    credit_applied_in_cents=190
)
```

