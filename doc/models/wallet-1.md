
# Wallet 1

## Structure

`Wallet1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Required | The subscription that will own the wallet. |
| `wallet_product_id` | int \| str | Required | This is a container for one-of cases. |
| `name` | `str` | Optional | (Optional) A merchant-facing label for the wallet. Surrounding spaces are stripped; a blank value is stored as `null`.<br><br>**Constraints**: *Maximum Length*: `255` |
| `depletion_policy` | `str` | Optional | Defaults to `hard_stop`, currently the only supported value. |
| `hard_stop_overflow` | [`WalletHardStopOverflow`](../../doc/models/wallet-hard-stop-overflow.md) | Optional | Defaults to `discard`. |
| `meter_id` | `int` | Optional | Pairs the wallet with a merchant-owned metering meter, so its balance factors in live usage (see the wallet resource's `meter` and `metered_through_at` fields). Only a `sum` or `count` meter can be paired. Requires metered wallet consumption to be enabled for the site, checked whenever this or `conversion_rate` is sent: `403` (plain text, not JSON) if it isn't. A meter id that doesn't resolve to a merchant-owned meter on this site, including a system-maintained shadow meter, is `404`. Immutable once the wallet is created. |
| `conversion_rate` | str \| int \| None | Optional | This is a container for one-of cases. |
| `price_point_id` | `int` | Optional | The price point used to price [Create Wallet Purchase](../../doc/controllers/wallet-purchases.md#create-wallet-purchase) calls against this wallet. Must belong to the Wallet Product, and can't be archived or a subscription-specific custom price point. Defaults to the Wallet Product's default price point. Immutable once the wallet is created. |
| `initial_balance` | str \| int \| None | Optional | This is a container for one-of cases. |
| `initial_balance_expires_at` | `str` | Optional | An expiration for the initial-balance grant. Only accepted together with a non-zero `initial_balance`, and must be in the future. Accepts either a bare calendar date (`YYYY-MM-DD`), resolved to the end of that day in the site's time zone, or a full timestamp. A calendar day that doesn't exist, such as `2027-02-30`, is rejected with `422` rather than rolled into the next month. |

## Example

```python
from advancedbilling.models.wallet_1 import Wallet1
from advancedbilling.models.wallet_hard_stop_overflow import WalletHardStopOverflow

wallet_1 = Wallet1(
    subscription_id=16,
    wallet_product_id=76,
    name='name6',
    depletion_policy='depletion_policy4',
    hard_stop_overflow=WalletHardStopOverflow.DISCARD,
    meter_id=32,
    conversion_rate='String9',
    initial_balance='String1'
)
```

