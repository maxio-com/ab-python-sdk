
# Wallet Product Usage Template

One wallet template billing through this Wallet Product, joined to the Feature and plan/component that assigns it, when there is one.

## Structure

`WalletProductUsageTemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_name` | `str` | Optional | The name of the product or component the Feature is assigned to. `null` when the wallet template has no assigning Feature. |
| `wallet_template_name` | `str` | Optional | The label set in `wallet_behavior.name` on the Feature, or the standalone wallet's own `name`. |
| `unit_name` | `str` | Optional | - |
| `purchase_mechanism` | `str` | Optional | A best-effort label for how this wallet is expected to be replenished. Currently reports `"Overage"` when the wallet template allows a negative balance, and `null` otherwise; there's no persisted field yet distinguishing, for example, an intended "Auto top-up" from "Purchase more" setup. Treat this as informational, not a stable enum. |
| `price_point_name` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `active` | `bool` | Optional | `false` when the assigning Feature is archived. |
| `feature_template_id` | `int` | Optional | - |
| `feature_template_name` | `str` | Optional | - |
| `price_point_override` | `bool` | Optional | `true` when this wallet template is priced at a price point other than the Wallet Product's default. |

## Example

```python
from advancedbilling.models.wallet_product_usage_template import WalletProductUsageTemplate

wallet_product_usage_template = WalletProductUsageTemplate(
    plan_name='plan_name8',
    wallet_template_name='wallet_template_name4',
    unit_name='unit_name8',
    purchase_mechanism='purchase_mechanism6',
    price_point_name='price_point_name0'
)
```

