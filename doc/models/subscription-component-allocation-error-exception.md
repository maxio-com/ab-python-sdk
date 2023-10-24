
# Subscription Component Allocation Error Exception

## Structure

`SubscriptionComponentAllocationErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List[SubscriptionComponentAllocationErrorItem]`](../../doc/models/subscription-component-allocation-error-item.md) | Optional | - |

## Example (as JSON)

```json
{
  "Example": null,
  "errors": [
    {
      "kind": "base",
      "message": "Credit scheme must be one of credit, refund or none."
    }
  ]
}
```

