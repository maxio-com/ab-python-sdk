# Components

```python
components_controller = client.components
```

## Class Name

`ComponentsController`

## Methods

* [Create Component](../../doc/controllers/components.md#create-component)
* [Read Component by Handle](../../doc/controllers/components.md#read-component-by-handle)
* [Read Component by Id](../../doc/controllers/components.md#read-component-by-id)
* [Update Product Family Component](../../doc/controllers/components.md#update-product-family-component)
* [Archive Component](../../doc/controllers/components.md#archive-component)
* [List Components](../../doc/controllers/components.md#list-components)
* [Update Component](../../doc/controllers/components.md#update-component)
* [Update Default Price Point for Component](../../doc/controllers/components.md#update-default-price-point-for-component)
* [List Components for Product Family](../../doc/controllers/components.md#list-components-for-product-family)
* [Create Component Price Point](../../doc/controllers/components.md#create-component-price-point)
* [List Component Price Points](../../doc/controllers/components.md#list-component-price-points)
* [Create Component Price Points](../../doc/controllers/components.md#create-component-price-points)
* [Update Component Price Point](../../doc/controllers/components.md#update-component-price-point)
* [Archive Component Price Point](../../doc/controllers/components.md#archive-component-price-point)
* [Unarchive Component Price Point](../../doc/controllers/components.md#unarchive-component-price-point)
* [Create Currency Prices](../../doc/controllers/components.md#create-currency-prices)
* [Update Currency Prices](../../doc/controllers/components.md#update-currency-prices)
* [List All Component Price Points](../../doc/controllers/components.md#list-all-component-price-points)


# Create Component

This request will create a component definition under the specified product family. These component definitions determine what components are named, how they are measured, and how much they cost.

Components can then be added and “allocated” for each subscription to a product in the product family. These component line-items affect how much a subscription will be charged, depending on the current allocations (i.e. 4 IP Addresses, or SSL “enabled”)

This documentation covers both component definitions and component line-items. Please understand the difference.

Please note that you may not edit components via API. To do so, please log into the application.

### Component Documentation

For more information on components, please see our documentation [here](https://maxio-chargify.zendesk.com/hc/en-us/articles/5405020625677).

For information on how to record component usage against a subscription, please see the following resources:

+ [Proration and Component Allocations](https://maxio-chargify.zendesk.com/hc/en-us/articles/5405020625677#applying-proration-and-recording-components)
+ [Recording component usage against a subscription](https://maxio-chargify.zendesk.com/hc/en-us/articles/5404606587917#recording-component-usage)

```python
def create_component(self,
                    product_family_id,
                    component_kind,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_family_id` | `int` | Template, Required | The Chargify id of the product family to which the component belongs |
| `component_kind` | [`ComponentKindPath`](../../doc/models/component-kind-path.md) | Template, Required | The component kind |
| `body` | [Create Metered Component](../../doc/models/create-metered-component.md) \| [Create Quantity Based Component](../../doc/models/create-quantity-based-component.md) \| [Create On/Off Component](../../doc/models/create-on-off-component.md) \| [Create Prepaid Component](../../doc/models/create-prepaid-component.md) \| [Create EBB Component](../../doc/models/create-ebb-component.md) \| None | Body, Optional | This is a container for one-of cases. |

## Response Type

[`ComponentResponse`](../../doc/models/component-response.md)

## Example Usage

```python
product_family_id = 140

component_kind = ComponentKindPath.ON_OFF_COMPONENTS

body = CreateMeteredComponent(
    metered_component=MeteredComponent(
        name='Text messages',
        unit_name='text message',
        pricing_scheme=PricingScheme.STAIRSTEP,
        taxable=False,
        prices=[
            Price(
                starting_quantity=1,
                unit_price=1
            )
        ]
    )
)

result = components_controller.create_component(
    product_family_id,
    component_kind,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "component": {
    "id": 292609,
    "name": "Text messages",
    "pricing_scheme": "stairstep",
    "unit_name": "text message",
    "unit_price": null,
    "product_family_id": 528484,
    "price_per_unit_in_cents": null,
    "kind": "metered_component",
    "archived": false,
    "taxable": false,
    "description": null,
    "created_at": "2019-08-02T05:54:53-04:00",
    "prices": [
      {
        "id": 47,
        "component_id": 292609,
        "starting_quantity": 1,
        "ending_quantity": null,
        "unit_price": "1.0",
        "price_point_id": 173,
        "formatted_unit_price": "$1.00"
      }
    ],
    "default_price_point_name": "Original"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Read Component by Handle

This request will return information regarding a component having the handle you provide. You can identify your components with a handle so you don't have to save or reference the IDs we generate.

```python
def read_component_by_handle(self,
                            handle)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `handle` | `str` | Query, Required | The handle of the component to find |

## Response Type

[`ComponentResponse`](../../doc/models/component-response.md)

## Example Usage

```python
handle = 'handle6'

result = components_controller.read_component_by_handle(handle)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "component": {
    "id": 399853,
    "name": "Annual Support Services",
    "pricing_scheme": null,
    "unit_name": "on/off",
    "unit_price": "100.0",
    "product_family_id": 997233,
    "price_per_unit_in_cents": null,
    "kind": "on_off_component",
    "archived": false,
    "taxable": true,
    "description": "Prepay for support services",
    "default_price_point_id": 121003,
    "price_point_count": 4,
    "price_points_url": "https://general-goods.chargify.com/components/399853/price_points",
    "tax_code": "D0000000",
    "recurring": true,
    "upgrade_charge": null,
    "downgrade_credit": null,
    "created_at": "2019-08-02T05:54:53-04:00",
    "default_price_point_name": "Original",
    "product_family_name": "Chargify"
  }
}
```


# Read Component by Id

This request will return information regarding a component from a specific product family.

You may read the component by either the component's id or handle. When using the handle, it must be prefixed with `handle:`.

```python
def read_component_by_id(self,
                        product_family_id,
                        component_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_family_id` | `int` | Template, Required | The Chargify id of the product family to which the component belongs |
| `component_id` | `str` | Template, Required | Either the Chargify id of the component or the handle for the component prefixed with `handle:`<br>**Constraints**: *Pattern*: `/\A(?:\d+\|handle:(?:uuid:\|[a-z])(?:\w\|-)+)\z/` |

## Response Type

[`ComponentResponse`](../../doc/models/component-response.md)

## Example Usage

```python
product_family_id = 140

component_id = 'component_id8'

result = components_controller.read_component_by_id(
    product_family_id,
    component_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "component": {
    "id": 399853,
    "name": "Annual Support Services",
    "pricing_scheme": null,
    "unit_name": "on/off",
    "unit_price": "100.0",
    "product_family_id": 997233,
    "price_per_unit_in_cents": null,
    "kind": "on_off_component",
    "archived": false,
    "taxable": true,
    "description": "Prepay for support services",
    "default_price_point_id": 121003,
    "price_point_count": 4,
    "price_points_url": "https://general-goods.chargify.com/components/399853/price_points",
    "tax_code": "D0000000",
    "recurring": true,
    "upgrade_charge": null,
    "downgrade_credit": null,
    "created_at": "2019-08-02T05:54:53-04:00",
    "default_price_point_name": "Original",
    "product_family_name": "Chargify"
  }
}
```


# Update Product Family Component

This request will update a component from a specific product family.

You may read the component by either the component's id or handle. When using the handle, it must be prefixed with `handle:`.

```python
def update_product_family_component(self,
                                   product_family_id,
                                   component_id,
                                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_family_id` | `int` | Template, Required | The Chargify id of the product family to which the component belongs |
| `component_id` | `str` | Template, Required | Either the Chargify id of the component or the handle for the component prefixed with `handle:`<br>**Constraints**: *Pattern*: `/\A(?:\d+\|handle:(?:uuid:\|[a-z])(?:\w\|-)+)\z/` |
| `body` | [`UpdateComponentRequest`](../../doc/models/update-component-request.md) | Body, Optional | - |

## Response Type

[`ComponentResponse`](../../doc/models/component-response.md)

## Example Usage

```python
product_family_id = 140

component_id = 'component_id8'

body = UpdateComponentRequest(
    component=UpdateComponent(
        item_category=ItemCategory.ENUM_BUSINESS_SOFTWARE
    )
)

result = components_controller.update_product_family_component(
    product_family_id,
    component_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "component": {
    "id": 399853,
    "name": "Annual Support Services",
    "pricing_scheme": null,
    "unit_name": "on/off",
    "unit_price": "100.0",
    "product_family_id": 997233,
    "price_per_unit_in_cents": null,
    "kind": "on_off_component",
    "archived": false,
    "taxable": true,
    "description": "Prepay for support services",
    "default_price_point_id": 121003,
    "price_point_count": 4,
    "price_points_url": "https://general-goods.chargify.com/components/399853/price_points",
    "tax_code": "D0000000",
    "recurring": true,
    "upgrade_charge": null,
    "downgrade_credit": null,
    "created_at": "2019-08-02T05:54:53-04:00",
    "default_price_point_name": "Original",
    "product_family_name": "Chargify"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Archive Component

Sending a DELETE request to this endpoint will archive the component. All current subscribers will be unffected; their subscription/purchase will continue to be charged as usual.

```python
def archive_component(self,
                     product_family_id,
                     component_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_family_id` | `int` | Template, Required | The Chargify id of the product family to which the component belongs |
| `component_id` | `str` | Template, Required | Either the Chargify id of the component or the handle for the component prefixed with `handle:`<br>**Constraints**: *Pattern*: `/\A(?:\d+\|handle:(?:uuid:\|[a-z])(?:\w\|-)+)\z/` |

## Response Type

[`ComponentResponse`](../../doc/models/component-response.md)

## Example Usage

```python
product_family_id = 140

component_id = 'component_id8'

result = components_controller.archive_component(
    product_family_id,
    component_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "component": {
    "id": 25407138,
    "name": "cillum aute",
    "pricing_scheme": "in incididu",
    "unit_name": "nulla in",
    "unit_price": "Excepteur veniam",
    "product_family_id": -56705047,
    "kind": "prepaid_usage_component",
    "archived": true,
    "taxable": false,
    "description": "reprehenderit laborum qui fugiat",
    "default_price_point_id": -64328176,
    "price_point_count": 15252407,
    "price_points_url": "dolor mollit consequat",
    "tax_code": "ea nisi",
    "recurring": false,
    "created_at": "dolor qui deserunt tempor",
    "default_price_point_name": "cupidatat Lorem non aliqua",
    "product_family_name": "do elit",
    "hide_date_range_on_invoice": false
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# List Components

This request will return a list of components for a site.

```python
def list_components(self,
                   options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_field` | [`BasicDateField`](../../doc/models/basic-date-field.md) | Query, Optional | The type of filter you would like to apply to your search. |
| `start_date` | `str` | Query, Optional | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. |
| `end_date` | `str` | Query, Optional | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. |
| `start_datetime` | `str` | Query, Optional | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date. |
| `end_datetime` | `str` | Query, Optional | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date.  optional |
| `include_archived` | `bool` | Query, Optional | Include archived items |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `20`<br>**Constraints**: `<= 200` |
| `filter_ids` | `List[str]` | Query, Optional | Allows fetching components with matching id based on provided value. Use in query `filter[ids]=1,2,3`. |
| `filter_use_site_exchange_rate` | `bool` | Query, Optional | Allows fetching components with matching use_site_exchange_rate based on provided value (refers to default price point). Use in query `filter[use_site_exchange_rate]=true`. |

## Response Type

[`List[ComponentResponse]`](../../doc/models/component-response.md)

## Example Usage

```python
collect = {Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')
    'date_field': BasicDateField.UPDATED_AT,
    'page': 2,
    'per_page': 50
}
result = components_controller.list_components(collect)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "component": {
      "id": 399850,
      "name": "$1.00 component",
      "pricing_scheme": "per_unit",
      "unit_name": "Component",
      "unit_price": "1.0",
      "product_family_id": 997233,
      "price_per_unit_in_cents": null,
      "kind": "quantity_based_component",
      "archived": false,
      "taxable": false,
      "description": "Component",
      "default_price_point_id": 121000,
      "prices": [
        {
          "id": 630687,
          "component_id": 399850,
          "starting_quantity": 1,
          "ending_quantity": null,
          "unit_price": "1.0",
          "price_point_id": 121000,
          "formatted_unit_price": "$1.00"
        }
      ],
      "price_point_count": 2,
      "price_points_url": "https://general-goods.chargify.com/components/399850/price_points",
      "tax_code": null,
      "recurring": true,
      "upgrade_charge": null,
      "downgrade_credit": null,
      "created_at": "2019-08-01T09:35:38-04:00",
      "default_price_point_name": "Original",
      "product_family_name": "Chargify",
      "use_site_exchange_rate": true
    }
  },
  {
    "component": {
      "id": 399853,
      "name": "Annual Support Services",
      "pricing_scheme": null,
      "unit_name": "on/off",
      "unit_price": "100.0",
      "product_family_id": 997233,
      "price_per_unit_in_cents": null,
      "kind": "on_off_component",
      "archived": false,
      "taxable": true,
      "description": "Prepay for support services",
      "default_price_point_id": 121003,
      "price_point_count": 4,
      "price_points_url": "https://general-goods.chargify.com/components/399853/price_points",
      "tax_code": "D0000000",
      "recurring": true,
      "upgrade_charge": null,
      "downgrade_credit": null,
      "created_at": "2019-08-01T09:35:37-04:00",
      "default_price_point_name": "Original",
      "product_family_name": "Chargify",
      "use_site_exchange_rate": true
    }
  },
  {
    "component": {
      "id": 386937,
      "name": "Cancellation fee",
      "pricing_scheme": null,
      "unit_name": "on/off",
      "unit_price": "35.0",
      "product_family_id": 997233,
      "price_per_unit_in_cents": null,
      "kind": "on_off_component",
      "archived": false,
      "taxable": false,
      "description": "",
      "default_price_point_id": 108307,
      "price_point_count": 1,
      "price_points_url": "https://general-goods.chargify.com/components/386937/price_points",
      "tax_code": null,
      "recurring": true,
      "upgrade_charge": null,
      "downgrade_credit": null,
      "created_at": "2019-08-01T09:35:38-04:00",
      "default_price_point_name": "Original",
      "product_family_name": "Chargify",
      "use_site_exchange_rate": true
    }
  }
]
```


# Update Component

This request will update a component.

You may read the component by either the component's id or handle. When using the handle, it must be prefixed with `handle:`.

```python
def update_component(self,
                    component_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | The id or handle of the component |
| `body` | [`UpdateComponentRequest`](../../doc/models/update-component-request.md) | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
component_id = 'component_id8'

body = UpdateComponentRequest(
    component=UpdateComponent(
        item_category=ItemCategory.ENUM_BUSINESS_SOFTWARE
    )
)

result = components_controller.update_component(
    component_id,
    body=body
)
print(result)
```


# Update Default Price Point for Component

Sets a new default price point for the component. This new default will apply to all new subscriptions going forward - existing subscriptions will remain on their current price point.

See [Price Points Documentation](https://chargify.zendesk.com/hc/en-us/articles/4407755865883#price-points) for more information on price points and moving subscriptions between price points.

Note: Custom price points are not able to be set as the default for a component.

```python
def update_default_price_point_for_component(self,
                                            component_id,
                                            price_point_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Chargify id of the component to which the price point belongs |
| `price_point_id` | `int` | Template, Required | The Chargify id of the price point |

## Response Type

`void`

## Example Usage

```python
component_id = 222

price_point_id = 10

result = components_controller.update_default_price_point_for_component(
    component_id,
    price_point_id
)
print(result)
```


# List Components for Product Family

This request will return a list of components for a particular product family.

```python
def list_components_for_product_family(self,
                                      options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_family_id` | `int` | Template, Required | The Chargify id of the product family |
| `include_archived` | `bool` | Query, Optional | Include archived items. |
| `filter_ids` | `List[int]` | Query, Optional | Allows fetching components with matching id based on provided value. Use in query `filter[ids]=1,2`. |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `20`<br>**Constraints**: `<= 200` |
| `date_field` | [`BasicDateField`](../../doc/models/basic-date-field.md) | Query, Optional | The type of filter you would like to apply to your search. Use in query `date_field=created_at`. |
| `end_date` | `str` | Query, Optional | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. |
| `end_datetime` | `str` | Query, Optional | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date. optional. |
| `start_date` | `str` | Query, Optional | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. |
| `start_datetime` | `str` | Query, Optional | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date. |
| `filter_use_site_exchange_rate` | `bool` | Query, Optional | Allows fetching components with matching use_site_exchange_rate based on provided value (refers to default price point). Use in query `filter[use_site_exchange_rate]=true`. |

## Response Type

[`List[ComponentResponse]`](../../doc/models/component-response.md)

## Example Usage

```python
collect = {Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')
    'product_family_id': 140,
    'page': 2,
    'per_page': 50,
    'date_field': BasicDateField.UPDATED_AT
}
result = components_controller.list_components_for_product_family(collect)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "component": {
      "id": 399850,
      "name": "$1.00 component",
      "pricing_scheme": "per_unit",
      "unit_name": "Component",
      "unit_price": "1.0",
      "product_family_id": 997233,
      "price_per_unit_in_cents": null,
      "kind": "quantity_based_component",
      "archived": false,
      "taxable": false,
      "description": "Component",
      "default_price_point_id": 121000,
      "prices": [
        {
          "id": 630687,
          "component_id": 399850,
          "starting_quantity": 1,
          "ending_quantity": null,
          "unit_price": "1.0",
          "price_point_id": 121000,
          "formatted_unit_price": "$1.00"
        }
      ],
      "price_point_count": 2,
      "price_points_url": "https://general-goods.chargify.com/components/399850/price_points",
      "tax_code": null,
      "recurring": true,
      "upgrade_charge": null,
      "downgrade_credit": null,
      "created_at": "2019-08-01T09:35:38-04:00",
      "default_price_point_name": "Original",
      "product_family_name": "Chargify",
      "use_site_exchange_rate": true
    }
  },
  {
    "component": {
      "id": 399853,
      "name": "Annual Support Services",
      "pricing_scheme": null,
      "unit_name": "on/off",
      "unit_price": "100.0",
      "product_family_id": 997233,
      "price_per_unit_in_cents": null,
      "kind": "on_off_component",
      "archived": false,
      "taxable": true,
      "description": "Prepay for support services",
      "default_price_point_id": 121003,
      "price_point_count": 4,
      "price_points_url": "https://general-goods.chargify.com/components/399853/price_points",
      "tax_code": "D0000000",
      "recurring": true,
      "upgrade_charge": null,
      "downgrade_credit": null,
      "created_at": "2019-08-01T09:35:37-04:00",
      "default_price_point_name": "Original",
      "product_family_name": "Chargify",
      "use_site_exchange_rate": true
    }
  },
  {
    "component": {
      "id": 386937,
      "name": "Cancellation fee",
      "pricing_scheme": null,
      "unit_name": "on/off",
      "unit_price": "35.0",
      "product_family_id": 997233,
      "price_per_unit_in_cents": null,
      "kind": "on_off_component",
      "archived": false,
      "taxable": false,
      "description": "",
      "default_price_point_id": 108307,
      "price_point_count": 1,
      "price_points_url": "https://general-goods.chargify.com/components/386937/price_points",
      "tax_code": null,
      "recurring": true,
      "upgrade_charge": null,
      "downgrade_credit": null,
      "created_at": "2019-08-01T09:35:38-04:00",
      "default_price_point_name": "Original",
      "product_family_name": "Chargify",
      "use_site_exchange_rate": true
    }
  }
]
```


# Create Component Price Point

This endpoint can be used to create a new price point for an existing component.

```python
def create_component_price_point(self,
                                component_id,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Chargify id of the component |
| `body` | [`CreateComponentPricePointRequest`](../../doc/models/create-component-price-point-request.md) | Body, Optional | - |

## Response Type

[`ComponentPricePointResponse`](../../doc/models/component-price-point-response.md)

## Example Usage

```python
component_id = 222

body = CreateComponentPricePointRequest(
    price_point=CreateComponentPricePoint(
        name='Wholesale',
        pricing_scheme='stairstep',
        prices=[
            Price(
                starting_quantity='1',
                unit_price='5.00',
                ending_quantity='100'
            ),
            Price(
                starting_quantity='101',
                unit_price='4.00'
            )
        ],
        handle='wholesale-handle'
    )
)

result = components_controller.create_component_price_point(
    component_id,
    body=body
)
print(result)
```


# List Component Price Points

Use this endpoint to read current price points that are associated with a component.

You may specify the component by using either the numeric id or the `handle:gold` syntax.

When fetching a component's price points, if you have defined multiple currencies at the site level, you can optionally pass the `?currency_prices=true` query param to include an array of currency price data in the response.

If the price point is set to `use_site_exchange_rate: true`, it will return pricing based on the current exchange rate. If the flag is set to false, it will return all of the defined prices for each currency.

```python
def list_component_price_points(self,
                               options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Chargify id of the component |
| `currency_prices` | `bool` | Query, Optional | Include an array of currency price data |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `20`<br>**Constraints**: `<= 200` |
| `filter_type` | [`List[PricePointType]`](../../doc/models/price-point-type.md) | Query, Optional | Use in query: `filter[type]=catalog,default`. |

## Response Type

[`ComponentPricePointsResponse`](../../doc/models/component-price-points-response.md)

## Example Usage

```python
collect = {Liquid error: Value cannot be null. (Parameter 'key')
    'component_id': 222,
    'page': 2,
    'per_page': 50
}
result = components_controller.list_component_price_points(collect)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "price_points": [
    {
      "id": 80,
      "default": false,
      "name": "Wholesale Two",
      "pricing_scheme": "per_unit",
      "component_id": 74,
      "handle": "wholesale-two",
      "archived_at": null,
      "created_at": "2017-07-05T13:55:40-04:00",
      "updated_at": "2017-07-05T13:55:40-04:00",
      "prices": [
        {
          "id": 121,
          "component_id": 74,
          "starting_quantity": 1,
          "ending_quantity": null,
          "unit_price": "5.0"
        }
      ]
    },
    {
      "id": 81,
      "default": false,
      "name": "MSRP",
      "pricing_scheme": "per_unit",
      "component_id": 74,
      "handle": "msrp",
      "archived_at": null,
      "created_at": "2017-07-05T13:55:40-04:00",
      "updated_at": "2017-07-05T13:55:40-04:00",
      "prices": [
        {
          "id": 122,
          "component_id": 74,
          "starting_quantity": 1,
          "ending_quantity": null,
          "unit_price": "4.0"
        }
      ]
    }
  ]
}
```


# Create Component Price Points

Use this endpoint to create multiple component price points in one request.

```python
def create_component_price_points(self,
                                 component_id,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | The Chargify id of the component for which you want to fetch price points. |
| `body` | [`CreateComponentPricePointsRequest`](../../doc/models/create-component-price-points-request.md) | Body, Optional | - |

## Response Type

[`ComponentPricePointsResponse`](../../doc/models/component-price-points-response.md)

## Example Usage

```python
component_id = 'component_id8'

body = CreateComponentPricePointsRequest(
    price_points=[
        CreateComponentPricePoint(
            name='Wholesale',
            pricing_scheme='per_unit',
            prices=[
                Price(
                    starting_quantity=1,
                    unit_price=5
                )
            ],
            handle='wholesale'
        ),
        CreateComponentPricePoint(
            name='MSRP',
            pricing_scheme='per_unit',
            prices=[
                Price(
                    starting_quantity=1,
                    unit_price=4
                )
            ],
            handle='msrp'
        ),
        CreateComponentPricePoint(
            name='Special Pricing',
            pricing_scheme='per_unit',
            prices=[
                Price(
                    starting_quantity=1,
                    unit_price=5
                )
            ],
            handle='special'
        )
    ]
)

result = components_controller.create_component_price_points(
    component_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "price_points": [
    {
      "id": 80,
      "default": false,
      "name": "Wholesale Two",
      "pricing_scheme": "per_unit",
      "component_id": 74,
      "handle": "wholesale-two",
      "archived_at": null,
      "created_at": "2017-07-05T13:55:40-04:00",
      "updated_at": "2017-07-05T13:55:40-04:00",
      "prices": [
        {
          "id": 121,
          "component_id": 74,
          "starting_quantity": 1,
          "ending_quantity": null,
          "unit_price": "5.0"
        }
      ]
    },
    {
      "id": 81,
      "default": false,
      "name": "MSRP",
      "pricing_scheme": "per_unit",
      "component_id": 74,
      "handle": "msrp",
      "archived_at": null,
      "created_at": "2017-07-05T13:55:40-04:00",
      "updated_at": "2017-07-05T13:55:40-04:00",
      "prices": [
        {
          "id": 122,
          "component_id": 74,
          "starting_quantity": 1,
          "ending_quantity": null,
          "unit_price": "4.0"
        }
      ]
    }
  ]
}
```


# Update Component Price Point

When updating a price point, it's prices can be updated as well by creating new prices or editing / removing existing ones.

Passing in a price bracket without an `id` will attempt to create a new price.

Including an `id` will update the corresponding price, and including the `_destroy` flag set to true along with the `id` will remove that price.

Note: Custom price points cannot be updated directly. They must be edited through the Subscription.

```python
def update_component_price_point(self,
                                component_id,
                                price_point_id,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Chargify id of the component to which the price point belongs |
| `price_point_id` | `int` | Template, Required | The Chargify id of the price point |
| `body` | [`UpdateComponentPricePointRequest`](../../doc/models/update-component-price-point-request.md) | Body, Optional | - |

## Response Type

[`ComponentPricePointResponse`](../../doc/models/component-price-point-response.md)

## Example Usage

```python
component_id = 222

price_point_id = 10

body = UpdateComponentPricePointRequest(
    price_point=UpdateComponentPricePoint(
        name='Default',
        prices=[
            UpdatePrice(
                id=1,
                ending_quantity=100,
                unit_price=5
            ),
            UpdatePrice(
                id=2,
                destroy='true'
            ),
            UpdatePrice(
                unit_price=4,
                starting_quantity=101
            )
        ]
    )
)

result = components_controller.update_component_price_point(
    component_id,
    price_point_id,
    body=body
)
print(result)
```


# Archive Component Price Point

A price point can be archived at any time. Subscriptions using a price point that has been archived will continue using it until they're moved to another price point.

```python
def archive_component_price_point(self,
                                 component_id,
                                 price_point_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Chargify id of the component to which the price point belongs |
| `price_point_id` | `int` | Template, Required | The Chargify id of the price point |

## Response Type

[`ComponentPricePointResponse`](../../doc/models/component-price-point-response.md)

## Example Usage

```python
component_id = 222

price_point_id = 10

result = components_controller.archive_component_price_point(
    component_id,
    price_point_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "price_point": {
    "id": 79,
    "default": false,
    "name": "Wholesale",
    "pricing_scheme": "stairstep",
    "component_id": 74,
    "handle": "wholesale-handle",
    "archived_at": "2017-07-06T15:04:00-04:00",
    "created_at": "2017-07-05T13:44:30-04:00",
    "updated_at": "2017-07-05T13:44:30-04:00",
    "prices": [
      {
        "id": 119,
        "component_id": 74,
        "starting_quantity": 1,
        "ending_quantity": 100,
        "unit_price": "5.0"
      },
      {
        "id": 120,
        "component_id": 74,
        "starting_quantity": 101,
        "ending_quantity": null,
        "unit_price": "4.0"
      }
    ]
  }
}
```


# Unarchive Component Price Point

Use this endpoint to unarchive a component price point.

```python
def unarchive_component_price_point(self,
                                   component_id,
                                   price_point_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Template, Required | The Chargify id of the component to which the price point belongs |
| `price_point_id` | `int` | Template, Required | The Chargify id of the price point |

## Response Type

[`ComponentPricePointResponse`](../../doc/models/component-price-point-response.md)

## Example Usage

```python
component_id = 222

price_point_id = 10

result = components_controller.unarchive_component_price_point(
    component_id,
    price_point_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "price_point": {
    "id": 79,
    "default": false,
    "name": "Wholesale",
    "pricing_scheme": "stairstep",
    "component_id": 74,
    "handle": "wholesale-handle",
    "archived_at": null,
    "created_at": "2017-07-05T13:44:30-04:00",
    "updated_at": "2017-07-05T13:44:30-04:00",
    "prices": [
      {
        "id": 119,
        "component_id": 74,
        "starting_quantity": 1,
        "ending_quantity": 100,
        "unit_price": "5.0"
      },
      {
        "id": 120,
        "component_id": 74,
        "starting_quantity": 101,
        "ending_quantity": null,
        "unit_price": "4.0"
      }
    ]
  }
}
```


# Create Currency Prices

This endpoint allows you to create currency prices for a given currency that has been defined on the site level in your settings.

When creating currency prices, they need to mirror the structure of your primary pricing. For each price level defined on the component price point, there should be a matching price level created in the given currency.

Note: Currency Prices are not able to be created for custom price points.

```python
def create_currency_prices(self,
                          price_point_id,
                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point_id` | `int` | Template, Required | The Chargify id of the price point |
| `body` | [`CreateCurrencyPricesRequest`](../../doc/models/create-currency-prices-request.md) | Body, Optional | - |

## Response Type

[`List[CurrencyPrice]`](../../doc/models/currency-price.md)

## Example Usage

```python
price_point_id = 10

body = CreateCurrencyPricesRequest(
    currency_prices=[
        CreateCurrencyPrice(
            currency='EUR',
            price=50,
            price_id=20
        ),
        CreateCurrencyPrice(
            currency='EUR',
            price=40,
            price_id=21
        )
    ]
)

result = components_controller.create_currency_prices(
    price_point_id,
    body=body
)
print(result)
```


# Update Currency Prices

This endpoint allows you to update currency prices for a given currency that has been defined on the site level in your settings.

Note: Currency Prices are not able to be updated for custom price points.

```python
def update_currency_prices(self,
                          price_point_id,
                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point_id` | `int` | Template, Required | The Chargify id of the price point |
| `body` | [`UpdateCurrencyPricesRequest`](../../doc/models/update-currency-prices-request.md) | Body, Optional | - |

## Response Type

[`List[CurrencyPrice]`](../../doc/models/currency-price.md)

## Example Usage

```python
price_point_id = 10

body = UpdateCurrencyPricesRequest(
    currency_prices=[
        UpdateCurrencyPrice(
            id=100,
            price=51
        ),
        UpdateCurrencyPrice(
            id=101,
            price=41
        )
    ]
)

result = components_controller.update_currency_prices(
    price_point_id,
    body=body
)
print(result)
```


# List All Component Price Points

This method allows to retrieve a list of Components Price Points belonging to a Site.

```python
def list_all_component_price_points(self,
                                   options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_date_field` | [`BasicDateField`](../../doc/models/basic-date-field.md) | Query, Optional | The type of filter you would like to apply to your search. Use in query: `filter[date_field]=created_at`. |
| `filter_end_date` | `str` | Query, Optional | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns price points with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. |
| `filter_end_datetime` | `str` | Query, Optional | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns price points with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date. |
| `include` | [`ListComponentsPricePointsInclude`](../../doc/models/list-components-price-points-include.md) | Query, Optional | Allows including additional data in the response. Use in query: `include=currency_prices`. |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `20`<br>**Constraints**: `<= 200` |
| `filter_start_date` | `str` | Query, Optional | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns price points with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. |
| `filter_start_datetime` | `str` | Query, Optional | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns price points with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date. |
| `filter_type` | [`PricePointType`](../../doc/models/price-point-type.md) | Query, Optional | Allows fetching price points with matching type. Use in query: `filter[type]=custom,catalog`. |
| `direction` | [Sorting direction](../../doc/models/sorting-direction.md) \| None | Query, Optional | This is a container for one-of cases. |
| `filter_ids` | `List[int]` | Query, Optional | Allows fetching price points with matching id based on provided values. Use in query: `filter[ids]=1,2,3`. |
| `filter_archived_at` | [`IncludeNotNull`](../../doc/models/include-not-null.md) | Query, Optional | Allows fetching price points only if archived_at is present or not. Use in query: `filter[archived_at]=not_null`. |

## Response Type

[`ListComponentsPricePointsResponse`](../../doc/models/list-components-price-points-response.md)

## Example Usage

```python
collect = {Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')
    'include': ListComponentsPricePointsInclude.CURRENCY_PRICES,
    'page': 2,
    'per_page': 50
}
result = components_controller.list_all_component_price_points(collect)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "price_points": [
    {
      "id": 1,
      "name": "Auto-created",
      "type": "default",
      "pricing_scheme": "per_unit",
      "component_id": 2,
      "handle": "auto-created",
      "archived_at": null,
      "created_at": "2021-02-21T11:05:57-05:00",
      "updated_at": "2021-02-21T11:05:57-05:00",
      "prices": [
        {
          "id": 3,
          "component_id": 2,
          "starting_quantity": 0,
          "ending_quantity": null,
          "unit_price": "1.0",
          "price_point_id": 1,
          "formatted_unit_price": "$1.00",
          "segment_id": null
        }
      ],
      "tax_included": false
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |

