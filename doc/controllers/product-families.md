# Product Families

```python
product_families_controller = client.product_families
```

## Class Name

`ProductFamiliesController`

## Methods

* [List Products for Product Family](../../doc/controllers/product-families.md#list-products-for-product-family)
* [Create Product Family](../../doc/controllers/product-families.md#create-product-family)
* [List Product Families](../../doc/controllers/product-families.md#list-product-families)
* [Read Product Family](../../doc/controllers/product-families.md#read-product-family)


# List Products for Product Family

This method allows to retrieve a list of Products belonging to a Product Family.

```python
def list_products_for_product_family(self,
                                    options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_family_id` | `str` | Template, Required | Either the product family's id or its handle prefixed with `handle:` |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br><br>**Default**: `20`<br><br>**Constraints**: `<= 200` |
| `date_field` | [`BasicDateField`](../../doc/models/basic-date-field.md) | Query, Optional | The type of filter you would like to apply to your search.<br>Use in query: `date_field=created_at`. |
| `filter` | [`ListProductsFilter`](../../doc/models/list-products-filter.md) | Query, Optional | Filter to use for List Products operations |
| `start_date` | `date` | Query, Optional | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. |
| `end_date` | `date` | Query, Optional | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. |
| `start_datetime` | `datetime` | Query, Optional | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns products with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date. |
| `end_datetime` | `datetime` | Query, Optional | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns products with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date. |
| `include_archived` | `bool` | Query, Optional | Include archived products |
| `include` | [`ListProductsInclude`](../../doc/models/list-products-include.md) | Query, Optional | Allows including additional data in the response. Use in query `include=prepaid_product_price_point`. |

## Response Type

[`List[ProductResponse]`](../../doc/models/product-response.md)

## Example Usage

```python
collect = {
    'product_family_id': 'product_family_id4',
    'page': 2,
    'per_page': 50,
    'date_field': BasicDateField.UPDATED_AT,
    'filter': ListProductsFilter(
        ids=[
            1,
            2,
            3
        ]
    ),
    'include': ListProductsInclude.PREPAID_PRODUCT_PRICE_POINT
}
result = product_families_controller.list_products_for_product_family(collect)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "product": {
      "id": 3801242,
      "name": "Free product",
      "handle": "zero-dollar-product",
      "description": "",
      "accounting_code": "",
      "request_credit_card": true,
      "expiration_interval": null,
      "expiration_interval_unit": "never",
      "created_at": "2016-04-21T16:08:39-04:00",
      "updated_at": "2016-08-03T11:27:53-04:00",
      "price_in_cents": 10000,
      "interval": 1,
      "interval_unit": "month",
      "initial_charge_in_cents": 0,
      "trial_price_in_cents": null,
      "trial_interval": null,
      "trial_interval_unit": "month",
      "archived_at": null,
      "require_credit_card": false,
      "return_params": "",
      "taxable": false,
      "update_return_url": "",
      "initial_charge_after_trial": false,
      "version_number": 4,
      "update_return_params": "",
      "product_family": {
        "id": 527890,
        "name": "Acme Projects",
        "description": "",
        "handle": "billing-plans",
        "accounting_code": null
      },
      "public_signup_pages": [
        {
          "id": 283460,
          "return_url": null,
          "return_params": "",
          "url": "https://general-goods.chargify.com/subscribe/smcc4j3d2w6h/zero-dollar-product"
        }
      ],
      "product_price_point_name": "Default",
      "use_site_exchange_rate": true
    }
  },
  {
    "product": {
      "id": 3858146,
      "name": "Calendar Billing Product",
      "handle": "calendar-billing-product",
      "description": "",
      "accounting_code": "",
      "request_credit_card": true,
      "expiration_interval": null,
      "expiration_interval_unit": "never",
      "created_at": "2016-07-05T13:07:38-04:00",
      "updated_at": "2016-07-05T13:07:38-04:00",
      "price_in_cents": 10000,
      "interval": 1,
      "interval_unit": "month",
      "initial_charge_in_cents": null,
      "trial_price_in_cents": null,
      "trial_interval": null,
      "trial_interval_unit": "month",
      "archived_at": null,
      "require_credit_card": true,
      "return_params": "",
      "taxable": false,
      "update_return_url": "",
      "initial_charge_after_trial": false,
      "version_number": 1,
      "update_return_params": "",
      "product_family": {
        "id": 527890,
        "name": "Acme Projects",
        "description": "",
        "handle": "billing-plans",
        "accounting_code": null
      },
      "public_signup_pages": [
        {
          "id": 289193,
          "return_url": "",
          "return_params": "",
          "url": "https://general-goods.chargify.com/subscribe/gxdbfxzxhcjq/calendar-billing-product"
        }
      ],
      "product_price_point_name": "Default",
      "use_site_exchange_rate": true
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# Create Product Family

This method will create a Product Family within your Advanced Billing site. Create a Product Family to act as a container for your products, components and coupons.

Full documentation on how Product Families operate within the Advanced Billing UI can be located [here](https://maxio.zendesk.com/hc/en-us/articles/24261098936205-Product-Families).

```python
def create_product_family(self,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateProductFamilyRequest`](../../doc/models/create-product-family-request.md) | Body, Optional | - |

## Response Type

[`ProductFamilyResponse`](../../doc/models/product-family-response.md)

## Example Usage

```python
body = CreateProductFamilyRequest(
    product_family=CreateProductFamily(
        name='Acme Projects',
        description='Amazing project management tool'
    )
)

result = product_families_controller.create_product_family(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "product_family": {
    "id": 933860,
    "name": "Acme Projects",
    "description": "Amazing project management tool",
    "handle": "acme-projects",
    "accounting_code": null
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# List Product Families

This method allows to retrieve a list of Product Families for a site.

```python
def list_product_families(self,
                         options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_field` | [`BasicDateField`](../../doc/models/basic-date-field.md) | Query, Optional | The type of filter you would like to apply to your search.<br>Use in query: `date_field=created_at`. |
| `start_date` | `date` | Query, Optional | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. |
| `end_date` | `date` | Query, Optional | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. |
| `start_datetime` | `datetime` | Query, Optional | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns products with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date. |
| `end_datetime` | `datetime` | Query, Optional | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns products with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date. |

## Response Type

[`List[ProductFamilyResponse]`](../../doc/models/product-family-response.md)

## Example Usage

```python
collect = {
    'date_field': BasicDateField.UPDATED_AT
}
result = product_families_controller.list_product_families(collect)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "product_family": {
      "id": 37,
      "name": "Acme Projects",
      "description": null,
      "handle": "acme-projects",
      "accounting_code": null,
      "created_at": "2013-02-20T15:05:51-07:00",
      "updated_at": "2013-02-20T15:05:51-07:00"
    }
  },
  {
    "product_family": {
      "id": 155,
      "name": "Bat Family",
      "description": "Another family.",
      "handle": "bat-family",
      "accounting_code": null,
      "created_at": "2014-04-16T12:41:13-06:00",
      "updated_at": "2014-04-16T12:41:13-06:00"
    }
  }
]
```


# Read Product Family

This method allows to retrieve a Product Family via the `product_family_id`. The response will contain a Product Family object.

The product family can be specified either with the id number, or with the `handle:my-family` format.

```python
def read_product_family(self,
                       id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | The Advanced Billing id of the product family |

## Response Type

[`ProductFamilyResponse`](../../doc/models/product-family-response.md)

## Example Usage

```python
id = 112

result = product_families_controller.read_product_family(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "product_family": {
    "id": 527890,
    "name": "Acme Projects",
    "description": "",
    "handle": "billing-plans",
    "accounting_code": null
  }
}
```

