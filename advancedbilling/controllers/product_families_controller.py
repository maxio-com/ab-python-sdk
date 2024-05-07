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
from advancedbilling.models.product_response import ProductResponse
from advancedbilling.models.product_family_response import ProductFamilyResponse
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException


class ProductFamiliesController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(ProductFamiliesController, self).__init__(config)

    def list_products_for_product_family(self,
                                         options=dict()):
        """Does a GET request to /product_families/{product_family_id}/products.json.

        This method allows to retrieve a list of Products belonging to a
        Product Family.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    product_family_id -- int -- The Chargify id of the product
                        family to which the product belongs
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
                        would like to apply to your search. Use in query:
                        `date_field=created_at`.
                    filter -- ListProductsFilter -- Filter to use for List
                        Products operations
                    start_date -- str -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns products
                        with a timestamp at or after midnight (12:00:00 AM) in
                        your site’s time zone on the date specified.
                    end_date -- str -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns products with
                        a timestamp up to and including 11:59:59PM in your
                        site’s time zone on the date specified.
                    start_datetime -- str -- The start date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns products with a timestamp at or
                        after exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date.
                    end_datetime -- str -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns products with a timestamp at or
                        before exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of end_date.
                    include_archived -- bool -- Include archived products
                    include -- ListProductsInclude -- Allows including
                        additional data in the response. Use in query
                        `include=prepaid_product_price_point`.

        Returns:
            List[ProductResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families/{product_family_id}/products.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(options.get('product_family_id', None))
                            .is_required(True)
                            .should_encode(True))
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
                         .key('filter')
                         .value(options.get('filter', None)))
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
                         .key('include')
                         .value(options.get('include', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ProductResponse.from_dictionary)
            .local_error('404', 'Not Found', APIException)
        ).execute()

    def create_product_family(self,
                              body=None):
        """Does a POST request to /product_families.json.

        This method will create a Product Family within your Chargify site.
        Create a Product Family to act as a container for your products,
        components and coupons.
        Full documentation on how Product Families operate within the Chargify
        UI can be located
        [here](https://maxio-chargify.zendesk.com/hc/en-us/articles/54053696334
        21).

        Args:
            body (CreateProductFamilyRequest, optional): TODO: type
                description here.

        Returns:
            ProductFamilyResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families.json')
            .http_method(HttpMethodEnum.POST)
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
            .deserialize_into(ProductFamilyResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def list_product_families(self,
                              options=dict()):
        """Does a GET request to /product_families.json.

        This method allows to retrieve a list of Product Families for a site.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    date_field -- BasicDateField -- The type of filter you
                        would like to apply to your search. Use in query:
                        `date_field=created_at`.
                    start_date -- str -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns products
                        with a timestamp at or after midnight (12:00:00 AM) in
                        your site’s time zone on the date specified.
                    end_date -- str -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns products with
                        a timestamp up to and including 11:59:59PM in your
                        site’s time zone on the date specified.
                    start_datetime -- str -- The start date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns products with a timestamp at or
                        after exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date.
                    end_datetime -- str -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns products with a timestamp at or
                        before exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of end_date.

        Returns:
            List[ProductFamilyResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families.json')
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
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ProductFamilyResponse.from_dictionary)
        ).execute()

    def read_product_family(self,
                            id):
        """Does a GET request to /product_families/{id}.json.

        This method allows to retrieve a Product Family via the
        `product_family_id`. The response will contain a Product Family
        object.
        The product family can be specified either with the id number, or with
        the `handle:my-family` format.

        Args:
            id (int): The Chargify id of the product family

        Returns:
            ProductFamilyResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/product_families/{id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ProductFamilyResponse.from_dictionary)
        ).execute()
