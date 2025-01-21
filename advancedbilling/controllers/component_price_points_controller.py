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
from advancedbilling.models.component_response import ComponentResponse
from advancedbilling.models.component_price_point_response import ComponentPricePointResponse
from advancedbilling.models.component_price_points_response import ComponentPricePointsResponse
from advancedbilling.models.component_currency_prices_response import ComponentCurrencyPricesResponse
from advancedbilling.models.list_components_price_points_response import ListComponentsPricePointsResponse
from advancedbilling.exceptions.error_array_map_response_exception import ErrorArrayMapResponseException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException


class ComponentPricePointsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(ComponentPricePointsController, self).__init__(config)

    def promote_component_price_point_to_default(self,
                                                 component_id,
                                                 price_point_id):
        """Does a PUT request to /components/{component_id}/price_points/{price_point_id}/default.json.

        Sets a new default price point for the component. This new default
        will apply to all new subscriptions going forward - existing
        subscriptions will remain on their current price point.
        See [Price Points
        Documentation](https://maxio.zendesk.com/hc/en-us/articles/242611917371
        01-Price-Points-Components) for more information on price points and
        moving subscriptions between price points.
        Note: Custom price points are not able to be set as the default for a
        component.

        Args:
            component_id (int): The Advanced Billing id of the component to
                which the price point belongs
            price_point_id (int): The Advanced Billing id of the price point

        Returns:
            ComponentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
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
            .auth(Single('BasicAuth'))
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
            component_id (int): The Advanced Billing id of the component
            body (CreateComponentPricePointRequest, optional): The request
                body parameter.

        Returns:
            ComponentPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentPricePointResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorArrayMapResponseException)
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

                    component_id -- int -- The Advanced Billing id of the
                        component
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
            RequestBuilder().server(Server.PRODUCTION)
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentPricePointsResponse.from_dictionary)
        ).execute()

    def bulk_create_component_price_points(self,
                                           component_id,
                                           body=None):
        """Does a POST request to /components/{component_id}/price_points/bulk.json.

        Use this endpoint to create multiple component price points in one
        request.

        Args:
            component_id (str): The Advanced Billing id of the component for
                which you want to fetch price points.
            body (CreateComponentPricePointsRequest, optional): The request
                body parameter.

        Returns:
            ComponentPricePointsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentPricePointsResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
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
            component_id (int | str): The id or handle of the component. When
                using the handle, it must be prefixed with `handle:`. Example:
                `123` for an integer ID, or `handle:example-product-handle`
                for a string handle.
            price_point_id (int | str): The id or handle of the price point.
                When using the handle, it must be prefixed with `handle:`.
                Example: `123` for an integer ID, or
                `handle:example-price_point-handle` for a string handle.
            body (UpdateComponentPricePointRequest, optional): The request
                body parameter.

        Returns:
            ComponentPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/components/{component_id}/price_points/{price_point_id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('UpdateComponentPricePointComponentId').validate(value)))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('UpdateComponentPricePointPricePointId').validate(value)))
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
            .deserialize_into(ComponentPricePointResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorArrayMapResponseException)
        ).execute()

    def read_component_price_point(self,
                                   component_id,
                                   price_point_id,
                                   currency_prices=None):
        """Does a GET request to /components/{component_id}/price_points/{price_point_id}.json.

        Use this endpoint to retrieve details for a specific component price
        point. You can achieve this by using either the component price point
        ID or handle.

        Args:
            component_id (int | str): The id or handle of the component. When
                using the handle, it must be prefixed with `handle:`. Example:
                `123` for an integer ID, or `handle:example-product-handle`
                for a string handle.
            price_point_id (int | str): The id or handle of the price point.
                When using the handle, it must be prefixed with `handle:`.
                Example: `123` for an integer ID, or
                `handle:example-price_point-handle` for a string handle.
            currency_prices (bool, optional): Include an array of currency
                price data

        Returns:
            ComponentPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/components/{component_id}/price_points/{price_point_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('ReadComponentPricePointComponentId').validate(value)))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('ReadComponentPricePointPricePointId').validate(value)))
            .query_param(Parameter()
                         .key('currency_prices')
                         .value(currency_prices))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
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
            component_id (int | str): The id or handle of the component. When
                using the handle, it must be prefixed with `handle:`. Example:
                `123` for an integer ID, or `handle:example-product-handle`
                for a string handle.
            price_point_id (int | str): The id or handle of the price point.
                When using the handle, it must be prefixed with `handle:`.
                Example: `123` for an integer ID, or
                `handle:example-price_point-handle` for a string handle.

        Returns:
            ComponentPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/components/{component_id}/price_points/{price_point_id}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('ArchiveComponentPricePointComponentId').validate(value)))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('ArchiveComponentPricePointPricePointId').validate(value)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentPricePointResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def unarchive_component_price_point(self,
                                        component_id,
                                        price_point_id):
        """Does a PUT request to /components/{component_id}/price_points/{price_point_id}/unarchive.json.

        Use this endpoint to unarchive a component price point.

        Args:
            component_id (int): The Advanced Billing id of the component to
                which the price point belongs
            price_point_id (int): The Advanced Billing id of the price point

        Returns:
            ComponentPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
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
            .auth(Single('BasicAuth'))
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
            price_point_id (int): The Advanced Billing id of the price point
            body (CreateCurrencyPricesRequest, optional): The request body
                parameter.

        Returns:
            ComponentCurrencyPricesResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentCurrencyPricesResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorArrayMapResponseException)
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
            price_point_id (int): The Advanced Billing id of the price point
            body (UpdateCurrencyPricesRequest, optional): The request body
                parameter.

        Returns:
            ComponentCurrencyPricesResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ComponentCurrencyPricesResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorArrayMapResponseException)
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
                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.
                    filter -- ListPricePointsFilter -- Filter to use for List
                        PricePoints operations

        Returns:
            ListComponentsPricePointsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/components_price_points.json')
            .http_method(HttpMethodEnum.GET)
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
            .deserialize_into(ListComponentsPricePointsResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()
