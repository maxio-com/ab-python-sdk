
# Clone Feature Catalog Item

A feature to put on the cloned price point. Requires Entitlements to be enabled for the site; ignored otherwise.

Unlike Create Feature Catalog Item, nothing falls back to the feature template's defaults: send `value`, and for a `usage_limit` feature its periodicity (and any grant expiration) explicitly. If any item can't be applied, for example a missing `value`, a `usage_limit` item without periodicity, or an archived or unknown feature template, the whole clone fails with `422` and nothing is created.

## Structure

`CloneFeatureCatalogItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `feature_template_id` | `int` | Required | - |
| `value` | `str` | Required | - |
| `periodicity_interval` | `int` | Optional | Required for `usage_limit` features; must be omitted for other kinds. |
| `periodicity_unit` | [`EntitlementPeriodicityUnit`](../../doc/models/entitlement-periodicity-unit.md) | Optional | Required for `usage_limit` features; must be omitted for other kinds. |
| `grant_expiration_interval` | `int` | Optional | `usage_limit` features only. A positive number of `grant_expiration_unit`s; required with `day` or `month`, and must be omitted with `until_next_refill`. |
| `grant_expiration_unit` | [`GrantExpirationUnit`](../../doc/models/grant-expiration-unit.md) | Optional | `usage_limit` features only. |

## Example

```python
from advancedbilling.models.clone_feature_catalog_item import CloneFeatureCatalogItem
from advancedbilling.models.entitlement_periodicity_unit import EntitlementPeriodicityUnit
from advancedbilling.models.grant_expiration_unit import GrantExpirationUnit

clone_feature_catalog_item = CloneFeatureCatalogItem(
    feature_template_id=76,
    value='value0',
    periodicity_interval=204,
    periodicity_unit=EntitlementPeriodicityUnit.DAY,
    grant_expiration_interval=128,
    grant_expiration_unit=GrantExpirationUnit.DAY
)
```

