
# Wallet Transaction Result Response

Returned by [Create Wallet Transaction](../../doc/controllers/wallet-transactions.md#create-wallet-transaction). `wallet_transactions` and `balance` are always present. `requested_amount`, `drained_amount`, and `rejected_amount` are present only when the request's `kind` was `debit`.

## Structure

`WalletTransactionResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet_transactions` | [`List[WalletTransaction]`](../../doc/models/wallet-transaction.md) | Required | - |
| `requested_amount` | `str` | Optional | `kind: debit` only. The amount that was requested, as a decimal string. |
| `drained_amount` | `str` | Optional | `kind: debit` only. The amount actually drained from the wallet's grants, as a decimal string. |
| `rejected_amount` | `str` | Optional | `kind: debit` only, as a decimal string. Under `hard_stop_overflow: discard`, this is the requested amount minus what the wallet could cover (`"0.0"` on a full drain). Always `"0.0"` under `allow_negative`; nothing is rejected, and the balance goes negative instead. |
| `balance` | `str` | Required | The wallet's new balance, as a decimal string. |

## Example

```python
from advancedbilling.models.wallet_transaction import WalletTransaction
from advancedbilling.models.wallet_transaction_result_response import WalletTransactionResultResponse

wallet_transaction_result_response = WalletTransactionResultResponse(
    wallet_transactions=[
        WalletTransaction(
            id=140,
            wallet_id=244,
            kind='grant',
            amount='-30.0',
            grant_id=160
        )
    ],
    balance='balance2',
    requested_amount='requested_amount0',
    drained_amount='drained_amount4',
    rejected_amount='rejected_amount6'
)
```

