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
* [Set Default Price Point for Product](../../doc/controllers/product-price-points.md#set-default-price-point-for-product)
* [Create Product Price Points](../../doc/controllers/product-price-points.md#create-product-price-points)
* [Create Product Currency Prices](../../doc/controllers/product-price-points.md#create-product-currency-prices)
* [Update Product Currency Prices](../../doc/controllers/product-price-points.md#update-product-currency-prices)
* [List All Product Price Points](../../doc/controllers/product-price-points.md#list-all-product-price-points)


# Create Product Price Point

[Product Price Point Documentation](https://chargify.zendesk.com/hc/en-us/articles/4407755824155)

```python
def create_product_price_point(self,
                              product_id,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Template, Required | The id or handle of the product. When using the handle, it must be prefixed with `handle:` |
| `body` | [`CreateProductPricePointRequest`](../../doc/models/create-product-price-point-request.md) | Body, Optional | - |

## Response Type

[`ProductPricePointResponse`](../../doc/models/product-price-point-response.md)

## Example Usage

```python
product_id = 202

body = CreateProductPricePointRequest(
    price_point=CreateProductPricePoint(
        name='Educational',
        price_in_cents=1000,
        interval=1,
        interval_unit='month',
        handle='educational',
        trial_price_in_cents=4900,
        trial_interval=1,
        trial_interval_unit='month',
        trial_type='payment_expected',
        initial_charge_in_cents=120000,
        initial_charge_after_trial=False,
        expiration_interval=12,
        expiration_interval_unit='month'
    )
)

result = product_price_points_controller.create_product_price_point(
    product_id,
    body=body
)
print(result)
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
    "archived_at": "Tue, 30 Oct 2018 18:49:47 EDT -04:00",
    "created_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00",
    "updated_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00"
  }
}
```


# List Product Price Points

Use this endpoint to retrieve a list of product price points.

```python
def list_product_price_points(self,
                             product_id,
                             page=1,
                             per_page=10,
                             currency_prices=None,
                             filter_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Template, Required | The id or handle of the product. When using the handle, it must be prefixed with `handle:` |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 10. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>**Default**: `10`<br>**Constraints**: `<= 200` |
| `currency_prices` | `bool` | Query, Optional | When fetching a product's price points, if you have defined multiple currencies at the site level, you can optionally pass the ?currency_prices=true query param to include an array of currency price data in the response. If the product price point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate. If the flag is set to false, it will return all of the defined prices for each currency. |
| `filter_type` | [`List[PricePointTypeEnum]`](../../doc/models/price-point-type-enum.md) | Query, Optional | Use in query: `filter[type]=catalog,default`. |

## Response Type

[`ListProductPricePointsResponse`](../../doc/models/list-product-price-points-response.md)

## Example Usage

```python
product_id = 202

page = 2

per_page = 10

Liquid error: Value cannot be null. (Parameter 'key')result = product_price_points_controller.list_product_price_points(Liquid error: Value cannot be null. (Parameter 'key')
    product_id,
    page=page,
    per_page=per_page
)
print(result)
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
      "archived_at": "Tue, 30 Oct 2018 18:49:47 EDT -04:00",
      "created_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00",
      "updated_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00"
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
| `product_id` | `int` | Template, Required | The id or handle of the product. When using the handle, it must be prefixed with `handle:` |
| `price_point_id` | `int` | Template, Required | The id or handle of the price point. When using the handle, it must be prefixed with `handle:` |
| `body` | [`UpdateProductPricePointRequest`](../../doc/models/update-product-price-point-request.md) | Body, Optional | - |

## Response Type

[`ProductPricePointResponse`](../../doc/models/product-price-point-response.md)

## Example Usage

```python
product_id = 202

price_point_id = 10

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
print(result)
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
    "archived_at": "Tue, 30 Oct 2018 18:49:47 EDT -04:00",
    "created_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00",
    "updated_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00"
  }
}
```


# Read Product Price Point

Use this endpoint to retrieve details for a specific product price point.

```python
def read_product_price_point(self,
                            product_id,
                            price_point_id,
                            currency_prices=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Template, Required | The id or handle of the product. When using the handle, it must be prefixed with `handle:` |
| `price_point_id` | `int` | Template, Required | The id or handle of the price point. When using the handle, it must be prefixed with `handle:` |
| `currency_prices` | `bool` | Query, Optional | When fetching a product's price points, if you have defined multiple currencies at the site level, you can optionally pass the ?currency_prices=true query param to include an array of currency price data in the response. If the product price point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate. If the flag is set to false, it will return all of the defined prices for each currency. |

## Response Type

[`ProductPricePointResponse`](../../doc/models/product-price-point-response.md)

## Example Usage

```python
product_id = 202

price_point_id = 10

result = product_price_points_controller.read_product_price_point(
    product_id,
    price_point_id
)
print(result)
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
    "archived_at": "Tue, 30 Oct 2018 18:49:47 EDT -04:00",
    "created_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00",
    "updated_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00"
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
| `product_id` | `int` | Template, Required | The id or handle of the product. When using the handle, it must be prefixed with `handle:` |
| `price_point_id` | `int` | Template, Required | The id or handle of the price point. When using the handle, it must be prefixed with `handle:` |

## Response Type

[`ProductPricePointResponse`](../../doc/models/product-price-point-response.md)

## Example Usage

```python
product_id = 202

price_point_id = 10

result = product_price_points_controller.archive_product_price_point(
    product_id,
    price_point_id
)
print(result)
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
    "archived_at": "Tue, 30 Oct 2018 18:49:47 EDT -04:00",
    "created_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00",
    "updated_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00"
  }
}
```


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
| `product_id` | `int` | Template, Required | The Chargify id of the product to which the price point belongs |
| `price_point_id` | `int` | Template, Required | The Chargify id of the product price point |

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
print(result)
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
    "archived_at": "Tue, 30 Oct 2018 18:49:47 EDT -04:00",
    "created_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00",
    "updated_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00"
  }
}
```


# Set Default Price Point for Product

Use this endpoint to make a product price point the default for the product.

Note: Custom product price points are not able to be set as the default for a product.

```python
def set_default_price_point_for_product(self,
                                       product_id,
                                       price_point_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Template, Required | The Chargify id of the product to which the price point belongs |
| `price_point_id` | `int` | Template, Required | The Chargify id of the product price point |

## Response Type

[`ProductPricePointResponse`](../../doc/models/product-price-point-response.md)

## Example Usage

```python
product_id = 202

price_point_id = 10

result = product_price_points_controller.set_default_price_point_for_product(
    product_id,
    price_point_id
)
print(result)
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
    "archived_at": "Tue, 30 Oct 2018 18:49:47 EDT -04:00",
    "created_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00",
    "updated_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00"
  }
}
```


# Create Product Price Points

Use this endpoint to create multiple product price points in one request.

```python
def create_product_price_points(self,
                               product_id,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Template, Required | The Chargify id of the product to which the price points belong |
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
            interval_unit='month',
            handle='educational',
            trial_price_in_cents=4900,
            trial_interval=1,
            trial_interval_unit='month',
            trial_type='payment_expected',
            initial_charge_in_cents=120000,
            initial_charge_after_trial=False,
            expiration_interval=12,
            expiration_interval_unit='month'
        ),
        CreateProductPricePoint(
            name='More Educational',
            price_in_cents=2000,
            interval=1,
            interval_unit='month',
            handle='more-educational',
            trial_price_in_cents=4900,
            trial_interval=1,
            trial_interval_unit='month',
            trial_type='payment_expected',
            initial_charge_in_cents=120000,
            initial_charge_after_trial=False,
            expiration_interval=12,
            expiration_interval_unit='month'
        )
    ]
)

result = product_price_points_controller.create_product_price_points(
    product_id,
    body=body
)
print(result)
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
      "archived_at": "Tue, 30 Oct 2018 18:49:47 EDT -04:00",
      "created_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00",
      "updated_at": "Tue, 23 Oct 2018 18:49:47 EDT -04:00"
    }
  ]
}
```


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
| `product_price_point_id` | `int` | Template, Required | The Chargify id of the product price point |
| `body` | [`CreateProductCurrencyPricesRequest`](../../doc/models/create-product-currency-prices-request.md) | Body, Optional | - |

## Response Type

[`ProductPricePointCurrencyPrice`](../../doc/models/product-price-point-currency-price.md)

## Example Usage

```python
product_price_point_id = 234

body = CreateProductCurrencyPricesRequest(
    currency_prices=[
        CreateProductCurrencyPrice(
            currency='EUR',
            price=60,
            role=CurrencyPriceRoleEnum.BASELINE
        ),
        CreateProductCurrencyPrice(
            currency='EUR',
            price=30,
            role=CurrencyPriceRoleEnum.TRIAL
        ),
        CreateProductCurrencyPrice(
            currency='EUR',
            price=100,
            role=CurrencyPriceRoleEnum.INITIAL
        )
    ]
)

result = product_price_points_controller.create_product_currency_prices(
    product_price_point_id,
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ProductPricePointsCurrencyPricesJson422ErrorException`](../../doc/models/product-price-points-currency-prices-json-422-error-exception.md) |


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
| `product_price_point_id` | `int` | Template, Required | The Chargify id of the product price point |
| `body` | [`UpdateCurrencyPricesRequest`](../../doc/models/update-currency-prices-request.md) | Body, Optional | - |

## Response Type

[`List[ProductPricePointCurrencyPrice]`](../../doc/models/product-price-point-currency-price.md)

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
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "id": 0,
    "currency": "string",
    "price": 0,
    "formatted_price": "string",
    "product_price_point_id": 0,
    "role": "baseline"
  }
]
```


# List All Product Price Points

This method allows retrieval of a list of Products Price Points belonging to a Site.

```python
def list_all_product_price_points(self,
                                 direction=None,
                                 filter_archived_at=None,
                                 filter_date_field=None,
                                 filter_end_date=None,
                                 filter_end_datetime=None,
                                 filter_ids=None,
                                 filter_start_date=None,
                                 filter_start_datetime=None,
                                 filter_type=None,
                                 include=None,
                                 page=1,
                                 per_page=20)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `direction` | [Sorting direction](../../doc/models/sorting-direction-enum.md) \| None | Query, Optional | This is a container for one-of cases. |
| `filter_archived_at` | [`IncludeNotNullEnum`](../../doc/models/include-not-null-enum.md) | Query, Optional | Allows fetching price points only if archived_at is present or not. Use in query: `filter[archived_at]=not_null`. |
| `filter_date_field` | [`BasicDateFieldEnum`](../../doc/models/basic-date-field-enum.md) | Query, Optional | The type of filter you would like to apply to your search. Use in query: `filter[date_field]=created_at`. |
| `filter_end_date` | `str` | Query, Optional | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns price points with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. |
| `filter_end_datetime` | `str` | Query, Optional | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns price points with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date. |
| `filter_ids` | `List[int]` | Query, Optional | Allows fetching price points with matching id based on provided values. Use in query: `filter[ids]=1,2,3`. |
| `filter_start_date` | `str` | Query, Optional | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns price points with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. |
| `filter_start_datetime` | `str` | Query, Optional | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns price points with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date. |
| `filter_type` | [`List[PricePointTypeEnum]`](../../doc/models/price-point-type-enum.md) | Query, Optional | Allows fetching price points with matching type. Use in query: `filter[type]=catalog,custom`. |
| `include` | [`ListProductsPricePointsIncludeEnum`](../../doc/models/list-products-price-points-include-enum.md) | Query, Optional | Allows including additional data in the response. Use in query: `include=currency_prices`. |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `20`<br>**Constraints**: `<= 200` |

## Response Type

[`ListProductPricePointsResponse`](../../doc/models/list-product-price-points-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')include = ListProductsPricePointsIncludeEnum.CURRENCY_PRICES

page = 2

per_page = 50

result = product_price_points_controller.list_all_product_price_points(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')
    include=include,
    page=page,
    per_page=per_page
)
print(result)
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

