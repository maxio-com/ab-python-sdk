
# Site

## Structure

`Site`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `subdomain` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `seller_id` | `int` | Optional | - |
| `non_primary_currencies` | `List[str]` | Optional | - |
| `relationship_invoicing_enabled` | `bool` | Optional | - |
| `schedule_subscription_cancellation_enabled` | `bool` | Optional | - |
| `customer_hierarchy_enabled` | `bool` | Optional | - |
| `whopays_enabled` | `bool` | Optional | - |
| `whopays_default_payer` | `str` | Optional | - |
| `allocation_settings` | [`AllocationSettings`](../../doc/models/allocation-settings.md) | Optional | - |
| `default_payment_collection_method` | `str` | Optional | - |
| `organization_address` | [`OrganizationAddress`](../../doc/models/organization-address.md) | Optional | - |
| `tax_configuration` | [`TaxConfiguration`](../../doc/models/tax-configuration.md) | Optional | - |
| `net_terms` | [`NetTerms`](../../doc/models/net-terms.md) | Optional | - |
| `test` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "id": 34,
  "name": "name0",
  "subdomain": "subdomain4",
  "currency": "currency0",
  "seller_id": 198
}
```

