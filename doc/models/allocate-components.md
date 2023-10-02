
# Allocate Components

## Structure

`AllocateComponents`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `proration_upgrade_scheme` | `str` | Optional | **Default**: `'no-prorate'` |
| `proration_downgrade_scheme` | `str` | Optional | **Default**: `'no-prorate'` |
| `allocations` | [`List[CreateAllocationRequest]`](../../doc/models/create-allocation-request.md) | Optional | - |
| `accrue_charge` | `bool` | Optional | - |
| `upgrade_charge` | `str` | Optional | - |
| `downgrade_credit` | `str` | Optional | - |
| `payment_collection_method` | [`LegacyPaymentCollectionMethodEnum`](../../doc/models/legacy-payment-collection-method-enum.md) | Optional | (Optional) If not passed, the allocation(s) will use the payment collection method on the subscription |

## Example (as JSON)

```json
{
  "proration_upgrade_scheme": "no-prorate",
  "proration_downgrade_scheme": "no-prorate",
  "allocations": [
    {
      "allocation": {
        "quantity": 32,
        "component_id": 8,
        "memo": "memo2",
        "proration_downgrade_scheme": "proration_downgrade_scheme4",
        "proration_upgrade_scheme": "proration_upgrade_scheme6",
        "accrue_charge": false
      }
    },
    {
      "allocation": {
        "quantity": 32,
        "component_id": 8,
        "memo": "memo2",
        "proration_downgrade_scheme": "proration_downgrade_scheme4",
        "proration_upgrade_scheme": "proration_upgrade_scheme6",
        "accrue_charge": false
      }
    }
  ],
  "accrue_charge": false,
  "upgrade_charge": "upgrade_charge4"
}
```

