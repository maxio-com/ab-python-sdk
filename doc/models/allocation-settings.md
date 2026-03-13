
# Allocation Settings

## Structure

`AllocationSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upgrade_charge` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided. |
| `downgrade_credit` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided. |
| `accrue_charge` | `str` | Optional | Either "true" or "false". |

## Example (as JSON)

```json
{
  "upgrade_charge": "none",
  "downgrade_credit": "prorated",
  "accrue_charge": "accrue_charge0"
}
```

