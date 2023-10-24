# Events

```python
events_controller = client.events
```

## Class Name

`EventsController`

## Methods

* [List Events](../../doc/controllers/events.md#list-events)
* [List Subscription Events](../../doc/controllers/events.md#list-subscription-events)
* [Read Events Count](../../doc/controllers/events.md#read-events-count)


# List Events

## Events Intro

Chargify Events include various activity that happens around a Site. This information is **especially** useful to track down issues that arise when subscriptions are not created due to errors.

Within the Chargify UI, "Events" are referred to as "Site Activity".  Full documentation on how to record view Events / Site Activty in the Chargify UI can be located [here](https://chargify.zendesk.com/hc/en-us/articles/4407864698139).

## List Events for a Site

This method will retrieve a list of events for a site. Use query string filters to narrow down results. You may use the `key` filter as part of your query string to narrow down results.

### Legacy Filters

The following keys are no longer supported.

+ `payment_failure_recreated`
+ `payment_success_recreated`
+ `renewal_failure_recreated`
+ `renewal_success_recreated`
+ `zferral_revenue_post_failure` - (Specific to the deprecated Zferral integration)
+ `zferral_revenue_post_success` - (Specific to the deprecated Zferral integration)

## Event Specific Data

Event Specific Data

Each event type has its own `event_specific_data` specified.

Here’s an example event for the `subscription_product_change` event:

```
{
    "event": {
        "id": 351,
        "key": "subscription_product_change",
        "message": "Product changed on Marky Mark's subscription from 'Basic' to 'Pro'",
        "subscription_id": 205,
        "event_specific_data": {
            "new_product_id": 3,
            "previous_product_id": 2
        },
        "created_at": "2012-01-30T10:43:31-05:00"
    }
}
```

Here’s an example event for the `subscription_state_change` event:

```
 {
     "event": {
         "id": 353,
         "key": "subscription_state_change",
         "message": "State changed on Marky Mark's subscription to Pro from trialing to active",
         "subscription_id": 205,
         "event_specific_data": {
             "new_subscription_state": "active",
             "previous_subscription_state": "trialing"
         },
         "created_at": "2012-01-30T10:43:33-05:00"
     }
 }
```

```python
def list_events(self,
               page=1,
               per_page=20,
               since_id=None,
               max_id=None,
               direction='desc',
               filter=None,
               date_field=None,
               start_date=None,
               end_date=None,
               start_datetime=None,
               end_datetime=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `20`<br>**Constraints**: `<= 200` |
| `since_id` | `int` | Query, Optional | Returns events with an id greater than or equal to the one specified |
| `max_id` | `int` | Query, Optional | Returns events with an id less than or equal to the one specified |
| `direction` | [`Direction`](../../doc/models/direction.md) | Query, Optional | The sort direction of the returned events.<br>**Default**: `'desc'` |
| `filter` | [`List[EventType]`](../../doc/models/event-type.md) | Query, Optional | You can pass multiple event keys after comma.<br>Use in query `filter=signup_success,payment_success`. |
| `date_field` | [`ListEventsDateField`](../../doc/models/list-events-date-field.md) | Query, Optional | The type of filter you would like to apply to your search. |
| `start_date` | `str` | Query, Optional | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. |
| `end_date` | `str` | Query, Optional | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. |
| `start_datetime` | `str` | Query, Optional | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date. |
| `end_datetime` | `str` | Query, Optional | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date. |

## Response Type

[`List[EventResponse]`](../../doc/models/event-response.md)

## Example Usage

```python
page = 2

per_page = 50

direction = Direction.DESC

filter = [
    EventType.CUSTOM_FIELD_VALUE_CHANGE,
    EventType.PAYMENT_SUCCESS
]

date_field = ListEventsDateField.CREATED_AT

result = events_controller.list_events(
    page=page,
    per_page=per_page,
    direction=direction,
    filter=filter,
    date_field=date_field
)
print(result)
```


# List Subscription Events

The following request will return a list of events for a subscription.

Each event type has its own `event_specific_data` specified.

```python
def list_subscription_events(self,
                            subscription_id,
                            page=1,
                            per_page=20,
                            since_id=None,
                            max_id=None,
                            direction='desc',
                            filter=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The Chargify id of the subscription |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `20`<br>**Constraints**: `<= 200` |
| `since_id` | `int` | Query, Optional | Returns events with an id greater than or equal to the one specified |
| `max_id` | `int` | Query, Optional | Returns events with an id less than or equal to the one specified |
| `direction` | [`Direction`](../../doc/models/direction.md) | Query, Optional | The sort direction of the returned events.<br>**Default**: `'desc'` |
| `filter` | [`List[EventType]`](../../doc/models/event-type.md) | Query, Optional | You can pass multiple event keys after comma.<br>Use in query `filter=signup_success,payment_success`. |

## Response Type

[`List[EventResponse]`](../../doc/models/event-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

page = 2

per_page = 50

direction = Direction.DESC

filter = [
    EventType.CUSTOM_FIELD_VALUE_CHANGE,
    EventType.PAYMENT_SUCCESS
]

result = events_controller.list_subscription_events(
    subscription_id,
    page=page,
    per_page=per_page,
    direction=direction,
    filter=filter
)
print(result)
```


# Read Events Count

Get a count of all the events for a given site by using this method.

```python
def read_events_count(self,
                     page=1,
                     per_page=20,
                     since_id=None,
                     max_id=None,
                     direction='desc',
                     filter=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `20`<br>**Constraints**: `<= 200` |
| `since_id` | `int` | Query, Optional | Returns events with an id greater than or equal to the one specified |
| `max_id` | `int` | Query, Optional | Returns events with an id less than or equal to the one specified |
| `direction` | [`Direction`](../../doc/models/direction.md) | Query, Optional | The sort direction of the returned events.<br>**Default**: `'desc'` |
| `filter` | [`List[EventType]`](../../doc/models/event-type.md) | Query, Optional | You can pass multiple event keys after comma.<br>Use in query `filter=signup_success,payment_success`. |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
page = 2

per_page = 50

direction = Direction.DESC

filter = [
    EventType.CUSTOM_FIELD_VALUE_CHANGE,
    EventType.PAYMENT_SUCCESS
]

result = events_controller.read_events_count(
    page=page,
    per_page=per_page,
    direction=direction,
    filter=filter
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "count": 144
}
```

