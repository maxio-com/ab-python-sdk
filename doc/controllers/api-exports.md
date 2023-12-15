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

This API returns an array of exported proforma invoices for a provided `batch_id`. Pay close attention to pagination in order to control responses from the server.

Example: `GET https://{subdomain}.chargify.com/api_exports/proforma_invoices/123/rows?per_page=10000&page=1`.

```python
def list_exported_proforma_invoices(self,
                                   options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request.<br>Default value is 100.<br>The maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.<br>**Default**: `100`<br>**Constraints**: `>= 1`, `<= 10000` |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |

## Response Type

[`List[ProformaInvoice]`](../../doc/models/proforma-invoice.md)

## Example Usage

```python
collect = {
    'batch_id': 'batch_id8',
    'per_page': 100,
    'page': 2
}
result = api_exports_controller.list_exported_proforma_invoices(collect)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# List Exported Invoices

This API returns an array of exported invoices for a provided `batch_id`. Pay close attention to pagination in order to control responses from the server.

Example: `GET https://{subdomain}.chargify.com/api_exports/invoices/123/rows?per_page=10000&page=1`.

```python
def list_exported_invoices(self,
                          options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request.<br>Default value is 100.<br>The maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.<br>**Default**: `100`<br>**Constraints**: `>= 1`, `<= 10000` |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |

## Response Type

[`List[Invoice]`](../../doc/models/invoice.md)

## Example Usage

```python
collect = {
    'batch_id': 'batch_id8',
    'per_page': 100,
    'page': 2
}
result = api_exports_controller.list_exported_invoices(collect)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# List Exported Subscriptions

This API returns an array of exported subscriptions for a provided `batch_id`. Pay close attention to pagination in order to control responses from the server.

Example: `GET https://{subdomain}.chargify.com/api_exports/subscriptions/123/rows?per_page=200&page=1`.

```python
def list_exported_subscriptions(self,
                               options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request.<br>Default value is 100.<br>The maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.<br>**Default**: `100`<br>**Constraints**: `>= 1`, `<= 10000` |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |

## Response Type

[`List[Subscription]`](../../doc/models/subscription.md)

## Example Usage

```python
collect = {
    'batch_id': 'batch_id8',
    'per_page': 100,
    'page': 2
}
result = api_exports_controller.list_exported_subscriptions(collect)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# Export Proforma Invoices

This API creates a proforma invoices export and returns a batchjob object.

It is only available for Relationship Invoicing architecture.

```python
def export_proforma_invoices(self)
```

## Response Type

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
| 409 | Conflict | [`SingleErrorResponseErrorException`](../../doc/models/single-error-response-error-exception.md) |


# Export Invoices

This API creates an invoices export and returns a batchjob object.

```python
def export_invoices(self)
```

## Response Type

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
| 409 | Conflict | [`SingleErrorResponseErrorException`](../../doc/models/single-error-response-error-exception.md) |


# Export Subscriptions

This API creates a subscriptions export and returns a batchjob object.

```python
def export_subscriptions(self)
```

## Response Type

[`BatchJobResponse`](../../doc/models/batch-job-response.md)

## Example Usage

```python
result = api_exports_controller.export_subscriptions()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 409 | Conflict | [`SingleErrorResponseErrorException`](../../doc/models/single-error-response-error-exception.md) |


# Read Proforma Invoices Export

This API returns a batchjob object for proforma invoices export.

```python
def read_proforma_invoices_export(self,
                                 batch_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |

## Response Type

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

This API returns a batchjob object for invoices export.

```python
def read_invoices_export(self,
                        batch_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |

## Response Type

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

This API returns a batchjob object for subscriptions export.

```python
def read_subscriptions_export(self,
                             batch_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch_id` | `str` | Template, Required | Id of a Batch Job. |

## Response Type

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

