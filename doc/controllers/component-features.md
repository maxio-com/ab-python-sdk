# Component Features

```python
component_features_controller = client.component_features
```

## Class Name

`ComponentFeaturesController`

## Methods

* [List Component Features](../../doc/controllers/component-features.md#list-component-features)
* [Create Component Feature](../../doc/controllers/component-features.md#create-component-feature)
* [Read Component Feature](../../doc/controllers/component-features.md#read-component-feature)
* [Update Component Feature](../../doc/controllers/component-features.md#update-component-feature)
* [Remove Component Feature](../../doc/controllers/component-features.md#remove-component-feature)
* [Restore Component Feature](../../doc/controllers/component-features.md#restore-component-feature)


# List Component Features

Lists the feature catalog items attached to this component, including price-point-specific overrides.

```python
def list_component_features(self,
                           component_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Advanced Billing id of the component. |

## Response Type

**200**: OK

[`FeatureCatalogItemsListResponse`](../../doc/models/feature-catalog-items-list-response.md)

## Example Usage

```python
component_id = 222

result = component_features_controller.list_component_features(component_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |
| 404 | Not Found | `APIException` |


# Create Component Feature

Attaches a feature template to this component. Pass `price_point_type: "PricePoint"` and `price_point_id` to scope the feature catalog item to a single component price point instead of the whole component. `value`, the periodicity and the grant expiration fall back to the feature template's defaults when omitted.

**Product- or component-level items are a template.** A feature catalog item without `price_point_id` is copied onto price points created after it (except bulk-created price points; [Clone Component Price Point](../../doc/controllers/component-price-points.md#clone-component-price-point) applies only the `feature_catalog_items` you send with it, and the automatic clone described below copies the source's features), but it is not added to price points that already exist, so their subscribers get nothing from it, even with `propagate_to_subscriptions: true`. To grant a feature to existing subscribers, create the item on each existing price point.

**Restoring a template item.** Restoring an archived product- or component-level item, or creating one again for the same feature template, also restores the price-point copies that were archived together with it (for example, when the feature template was archived). If one of those price points has subscribers without the feature, the call returns `422` naming that price point, unless you send `propagate_to_subscriptions: true`, which restores the copies and grants the feature to those subscribers.

**Price points with subscribers.** When the feature catalog item is scoped to a price point that already has subscribers and you don't send `propagate_to_subscriptions: true`, the new feature applies to new subscriptions only. The price point is cloned with its current features, the new feature is applied to the clone, and the response carries the clone's `price_point_id`. The feature catalog item in the response is also a different record, with a new `id`: later calls for the clone must use that `id`, not the original one. Existing subscribers stay on the original price point, unchanged; sign new subscriptions up on the clone to give them the change. A component price point has subscribers when any subscription, including a canceled one or one allocated a quantity of zero, has the component at that price point. Price points that can't be cloned (archived or custom ones, or a component price point with an interval on a site without multi-frequency) make the request return `422`, with a message naming `propagate_to_subscriptions: true` as the way to apply the change to existing subscribers instead.

```python
def create_component_feature(self,
                            component_id,
                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Advanced Billing id of the component. |
| `body` | [`CreateFeatureCatalogItemRequest`](../../doc/models/create-feature-catalog-item-request.md) | Body, Optional | The owning product or component is taken from the URL and must not be included in the request body. |

## Response Type

**201**: Created

[`FeatureCatalogItemResponse`](../../doc/models/feature-catalog-item-response.md)

## Example Usage

```python
component_id = 222

body = CreateFeatureCatalogItemRequest(
    feature=Feature2(
        feature_template_id=196,
        propagate_to_subscriptions=False
    )
)

result = component_features_controller.create_component_feature(
    component_id,
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Read Component Feature

Returns a single feature catalog item attached to this component.

```python
def read_component_feature(self,
                          component_id,
                          id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Advanced Billing id of the component. |
| `id` | `int` | Template, Required | The Advanced Billing id of the feature catalog item. |

## Response Type

**200**: OK

[`FeatureCatalogItemResponse`](../../doc/models/feature-catalog-item-response.md)

## Example Usage

```python
component_id = 222

id = 112

result = component_features_controller.read_component_feature(
    component_id,
    id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |
| 404 | Not Found | `APIException` |


# Update Component Feature

Updates the value or periodicity of a feature catalog item attached to this component. A request that changes nothing returns the item as it is.

**Price points with subscribers.** When the feature catalog item is scoped to a price point that already has subscribers and you don't send `propagate_to_subscriptions: true`, the update applies to new subscriptions only. The price point is cloned with its current features, the update is applied to the clone, and the response carries the clone's `price_point_id`. The feature catalog item in the response is also a different record, with a new `id`: later calls for the clone must use that `id`, not the original one. Existing subscribers stay on the original price point, unchanged; sign new subscriptions up on the clone to give them the change. A component price point has subscribers when any subscription, including a canceled one or one allocated a quantity of zero, has the component at that price point. Price points that can't be cloned (archived or custom ones, or a component price point with an interval on a site without multi-frequency) make the request return `422`, with a message naming `propagate_to_subscriptions: true` as the way to apply the change to existing subscribers instead.

```python
def update_component_feature(self,
                            component_id,
                            id,
                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Advanced Billing id of the component. |
| `id` | `int` | Template, Required | The Advanced Billing id of the feature catalog item. |
| `body` | [`UpdateFeatureCatalogItemRequest`](../../doc/models/update-feature-catalog-item-request.md) | Body, Optional | - |

## Response Type

**200**: OK

[`FeatureCatalogItemResponse`](../../doc/models/feature-catalog-item-response.md)

## Example Usage

```python
component_id = 222

id = 112

body = UpdateFeatureCatalogItemRequest(
    feature=Feature3(
        propagate_to_subscriptions=False
    )
)

result = component_features_controller.update_component_feature(
    component_id,
    id,
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Remove Component Feature

Removes a feature catalog item from this component. Returns `204` when the item is removed in place.

**Price points with subscribers.** When the feature catalog item is scoped to a price point that already has subscribers and you don't send `destroy_entitlements=true`, the removal applies to new subscriptions only. The price point is cloned with its current features, the removal is applied to the clone, and the call returns `200` with the archived feature catalog item on the clone (carrying the clone's `price_point_id` and a new `id`) instead of `204`. Existing subscribers stay on the original price point, unchanged; sign new subscriptions up on the clone to give them the change. A component price point has subscribers when any subscription, including a canceled one or one allocated a quantity of zero, has the component at that price point. Price points that can't be cloned (archived or custom ones, or a component price point with an interval on a site without multi-frequency) make the request return `422`, with a message naming `destroy_entitlements=true` as the way to apply the change to existing subscribers instead.

```python
def remove_component_feature(self,
                            component_id,
                            id,
                            destroy_entitlements=False)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Advanced Billing id of the component. |
| `id` | `int` | Template, Required | The Advanced Billing id of the feature catalog item. |
| `destroy_entitlements` | `bool` | Query, Optional | When `true`, permanently deletes this feature catalog item and every entitlement it created, revoking subscriber access immediately. When `false` (default), the feature catalog item is archived and existing entitlements are preserved.<br><br>**Default**: `False` |

## Response Type

**200**: The price point had subscribers, so the removal was made on a clone of it. Returns the archived feature catalog item on the clone.

[`FeatureCatalogItemResponse`](../../doc/models/feature-catalog-item-response.md)

## Example Usage

```python
component_id = 222

id = 112

destroy_entitlements = False

result = component_features_controller.remove_component_feature(
    component_id,
    id,
    destroy_entitlements=destroy_entitlements
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |
| 404 | Not Found | `APIException` |
| 422 | The price point has subscribers but can't be cloned (it is archived or custom, or it is a component price point with an interval on a site without multi-frequency). Send `destroy_entitlements=true` to remove the feature from its existing subscribers instead. | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Restore Component Feature

Clears the archived state of a feature catalog item attached to this component. Returns `422` if the parent feature template is still archived. Restore the feature template first. Otherwise, restoring an item that isn't archived returns it unchanged.

**Price points with subscribers.** When the feature catalog item is scoped to a price point that already has subscribers and you don't send `propagate_to_subscriptions=true`, the restore applies to new subscriptions only. The price point is cloned with its current features, the restore is applied to the clone, and the response carries the clone's `price_point_id`. The feature catalog item in the response is also a different record, with a new `id`: later calls for the clone must use that `id`, not the original one. Existing subscribers stay on the original price point, unchanged; sign new subscriptions up on the clone to give them the change. A component price point has subscribers when any subscription, including a canceled one or one allocated a quantity of zero, has the component at that price point. Price points that can't be cloned (archived or custom ones, or a component price point with an interval on a site without multi-frequency) make the request return `422`, with a message naming `propagate_to_subscriptions: true` as the way to apply the change to existing subscribers instead.

```python
def restore_component_feature(self,
                             component_id,
                             id,
                             propagate_to_subscriptions=False)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Advanced Billing id of the component. |
| `id` | `int` | Template, Required | The Advanced Billing id of the feature catalog item. |
| `propagate_to_subscriptions` | `bool` | Query, Optional | When `true`, the restored feature is applied to the existing subscriptions on its price point. When `false` (default), an item scoped to a price point with subscribers is restored on a clone of that price point instead; a product- or component-level item is never cloned, and returns `422` if a price-point copy it restores has subscribers without the feature. See the description.<br><br>**Default**: `False` |

## Response Type

**200**: OK

[`FeatureCatalogItemResponse`](../../doc/models/feature-catalog-item-response.md)

## Example Usage

```python
component_id = 222

id = 112

propagate_to_subscriptions = False

result = component_features_controller.restore_component_feature(
    component_id,
    id,
    propagate_to_subscriptions=propagate_to_subscriptions
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |

