
# Aggregated Entitlements Response

## Structure

`AggregatedEntitlementsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Required | - |
| `customer_id` | `int` | Required | - |
| `status` | `str` | Required | The subscription's current state, e.g. `active`, `trialing`, `canceled`. |
| `entitlements` | [`List[AggregatedEntitlement]`](../../doc/models/aggregated-entitlement.md) | Required | - |

## Example

```python
from advancedbilling.models.aggregated_entitlement import AggregatedEntitlement
from advancedbilling.models.aggregated_entitlements_response import AggregatedEntitlementsResponse
from advancedbilling.models.feature_kind import FeatureKind

aggregated_entitlements_response = AggregatedEntitlementsResponse(
    subscription_id=220,
    customer_id=148,
    status='status2',
    entitlements=[
        AggregatedEntitlement(
            feature_key='feature.sso',
            periodicity_key='usage.api_calls:1:month',
            name='name6',
            mtype=FeatureKind.SERVICE_RIGHT,
            value=True
        )
    ]
)
```

