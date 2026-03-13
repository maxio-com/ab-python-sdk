# Subscription Renewals

```python
subscription_renewals_controller = client.subscription_renewals
```

## Class Name

`SubscriptionRenewalsController`

## Methods

* [Create Scheduled Renewal Configuration](../../doc/controllers/subscription-renewals.md#create-scheduled-renewal-configuration)
* [List Scheduled Renewal Configurations](../../doc/controllers/subscription-renewals.md#list-scheduled-renewal-configurations)
* [Read Scheduled Renewal Configuration](../../doc/controllers/subscription-renewals.md#read-scheduled-renewal-configuration)
* [Update Scheduled Renewal Configuration](../../doc/controllers/subscription-renewals.md#update-scheduled-renewal-configuration)
* [Schedule Scheduled Renewal Lock In](../../doc/controllers/subscription-renewals.md#schedule-scheduled-renewal-lock-in)
* [Lock in Scheduled Renewal Immediately](../../doc/controllers/subscription-renewals.md#lock-in-scheduled-renewal-immediately)
* [Unpublish Scheduled Renewal Configuration](../../doc/controllers/subscription-renewals.md#unpublish-scheduled-renewal-configuration)
* [Cancel Scheduled Renewal Configuration](../../doc/controllers/subscription-renewals.md#cancel-scheduled-renewal-configuration)
* [Create Scheduled Renewal Configuration Item](../../doc/controllers/subscription-renewals.md#create-scheduled-renewal-configuration-item)
* [Update Scheduled Renewal Configuration Item](../../doc/controllers/subscription-renewals.md#update-scheduled-renewal-configuration-item)
* [Delete Scheduled Renewal Configuration Item](../../doc/controllers/subscription-renewals.md#delete-scheduled-renewal-configuration-item)


# Create Scheduled Renewal Configuration

Creates a scheduled renewal configuration for a subscription. The scheduled renewal is based on the subscription’s current product and component setup.

```python
def create_scheduled_renewal_configuration(self,
                                          subscription_id,
                                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription. |
| `body` | [`ScheduledRenewalConfigurationRequest`](../../doc/models/scheduled-renewal-configuration-request.md) | Body, Optional | - |

## Response Type

[`ScheduledRenewalConfigurationResponse`](../../doc/models/scheduled-renewal-configuration-response.md)

## Example Usage

```python
subscription_id = 222

body = ScheduledRenewalConfigurationRequest(
    renewal_configuration=ScheduledRenewalConfigurationRequestBody(
        starts_at=dateutil.parser.parse('2024-12-01T00:00:00Z'),
        ends_at=dateutil.parser.parse('2025-12-01T00:00:00Z'),
        lock_in_at=dateutil.parser.parse('2024-11-15T00:00:00Z'),
        contract_id=222
    )
)

result = subscription_renewals_controller.create_scheduled_renewal_configuration(
    subscription_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "scheduled_renewal_configuration": {
    "id": 123,
    "site_id": 456,
    "subscription_id": 12345,
    "starts_at": "2024-12-01T00:00:00Z",
    "ends_at": "2025-12-01T00:00:00Z",
    "lock_in_at": "2024-11-15T00:00:00Z",
    "created_at": "2024-09-01T12:00:00Z",
    "status": "scheduled",
    "scheduled_renewal_configuration_items": [
      {
        "id": 789,
        "subscription_id": 12345,
        "subscription_renewal_configuration_id": 123,
        "item_id": 4,
        "item_type": "Product",
        "item_subclass": "Product",
        "price_point_id": 7,
        "price_point_type": "ProductPricePoint",
        "quantity": 1,
        "decimal_quantity": "1.0",
        "created_at": "2024-09-01T12:00:00Z"
      }
    ],
    "contract": {
      "id": 107,
      "maxio_id": "maxio-id",
      "number": null,
      "register": {
        "id": 12,
        "maxio_id": "maxio_id-id",
        "name": "Register",
        "currency_code": "USD"
      }
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# List Scheduled Renewal Configurations

Lists scheduled renewal configurations for the subscription and permits an optional status query filter.

```python
def list_scheduled_renewal_configurations(self,
                                         subscription_id,
                                         status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription. |
| `status` | [`Status`](../../doc/models/status.md) | Query, Optional | (Optional) Status filter for scheduled renewal configurations. |

## Response Type

[`ScheduledRenewalConfigurationsResponse`](../../doc/models/scheduled-renewal-configurations-response.md)

## Example Usage

```python
subscription_id = 222

result = subscription_renewals_controller.list_scheduled_renewal_configurations(subscription_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "scheduled_renewal_configurations": [
    {
      "id": 123,
      "site_id": 456,
      "subscription_id": 12345,
      "starts_at": "2024-12-01T00:00:00Z",
      "ends_at": "2025-12-01T00:00:00Z",
      "lock_in_at": "2024-11-15T00:00:00Z",
      "created_at": "2024-09-01T12:00:00Z",
      "status": "scheduled",
      "scheduled_renewal_configuration_items": [
        {
          "id": 789,
          "subscription_id": 12345,
          "subscription_renewal_configuration_id": 123,
          "item_id": 4,
          "item_type": "Product",
          "item_subclass": "Product",
          "price_point_id": 7,
          "price_point_type": "ProductPricePoint",
          "quantity": 1,
          "decimal_quantity": "1.0",
          "created_at": "2024-09-01T12:00:00Z"
        }
      ],
      "contract": {
        "id": 107,
        "maxio_id": "maxio-id",
        "number": null,
        "register": {
          "id": 12,
          "maxio_id": "maxio-id",
          "name": "Register",
          "currency_code": "USD"
        }
      }
    }
  ]
}
```


# Read Scheduled Renewal Configuration

Retrieves the configuration settings for the scheduled renewal.

```python
def read_scheduled_renewal_configuration(self,
                                        subscription_id,
                                        id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription. |
| `id` | `int` | Template, Required | The renewal id. |

## Response Type

[`ScheduledRenewalConfigurationResponse`](../../doc/models/scheduled-renewal-configuration-response.md)

## Example Usage

```python
subscription_id = 222

id = 112

result = subscription_renewals_controller.read_scheduled_renewal_configuration(
    subscription_id,
    id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "scheduled_renewal_configuration": {
    "id": 123,
    "site_id": 456,
    "subscription_id": 12345,
    "starts_at": "2024-12-01T00:00:00Z",
    "ends_at": "2025-12-01T00:00:00Z",
    "lock_in_at": "2024-11-15T00:00:00Z",
    "created_at": "2024-09-01T12:00:00Z",
    "status": "scheduled",
    "scheduled_renewal_configuration_items": [
      {
        "id": 789,
        "subscription_id": 12345,
        "subscription_renewal_configuration_id": 123,
        "item_id": 4,
        "item_type": "Product",
        "item_subclass": "Product",
        "price_point_id": 7,
        "price_point_type": "ProductPricePoint",
        "quantity": 1,
        "decimal_quantity": "1.0",
        "created_at": "2024-09-01T12:00:00Z"
      }
    ],
    "contract": {
      "id": 107,
      "maxio_id": "maxio-id",
      "number": null,
      "register": {
        "id": 12,
        "maxio_id": "maxio-id",
        "name": "Register",
        "currency_code": "USD"
      }
    }
  }
}
```


# Update Scheduled Renewal Configuration

Updates an existing configuration.

```python
def update_scheduled_renewal_configuration(self,
                                          subscription_id,
                                          id,
                                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription. |
| `id` | `int` | Template, Required | The renewal id. |
| `body` | [`ScheduledRenewalConfigurationRequest`](../../doc/models/scheduled-renewal-configuration-request.md) | Body, Optional | - |

## Response Type

[`ScheduledRenewalConfigurationResponse`](../../doc/models/scheduled-renewal-configuration-response.md)

## Example Usage

```python
subscription_id = 222

id = 112

body = ScheduledRenewalConfigurationRequest(
    renewal_configuration=ScheduledRenewalConfigurationRequestBody(
        starts_at=dateutil.parser.parse('2025-12-01T00:00:00Z'),
        ends_at=dateutil.parser.parse('2026-12-01T00:00:00Z'),
        lock_in_at=dateutil.parser.parse('2025-11-15T00:00:00Z')
    )
)

result = subscription_renewals_controller.update_scheduled_renewal_configuration(
    subscription_id,
    id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "scheduled_renewal_configuration": {
    "id": 123,
    "site_id": 456,
    "subscription_id": 12345,
    "starts_at": "2025-12-01T00:00:00Z",
    "ends_at": "2026-12-01T00:00:00Z",
    "lock_in_at": "2025-11-15T00:00:00Z",
    "created_at": "2025-09-01T12:00:00Z",
    "status": "scheduled",
    "scheduled_renewal_configuration_items": [
      {
        "id": 789,
        "subscription_id": 12345,
        "subscription_renewal_configuration_id": 123,
        "item_id": 4,
        "item_type": "Product",
        "item_subclass": "Product",
        "price_point_id": 7,
        "price_point_type": "ProductPricePoint",
        "quantity": 1,
        "decimal_quantity": "1.0",
        "created_at": "2025-09-01T12:00:00Z"
      }
    ],
    "contract": {
      "id": 107,
      "maxio_id": "maxio-id",
      "number": null,
      "register": {
        "id": 12,
        "maxio_id": "maxio-id",
        "name": "Register",
        "currency_code": "USD"
      }
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Schedule Scheduled Renewal Lock In

Schedules a future lock-in date for the renewal.

```python
def schedule_scheduled_renewal_lock_in(self,
                                      subscription_id,
                                      id,
                                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription. |
| `id` | `int` | Template, Required | The renewal id. |
| `body` | [`ScheduledRenewalLockInRequest`](../../doc/models/scheduled-renewal-lock-in-request.md) | Body, Optional | - |

## Response Type

[`ScheduledRenewalConfigurationResponse`](../../doc/models/scheduled-renewal-configuration-response.md)

## Example Usage

```python
subscription_id = 222

id = 112

body = ScheduledRenewalLockInRequest(
    lock_in_at=dateutil.parser.parse('2025-11-15').date()
)

result = subscription_renewals_controller.schedule_scheduled_renewal_lock_in(
    subscription_id,
    id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "scheduled_renewal_configuration": {
    "id": 123,
    "site_id": 456,
    "subscription_id": 12345,
    "starts_at": "2025-12-01T00:00:00Z",
    "ends_at": "2026-12-01T00:00:00Z",
    "lock_in_at": "2025-11-15T00:00:00Z",
    "created_at": "2025-09-01T12:00:00Z",
    "status": "scheduled",
    "scheduled_renewal_configuration_items": [
      {
        "id": 789,
        "subscription_id": 12345,
        "subscription_renewal_configuration_id": 123,
        "item_id": 4,
        "item_type": "Product",
        "item_subclass": "Product",
        "price_point_id": 7,
        "price_point_type": "ProductPricePoint",
        "quantity": 1,
        "decimal_quantity": "1.0",
        "created_at": "2025-09-01T12:00:00Z"
      }
    ],
    "contract": {
      "id": 107,
      "maxio_id": "maxio-id",
      "number": null,
      "register": {
        "id": 12,
        "maxio_id": "maxio-id",
        "name": "Register",
        "currency_code": "USD"
      }
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Lock in Scheduled Renewal Immediately

Locks in the renewal immediately.

```python
def lock_in_scheduled_renewal_immediately(self,
                                         subscription_id,
                                         id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription. |
| `id` | `int` | Template, Required | The renewal id. |

## Response Type

[`ScheduledRenewalConfigurationResponse`](../../doc/models/scheduled-renewal-configuration-response.md)

## Example Usage

```python
subscription_id = 222

id = 112

result = subscription_renewals_controller.lock_in_scheduled_renewal_immediately(
    subscription_id,
    id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "scheduled_renewal_configuration": {
    "id": 987,
    "site_id": 321,
    "subscription_id": 12345,
    "starts_at": "2025-12-01T00:00:00Z",
    "ends_at": "2026-12-01T00:00:00Z",
    "lock_in_at": "2025-11-15T00:00:00Z",
    "created_at": "2025-09-01T12:00:00Z",
    "status": "scheduled",
    "scheduled_renewal_configuration_items": [
      {
        "id": 555,
        "subscription_id": 12345,
        "subscription_renewal_configuration_id": 987,
        "item_id": 42,
        "item_type": "Product",
        "price_point_id": 73,
        "price_point_type": "ProductPricePoint",
        "quantity": 1,
        "decimal_quantity": "1.0",
        "created_at": "2025-09-01T12:00:00Z"
      }
    ],
    "contract": {
      "id": 222,
      "maxio_id": "maxio-id",
      "number": null,
      "register": {
        "id": 12,
        "maxio_id": "maxio-id",
        "name": "Register",
        "currency_code": "USD"
      }
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Unpublish Scheduled Renewal Configuration

Returns a scheduled renewal configuration to an editable state.

```python
def unpublish_scheduled_renewal_configuration(self,
                                             subscription_id,
                                             id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription. |
| `id` | `int` | Template, Required | The renewal id. |

## Response Type

[`ScheduledRenewalConfigurationResponse`](../../doc/models/scheduled-renewal-configuration-response.md)

## Example Usage

```python
subscription_id = 222

id = 112

result = subscription_renewals_controller.unpublish_scheduled_renewal_configuration(
    subscription_id,
    id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "scheduled_renewal_configuration": {
    "id": 987,
    "site_id": 321,
    "subscription_id": 12345,
    "starts_at": "2025-12-01T00:00:00Z",
    "ends_at": "2026-12-01T00:00:00Z",
    "lock_in_at": "2025-11-15T00:00:00Z",
    "created_at": "2025-09-01T12:00:00Z",
    "status": "draft",
    "scheduled_renewal_configuration_items": [
      {
        "id": 555,
        "subscription_id": 12345,
        "subscription_renewal_configuration_id": 987,
        "item_id": 42,
        "item_type": "Product",
        "price_point_id": 73,
        "price_point_type": "ProductPricePoint",
        "quantity": 1,
        "decimal_quantity": "1.0",
        "created_at": "2025-09-01T12:00:00Z"
      }
    ],
    "contract": {
      "id": 222
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Cancel Scheduled Renewal Configuration

Cancels a scheduled renewal configuration.

```python
def cancel_scheduled_renewal_configuration(self,
                                          subscription_id,
                                          id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription. |
| `id` | `int` | Template, Required | The renewal id. |

## Response Type

[`ScheduledRenewalConfigurationResponse`](../../doc/models/scheduled-renewal-configuration-response.md)

## Example Usage

```python
subscription_id = 222

id = 112

result = subscription_renewals_controller.cancel_scheduled_renewal_configuration(
    subscription_id,
    id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "scheduled_renewal_configuration": {
    "id": 987,
    "site_id": 321,
    "subscription_id": 12345,
    "starts_at": "2025-12-01T00:00:00Z",
    "ends_at": "2026-12-01T00:00:00Z",
    "lock_in_at": "2025-11-15T00:00:00Z",
    "created_at": "2025-09-01T12:00:00Z",
    "status": "canceled",
    "scheduled_renewal_configuration_items": [
      {
        "id": 555,
        "subscription_id": 12345,
        "subscription_renewal_configuration_id": 987,
        "item_id": 42,
        "item_type": "Product",
        "price_point_id": 73,
        "price_point_type": "ProductPricePoint",
        "quantity": 1,
        "decimal_quantity": "1.0",
        "created_at": "2025-09-01T12:00:00Z"
      }
    ],
    "contract": {
      "id": 222
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Create Scheduled Renewal Configuration Item

Adds product and component line items to the scheduled renewal.

```python
def create_scheduled_renewal_configuration_item(self,
                                               subscription_id,
                                               scheduled_renewals_configuration_id,
                                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription. |
| `scheduled_renewals_configuration_id` | `int` | Template, Required | The scheduled renewal configuration id. |
| `body` | [`ScheduledRenewalConfigurationItemRequest`](../../doc/models/scheduled-renewal-configuration-item-request.md) | Body, Optional | - |

## Response Type

[`ScheduledRenewalConfigurationItemResponse`](../../doc/models/scheduled-renewal-configuration-item-response.md)

## Example Usage

```python
subscription_id = 222

scheduled_renewals_configuration_id = 250

body = ScheduledRenewalConfigurationItemRequest(
    renewal_configuration_item=ScheduledRenewalItemRequestBodyComponent(
        item_id=57,
        quantity=1,
        custom_price=ScheduledRenewalComponentCustomPrice(
            pricing_scheme=PricingScheme.STAIRSTEP,
            prices=[
                Price(
                    starting_quantity=1,
                    unit_price=5,
                    ending_quantity=None
                )
            ]
        )
    )
)

result = subscription_renewals_controller.create_scheduled_renewal_configuration_item(
    subscription_id,
    scheduled_renewals_configuration_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "scheduled_renewal_configuration_item": {
    "id": 555,
    "subscription_id": 12345,
    "subscription_renewal_configuration_id": 987,
    "item_id": 42,
    "item_type": "Product",
    "item_subclass": "SubscriptionProduct",
    "price_point_id": 73,
    "price_point_type": "ProductPricePoint",
    "quantity": 1,
    "decimal_quantity": "1.0",
    "created_at": "2025-09-01T12:00:00Z"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Update Scheduled Renewal Configuration Item

Updates an existing configuration item’s pricing and quantity.

```python
def update_scheduled_renewal_configuration_item(self,
                                               subscription_id,
                                               scheduled_renewals_configuration_id,
                                               id,
                                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription. |
| `scheduled_renewals_configuration_id` | `int` | Template, Required | The scheduled renewal configuration id. |
| `id` | `int` | Template, Required | The scheduled renewal configuration item id. |
| `body` | [`ScheduledRenewalUpdateRequest`](../../doc/models/scheduled-renewal-update-request.md) | Body, Optional | - |

## Response Type

[`ScheduledRenewalConfigurationItemResponse`](../../doc/models/scheduled-renewal-configuration-item-response.md)

## Example Usage

```python
subscription_id = 222

scheduled_renewals_configuration_id = 250

id = 112

body = ScheduledRenewalUpdateRequest(
    renewal_configuration_item=ScheduledRenewalItemRequestBodyComponent(
        item_id=57,
        quantity=2,
        custom_price=ScheduledRenewalComponentCustomPrice(
            pricing_scheme=PricingScheme.STAIRSTEP,
            prices=[
                Price(
                    starting_quantity=1,
                    unit_price=5,
                    ending_quantity=None
                )
            ]
        )
    )
)

result = subscription_renewals_controller.update_scheduled_renewal_configuration_item(
    subscription_id,
    scheduled_renewals_configuration_id,
    id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "scheduled_renewal_configuration_item": {
    "id": 555,
    "subscription_id": 12345,
    "subscription_renewal_configuration_id": 987,
    "item_id": 42,
    "item_type": "Component",
    "item_subclass": "SubscriptionComponent",
    "price_point_id": 73,
    "price_point_type": "ComponentPricePoint",
    "quantity": 3,
    "decimal_quantity": "3.0",
    "created_at": "2025-09-01T12:00:00Z"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Delete Scheduled Renewal Configuration Item

Removes an item from the pending renewal configuration.

```python
def delete_scheduled_renewal_configuration_item(self,
                                               subscription_id,
                                               scheduled_renewals_configuration_id,
                                               id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription. |
| `scheduled_renewals_configuration_id` | `int` | Template, Required | The scheduled renewal configuration id. |
| `id` | `int` | Template, Required | The scheduled renewal configuration item id. |

## Response Type

`void`

## Example Usage

```python
subscription_id = 222

scheduled_renewals_configuration_id = 250

id = 112

subscription_renewals_controller.delete_scheduled_renewal_configuration_item(
    subscription_id,
    scheduled_renewals_configuration_id,
    id
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |

