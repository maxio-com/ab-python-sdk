
# Preview Allocations Request

## Structure

`PreviewAllocationsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allocations` | [`List[CreateAllocation]`](../../doc/models/create-allocation.md) | Required | - |
| `effective_proration_date` | `date` | Optional | To calculate proration amounts for a future time. Only within a current subscription period. Only ISO8601 format is supported. |
| `upgrade_charge` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided. |
| `downgrade_credit` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided. |

## Example (as JSON)

```json
{
  "allocations": [
    {
      "quantity": 26.48,
      "decimal_quantity": "decimal_quantity8",
      "previous_quantity": 55.5,
      "decimal_previous_quantity": "decimal_previous_quantity2",
      "component_id": 242,
      "memo": "memo6"
    }
  ],
  "effective_proration_date": "2023-12-01",
  "upgrade_charge": "none",
  "downgrade_credit": "prorated"
}
```

