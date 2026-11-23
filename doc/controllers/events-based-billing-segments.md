# Events-Based Billing Segments

```python
events_based_billing_segments_controller = client.events_based_billing_segments
```

## Class Name

`EventsBasedBillingSegmentsController`

## Methods

* [Create Segment](../../doc/controllers/events-based-billing-segments.md#create-segment)
* [List Segments for Price Point](../../doc/controllers/events-based-billing-segments.md#list-segments-for-price-point)
* [Update Segment](../../doc/controllers/events-based-billing-segments.md#update-segment)
* [Delete Segment](../../doc/controllers/events-based-billing-segments.md#delete-segment)
* [Bulk Create Segments](../../doc/controllers/events-based-billing-segments.md#bulk-create-segments)
* [Bulk Update Segments](../../doc/controllers/events-based-billing-segments.md#bulk-update-segments)


# Create Segment

Creates a new segment for a component with a segmented metric. It allows you to specify properties to bill upon and prices for each Segment. You can only pass as many "property_values" as the related Metric has segmenting properties defined.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

## Custom Price Points

This endpoint changes segments on catalog price points only. If the price point is a subscription's custom price point, the request returns `422 Unprocessable Entity` with a `price_point` error such as "Segments on a subscription's custom price point can't be changed here. Set them with custom_price on the subscription or component endpoints.", and nothing is saved. To change a subscription's segment rates, send `custom_price.segments` to [Update Subscription](../../doc/controllers/subscriptions.md#update-subscription).

```python
def create_segment(self,
                  component_id,
                  price_point_id,
                  body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle for the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle for the Price Point belonging to the Component |
| `body` | [`CreateSegmentRequest`](../../doc/models/create-segment-request.md) | Body, Optional | - |

## Response Type

**201**: Created

[`SegmentResponse`](../../doc/models/segment-response.md)

## Example Usage

```python
component_id = 'component_id8'

price_point_id = 'price_point_id8'

body = CreateSegmentRequest(
    segment=CreateSegment(
        pricing_scheme=PricingScheme.VOLUME,
        segment_property_1_value='France',
        segment_property_2_value='Spain',
        prices=[
            CreateOrUpdateSegmentPrice(
                unit_price=0.19,
                starting_quantity=1,
                ending_quantity=10000
            ),
            CreateOrUpdateSegmentPrice(
                unit_price=0.09,
                starting_quantity=10001
            )
        ]
    )
)

result = events_based_billing_segments_controller.create_segment(
    component_id,
    price_point_id,
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`EventBasedBillingSegmentWriteErrorResponseException`](../../doc/models/event-based-billing-segment-write-error-response-exception.md) |


# List Segments for Price Point

Lists segments created for a given price point, in order of creation.

You can pass `page` and `per_page` parameters in order to access all of the segments. By default it will return `30` records. You can set `per_page` to `200` at most.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

## Subscription Segment Rates

This endpoint also returns the segments of a subscription's custom price point, including segment rates set through `custom_price.segments` on [Create Subscription](../../doc/controllers/subscriptions.md#create-subscription) or [Update Subscription](../../doc/controllers/subscriptions.md#update-subscription). Use the subscription component's `price_point_id`, available from [Read Subscription Component](../../doc/controllers/subscription-components.md#read-subscription-component).

```python
def list_segments_for_price_point(self,
                                 options=dict())
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle for the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle for the Price Point belonging to the Component |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 30. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br><br>**Default**: `30`<br><br>**Constraints**: `<= 200` |
| `filter` | [`ListSegmentsFilter`](../../doc/models/list-segments-filter.md) | Query, Optional | Filter to use for List Segments for a Price Point operation |
| `currency_prices` | `bool` | Query, Optional | (Optional) If you have defined multiple currencies at the site level, pass `true` to include each segment's `currency_prices` in the response. Use in query: `currency_prices=true`. |

## Response Type

**200**: OK

[`ListSegmentsResponse`](../../doc/models/list-segments-response.md)

## Example Usage

```python
collect = {
    'component_id': 'component_id8',
    'price_point_id': 'price_point_id8',
    'page': 1,
    'per_page': 50,
    'filter': ListSegmentsFilter(
        segment_property_1_value='EU'
    ),
    'currency_prices': True
}
result = events_based_billing_segments_controller.list_segments_for_price_point(collect)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`EventBasedBillingListSegmentsErrorsException`](../../doc/models/event-based-billing-list-segments-errors-exception.md) |


# Update Segment

Updates a single segment for a component with a segmented metric. You can also update the pricing for the segment.

You can specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

## Custom Price Points

This endpoint changes segments on catalog price points only. If the segment belongs to a subscription's custom price point, or the `price_point_id` in the URL names one, the request returns `422 Unprocessable Entity` with a `price_point` error such as "Segments on a subscription's custom price point can't be changed here. Set them with custom_price on the subscription or component endpoints.", and nothing is saved. To change a subscription's segment rates, send `custom_price.segments` to [Update Subscription](../../doc/controllers/subscriptions.md#update-subscription).

```python
def update_segment(self,
                  component_id,
                  price_point_id,
                  id,
                  body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle of the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle of the Price Point belonging to the Component |
| `id` | `float` | Template, Required | The ID of the Segment |
| `body` | [`UpdateSegmentRequest`](../../doc/models/update-segment-request.md) | Body, Optional | - |

## Response Type

**200**: OK

[`SegmentResponse`](../../doc/models/segment-response.md)

## Example Usage

```python
component_id = 'component_id8'

price_point_id = 'price_point_id8'

id = 60

result = events_based_billing_segments_controller.update_segment(
    component_id,
    price_point_id,
    id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`EventBasedBillingSegmentWriteErrorResponseException`](../../doc/models/event-based-billing-segment-write-error-response-exception.md) |


# Delete Segment

Deletes a segment with the specified ID.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

## Custom Price Points

This endpoint changes segments on catalog price points only. If the segment belongs to a subscription's custom price point, the request returns `422 Unprocessable Entity` with a `price_point` error such as "Segments on a subscription's custom price point can't be changed here. Set them with custom_price on the subscription or component endpoints.", and nothing is saved. The check uses the segment's own price point, whichever `price_point_id` the URL names. To change a subscription's segment rates, send `custom_price.segments` to [Update Subscription](../../doc/controllers/subscriptions.md#update-subscription).

```python
def delete_segment(self,
                  component_id,
                  price_point_id,
                  id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle of the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle of the Price Point belonging to the Component |
| `id` | `float` | Template, Required | The ID of the Segment |

## Response Type

**204**: No Content

`void`

## Example Usage

```python
component_id = 'component_id8'

price_point_id = 'price_point_id8'

id = 60

events_based_billing_segments_controller.delete_segment(
    component_id,
    price_point_id,
    id
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`SegmentPricePointErrorsException`](../../doc/models/segment-price-point-errors-exception.md) |


# Bulk Create Segments

Creates multiple segments in one request. The array of segments can contain up to `2000` records.

If any of the records contain an error the whole request would fail and none of the requested segments get created. The error response contains a message for only the one segment that failed validation, with the corresponding index in the array.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

## Custom Price Points

This endpoint changes segments on catalog price points only. If the price point is a subscription's custom price point, the request returns `422 Unprocessable Entity` with a `price_point` error such as "Segments on a subscription's custom price point can't be changed here. Set them with custom_price on the subscription or component endpoints.", and nothing is saved. To change a subscription's segment rates, send `custom_price.segments` to [Update Subscription](../../doc/controllers/subscriptions.md#update-subscription).

```python
def bulk_create_segments(self,
                        component_id,
                        price_point_id,
                        body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle for the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle for the Price Point belonging to the Component |
| `body` | [`BulkCreateSegments`](../../doc/models/bulk-create-segments.md) | Body, Optional | - |

## Response Type

**201**: Created

[`ListSegmentsResponse`](../../doc/models/list-segments-response.md)

## Example Usage

```python
component_id = 'component_id8'

price_point_id = 'price_point_id8'

result = events_based_billing_segments_controller.bulk_create_segments(
    component_id,
    price_point_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | `APIException` |


# Bulk Update Segments

Updates multiple segments in one request. The array of segments can contain up to `1000` records.

If any of the records contain an error the whole request would fail and none of the requested segments get updated. The error response contains a message for only the one segment that failed validation, with the corresponding index in the array.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

## Custom Price Points

This endpoint changes segments on catalog price points only. If the price point is a subscription's custom price point, the request returns `422 Unprocessable Entity` with a `price_point` error such as "Segments on a subscription's custom price point can't be changed here. Set them with custom_price on the subscription or component endpoints.", and nothing is saved. To change a subscription's segment rates, send `custom_price.segments` to [Update Subscription](../../doc/controllers/subscriptions.md#update-subscription).

```python
def bulk_update_segments(self,
                        component_id,
                        price_point_id,
                        body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle for the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle for the Price Point belonging to the Component |
| `body` | [`BulkUpdateSegments`](../../doc/models/bulk-update-segments.md) | Body, Optional | - |

## Response Type

**200**: OK

[`ListSegmentsResponse`](../../doc/models/list-segments-response.md)

## Example Usage

```python
component_id = 'component_id8'

price_point_id = 'price_point_id8'

result = events_based_billing_segments_controller.bulk_update_segments(
    component_id,
    price_point_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | `APIException` |

