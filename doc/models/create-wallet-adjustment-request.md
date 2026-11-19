
# Create Wallet Adjustment Request

A signed correction to a specific grant's balance, or to an overdraft entry's usage, intended for support and ops use.

## Structure

`CreateWalletAdjustmentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adjustment` | [`Adjustment`](../../doc/models/adjustment.md) | Required | - |

## Example

```python
from advancedbilling.models.adjustment import Adjustment
from advancedbilling.models.create_wallet_adjustment_request import CreateWalletAdjustmentRequest

create_wallet_adjustment_request = CreateWalletAdjustmentRequest(
    adjustment=Adjustment(
        amount='String7',
        reason='reason0',
        grant_id=104,
        source_transaction_id=126,
        expected_remaining='expected_remaining6',
        expected_source_corrections='expected_source_corrections8'
    )
)
```

