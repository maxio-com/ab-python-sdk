
# Wallets List Response

## Structure

`WalletsListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallets` | [`List[Wallet]`](../../doc/models/wallet.md) | Required | - |
| `meta` | [`ListPublicKeysMeta`](../../doc/models/list-public-keys-meta.md) | Required | - |

## Example

```python
from advancedbilling.models.list_public_keys_meta import ListPublicKeysMeta
from advancedbilling.models.owner_type import OwnerType
from advancedbilling.models.wallet import Wallet
from advancedbilling.models.wallets_list_response import WalletsListResponse

wallets_list_response = WalletsListResponse(
    wallets=[
        Wallet(
            id=80,
            owner_type=OwnerType.SUBSCRIPTION,
            owner_id=156,
            name='name4',
            wallet_product_id=72,
            unit='tokens',
            balance='150.0',
            posted_balance='150.0',
            depletion_policy='hard_stop'
        )
    ],
    meta=ListPublicKeysMeta(
        total_count=150,
        current_page=126,
        total_pages=138,
        per_page=152
    )
)
```

