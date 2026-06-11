# API Exports

```python
api_exports_controller = client.api_exports
```

## Class Name

`APIExportsController`

## Methods

* [List Exported Proforma Invoices](../../doc/controllers/api-exports.md#list-exported-proforma-invoices)
* [List Exported Invoices](../../doc/controllers/api-exports.md#list-exported-invoices)
* [List Exported Subscriptions](../../doc/controllers/api-exports.md#list-exported-subscriptions)
* [Export Proforma Invoices](../../doc/controllers/api-exports.md#export-proforma-invoices)
* [Export Invoices](../../doc/controllers/api-exports.md#export-invoices)
* [Export Subscriptions](../../doc/controllers/api-exports.md#export-subscriptions)
* [Read Proforma Invoices Export](../../doc/controllers/api-exports.md#read-proforma-invoices-export)
* [Read Invoices Export](../../doc/controllers/api-exports.md#read-invoices-export)
* [Read Subscriptions Export](../../doc/controllers/api-exports.md#read-subscriptions-export)


# List Exported Proforma Invoices

Lists exported proforma invoices for a provided `batch_id`. Use pagination to control responses returned from the server.

Example: `GET https://{subdomain}.chargify.com/api_exports/proforma_invoices/123/rows?per_page=10000&page=1`.

```python
def list_exported_proforma_invoices(self,
                                   options=dict())
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request.<br>Default value is 100.<br>The maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.<br><br>**Default**: `100`<br><br>**Constraints**: `>= 1`, `<= 10000` |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1` |

## Response Type

**200**: OK

[`List[ProformaInvoice]`](../../doc/models/proforma-invoice.md)

## Example Usage

```python
collect = {
    'batch_id': 'batch_id8',
    'per_page': 100,
    'page': 1
}
result = api_exports_controller.list_exported_proforma_invoices(collect)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# List Exported Invoices

Lists exported invoices for a provided `batch_id`. Use pagination to control responses returned from the server.

Example: `GET https://{subdomain}.chargify.com/api_exports/invoices/123/rows?per_page=10000&page=1`.

```python
def list_exported_invoices(self,
                          options=dict())
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request.<br>Default value is 100.<br>The maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.<br><br>**Default**: `100`<br><br>**Constraints**: `>= 1`, `<= 10000` |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1` |

## Response Type

**200**: OK

[`List[Invoice]`](../../doc/models/invoice.md)

## Example Usage

```python
collect = {
    'batch_id': 'batch_id8',
    'per_page': 100,
    'page': 1
}
result = api_exports_controller.list_exported_invoices(collect)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# List Exported Subscriptions

Lists exported subscriptions for a provided `batch_id`. Use pagination to control responses returned from the server.

Example: `GET https://{subdomain}.chargify.com/api_exports/subscriptions/123/rows?per_page=200&page=1`.

```python
def list_exported_subscriptions(self,
                               options=dict())
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request.<br>Default value is 100.<br>The maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.<br><br>**Default**: `100`<br><br>**Constraints**: `>= 1`, `<= 10000` |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1` |

## Response Type

**200**: OK

[`List[Subscription]`](../../doc/models/subscription.md)

## Example Usage

```python
collect = {
    'batch_id': 'batch_id8',
    'per_page': 100,
    'page': 1
}
result = api_exports_controller.list_exported_subscriptions(collect)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# Export Proforma Invoices

Creates a proforma invoices export and returns a batch job object.

It is only available for Relationship Invoicing architecture.

```python
def export_proforma_invoices(self)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Response Type

**201**: Created

[`BatchJobResponse`](../../doc/models/batch-job-response.md)

## Example Usage

```python
result = api_exports_controller.export_proforma_invoices()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |
| 409 | Conflict | [`SingleErrorResponseException`](../../doc/models/single-error-response-exception.md) |


# Export Invoices

Creates an invoices export and returns a batch job object.

```python
def export_invoices(self)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Response Type

**201**: Created

[`BatchJobResponse`](../../doc/models/batch-job-response.md)

## Example Usage

```python
result = api_exports_controller.export_invoices()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |
| 409 | Conflict | [`SingleErrorResponseException`](../../doc/models/single-error-response-exception.md) |


# Export Subscriptions

Creates a subscriptions export and returns a batch job object.

```python
def export_subscriptions(self)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Response Type

**201**: Created

[`BatchJobResponse`](../../doc/models/batch-job-response.md)

## Example Usage

```python
result = api_exports_controller.export_subscriptions()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 409 | Conflict | [`SingleErrorResponseException`](../../doc/models/single-error-response-exception.md) |


# Read Proforma Invoices Export

Returns a batch job object for a proforma invoices export.

```python
def read_proforma_invoices_export(self,
                                 batch_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |

## Response Type

**200**: OK

[`BatchJobResponse`](../../doc/models/batch-job-response.md)

## Example Usage

```python
batch_id = 'batch_id8'

result = api_exports_controller.read_proforma_invoices_export(batch_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# Read Invoices Export

Returns a batch job object for an invoices export.

```python
def read_invoices_export(self,
                        batch_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |

## Response Type

**200**: OK

[`BatchJobResponse`](../../doc/models/batch-job-response.md)

## Example Usage

```python
batch_id = 'batch_id8'

result = api_exports_controller.read_invoices_export(batch_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# Read Subscriptions Export

Returns a batch job object for a subscriptions export.

```python
def read_subscriptions_export(self,
                             batch_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |

## Response Type

**200**: OK

[`BatchJobResponse`](../../doc/models/batch-job-response.md)

## Example Usage

```python
batch_id = 'batch_id8'

result = api_exports_controller.read_subscriptions_export(batch_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |

