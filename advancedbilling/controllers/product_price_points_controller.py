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
from advancedbilling.models.product_price_point_response import ProductPricePointResponse
from advancedbilling.models.list_product_price_points_response import ListProductPricePointsResponse
from advancedbilling.models.product_response import ProductResponse
from advancedbilling.models.bulk_create_product_price_points_response import BulkCreateProductPricePointsResponse
from advancedbilling.models.product_price_point_currency_price import ProductPricePointCurrencyPrice
from advancedbilling.exceptions.product_price_point_error_response_exception import ProductPricePointErrorResponseException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_map_response_exception import ErrorMapResponseException


class ProductPricePointsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(ProductPricePointsController, self).__init__(config)

    def create_product_price_point(self,
                                   product_id,
                                   body=None):
        """Does a POST request to /products/{product_id}/price_points.json.

        [Product Price Point
        Documentation](https://chargify.zendesk.com/hc/en-us/articles/440775582
        4155)

        Args:
            product_id (int | str): The id or handle of the product. When
                using the handle, it must be prefixed with `handle:`
            body (CreateProductPricePointRequest, optional): TODO: type
                description here.

        Returns:
            ProductPricePointResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/products/{product_id}/price_points.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('product_id')
                            .value(product_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('CreateProductPricePointProductId').validate(value)))
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
            .deserialize_into(ProductPricePointResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ProductPricePointErrorResponseException)
        ).execute()

    def list_product_price_points(self,
                                  options=dict()):
        """Does a GET request to /products/{product_id}/price_points.json.

        Use this endpoint to retrieve a list of product price points.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    product_id -- int | str -- The id or handle of the
                        product. When using the handle, it must be prefixed
                        with `handle:`
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
                        records to fetch in each request. Default value is 10.
                        The maximum allowed values is 200; any per_page value
                        over 200 will be changed to 200.
                    currency_prices -- bool -- When fetching a product's price
                        points, if you have defined multiple currencies at the
                        site level, you can optionally pass the
                        ?currency_prices=true query param to include an array
                        of currency price data in the response. If the product
                        price point is set to use_site_exchange_rate: true, it
                        will return pricing based on the current exchange
                        rate. If the flag is set to false, it will return all
                        of the defined prices for each currency.
                    filter_type -- List[PricePointType] -- Use in query:
                        `filter[type]=catalog,default`.

        Returns:
            ListProductPricePointsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/products/{product_id}/price_points.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('product_id')
                            .value(options.get('product_id', None))
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('ListProductPricePointsInputProductId').validate(value)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('currency_prices')
                         .value(options.get('currency_prices', None)))
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
            .deserialize_into(ListProductPricePointsResponse.from_dictionary)
        ).execute()

    def update_product_price_point(self,
                                   product_id,
                                   price_point_id,
                                   body=None):
        """Does a PUT request to /products/{product_id}/price_points/{price_point_id}.json.

        Use this endpoint to update a product price point.
        Note: Custom product price points are not able to be updated.

        Args:
            product_id (int | str): The id or handle of the product. When
                using the handle, it must be prefixed with `handle:`
            price_point_id (int | str): The id or handle of the price point.
                When using the handle, it must be prefixed with `handle:`
            body (UpdateProductPricePointRequest, optional): TODO: type
                description here.

        Returns:
            ProductPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/products/{product_id}/price_points/{price_point_id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('product_id')
                            .value(product_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('UpdateProductPricePointProductId').validate(value)))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('UpdateProductPricePointPricePointId').validate(value)))
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
            .deserialize_into(ProductPricePointResponse.from_dictionary)
        ).execute()

    def read_product_price_point(self,
                                 product_id,
                                 price_point_id,
                                 currency_prices=None):
        """Does a GET request to /products/{product_id}/price_points/{price_point_id}.json.

        Use this endpoint to retrieve details for a specific product price
        point.

        Args:
            product_id (int | str): The id or handle of the product. When
                using the handle, it must be prefixed with `handle:`
            price_point_id (int | str): The id or handle of the price point.
                When using the handle, it must be prefixed with `handle:`
            currency_prices (bool, optional): When fetching a product's price
                points, if you have defined multiple currencies at the site
                level, you can optionally pass the ?currency_prices=true query
                param to include an array of currency price data in the
                response. If the product price point is set to
                use_site_exchange_rate: true, it will return pricing based on
                the current exchange rate. If the flag is set to false, it
                will return all of the defined prices for each currency.

        Returns:
            ProductPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/products/{product_id}/price_points/{price_point_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('product_id')
                            .value(product_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('ReadProductPricePointProductId').validate(value)))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('ReadProductPricePointPricePointId').validate(value)))
            .query_param(Parameter()
                         .key('currency_prices')
                         .value(currency_prices))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ProductPricePointResponse.from_dictionary)
        ).execute()

    def archive_product_price_point(self,
                                    product_id,
                                    price_point_id):
        """Does a DELETE request to /products/{product_id}/price_points/{price_point_id}.json.

        Use this endpoint to archive a product price point.

        Args:
            product_id (int | str): The id or handle of the product. When
                using the handle, it must be prefixed with `handle:`
            price_point_id (int | str): The id or handle of the price point.
                When using the handle, it must be prefixed with `handle:`

        Returns:
            ProductPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/products/{product_id}/price_points/{price_point_id}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('product_id')
                            .value(product_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('ArchiveProductPricePointProductId').validate(value)))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('ArchiveProductPricePointPricePointId').validate(value)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ProductPricePointResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()

    def unarchive_product_price_point(self,
                                      product_id,
                                      price_point_id):
        """Does a PATCH request to /products/{product_id}/price_points/{price_point_id}/unarchive.json.

        Use this endpoint to unarchive an archived product price point.

        Args:
            product_id (int): The Chargify id of the product to which the
                price point belongs
            price_point_id (int): The Chargify id of the product price point

        Returns:
            ProductPricePointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/products/{product_id}/price_points/{price_point_id}/unarchive.json')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('product_id')
                            .value(product_id)
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
            .deserialize_into(ProductPricePointResponse.from_dictionary)
        ).execute()

    def promote_product_price_point_to_default(self,
                                               product_id,
                                               price_point_id):
        """Does a PATCH request to /products/{product_id}/price_points/{price_point_id}/default.json.

        Use this endpoint to make a product price point the default for the
        product.
        Note: Custom product price points are not able to be set as the
        default for a product.

        Args:
            product_id (int): The Chargify id of the product to which the
                price point belongs
            price_point_id (int): The Chargify id of the product price point

        Returns:
            ProductResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/products/{product_id}/price_points/{price_point_id}/default.json')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('product_id')
                            .value(product_id)
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
            .deserialize_into(ProductResponse.from_dictionary)
        ).execute()

    def create_product_price_points(self,
                                    product_id,
                                    body=None):
        """Does a POST request to /products/{product_id}/price_points/bulk.json.

        Use this endpoint to create multiple product price points in one
        request.

        Args:
            product_id (int): The Chargify id of the product to which the
                price points belong
            body (BulkCreateProductPricePointsRequest, optional): TODO: type
                description here.

        Returns:
            BulkCreateProductPricePointsResponse: Response from the API.
                Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/products/{product_id}/price_points/bulk.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('product_id')
                            .value(product_id)
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
            .deserialize_into(BulkCreateProductPricePointsResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', APIException)
        ).execute()

    def create_product_currency_prices(self,
                                       product_price_point_id,
                                       body=None):
        """Does a POST request to /product_price_points/{product_price_point_id}/currency_prices.json.

        This endpoint allows you to create currency prices for a given
        currency that has been defined on the site level in your settings.
        When creating currency prices, they need to mirror the structure of
        your primary pricing. If the product price point defines a trial
        and/or setup fee, each currency must also define a trial and/or setup
        fee.
        Note: Currency Prices are not able to be created for custom product
        price points.

        Args:
            product_price_point_id (int): The Chargify id of the product price
                point
            body (CreateProductCurrencyPricesRequest, optional): TODO: type
                description here.

        Returns:
            ProductPricePointCurrencyPrice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_price_points/{product_price_point_id}/currency_prices.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('product_price_point_id')
                            .value(product_price_point_id)
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
            .deserialize_into(ProductPricePointCurrencyPrice.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorMapResponseException)
        ).execute()

    def update_product_currency_prices(self,
                                       product_price_point_id,
                                       body=None):
        """Does a PUT request to /product_price_points/{product_price_point_id}/currency_prices.json.

        This endpoint allows you to update the `price`s of currency prices for
        a given currency that exists on the product price point.
        When updating the pricing, it needs to mirror the structure of your
        primary pricing. If the product price point defines a trial and/or
        setup fee, each currency must also define a trial and/or setup fee.
        Note: Currency Prices are not able to be updated for custom product
        price points.

        Args:
            product_price_point_id (int): The Chargify id of the product price
                point
            body (UpdateCurrencyPricesRequest, optional): TODO: type
                description here.

        Returns:
            ProductPricePointCurrencyPrice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_price_points/{product_price_point_id}/currency_prices.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('product_price_point_id')
                            .value(product_price_point_id)
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
            .deserialize_into(ProductPricePointCurrencyPrice.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorMapResponseException)
        ).execute()

    def list_all_product_price_points(self,
                                      options=dict()):
        """Does a GET request to /products_price_points.json.

        This method allows retrieval of a list of Products Price Points
        belonging to a Site.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.
                    filter_archived_at -- IncludeNotNull -- Allows fetching
                        price points only if archived_at is present or not.
                        Use in query: `filter[archived_at]=not_null`.
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
                    filter_ids -- List[int] -- Allows fetching price points
                        with matching id based on provided values. Use in
                        query: `filter[ids]=1,2,3`.
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
                        `filter[type]=catalog,custom`.
                    include -- ListProductsPricePointsInclude -- Allows
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

        Returns:
            ListProductPricePointsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/products_price_points.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .query_param(Parameter()
                         .key('filter[archived_at]')
                         .value(options.get('filter_archived_at', None)))
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
                         .key('filter[ids]')
                         .value(options.get('filter_ids', None)))
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
                         .key('include')
                         .value(options.get('include', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListProductPricePointsResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()
