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
from advancedbilling.models.component_response import ComponentResponse
from advancedbilling.models.component import Component
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException


class ComponentsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(ComponentsController, self).__init__(config)

    def create_metered_component(self,
                                 product_family_id,
                                 body=None):
        """Does a POST request to /product_families/{product_family_id}/metered_components.json.

        This request will create a component definition of kind
        **metered_component** under the specified product family. Metered
        component can then be added and “allocated” for a subscription.
        Metered components are used to bill for any type of unit that resets
        to 0 at the end of the billing period (think daily Google Adwords
        clicks or monthly cell phone minutes). This is most commonly
        associated with usage-based billing and many other pricing schemes.
        Note that this is different from recurring quantity-based components,
        which DO NOT reset to zero at the start of every billing period. If
        you want to bill for a quantity of something that does not change
        unless you change it, then you want quantity components, instead.
        For more information on components, please see our documentation
        [here](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Compo
        nents-Overview).

        Args:
            product_family_id (str): Either the product family's id or its
                handle prefixed with `handle:`
            body (CreateMeteredComponent, optional): TODO: type description
                here.

        Returns:
            ComponentResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families/{product_family_id}/metered_components.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def create_quantity_based_component(self,
                                        product_family_id,
                                        body=None):
        """Does a POST request to /product_families/{product_family_id}/quantity_based_components.json.

        This request will create a component definition of kind
        **quantity_based_component** under the specified product family.
        Quantity Based component can then be added and “allocated” for a
        subscription.
        When defining Quantity Based component, You can choose one of 2
        types:
        #### Recurring
        Recurring quantity-based components are used to bill for the number of
        some unit (think monthly software user licenses or the number of pairs
        of socks in a box-a-month club). This is most commonly associated with
        billing for user licenses, number of users, number of employees, etc.
        #### One-time
        One-time quantity-based components are used to create ad hoc usage
        charges that do not recur. For example, at the time of signup, you
        might want to charge your customer a one-time fee for onboarding or
        other services.
        The allocated quantity for one-time quantity-based components
        immediately gets reset back to zero after the allocation is made.
        For more information on components, please see our documentation
        [here](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Compo
        nents-Overview).

        Args:
            product_family_id (str): Either the product family's id or its
                handle prefixed with `handle:`
            body (CreateQuantityBasedComponent, optional): TODO: type
                description here.

        Returns:
            ComponentResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families/{product_family_id}/quantity_based_components.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def create_on_off_component(self,
                                product_family_id,
                                body=None):
        """Does a POST request to /product_families/{product_family_id}/on_off_components.json.

        This request will create a component definition of kind
        **on_off_component** under the specified product family. On/Off
        component can then be added and “allocated” for a subscription.
        On/off components are used for any flat fee, recurring add on (think
        $99/month for tech support or a flat add on shipping fee).
        For more information on components, please see our documentation
        [here](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Compo
        nents-Overview).

        Args:
            product_family_id (str): Either the product family's id or its
                handle prefixed with `handle:`
            body (CreateOnOffComponent, optional): TODO: type description
                here.

        Returns:
            ComponentResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families/{product_family_id}/on_off_components.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def create_prepaid_usage_component(self,
                                       product_family_id,
                                       body=None):
        """Does a POST request to /product_families/{product_family_id}/prepaid_usage_components.json.

        This request will create a component definition of kind
        **prepaid_usage_component** under the specified product family.
        Prepaid component can then be added and “allocated” for a
        subscription.
        Prepaid components allow customers to pre-purchase units that can be
        used up over time on their subscription. In a sense, they are the
        mirror image of metered components; while metered components charge at
        the end of the period for the amount of units used, prepaid components
        are charged for at the time of purchase, and we subsequently keep
        track of the usage against the amount purchased.
        For more information on components, please see our documentation
        [here](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Compo
        nents-Overview).

        Args:
            product_family_id (str): Either the product family's id or its
                handle prefixed with `handle:`
            body (CreatePrepaidComponent, optional): TODO: type description
                here.

        Returns:
            ComponentResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families/{product_family_id}/prepaid_usage_components.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def create_event_based_component(self,
                                     product_family_id,
                                     body=None):
        """Does a POST request to /product_families/{product_family_id}/event_based_components.json.

        This request will create a component definition of kind
        **event_based_component** under the specified product family.
        Event-based component can then be added and “allocated” for a
        subscription.
        Event-based components are similar to other component types, in that
        you define the component parameters (such as name and taxability) and
        the pricing. A key difference for the event-based component is that it
        must be attached to a metric. This is because the metric provides the
        component with the actual quantity used in computing what and how much
        will be billed each period for each subscription.
        So, instead of reporting usage directly for each component (as you
        would with metered components), the usage is derived from analysis of
        your events.
        For more information on components, please see our documentation
        [here](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Compo
        nents-Overview).

        Args:
            product_family_id (str): Either the product family's id or its
                handle prefixed with `handle:`
            body (CreateEBBComponent, optional): TODO: type description here.

        Returns:
            ComponentResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families/{product_family_id}/event_based_components.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def find_component(self,
                       handle):
        """Does a GET request to /components/lookup.json.

        This request will return information regarding a component having the
        handle you provide. You can identify your components with a handle so
        you don't have to save or reference the IDs we generate.

        Args:
            handle (str): The handle of the component to find

        Returns:
            ComponentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/components/lookup.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('handle')
                         .value(handle)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
        ).execute()

    def read_component(self,
                       product_family_id,
                       component_id):
        """Does a GET request to /product_families/{product_family_id}/components/{component_id}.json.

        This request will return information regarding a component from a
        specific product family.
        You may read the component by either the component's id or handle.
        When using the handle, it must be prefixed with `handle:`.

        Args:
            product_family_id (int): The Advanced Billing id of the product
                family to which the component belongs
            component_id (str): Either the Advanced Billing id of the
                component or the handle for the component prefixed with
                `handle:`

        Returns:
            ComponentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families/{product_family_id}/components/{component_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
        ).execute()

    def update_product_family_component(self,
                                        product_family_id,
                                        component_id,
                                        body=None):
        """Does a PUT request to /product_families/{product_family_id}/components/{component_id}.json.

        This request will update a component from a specific product family.
        You may read the component by either the component's id or handle.
        When using the handle, it must be prefixed with `handle:`.

        Args:
            product_family_id (int): The Advanced Billing id of the product
                family to which the component belongs
            component_id (str): Either the Advanced Billing id of the
                component or the handle for the component prefixed with
                `handle:`
            body (UpdateComponentRequest, optional): TODO: type description
                here.

        Returns:
            ComponentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families/{product_family_id}/components/{component_id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def archive_component(self,
                          product_family_id,
                          component_id):
        """Does a DELETE request to /product_families/{product_family_id}/components/{component_id}.json.

        Sending a DELETE request to this endpoint will archive the component.
        All current subscribers will be unffected; their subscription/purchase
        will continue to be charged as usual.

        Args:
            product_family_id (int): The Advanced Billing id of the product
                family to which the component belongs
            component_id (str): Either the Advanced Billing id of the
                component or the handle for the component prefixed with
                `handle:`

        Returns:
            Component: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families/{product_family_id}/components/{component_id}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Component.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def list_components(self,
                        options=dict()):
        """Does a GET request to /components.json.

        This request will return a list of components for a site.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    date_field -- BasicDateField -- The type of filter you
                        would like to apply to your search.
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
                        instead of end_date.  optional
                    include_archived -- bool -- Include archived items
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
                    filter -- ListComponentsFilter -- Filter to use for List
                        Components operations

        Returns:
            List[ComponentResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/components.json')
            .http_method(HttpMethodEnum.GET)
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
            .query_param(Parameter()
                         .key('include_archived')
                         .value(options.get('include_archived', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
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
            .deserialize_into(ComponentResponse.from_dictionary)
        ).execute()

    def update_component(self,
                         component_id,
                         body=None):
        """Does a PUT request to /components/{component_id}.json.

        This request will update a component.
        You may read the component by either the component's id or handle.
        When using the handle, it must be prefixed with `handle:`.

        Args:
            component_id (str): The id or handle of the component
            body (UpdateComponentRequest, optional): TODO: type description
                here.

        Returns:
            ComponentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/components/{component_id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def list_components_for_product_family(self,
                                           options=dict()):
        """Does a GET request to /product_families/{product_family_id}/components.json.

        This request will return a list of components for a particular product
        family.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    product_family_id -- int -- The Advanced Billing id of the
                        product family
                    include_archived -- bool -- Include archived items.
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
                    filter -- ListComponentsFilter -- Filter to use for List
                        Components operations
                    date_field -- BasicDateField -- The type of filter you
                        would like to apply to your search. Use in query
                        `date_field=created_at`.
                    end_date -- str -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns components
                        with a timestamp up to and including 11:59:59PM in
                        your site’s time zone on the date specified.
                    end_datetime -- str -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns components with a timestamp at or
                        before exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of end_date. optional.
                    start_date -- str -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns
                        components with a timestamp at or after midnight
                        (12:00:00 AM) in your site’s time zone on the date
                        specified.
                    start_datetime -- str -- The start date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns components with a timestamp at or
                        after exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date.

        Returns:
            List[ComponentResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families/{product_family_id}/components.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(options.get('product_family_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('include_archived')
                         .value(options.get('include_archived', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('filter')
                         .value(options.get('filter', None)))
            .query_param(Parameter()
                         .key('date_field')
                         .value(options.get('date_field', None)))
            .query_param(Parameter()
                         .key('end_date')
                         .value(options.get('end_date', None)))
            .query_param(Parameter()
                         .key('end_datetime')
                         .value(options.get('end_datetime', None)))
            .query_param(Parameter()
                         .key('start_date')
                         .value(options.get('start_date', None)))
            .query_param(Parameter()
                         .key('start_datetime')
                         .value(options.get('start_datetime', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
        ).execute()
