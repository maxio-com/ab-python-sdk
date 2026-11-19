
# Wallet Products List Response

## Structure

`WalletProductsListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet_products` | [`List[WalletProductListItem]`](../../doc/models/wallet-product-list-item.md) | Required | - |
| `total_count` | `int` | Required | Total number of Wallet Products matching the filters, across all pages. |
| `archived_count` | `int` | Required | Not a simple count of archived products matching the filters. With `status=archived`, equals `total_count` (there's nothing else to report). With any other `status`, it's `0` whenever `total_count` is non-zero, and only when `total_count` is `0` does it become the number of archived Wallet Products matching the same `q` search term (ignoring `status`): an empty-state hint, not a running total. |

## Example

```python
from advancedbilling.models.item_category import ItemCategory
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.wallet_product_list_item import WalletProductListItem
from advancedbilling.models.wallet_products_list_response import WalletProductsListResponse

wallet_products_list_response = WalletProductsListResponse(
    wallet_products=[
        WalletProductListItem(
            id=70,
            name='name4',
            handle='handle0',
            pricing_scheme=PricingScheme.STAIRSTEP,
            unit_name='unit_name6',
            item_category=ItemCategory.ENUM_BUSINESS_SOFTWARE
        )
    ],
    total_count=152,
    archived_count=176
)
```

