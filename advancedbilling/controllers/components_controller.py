# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.api_helper import APIHelper
from advancedbilling.configuration import Server
from advancedbilling.controllers.base_controller import BaseController
from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from advancedbilling.http.http_method_enum import HttpMethodEnum
from apimatic_core.types.array_serialization_format import SerializationFormats
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from advancedbilling.models.component_response import ComponentResponse
from advancedbilling.models.component import Component
from advancedbilling.models.component_price_point_response import ComponentPricePointResponse
from advancedbilling.models.component_price_points_response import ComponentPricePointsResponse
from advancedbilling.models.currency_price import CurrencyPrice
from advancedbilling.models.list_components_price_points_response import ListComponentsPricePointsResponse
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException


class ComponentsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(ComponentsController, self).__init__(config)

    def create_component(self,
                         product_family_id,
                         component_kind,
                         body=None):
        """Does a POST request to /product_families/{product_family_id}/{component_kind}.json.

        This request will create a component definition under the specified
        product family. These component definitions determine what components
        are named, how they are measured, and how much they cost.
        Components can then be added and “allocated” for each subscription to
        a product in the product family. These component line-items affect how
        much a subscription will be charged, depending on the current
        allocations (i.e. 4 IP Addresses, or SSL “enabled”)
        This documentation covers both component definitions and component
        line-items. Please understand the difference.
        Please note that you may not edit components via API. To do so, please
        log into the application.
        ### Component Documentation
        For more information on components, please see our documentation
        [here](https://maxio-chargify.zendesk.com/hc/en-us/articles/54050206256
        77).
        For information on how to record component usage against a
        subscription, please see the following resources:
        + [Proration and Component
        Allocations](https://maxio-chargify.zendesk.com/hc/en-us/articles/54050
        20625677#applying-proration-and-recording-components)
        + [Recording component usage against a
        subscription](https://maxio-chargify.zendesk.com/hc/en-us/articles/5404
        606587917#recording-component-usage)

        Args:
            product_family_id (int): The Chargify id of the product family to
                which the component belongs
            component_kind (ComponentKindPath): The component kind
            body (CreateMeteredComponent | CreateQuantityBasedComponent |
                CreateOnOffComponent | CreatePrepaidComponent |
                CreateEBBComponent | None, optional): TODO: type description
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
            .path('/product_families/{product_family_id}/{component_kind}.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_kind')
                            .value(component_kind)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body)
                        .validator(lambda value: UnionTypeLookUp.get('CreateComponentBody').validate(value)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def read_component_by_handle(self,
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
        ).execute()

    def read_component_by_id(self,
                             product_family_id,
                             component_id):
        """Does a GET request to /product_families/{product_family_id}/components/{component_id}.json.

        This request will return information regarding a component from a
        specific product family.
        You may read the component by either the component's id or handle.
        When using the handle, it must be prefixed with `handle:`.

        Args:
            product_family_id (int): The Chargify id of the product family to
                which the component belongs
            component_id (str): Either the Chargify id of the component or the
                handle for the component prefixed with `handle:`

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
            .auth(Single('global'))
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
            product_family_id (int): The Chargify id of the product family to
                which the component belongs
            component_id (str): Either the Chargify id of the component or the
                handle for the component prefixed with `handle:`
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
            .auth(Single('global'))
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
            product_family_id (int): The Chargify id of the product family to
                which the component belongs
            component_id (str): Either the Chargify id of the component or the
                handle for the component prefixed with `handle:`

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
            .auth(Single('global'))
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
                    filter_ids -- List[str] -- Allows fetching components with
                        matching id based on provided value. Use in query
                        `filter[ids]=1,2,3`.
                    filter_use_site_exchange_rate -- bool -- Allows fetching
                        components with matching use_site_exchange_rate based
                        on provided value (refers to default price point). Use
                        in query `filter[use_site_exchange_rate]=true`.

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
                         .key('filter[ids]')
                         .value(options.get('filter_ids', None)))
            .query_param(Parameter()
                         .key('filter[use_site_exchange_rate]')
                         .value(options.get('filter_use_site_exchange_rate', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('global'))
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def update_default_price_point_for_component(self,
                                                 component_id,
                                                 price_point_id):
        """Does a PUT request to /components/{component_id}/price_points/{price_point_id}/default.json.

        Sets a new default price point for the component. This new default
        will apply to all new subscriptions going forward - existing
        subscriptions will remain on their current price point.
        See [Price Points
        Documentation](https://chargify.zendesk.com/hc/en-us/articles/440775586
        5883#price-points) for more information on price points and moving
        subscriptions between price points.
        Note: Custom price points are not able to be set as the default for a
        component.

        Args:
            component_id (int): The Chargify id of the component to which the
                price point belongs
            price_point_id (int): The Chargify id of the price point

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
            .path('/components/{component_id}/price_points/{price_point_id}/default.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
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

                    product_family_id -- int -- The Chargify id of the product
                        family
                    include_archived -- bool -- Include archived items.
                    filter_ids -- List[int] -- Allows fetching components with
                        matching id based on provided value. Use in query
                        `filter[ids]=1,2`.
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
                    filter_use_site_exchange_rate -- bool -- Allows fetching
                        components with matching use_site_exchange_rate based
                        on provided value (refers to default price point). Use
                        in query `filter[use_site_exchange_rate]=true`.

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
                         .key('filter[ids]')
                         .value(options.get('filter_ids', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
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
            .query_param(Parameter()
                         .key('filter[use_site_exchange_rate]')
                         .value(options.get('filter_use_site_exchange_rate', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentResponse.from_dictionary)
        ).execute()

    def create_component_price_point(self,
                                     component_id,
                                     body=None):
        """Does a POST request to /components/{component_id}/price_points.json.

        This endpoint can be used to create a new price point for an existing
        component.

        Args:
            component_id (int): The Chargify id of the component
            body (CreateComponentPricePointRequest, optional): TODO: type
                description here.

        Returns:
            ComponentPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/components/{component_id}/price_points.json')
            .http_method(HttpMethodEnum.POST)
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentPricePointResponse.from_dictionary)
        ).execute()

    def list_component_price_points(self,
                                    options=dict()):
        """Does a GET request to /components/{component_id}/price_points.json.

        Use this endpoint to read current price points that are associated
        with a component.
        You may specify the component by using either the numeric id or the
        `handle:gold` syntax.
        When fetching a component's price points, if you have defined multiple
        currencies at the site level, you can optionally pass the
        `?currency_prices=true` query param to include an array of currency
        price data in the response.
        If the price point is set to `use_site_exchange_rate: true`, it will
        return pricing based on the current exchange rate. If the flag is set
        to false, it will return all of the defined prices for each currency.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    component_id -- int -- The Chargify id of the component
                    currency_prices -- bool -- Include an array of currency
                        price data
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
                    filter_type -- List[PricePointType] -- Use in query:
                        `filter[type]=catalog,default`.

        Returns:
            ComponentPricePointsResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/components/{component_id}/price_points.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('component_id')
                            .value(options.get('component_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('currency_prices')
                         .value(options.get('currency_prices', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('filter[type]')
                         .value(options.get('filter_type', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentPricePointsResponse.from_dictionary)
        ).execute()

    def create_component_price_points(self,
                                      component_id,
                                      body=None):
        """Does a POST request to /components/{component_id}/price_points/bulk.json.

        Use this endpoint to create multiple component price points in one
        request.

        Args:
            component_id (str): The Chargify id of the component for which you
                want to fetch price points.
            body (CreateComponentPricePointsRequest, optional): TODO: type
                description here.

        Returns:
            ComponentPricePointsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/components/{component_id}/price_points/bulk.json')
            .http_method(HttpMethodEnum.POST)
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentPricePointsResponse.from_dictionary)
        ).execute()

    def update_component_price_point(self,
                                     component_id,
                                     price_point_id,
                                     body=None):
        """Does a PUT request to /components/{component_id}/price_points/{price_point_id}.json.

        When updating a price point, it's prices can be updated as well by
        creating new prices or editing / removing existing ones.
        Passing in a price bracket without an `id` will attempt to create a
        new price.
        Including an `id` will update the corresponding price, and including
        the `_destroy` flag set to true along with the `id` will remove that
        price.
        Note: Custom price points cannot be updated directly. They must be
        edited through the Subscription.

        Args:
            component_id (int): The Chargify id of the component to which the
                price point belongs
            price_point_id (int): The Chargify id of the price point
            body (UpdateComponentPricePointRequest, optional): TODO: type
                description here.

        Returns:
            ComponentPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/components/{component_id}/price_points/{price_point_id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentPricePointResponse.from_dictionary)
        ).execute()

    def archive_component_price_point(self,
                                      component_id,
                                      price_point_id):
        """Does a DELETE request to /components/{component_id}/price_points/{price_point_id}.json.

        A price point can be archived at any time. Subscriptions using a price
        point that has been archived will continue using it until they're
        moved to another price point.

        Args:
            component_id (int): The Chargify id of the component to which the
                price point belongs
            price_point_id (int): The Chargify id of the price point

        Returns:
            ComponentPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/components/{component_id}/price_points/{price_point_id}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentPricePointResponse.from_dictionary)
        ).execute()

    def unarchive_component_price_point(self,
                                        component_id,
                                        price_point_id):
        """Does a PUT request to /components/{component_id}/price_points/{price_point_id}/unarchive.json.

        Use this endpoint to unarchive a component price point.

        Args:
            component_id (int): The Chargify id of the component to which the
                price point belongs
            price_point_id (int): The Chargify id of the price point

        Returns:
            ComponentPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/components/{component_id}/price_points/{price_point_id}/unarchive.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentPricePointResponse.from_dictionary)
        ).execute()

    def create_currency_prices(self,
                               price_point_id,
                               body=None):
        """Does a POST request to /price_points/{price_point_id}/currency_prices.json.

        This endpoint allows you to create currency prices for a given
        currency that has been defined on the site level in your settings.
        When creating currency prices, they need to mirror the structure of
        your primary pricing. For each price level defined on the component
        price point, there should be a matching price level created in the
        given currency.
        Note: Currency Prices are not able to be created for custom price
        points.

        Args:
            price_point_id (int): The Chargify id of the price point
            body (CreateCurrencyPricesRequest, optional): TODO: type
                description here.

        Returns:
            List[CurrencyPrice]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/price_points/{price_point_id}/currency_prices.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CurrencyPrice.from_dictionary)
        ).execute()

    def update_currency_prices(self,
                               price_point_id,
                               body=None):
        """Does a PUT request to /price_points/{price_point_id}/currency_prices.json.

        This endpoint allows you to update currency prices for a given
        currency that has been defined on the site level in your settings.
        Note: Currency Prices are not able to be updated for custom price
        points.

        Args:
            price_point_id (int): The Chargify id of the price point
            body (UpdateCurrencyPricesRequest, optional): TODO: type
                description here.

        Returns:
            List[CurrencyPrice]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/price_points/{price_point_id}/currency_prices.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CurrencyPrice.from_dictionary)
        ).execute()

    def list_all_component_price_points(self,
                                        options=dict()):
        """Does a GET request to /components_price_points.json.

        This method allows to retrieve a list of Components Price Points
        belonging to a Site.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    filter_date_field -- BasicDateField -- The type of filter
                        you would like to apply to your search. Use in query:
                        `filter[date_field]=created_at`.
                    filter_end_date -- date -- The end date (format
                        YYYY-MM-DD) with which to filter the date_field.
                        Returns price points with a timestamp up to and
                        including 11:59:59PM in your site’s time zone on the
                        date specified.
                    filter_end_datetime -- datetime -- The end date and time
                        (format YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns price points with a timestamp at
                        or before exact time provided in query. You can
                        specify timezone in query - otherwise your site's time
                        zone will be used. If provided, this parameter will be
                        used instead of end_date.
                    include -- ListComponentsPricePointsInclude -- Allows
                        including additional data in the response. Use in
                        query: `include=currency_prices`.
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
                    filter_start_date -- date -- The start date (format
                        YYYY-MM-DD) with which to filter the date_field.
                        Returns price points with a timestamp at or after
                        midnight (12:00:00 AM) in your site’s time zone on the
                        date specified.
                    filter_start_datetime -- datetime -- The start date and
                        time (format YYYY-MM-DD HH:MM:SS) with which to filter
                        the date_field. Returns price points with a timestamp
                        at or after exact time provided in query. You can
                        specify timezone in query - otherwise your site's time
                        zone will be used. If provided, this parameter will be
                        used instead of start_date.
                    filter_type -- List[PricePointType] -- Allows fetching
                        price points with matching type. Use in query:
                        `filter[type]=custom,catalog`.
                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.
                    filter_ids -- List[int] -- Allows fetching price points
                        with matching id based on provided values. Use in
                        query: `filter[ids]=1,2,3`.
                    filter_archived_at -- IncludeNotNull -- Allows fetching
                        price points only if archived_at is present or not.
                        Use in query: `filter[archived_at]=not_null`.

        Returns:
            ListComponentsPricePointsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/components_price_points.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('filter[date_field]')
                         .value(options.get('filter_date_field', None)))
            .query_param(Parameter()
                         .key('filter[end_date]')
                         .value(options.get('filter_end_date', None)))
            .query_param(Parameter()
                         .key('filter[end_datetime]')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('filter_end_datetime', None))))
            .query_param(Parameter()
                         .key('include')
                         .value(options.get('include', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('filter[start_date]')
                         .value(options.get('filter_start_date', None)))
            .query_param(Parameter()
                         .key('filter[start_datetime]')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('filter_start_datetime', None))))
            .query_param(Parameter()
                         .key('filter[type]')
                         .value(options.get('filter_type', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .query_param(Parameter()
                         .key('filter[ids]')
                         .value(options.get('filter_ids', None)))
            .query_param(Parameter()
                         .key('filter[archived_at]')
                         .value(options.get('filter_archived_at', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListComponentsPricePointsResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()
