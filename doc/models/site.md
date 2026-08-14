
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
| `multi_frequency_enabled` | `bool` | Optional | Whether the site has the multi-frequency billing feature enabled. Only present when relationship invoicing is active. |
| `auto_renewals_enabled` | `bool` | Optional | Whether the auto-renewals feature is enabled for this site. |
| `portal_enabled` | `bool` | Optional | Whether the Billing Portal is enabled for this site. |
| `test` | `bool` | Optional | - |

## Example

```python
from advancedbilling.models.site import Site

site = Site(
    id=64,
    name='name4',
    subdomain='subdomain0',
    currency='currency4',
    seller_id=228
)
```

