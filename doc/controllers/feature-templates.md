# Feature Templates

```python
feature_templates_controller = client.feature_templates
```

## Class Name

`FeatureTemplatesController`

## Methods

* [List Feature Templates](../../doc/controllers/feature-templates.md#list-feature-templates)
* [Create Feature Template](../../doc/controllers/feature-templates.md#create-feature-template)
* [Read Feature Template](../../doc/controllers/feature-templates.md#read-feature-template)
* [Update Feature Template](../../doc/controllers/feature-templates.md#update-feature-template)
* [Archive Feature Template](../../doc/controllers/feature-templates.md#archive-feature-template)
* [Restore Feature Template](../../doc/controllers/feature-templates.md#restore-feature-template)


# List Feature Templates

Lists the feature templates defined for your site, active (non-archived) ones by default. Pass `status=archived` or `status=all` to widen the result set.

Supply `page` or `per_page` to paginate. Without either parameter, the response includes the full result set.

```python
def list_feature_templates(self,
                          page=1,
                          per_page=20,
                          status="active",
                          q=None,
                          kind=None,
                          updated_from=None,
                          updated_to=None,
                          sort_by="name",
                          sort_direction="asc")
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br><br>**Default**: `20`<br><br>**Constraints**: `<= 200` |
| `status` | [`Status1`](../../doc/models/status-1.md) | Query, Optional | Filters by archived state. Defaults to `active` (non-archived templates only).<br><br>**Default**: `"active"` |
| `q` | `str` | Query, Optional | Filters to feature templates whose name contains this substring (case-insensitive). |
| `kind` | [`Kind`](../../doc/models/kind.md) | Query, Optional | Filters by feature kind. |
| `updated_from` | `date` | Query, Optional | Returns feature templates updated on or after this date. |
| `updated_to` | `date` | Query, Optional | Returns feature templates updated on or before this date. |
| `sort_by` | [`SortBy`](../../doc/models/sort-by.md) | Query, Optional | The field to sort results by.<br><br>**Default**: `"name"` |
| `sort_direction` | [`SortDirection`](../../doc/models/sort-direction.md) | Query, Optional | The sort direction of the returned feature templates.<br><br>**Default**: `"asc"` |

## Response Type

**200**: OK

[`FeatureTemplatesListResponse`](../../doc/models/feature-templates-list-response.md)

## Example Usage

```python
page = 1

per_page = 50

status = Status1.ACTIVE

sort_by = SortBy.NAME

sort_direction = SortDirection.ASC

result = feature_templates_controller.list_feature_templates(
    page=page,
    per_page=per_page,
    status=status,
    sort_by=sort_by,
    sort_direction=sort_direction
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "items": [
    {
      "id": 1001,
      "key": "sso",
      "name": "Single Sign-On",
      "description": null,
      "kind": "access_right",
      "unit": null,
      "value_type": "boolean",
      "default_value": "true",
      "default_periodicity_interval": null,
      "default_periodicity_unit": null,
      "archived_at": null,
      "created_at": "2024-01-15T10:00:00-05:00",
      "updated_at": "2024-01-15T10:00:00-05:00",
      "products_count": 2,
      "plans_count": 5
    }
  ],
  "total_count": 1,
  "archived_count": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Create Feature Template

Defines a new feature at the site level. Feature templates aren't billable on their own. Attach a template to products or components to grant the feature to subscribers.

```python
def create_feature_template(self,
                           body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateFeatureTemplateRequest`](../../doc/models/create-feature-template-request.md) | Body, Optional | - |

## Response Type

**201**: Created

[`FeatureTemplateResponse`](../../doc/models/feature-template-response.md)

## Example Usage

```python
body = CreateFeatureTemplateRequest(
    feature=Feature(
        key='sso',
        name='Single Sign-On',
        kind=FeatureKind.ACCESS_RIGHT
    )
)

result = feature_templates_controller.create_feature_template(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "feature": {
    "id": 1001,
    "key": "sso",
    "name": "Single Sign-On",
    "description": null,
    "kind": "access_right",
    "unit": null,
    "value_type": "boolean",
    "default_value": "true",
    "default_periodicity_interval": null,
    "default_periodicity_unit": null,
    "archived_at": null,
    "created_at": "2024-01-15T10:00:00-05:00",
    "updated_at": "2024-01-15T10:00:00-05:00",
    "products_count": 0,
    "plans_count": 0
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Read Feature Template

Returns a single feature template. Archived feature templates are not addressable here and return `404`. Restore a template first to read or update it.

```python
def read_feature_template(self,
                         id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | The Advanced Billing id of the feature template. |

## Response Type

**200**: OK

[`FeatureTemplateResponse`](../../doc/models/feature-template-response.md)

## Example Usage

```python
id = 112

result = feature_templates_controller.read_feature_template(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |
| 404 | Not Found | `APIException` |


# Update Feature Template

Updates the name, description, unit, value type, default value, or default periodicity of a feature template. `key` is rejected on every update. `kind` is rejected once any feature catalog item has been created from this template.

Archived feature templates are not addressable here and return `404`. Restore a template first to update it.

```python
def update_feature_template(self,
                           id,
                           body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | The Advanced Billing id of the feature template. |
| `body` | [`UpdateFeatureTemplateRequest`](../../doc/models/update-feature-template-request.md) | Body, Optional | - |

## Response Type

**200**: OK

[`FeatureTemplateResponse`](../../doc/models/feature-template-response.md)

## Example Usage

```python
id = 112

result = feature_templates_controller.update_feature_template(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Archive Feature Template

Archives a feature template. Archived feature templates are not addressable via [Read Feature Template](../../doc/controllers/feature-templates.md#read-feature-template) or [Update Feature Template](../../doc/controllers/feature-templates.md#update-feature-template). Both endpoints return `404` until the template is restored.

The feature template record itself is never hard-deleted, and can always be restored with [Restore Feature Template](../../doc/controllers/feature-templates.md#restore-feature-template). Reversibility does not extend to `remove_from_catalog=true`: the feature catalog items and entitlements that parameter destroys are gone permanently, and restoring the template will not bring subscriber access back.

```python
def archive_feature_template(self,
                            id,
                            remove_from_catalog=False)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | The Advanced Billing id of the feature template. |
| `remove_from_catalog` | `bool` | Query, Optional | When `true`, also destroys every feature catalog item created from this template and cascades to their entitlements, revoking subscriber access immediately. When `false` (default), the feature template and its feature catalog items are archived, and existing entitlements are preserved.<br><br>**Default**: `False` |

## Response Type

**204**: No Content

`void`

## Example Usage

```python
id = 112

remove_from_catalog = False

feature_templates_controller.archive_feature_template(
    id,
    remove_from_catalog=remove_from_catalog
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |
| 404 | Not Found | `APIException` |


# Restore Feature Template

Clears the feature template's archived state. Feature catalog items created from this template are not automatically restored. Restore each one individually.

```python
def restore_feature_template(self,
                            id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | The Advanced Billing id of the feature template. |

## Response Type

**200**: OK

[`FeatureTemplateResponse`](../../doc/models/feature-template-response.md)

## Example Usage

```python
id = 112

result = feature_templates_controller.restore_feature_template(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |

