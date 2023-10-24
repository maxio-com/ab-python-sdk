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
* [Create Segments](../../doc/controllers/events-based-billing-segments.md#create-segments)
* [Update Segments](../../doc/controllers/events-based-billing-segments.md#update-segments)


# Create Segment

This endpoint creates a new Segment for a Component with segmented Metric. It allows you to specify properties to bill upon and prices for each Segment. You can only pass as many "property_values" as the related Metric has segmenting properties defined.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

```python
def create_segment(self,
                  component_id,
                  price_point_id,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle for the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle for the Price Point belonging to the Component |
| `body` | [`CreateSegmentRequest`](../../doc/models/create-segment-request.md) | Body, Optional | - |

## Response Type

[`SegmentResponse`](../../doc/models/segment-response.md)

## Example Usage

```python
component_id = 'component_id8'

price_point_id = 'price_point_id8'

body = CreateSegmentRequest(
    segment=CreateSegment(
        pricing_scheme='volume',
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
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`EventBasedBillingSegmentErrorsException`](../../doc/models/event-based-billing-segment-errors-exception.md) |


# List Segments for Price Point

This endpoint allows you to fetch Segments created for a given Price Point. They will be returned in the order of creation.

You can pass `page` and `per_page` parameters in order to access all of the segments. By default it will return `30` records. You can set `per_page` to `200` at most.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

```python
def list_segments_for_price_point(self,
                                 component_id,
                                 price_point_id,
                                 page=1,
                                 per_page=30,
                                 filter_segment_property_1_value=None,
                                 filter_segment_property_2_value=None,
                                 filter_segment_property_3_value=None,
                                 filter_segment_property_4_value=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle for the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle for the Price Point belonging to the Component |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 30. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `30`<br>**Constraints**: `<= 200` |
| `filter_segment_property_1_value` | `str` | Query, Optional | The value passed here would be used to filter segments. Pass a value related to `segment_property_1` on attached Metric. If empty string is passed, this filter would be rejected. Use in query `filter[segment_property_1_value]=EU`. |
| `filter_segment_property_2_value` | `str` | Query, Optional | The value passed here would be used to filter segments. Pass a value related to `segment_property_2` on attached Metric. If empty string is passed, this filter would be rejected. |
| `filter_segment_property_3_value` | `str` | Query, Optional | The value passed here would be used to filter segments. Pass a value related to `segment_property_3` on attached Metric. If empty string is passed, this filter would be rejected. |
| `filter_segment_property_4_value` | `str` | Query, Optional | The value passed here would be used to filter segments. Pass a value related to `segment_property_4` on attached Metric. If empty string is passed, this filter would be rejected. |

## Response Type

[`ListSegmentsResponse`](../../doc/models/list-segments-response.md)

## Example Usage

```python
component_id = 'component_id8'

price_point_id = 'price_point_id8'

page = 2

per_page = 50

Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = events_based_billing_segments_controller.list_segments_for_price_point(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')
    component_id,
    price_point_id,
    page=page,
    per_page=per_page
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`EventBasedBillingListSegmentsErrorsException`](../../doc/models/event-based-billing-list-segments-errors-exception.md) |


# Update Segment

This endpoint updates a single Segment for a Component with a segmented Metric. It allows you to update the pricing for the segment.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

```python
def update_segment(self,
                  component_id,
                  price_point_id,
                  id,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle of the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle of the Price Point belonging to the Component |
| `id` | `float` | Template, Required | The ID of the Segment |
| `body` | [`UpdateSegmentRequest`](../../doc/models/update-segment-request.md) | Body, Optional | - |

## Response Type

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
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`EventBasedBillingSegmentErrorsException`](../../doc/models/event-based-billing-segment-errors-exception.md) |


# Delete Segment

This endpoint allows you to delete a Segment with specified ID.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

```python
def delete_segment(self,
                  component_id,
                  price_point_id,
                  id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle of the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle of the Price Point belonging to the Component |
| `id` | `float` | Template, Required | The ID of the Segment |

## Response Type

`void`

## Example Usage

```python
component_id = 'component_id8'

price_point_id = 'price_point_id8'

id = 60

result = events_based_billing_segments_controller.delete_segment(
    component_id,
    price_point_id,
    id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | `APIException` |


# Create Segments

This endpoint allows you to create multiple segments in one request. The array of segments can contain up to `2000` records.

If any of the records contain an error the whole request would fail and none of the requested segments get created. The error response contains a message for only the one segment that failed validation, with the corresponding index in the array.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

```python
def create_segments(self,
                   component_id,
                   price_point_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle for the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle for the Price Point belonging to the Component |
| `body` | [`BulkCreateSegments`](../../doc/models/bulk-create-segments.md) | Body, Optional | - |

## Response Type

[`ListSegmentsResponse`](../../doc/models/list-segments-response.md)

## Example Usage

```python
component_id = 'component_id8'

price_point_id = 'price_point_id8'

result = events_based_billing_segments_controller.create_segments(
    component_id,
    price_point_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`EventBasedBillingSegmentException`](../../doc/models/event-based-billing-segment-exception.md) |


# Update Segments

This endpoint allows you to update multiple segments in one request. The array of segments can contain up to `1000` records.

If any of the records contain an error the whole request would fail and none of the requested segments get updated. The error response contains a message for only the one segment that failed validation, with the corresponding index in the array.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

```python
def update_segments(self,
                   component_id,
                   price_point_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `str` | Template, Required | ID or Handle for the Component |
| `price_point_id` | `str` | Template, Required | ID or Handle for the Price Point belonging to the Component |
| `body` | [`BulkUpdateSegments`](../../doc/models/bulk-update-segments.md) | Body, Optional | - |

## Response Type

[`ListSegmentsResponse`](../../doc/models/list-segments-response.md)

## Example Usage

```python
component_id = 'component_id8'

price_point_id = 'price_point_id8'

result = events_based_billing_segments_controller.update_segments(
    component_id,
    price_point_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`EventBasedBillingSegmentException`](../../doc/models/event-based-billing-segment-exception.md) |

