# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.api_helper import APIHelper
from advancedbilling.configuration import Server
from advancedbilling.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from advancedbilling.http.http_method_enum import HttpMethodEnum
from apimatic_core.types.array_serialization_format import SerializationFormats
from apimatic_core.authentication.multiple.single_auth import Single
from advancedbilling.models.event_response import EventResponse
from advancedbilling.models.count_response import CountResponse


class EventsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(EventsController, self).__init__(config)

    def list_events(self,
                    options=dict()):
        """Does a GET request to /events.json.

        ## Events Intro
        Advanced Billing Events include various activity that happens around a
        Site. This information is **especially** useful to track down issues
        that arise when subscriptions are not created due to errors.
        Within the Advanced Billing UI, "Events" are referred to as "Site
        Activity".  Full documentation on how to record view Events / Site
        Activty in the Advanced Billing UI can be located
        [here](https://maxio.zendesk.com/hc/en-us/articles/24250671733517-Site-
        Activity).
        ## List Events for a Site
        This method will retrieve a list of events for a site. Use query
        string filters to narrow down results. You may use the `key` filter as
        part of your query string to narrow down results.
        ### Legacy Filters
        The following keys are no longer supported.
        + `payment_failure_recreated`
        + `payment_success_recreated`
        + `renewal_failure_recreated`
        + `renewal_success_recreated`
        + `zferral_revenue_post_failure` - (Specific to the deprecated Zferral
        integration)
        + `zferral_revenue_post_success` - (Specific to the deprecated Zferral
        integration)
        ## Event Key
        The event type is identified by the key property. You can check
        supported keys [here]($m/Event%20Key).
        ## Event Specific Data
        Different event types may include additional data in
        `event_specific_data` property.
        While some events share the same schema for `event_specific_data`,
        others may not include it at all.
        For precise mappings from key to event_specific_data, refer to
        [Event]($m/Event).
        ### Example
        Here’s an example event for the `subscription_product_change` event:
        ```
        {
            "event": {
                "id": 351,
                "key": "subscription_product_change",
                "message": "Product changed on Marky Mark's subscription from
        'Basic' to 'Pro'",
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
                 "message": "State changed on Marky Mark's subscription to Pro
        from trialing to active",
                 "subscription_id": 205,
                 "event_specific_data": {
                     "new_subscription_state": "active",
                     "previous_subscription_state": "trialing"
                 },
                 "created_at": "2012-01-30T10:43:33-05:00"
             }
         }
        ```

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    page -- int -- Result records are organized in pages. By
                        default, the first page of results is displayed. The
                        page parameter specifies a page number of results to
                        fetch. You can start navigating through the pages to
                        consume the results. You do this by passing in a page
                        parameter. Retrieve the next page by adding ?page=2 to
                        the query string. If there are no results to return,
                        then an empty result set will be returned. Use in
                        query `page=1`.
                    per_page -- int -- This parameter indicates how many
                        records to fetch in each request. Default value is 20.
                        The maximum allowed values is 200; any per_page value
                        over 200 will be changed to 200. Use in query
                        `per_page=200`.
                    since_id -- int -- Returns events with an id greater than
                        or equal to the one specified
                    max_id -- int -- Returns events with an id less than or
                        equal to the one specified
                    direction -- Direction -- The sort direction of the
                        returned events.
                    filter -- List[EventKey] -- You can pass multiple event
                        keys after comma. Use in query
                        `filter=signup_success,payment_success`.
                    date_field -- ListEventsDateField -- The type of filter
                        you would like to apply to your search.
                    start_date -- str -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns
                        components with a timestamp at or after midnight
                        (12:00:00 AM) in your site’s time zone on the date
                        specified.
                    end_date -- str -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns components
                        with a timestamp up to and including 11:59:59PM in
                        your site’s time zone on the date specified.
                    start_datetime -- str -- The start date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns components with a timestamp at or
                        after exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date.
                    end_datetime -- str -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns components with a timestamp at or
                        before exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of end_date.

        Returns:
            List[EventResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/events.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('since_id')
                         .value(options.get('since_id', None)))
            .query_param(Parameter()
                         .key('max_id')
                         .value(options.get('max_id', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .query_param(Parameter()
                         .key('filter')
                         .value(options.get('filter', None)))
            .query_param(Parameter()
                         .key('date_field')
                         .value(options.get('date_field', None)))
            .query_param(Parameter()
                         .key('start_date')
                         .value(options.get('start_date', None)))
            .query_param(Parameter()
                         .key('end_date')
                         .value(options.get('end_date', None)))
            .query_param(Parameter()
                         .key('start_datetime')
                         .value(options.get('start_datetime', None)))
            .query_param(Parameter()
                         .key('end_datetime')
                         .value(options.get('end_datetime', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(EventResponse.from_dictionary)
        ).execute()

    def list_subscription_events(self,
                                 options=dict()):
        """Does a GET request to /subscriptions/{subscription_id}/events.json.

        The following request will return a list of events for a subscription.
        ## Event Key
        The event type is identified by the key property. You can check
        supported keys [here]($m/Event%20Key).
        ## Event Specific Data
        Different event types may include additional data in
        `event_specific_data` property.
        While some events share the same schema for `event_specific_data`,
        others may not include it at all.
        For precise mappings from key to event_specific_data, refer to
        [Event]($m/Event).

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    subscription_id -- int -- The Chargify id of the
                        subscription
                    page -- int -- Result records are organized in pages. By
                        default, the first page of results is displayed. The
                        page parameter specifies a page number of results to
                        fetch. You can start navigating through the pages to
                        consume the results. You do this by passing in a page
                        parameter. Retrieve the next page by adding ?page=2 to
                        the query string. If there are no results to return,
                        then an empty result set will be returned. Use in
                        query `page=1`.
                    per_page -- int -- This parameter indicates how many
                        records to fetch in each request. Default value is 20.
                        The maximum allowed values is 200; any per_page value
                        over 200 will be changed to 200. Use in query
                        `per_page=200`.
                    since_id -- int -- Returns events with an id greater than
                        or equal to the one specified
                    max_id -- int -- Returns events with an id less than or
                        equal to the one specified
                    direction -- Direction -- The sort direction of the
                        returned events.
                    filter -- List[EventKey] -- You can pass multiple event
                        keys after comma. Use in query
                        `filter=signup_success,payment_success`.

        Returns:
            List[EventResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/events.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(options.get('subscription_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('since_id')
                         .value(options.get('since_id', None)))
            .query_param(Parameter()
                         .key('max_id')
                         .value(options.get('max_id', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .query_param(Parameter()
                         .key('filter')
                         .value(options.get('filter', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(EventResponse.from_dictionary)
        ).execute()

    def read_events_count(self,
                          options=dict()):
        """Does a GET request to /events/count.json.

        Get a count of all the events for a given site by using this method.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    page -- int -- Result records are organized in pages. By
                        default, the first page of results is displayed. The
                        page parameter specifies a page number of results to
                        fetch. You can start navigating through the pages to
                        consume the results. You do this by passing in a page
                        parameter. Retrieve the next page by adding ?page=2 to
                        the query string. If there are no results to return,
                        then an empty result set will be returned. Use in
                        query `page=1`.
                    per_page -- int -- This parameter indicates how many
                        records to fetch in each request. Default value is 20.
                        The maximum allowed values is 200; any per_page value
                        over 200 will be changed to 200. Use in query
                        `per_page=200`.
                    since_id -- int -- Returns events with an id greater than
                        or equal to the one specified
                    max_id -- int -- Returns events with an id less than or
                        equal to the one specified
                    direction -- Direction -- The sort direction of the
                        returned events.
                    filter -- List[EventKey] -- You can pass multiple event
                        keys after comma. Use in query
                        `filter=signup_success,payment_success`.

        Returns:
            CountResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/events/count.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('since_id')
                         .value(options.get('since_id', None)))
            .query_param(Parameter()
                         .key('max_id')
                         .value(options.get('max_id', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .query_param(Parameter()
                         .key('filter')
                         .value(options.get('filter', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CountResponse.from_dictionary)
        ).execute()
