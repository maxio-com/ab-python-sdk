# Proforma Invoices

```python
proforma_invoices_controller = client.proforma_invoices
```

## Class Name

`ProformaInvoicesController`

## Methods

* [Create Consolidated Proforma Invoice](../../doc/controllers/proforma-invoices.md#create-consolidated-proforma-invoice)
* [List Subscription Group Proforma Invoices](../../doc/controllers/proforma-invoices.md#list-subscription-group-proforma-invoices)
* [Read Proforma Invoice](../../doc/controllers/proforma-invoices.md#read-proforma-invoice)
* [Create Proforma Invoice](../../doc/controllers/proforma-invoices.md#create-proforma-invoice)
* [List Proforma Invoices](../../doc/controllers/proforma-invoices.md#list-proforma-invoices)
* [Void Proforma Invoice](../../doc/controllers/proforma-invoices.md#void-proforma-invoice)
* [Preview Proforma Invoice](../../doc/controllers/proforma-invoices.md#preview-proforma-invoice)
* [Create Signup Proforma Invoice](../../doc/controllers/proforma-invoices.md#create-signup-proforma-invoice)
* [Preview Signup Proforma Invoice](../../doc/controllers/proforma-invoices.md#preview-signup-proforma-invoice)


# Create Consolidated Proforma Invoice

This endpoint will trigger the creation of a consolidated proforma invoice asynchronously. It will return a 201 with no message, or a 422 with any errors. To find and view the new consolidated proforma invoice, you may poll the subscription group listing for proforma invoices; only one consolidated proforma invoice may be created per group at a time.

If the information becomes outdated, simply void the old consolidated proforma invoice and generate a new one.

## Restrictions

Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the subscription must not be prepaid, and must be in a live state.

```python
def create_consolidated_proforma_invoice(self,
                                        uid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Template, Required | The uid of the subscription group |

## Response Type

`void`

## Example Usage

```python
uid = 'uid0'

result = proforma_invoices_controller.create_consolidated_proforma_invoice(uid)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# List Subscription Group Proforma Invoices

Only proforma invoices with a `consolidation_level` of parent are returned.

By default, proforma invoices returned on the index will only include totals, not detailed breakdowns for `line_items`, `discounts`, `taxes`, `credits`, `payments`, `custom_fields`. To include breakdowns, pass the specific field as a key in the query with a value set to true.

```python
def list_subscription_group_proforma_invoices(self,
                                             uid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Template, Required | The uid of the subscription group |

## Response Type

[`ProformaInvoice`](../../doc/models/proforma-invoice.md)

## Example Usage

```python
uid = 'uid0'

result = proforma_invoices_controller.list_subscription_group_proforma_invoices(uid)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | `APIException` |


# Read Proforma Invoice

Use this endpoint to read the details of an existing proforma invoice.

## Restrictions

Proforma invoices are only available on Relationship Invoicing sites.

```python
def read_proforma_invoice(self,
                         proforma_invoice_uid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `proforma_invoice_uid` | `int` | Template, Required | The uid of the proforma invoice |

## Response Type

[`ProformaInvoice`](../../doc/models/proforma-invoice.md)

## Example Usage

```python
proforma_invoice_uid = 242

result = proforma_invoices_controller.read_proforma_invoice(proforma_invoice_uid)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | `APIException` |


# Create Proforma Invoice

This endpoint will create a proforma invoice and return it as a response. If the information becomes outdated, simply void the old proforma invoice and generate a new one.

If you would like to preview the next billing amounts without generating a full proforma invoice, please use the renewal preview endpoint.

## Restrictions

Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the subscription must not be in a group, must not be prepaid, and must be in a live state.

```python
def create_proforma_invoice(self,
                           subscription_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription |

## Response Type

[`ProformaInvoice`](../../doc/models/proforma-invoice.md)

## Example Usage

```python
subscription_id = 222

result = proforma_invoices_controller.create_proforma_invoice(subscription_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# List Proforma Invoices

By default, proforma invoices returned on the index will only include totals, not detailed breakdowns for `line_items`, `discounts`, `taxes`, `credits`, `payments`, or `custom_fields`. To include breakdowns, pass the specific field as a key in the query with a value set to `true`.

```python
def list_proforma_invoices(self,
                          options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription |
| `start_date` | `str` | Query, Optional | The beginning date range for the invoice's Due Date, in the YYYY-MM-DD format. |
| `end_date` | `str` | Query, Optional | The ending date range for the invoice's Due Date, in the YYYY-MM-DD format. |
| `status` | [`InvoiceStatus`](../../doc/models/invoice-status.md) | Query, Optional | The current status of the invoice.  Allowed Values: draft, open, paid, pending, voided |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `20`<br>**Constraints**: `<= 200` |
| `direction` | [`Direction`](../../doc/models/direction.md) | Query, Optional | The sort direction of the returned invoices.<br>**Default**: `'desc'` |
| `line_items` | `bool` | Query, Optional | Include line items data<br>**Default**: `False` |
| `discounts` | `bool` | Query, Optional | Include discounts data<br>**Default**: `False` |
| `taxes` | `bool` | Query, Optional | Include taxes data<br>**Default**: `False` |
| `credits` | `bool` | Query, Optional | Include credits data<br>**Default**: `False` |
| `payments` | `bool` | Query, Optional | Include payments data<br>**Default**: `False` |
| `custom_fields` | `bool` | Query, Optional | Include custom fields data<br>**Default**: `False` |

## Response Type

[`List[ProformaInvoice]`](../../doc/models/proforma-invoice.md)

## Example Usage

```python
collect = {
    'subscription_id': 222,
    'page': 2,
    'per_page': 50,
    'direction': Direction.DESC,
    'line_items': False,
    'discounts': False,
    'taxes': False,
    'credits': False,
    'payments': False,
    'custom_fields': False
}
result = proforma_invoices_controller.list_proforma_invoices(collect)
print(result)
```


# Void Proforma Invoice

This endpoint will void a proforma invoice that has the status "draft".

## Restrictions

Proforma invoices are only available on Relationship Invoicing sites.

Only proforma invoices that have the appropriate status may be reopened. If the invoice identified by {uid} does not have the appropriate status, the response will have HTTP status code 422 and an error message.

A reason for the void operation is required to be included in the request body. If one is not provided, the response will have HTTP status code 422 and an error message.

```python
def void_proforma_invoice(self,
                         proforma_invoice_uid,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `proforma_invoice_uid` | `str` | Template, Required | The uid of the proforma invoice |
| `body` | [`VoidInvoiceRequest`](../../doc/models/void-invoice-request.md) | Body, Optional | - |

## Response Type

[`ProformaInvoice`](../../doc/models/proforma-invoice.md)

## Example Usage

```python
proforma_invoice_uid = 'proforma_invoice_uid4'

result = proforma_invoices_controller.void_proforma_invoice(proforma_invoice_uid)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Preview Proforma Invoice

Return a preview of the data that will be included on a given subscription's proforma invoice if one were to be generated. It will have similar line items and totals as a renewal preview, but the response will be presented in the format of a proforma invoice. Consequently it will include additional information such as the name and addresses that will appear on the proforma invoice.

The preview endpoint is subject to all the same conditions as the proforma invoice endpoint. For example, previews are only available on the Relationship Invoicing architecture, and previews cannot be made for end-of-life subscriptions.

If all the data returned in the preview is as expected, you may then create a static proforma invoice and send it to your customer. The data within a preview will not be saved and will not be accessible after the call is made.

Alternatively, if you have some proforma invoices already, you may make a preview call to determine whether any billing information for the subscription's upcoming renewal has changed.

```python
def preview_proforma_invoice(self,
                            subscription_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription |

## Response Type

[`ProformaInvoicePreview`](../../doc/models/proforma-invoice-preview.md)

## Example Usage

```python
subscription_id = 222

result = proforma_invoices_controller.preview_proforma_invoice(subscription_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Create Signup Proforma Invoice

This endpoint is only available for Relationship Invoicing sites. It cannot be used to create consolidated proforma invoices or preview prepaid subscriptions.

Create a proforma invoice to preview costs before a subscription's signup. Like other proforma invoices, it can be emailed to the customer, voided, and publicly viewed on the chargifypay domain.

Pass a payload that resembles a subscription create or signup preview request. For example, you can specify components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate a shipping or billing address.

A product and customer first name, last name, and email are the minimum requirements. We recommend associating the proforma invoice with a customer_id to easily find their proforma invoices, since the subscription_id will always be blank.

```python
def create_signup_proforma_invoice(self,
                                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateSubscriptionRequest`](../../doc/models/create-subscription-request.md) | Body, Optional | - |

## Response Type

[`ProformaInvoice`](../../doc/models/proforma-invoice.md)

## Example Usage

```python
body = CreateSubscriptionRequest(
    subscription=CreateSubscription(
        product_handle='gold-product',
        customer_attributes=CustomerAttributes(
            first_name='Myra',
            last_name='Maisel',
            email='mmaisel@example.com'
        )
    )
)

result = proforma_invoices_controller.create_signup_proforma_invoice(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ProformaBadRequestErrorResponseException`](../../doc/models/proforma-bad-request-error-response-exception.md) |
| 403 | Forbidden | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorMapResponseException`](../../doc/models/error-map-response-exception.md) |


# Preview Signup Proforma Invoice

This endpoint is only available for Relationship Invoicing sites. It cannot be used to create consolidated proforma invoice previews or preview prepaid subscriptions.

Create a signup preview in the format of a proforma invoice to preview costs before a subscription's signup. You have the option of optionally previewing the first renewal's costs as well. The proforma invoice preview will not be persisted.

Pass a payload that resembles a subscription create or signup preview request. For example, you can specify components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate a shipping or billing address.

A product and customer first name, last name, and email are the minimum requirements.

```python
def preview_signup_proforma_invoice(self,
                                   include_next_proforma_invoice=None,
                                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_next_proforma_invoice` | `str` | Query, Optional | Choose to include a proforma invoice preview for the first renewal |
| `body` | [`CreateSubscriptionRequest`](../../doc/models/create-subscription-request.md) | Body, Optional | - |

## Response Type

[`SignupProformaPreviewResponse`](../../doc/models/signup-proforma-preview-response.md)

## Example Usage

```python
body = CreateSubscriptionRequest(
    subscription=CreateSubscription(
        product_handle='gold-plan',
        customer_attributes=CustomerAttributes(
            first_name='first',
            last_name='last',
            email='flast@example.com'
        )
    )
)

result = proforma_invoices_controller.preview_signup_proforma_invoice(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ProformaBadRequestErrorResponseException`](../../doc/models/proforma-bad-request-error-response-exception.md) |
| 403 | Forbidden | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorMapResponseException`](../../doc/models/error-map-response-exception.md) |

