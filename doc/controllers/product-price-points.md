# Product Price Points

```python
product_price_points_controller = client.product_price_points
```

## Class Name

`ProductPricePointsController`

## Methods

* [Create Product Price Point](../../doc/controllers/product-price-points.md#create-product-price-point)
* [List Product Price Points](../../doc/controllers/product-price-points.md#list-product-price-points)
* [Update Product Price Point](../../doc/controllers/product-price-points.md#update-product-price-point)
* [Read Product Price Point](../../doc/controllers/product-price-points.md#read-product-price-point)
* [Archive Product Price Point](../../doc/controllers/product-price-points.md#archive-product-price-point)
* [Unarchive Product Price Point](../../doc/controllers/product-price-points.md#unarchive-product-price-point)
* [Promote Product Price Point to Default](../../doc/controllers/product-price-points.md#promote-product-price-point-to-default)
* [Bulk Create Product Price Points](../../doc/controllers/product-price-points.md#bulk-create-product-price-points)
* [Create Product Currency Prices](../../doc/controllers/product-price-points.md#create-product-currency-prices)
* [Update Product Currency Prices](../../doc/controllers/product-price-points.md#update-product-currency-prices)
* [List All Product Price Points](../../doc/controllers/product-price-points.md#list-all-product-price-points)


# Create Product Price Point

[Product Price Point Documentation](https://maxio.zendesk.com/hc/en-us/articles/24261111947789-Product-Price-Points)

```python
def create_product_price_point(self,
                              product_id,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | int \| str | Template, Required | This is a container for one-of cases. |
| `body` | [`CreateProductPricePointRequest`](../../doc/models/create-product-price-point-request.md) | Body, Optional | - |

## Response Type

[`ProductPricePointResponse`](../../doc/models/product-price-point-response.md)

## Example Usage

```python
product_id = 124

body = CreateProductPricePointRequest(
    price_point=CreateProductPricePoint(
        name='Educational',
        price_in_cents=1000,
        interval=1,
        interval_unit=IntervalUnit.MONTH,
        handle='educational',
        trial_price_in_cents=4900,
        trial_interval=1,
        trial_interval_unit=IntervalUnit.MONTH,
        trial_type='payment_expected',
        initial_charge_in_cents=120000,
        initial_charge_after_trial=False,
        expiration_interval=12,
        expiration_interval_unit=ExpirationIntervalUnit.MONTH
    )
)

result = product_price_points_controller.create_product_price_point(
    product_id,
    body=body
)
```

## Example Response *(as JSON)*

```json
{
  "price_point": {
    "id": 283,
    "name": "Educational",
    "handle": "educational",
    "price_in_cents": 1000,
    "interval": 1,
    "interval_unit": "month",
    "trial_price_in_cents": 4900,
    "trial_interval": 1,
    "trial_interval_unit": "month",
    "trial_type": "payment_expected",
    "initial_charge_in_cents": 120000,
    "initial_charge_after_trial": false,
    "expiration_interval": 12,
    "expiration_interval_unit": "month",
    "product_id": 901,
    "archived_at": "2023-11-30T06:37:20-05:00",
    "created_at": "2023-11-27T06:37:20-05:00",
    "updated_at": "2023-11-27T06:37:20-05:00"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ProductPricePointErrorResponseException`](../../doc/models/product-price-point-error-response-exception.md) |


# List Product Price Points

Use this endpoint to retrieve a list of product price points.

```python
def list_product_price_points(self,
                             options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | int \| str | Template, Required | This is a container for one-of cases. |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 10. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>**Default**: `10`<br>**Constraints**: `<= 200` |
| `currency_prices` | `bool` | Query, Optional | When fetching a product's price points, if you have defined multiple currencies at the site level, you can optionally pass the ?currency_prices=true query param to include an array of currency price data in the response. If the product price point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate. If the flag is set to false, it will return all of the defined prices for each currency. |
| `filter_type` | [`List[PricePointType]`](../../doc/models/price-point-type.md) | Query, Optional | Use in query: `filter[type]=catalog,default`. |
| `archived` | `bool` | Query, Optional | Set to include archived price points in the response. |

## Response Type

[`ListProductPricePointsResponse`](../../doc/models/list-product-price-points-response.md)

## Example Usage

```python
collect = {Liquid error: Value cannot be null. (Parameter 'key')
    'product_id': 124,
    'page': 2,
    'per_page': 10
}
result = product_price_points_controller.list_product_price_points(collect)
```

## Example Response *(as JSON)*

```json
{
  "price_points": [
    {
      "id": 283,
      "name": "Educational",
      "handle": "educational",
      "price_in_cents": 1000,
      "interval": 1,
      "interval_unit": "month",
      "trial_price_in_cents": 4900,
      "trial_interval": 1,
      "trial_interval_unit": "month",
      "trial_type": "payment_expected",
      "initial_charge_in_cents": 120000,
      "initial_charge_after_trial": false,
      "expiration_interval": 12,
      "expiration_interval_unit": "month",
      "product_id": 901,
      "archived_at": "2023-11-30T06:37:20-05:00",
      "created_at": "2023-11-27T06:37:20-05:00",
      "updated_at": "2023-11-27T06:37:20-05:00"
    }
  ]
}
```


# Update Product Price Point

Use this endpoint to update a product price point.

Note: Custom product price points are not able to be updated.

```python
def update_product_price_point(self,
                              product_id,
                              price_point_id,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | int \| str | Template, Required | This is a container for one-of cases. |
| `price_point_id` | int \| str | Template, Required | This is a container for one-of cases. |
| `body` | [`UpdateProductPricePointRequest`](../../doc/models/update-product-price-point-request.md) | Body, Optional | - |

## Response Type

[`ProductPricePointResponse`](../../doc/models/product-price-point-response.md)

## Example Usage

```python
product_id = 124

price_point_id = 188

body = UpdateProductPricePointRequest(
    price_point=UpdateProductPricePoint(
        handle='educational',
        price_in_cents=1250
    )
)

result = product_price_points_controller.update_product_price_point(
    product_id,
    price_point_id,
    body=body
)
```

## Example Response *(as JSON)*

```json
{
  "price_point": {
    "id": 283,
    "name": "Educational",
    "handle": "educational",
    "price_in_cents": 1000,
    "interval": 1,
    "interval_unit": "month",
    "trial_price_in_cents": 4900,
    "trial_interval": 1,
    "trial_interval_unit": "month",
    "trial_type": "payment_expected",
    "initial_charge_in_cents": 120000,
    "initial_charge_after_trial": false,
    "expiration_interval": 12,
    "expiration_interval_unit": "month",
    "product_id": 901,
    "archived_at": "2023-11-30T06:37:20-05:00",
    "created_at": "2023-11-27T06:37:20-05:00",
    "updated_at": "2023-11-27T06:37:20-05:00"
  }
}
```


# Read Product Price Point

Use this endpoint to retrieve details for a specific product price point. You can achieve this by using either the product price point ID or handle.

```python
def read_product_price_point(self,
                            product_id,
                            price_point_id,
                            currency_prices=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | int \| str | Template, Required | This is a container for one-of cases. |
| `price_point_id` | int \| str | Template, Required | This is a container for one-of cases. |
| `currency_prices` | `bool` | Query, Optional | When fetching a product's price points, if you have defined multiple currencies at the site level, you can optionally pass the ?currency_prices=true query param to include an array of currency price data in the response. If the product price point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate. If the flag is set to false, it will return all of the defined prices for each currency. |

## Response Type

[`ProductPricePointResponse`](../../doc/models/product-price-point-response.md)

## Example Usage

```python
product_id = 124

price_point_id = 188

result = product_price_points_controller.read_product_price_point(
    product_id,
    price_point_id
)
```

## Example Response *(as JSON)*

```json
{
  "price_point": {
    "id": 283,
    "name": "Educational",
    "handle": "educational",
    "price_in_cents": 1000,
    "interval": 1,
    "interval_unit": "month",
    "trial_price_in_cents": 4900,
    "trial_interval": 1,
    "trial_interval_unit": "month",
    "trial_type": "payment_expected",
    "initial_charge_in_cents": 120000,
    "initial_charge_after_trial": false,
    "expiration_interval": 12,
    "expiration_interval_unit": "month",
    "product_id": 901,
    "archived_at": "2023-11-30T06:37:20-05:00",
    "created_at": "2023-11-27T06:37:20-05:00",
    "updated_at": "2023-11-27T06:37:20-05:00"
  }
}
```


# Archive Product Price Point

Use this endpoint to archive a product price point.

```python
def archive_product_price_point(self,
                               product_id,
                               price_point_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | int \| str | Template, Required | This is a container for one-of cases. |
| `price_point_id` | int \| str | Template, Required | This is a container for one-of cases. |

## Response Type

[`ProductPricePointResponse`](../../doc/models/product-price-point-response.md)

## Example Usage

```python
product_id = 124

price_point_id = 188

result = product_price_points_controller.archive_product_price_point(
    product_id,
    price_point_id
)
```

## Example Response *(as JSON)*

```json
{
  "price_point": {
    "id": 283,
    "name": "Educational",
    "handle": "educational",
    "price_in_cents": 1000,
    "interval": 1,
    "interval_unit": "month",
    "trial_price_in_cents": 4900,
    "trial_interval": 1,
    "trial_interval_unit": "month",
    "trial_type": "payment_expected",
    "initial_charge_in_cents": 120000,
    "initial_charge_after_trial": false,
    "expiration_interval": 12,
    "expiration_interval_unit": "month",
    "product_id": 901,
    "archived_at": "2023-11-30T06:37:20-05:00",
    "created_at": "2023-11-27T06:37:20-05:00",
    "updated_at": "2023-11-27T06:37:20-05:00"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Unarchive Product Price Point

Use this endpoint to unarchive an archived product price point.

```python
def unarchive_product_price_point(self,
                                 product_id,
                                 price_point_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Template, Required | The Advanced Billing id of the product to which the price point belongs |
| `price_point_id` | `int` | Template, Required | The Advanced Billing id of the product price point |

## Response Type

[`ProductPricePointResponse`](../../doc/models/product-price-point-response.md)

## Example Usage

```python
product_id = 202

price_point_id = 10

result = product_price_points_controller.unarchive_product_price_point(
    product_id,
    price_point_id
)
```

## Example Response *(as JSON)*

```json
{
  "price_point": {
    "id": 283,
    "name": "Educational",
    "handle": "educational",
    "price_in_cents": 1000,
    "interval": 1,
    "interval_unit": "month",
    "trial_price_in_cents": 4900,
    "trial_interval": 1,
    "trial_interval_unit": "month",
    "trial_type": "payment_expected",
    "initial_charge_in_cents": 120000,
    "initial_charge_after_trial": false,
    "expiration_interval": 12,
    "expiration_interval_unit": "month",
    "product_id": 901,
    "archived_at": "2023-11-30T06:37:20-05:00",
    "created_at": "2023-11-27T06:37:20-05:00",
    "updated_at": "2023-11-27T06:37:20-05:00"
  }
}
```


# Promote Product Price Point to Default

Use this endpoint to make a product price point the default for the product.

Note: Custom product price points are not able to be set as the default for a product.

```python
def promote_product_price_point_to_default(self,
                                          product_id,
                                          price_point_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Template, Required | The Advanced Billing id of the product to which the price point belongs |
| `price_point_id` | `int` | Template, Required | The Advanced Billing id of the product price point |

## Response Type

[`ProductResponse`](../../doc/models/product-response.md)

## Example Usage

```python
product_id = 202

price_point_id = 10

result = product_price_points_controller.promote_product_price_point_to_default(
    product_id,
    price_point_id
)
```

## Example Response *(as JSON)*

```json
{
  "product": {
    "id": 29778,
    "name": "Educational",
    "handle": "educational",
    "description": null,
    "accounting_code": null,
    "request_credit_card": true,
    "expiration_interval": 12,
    "expiration_interval_unit": "month",
    "created_at": "2023-12-01T06:56:12-05:00",
    "updated_at": "2023-12-01T06:56:26-05:00",
    "price_in_cents": 100,
    "interval": 2,
    "interval_unit": "month",
    "initial_charge_in_cents": 120000,
    "trial_price_in_cents": 4900,
    "trial_interval": 1,
    "trial_interval_unit": "month",
    "archived_at": null,
    "require_credit_card": true,
    "return_params": null,
    "taxable": false,
    "update_return_url": null,
    "tax_code": null,
    "initial_charge_after_trial": false,
    "version_number": 1,
    "update_return_params": null,
    "default_product_price_point_id": 32395,
    "request_billing_address": false,
    "require_billing_address": false,
    "require_shipping_address": false,
    "use_site_exchange_rate": true,
    "item_category": null,
    "product_price_point_id": 32395,
    "product_price_point_name": "Default",
    "product_price_point_handle": "uuid:8c878f50-726e-013c-c71b-0286551bb34f",
    "product_family": {
      "id": 933860,
      "name": "Acme Projects",
      "description": "Amazing project management tool",
      "handle": "acme-projects",
      "accounting_code": null,
      "created_at": "2023-12-01T06:56:12-05:00",
      "updated_at": "2023-12-01T06:56:12-05:00"
    }
  }
}
```


# Bulk Create Product Price Points

Use this endpoint to create multiple product price points in one request.

```python
def bulk_create_product_price_points(self,
                                    product_id,
                                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Template, Required | The Advanced Billing id of the product to which the price points belong |
| `body` | [`BulkCreateProductPricePointsRequest`](../../doc/models/bulk-create-product-price-points-request.md) | Body, Optional | - |

## Response Type

[`BulkCreateProductPricePointsResponse`](../../doc/models/bulk-create-product-price-points-response.md)

## Example Usage

```python
product_id = 202

body = BulkCreateProductPricePointsRequest(
    price_points=[
        CreateProductPricePoint(
            name='Educational',
            price_in_cents=1000,
            interval=1,
            interval_unit=IntervalUnit.MONTH,
            handle='educational',
            trial_price_in_cents=4900,
            trial_interval=1,
            trial_interval_unit=IntervalUnit.MONTH,
            trial_type='payment_expected',
            initial_charge_in_cents=120000,
            initial_charge_after_trial=False,
            expiration_interval=12,
            expiration_interval_unit=ExpirationIntervalUnit.MONTH
        ),
        CreateProductPricePoint(
            name='More Educational',
            price_in_cents=2000,
            interval=1,
            interval_unit=IntervalUnit.MONTH,
            handle='more-educational',
            trial_price_in_cents=4900,
            trial_interval=1,
            trial_interval_unit=IntervalUnit.MONTH,
            trial_type='payment_expected',
            initial_charge_in_cents=120000,
            initial_charge_after_trial=False,
            expiration_interval=12,
            expiration_interval_unit=ExpirationIntervalUnit.MONTH
        )
    ]
)

result = product_price_points_controller.bulk_create_product_price_points(
    product_id,
    body=body
)
```

## Example Response *(as JSON)*

```json
{
  "price_points": [
    {
      "id": 283,
      "name": "Educational",
      "handle": "educational",
      "price_in_cents": 1000,
      "interval": 1,
      "interval_unit": "month",
      "trial_price_in_cents": 4900,
      "trial_interval": 1,
      "trial_interval_unit": "month",
      "trial_type": "payment_expected",
      "initial_charge_in_cents": 120000,
      "initial_charge_after_trial": false,
      "expiration_interval": 12,
      "expiration_interval_unit": "month",
      "product_id": 901,
      "archived_at": "2023-11-30T06:37:20-05:00",
      "created_at": "2023-11-27T06:37:20-05:00",
      "updated_at": "2023-11-27T06:37:20-05:00"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | `APIException` |


# Create Product Currency Prices

This endpoint allows you to create currency prices for a given currency that has been defined on the site level in your settings.

When creating currency prices, they need to mirror the structure of your primary pricing. If the product price point defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

Note: Currency Prices are not able to be created for custom product price points.

```python
def create_product_currency_prices(self,
                                  product_price_point_id,
                                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_price_point_id` | `int` | Template, Required | The Advanced Billing id of the product price point |
| `body` | [`CreateProductCurrencyPricesRequest`](../../doc/models/create-product-currency-prices-request.md) | Body, Optional | - |

## Response Type

[`CurrencyPricesResponse`](../../doc/models/currency-prices-response.md)

## Example Usage

```python
product_price_point_id = 234

body = CreateProductCurrencyPricesRequest(
    currency_prices=[
        CreateProductCurrencyPrice(
            currency='EUR',
            price=60,
            role=CurrencyPriceRole.BASELINE
        ),
        CreateProductCurrencyPrice(
            currency='EUR',
            price=30,
            role=CurrencyPriceRole.TRIAL
        ),
        CreateProductCurrencyPrice(
            currency='EUR',
            price=100,
            role=CurrencyPriceRole.INITIAL
        )
    ]
)

result = product_price_points_controller.create_product_currency_prices(
    product_price_point_id,
    body=body
)
```

## Example Response *(as JSON)*

```json
{
  "currency_prices": [
    {
      "id": 100,
      "currency": "EUR",
      "price": 123,
      "formatted_price": "€123,00",
      "product_price_point_id": 32669,
      "role": "baseline"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorArrayMapResponseException`](../../doc/models/error-array-map-response-exception.md) |


# Update Product Currency Prices

This endpoint allows you to update the `price`s of currency prices for a given currency that exists on the product price point.

When updating the pricing, it needs to mirror the structure of your primary pricing. If the product price point defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

Note: Currency Prices are not able to be updated for custom product price points.

```python
def update_product_currency_prices(self,
                                  product_price_point_id,
                                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_price_point_id` | `int` | Template, Required | The Advanced Billing id of the product price point |
| `body` | [`UpdateCurrencyPricesRequest`](../../doc/models/update-currency-prices-request.md) | Body, Optional | - |

## Response Type

[`CurrencyPricesResponse`](../../doc/models/currency-prices-response.md)

## Example Usage

```python
product_price_point_id = 234

body = UpdateCurrencyPricesRequest(
    currency_prices=[
        UpdateCurrencyPrice(
            id=200,
            price=15
        ),
        UpdateCurrencyPrice(
            id=201,
            price=5
        )
    ]
)

result = product_price_points_controller.update_product_currency_prices(
    product_price_point_id,
    body=body
)
```

## Example Response *(as JSON)*

```json
{
  "currency_prices": [
    {
      "id": 123,
      "currency": "EUR",
      "price": 100,
      "formatted_price": "€123,00",
      "product_price_point_id": 32669,
      "role": "baseline"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorArrayMapResponseException`](../../doc/models/error-array-map-response-exception.md) |


# List All Product Price Points

This method allows retrieval of a list of Products Price Points belonging to a Site.

```python
def list_all_product_price_points(self,
                                 options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `direction` | [`SortingDirection`](../../doc/models/sorting-direction.md) | Query, Optional | Controls the order in which results are returned.<br>Use in query `direction=asc`. |
| `filter` | [`ListPricePointsFilter`](../../doc/models/list-price-points-filter.md) | Query, Optional | Filter to use for List PricePoints operations |
| `include` | [`ListProductsPricePointsInclude`](../../doc/models/list-products-price-points-include.md) | Query, Optional | Allows including additional data in the response. Use in query: `include=currency_prices`. |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `20`<br>**Constraints**: `<= 200` |

## Response Type

[`ListProductPricePointsResponse`](../../doc/models/list-product-price-points-response.md)

## Example Usage

```python
collect = {
    'filter': ListPricePointsFilter(
        start_date=dateutil.parser.parse('2011-12-17').date(),
        end_date=dateutil.parser.parse('2011-12-15').date(),
        start_datetime=dateutil.parser.parse('12/19/2011 09:15:30'),
        end_datetime=dateutil.parser.parse('06/07/2019 17:20:06'),
        mtype=[
            PricePointType.CATALOG,
            PricePointType.DEFAULT,
            PricePointType.CUSTOM
        ],
        ids=[
            1,
            2,
            3
        ]
    ),
    'include': ListProductsPricePointsInclude.CURRENCY_PRICES,
    'page': 2,
    'per_page': 50
}
result = product_price_points_controller.list_all_product_price_points(collect)
```

## Example Response *(as JSON)*

```json
{
  "price_points": [
    {
      "id": 0,
      "name": "My pricepoint",
      "handle": "handle",
      "price_in_cents": 10,
      "interval": 5,
      "interval_unit": "month",
      "trial_price_in_cents": 10,
      "trial_interval": 1,
      "trial_interval_unit": "month",
      "trial_type": "payment_expected",
      "introductory_offer": true,
      "initial_charge_in_cents": 0,
      "initial_charge_after_trial": true,
      "expiration_interval": 0,
      "expiration_interval_unit": "month",
      "product_id": 1230,
      "created_at": "2021-04-02T17:52:09-04:00",
      "updated_at": "2021-04-02T17:52:09-04:00",
      "use_site_exchange_rate": true
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |

