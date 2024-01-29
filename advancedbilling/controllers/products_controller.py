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
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from advancedbilling.models.product_response import ProductResponse
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException


class ProductsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(ProductsController, self).__init__(config)

    def create_product(self,
                       product_family_id,
                       body=None):
        """Does a POST request to /product_families/{product_family_id}/products.json.

        Use this method to create a product within your Chargify site.
        + [Products
        Documentation](https://maxio-chargify.zendesk.com/hc/en-us/articles/540
        5561405709)
        + [Changing a Subscription's
        Product](https://maxio-chargify.zendesk.com/hc/en-us/articles/540422533
        4669-Product-Changes-Migrations)

        Args:
            product_family_id (int): The Chargify id of the product family to
                which the product belongs
            body (CreateOrUpdateProductRequest, optional): TODO: type
                description here.

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
            .path('/product_families/{product_family_id}/products.json')
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ProductResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def read_product(self,
                     product_id):
        """Does a GET request to /products/{product_id}.json.

        This endpoint allows you to read the current details of a product that
        you've created in Chargify.

        Args:
            product_id (int): The Chargify id of the product

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
            .path('/products/{product_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('product_id')
                            .value(product_id)
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

    def update_product(self,
                       product_id,
                       body=None):
        """Does a PUT request to /products/{product_id}.json.

        Use this method to change aspects of an existing product.
        ### Input Attributes Update Notes
        + `update_return_params` The parameters we will append to your
        `update_return_url`. See Return URLs and Parameters
        ### Product Price Point
        Updating a product using this endpoint will create a new price point
        and set it as the default price point for this product. If you should
        like to update an existing product price point, that must be done
        separately.

        Args:
            product_id (int): The Chargify id of the product
            body (CreateOrUpdateProductRequest, optional): TODO: type
                description here.

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
            .path('/products/{product_id}.json')
            .http_method(HttpMethodEnum.PUT)
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
            .deserialize_into(ProductResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def archive_product(self,
                        product_id):
        """Does a DELETE request to /products/{product_id}.json.

        Sending a DELETE request to this endpoint will archive the product.
        All current subscribers will be unffected; their subscription/purchase
        will continue to be charged monthly.
        This will restrict the option to chose the product for purchase via
        the Billing Portal, as well as disable Public Signup Pages for the
        product.

        Args:
            product_id (int): The Chargify id of the product

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
            .path('/products/{product_id}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('product_id')
                            .value(product_id)
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
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def read_product_by_handle(self,
                               api_handle):
        """Does a GET request to /products/handle/{api_handle}.json.

        This method allows to retrieve a Product object by its `api_handle`.

        Args:
            api_handle (str): The handle of the product

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
            .path('/products/handle/{api_handle}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('api_handle')
                            .value(api_handle)
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

    def list_products(self,
                      options=dict()):
        """Does a GET request to /products.json.

        This method allows to retrieve a list of Products belonging to a
        Site.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    date_field -- BasicDateField -- The type of filter you
                        would like to apply to your search. Use in query:
                        `date_field=created_at`.
                    end_date -- date -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns products with
                        a timestamp up to and including 11:59:59PM in your
                        site’s time zone on the date specified.
                    end_datetime -- datetime -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns products with a timestamp at or
                        before exact time provided in query. You can specify
                        timezone in query - otherwise your site''s time zone
                        will be used. If provided, this parameter will be used
                        instead of end_date.
                    start_date -- date -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns products
                        with a timestamp at or after midnight (12:00:00 AM) in
                        your site’s time zone on the date specified.
                    start_datetime -- datetime -- The start date and time
                        (format YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns products with a timestamp at or
                        after exact time provided in query. You can specify
                        timezone in query - otherwise your site''s time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date.
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
                    include_archived -- bool -- Include archived products. Use
                        in query: `include_archived=true`.
                    include -- ListProductsInclude -- Allows including
                        additional data in the response. Use in query
                        `include=prepaid_product_price_point`.
                    filter_prepaid_product_price_point_product_price_point_id
                        -- IncludeNotNull -- Allows fetching products only if
                        a prepaid product price point is present or not. To
                        use this filter you also have to include the following
                        param in the request
                        `include=prepaid_product_price_point`. Use in query
                        `filter[prepaid_product_price_point][product_price_poin
                        t_id]=not_null`.
                    filter_use_site_exchange_rate -- bool -- Allows fetching
                        products with matching use_site_exchange_rate based on
                        provided value (refers to default price point). Use in
                        query `filter[use_site_exchange_rate]=true`.

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
            .path('/products.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('date_field')
                         .value(options.get('date_field', None)))
            .query_param(Parameter()
                         .key('end_date')
                         .value(options.get('end_date', None)))
            .query_param(Parameter()
                         .key('end_datetime')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('end_datetime', None))))
            .query_param(Parameter()
                         .key('start_date')
                         .value(options.get('start_date', None)))
            .query_param(Parameter()
                         .key('start_datetime')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('start_datetime', None))))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('include_archived')
                         .value(options.get('include_archived', None)))
            .query_param(Parameter()
                         .key('include')
                         .value(options.get('include', None)))
            .query_param(Parameter()
                         .key('filter[prepaid_product_price_point][product_price_point_id]')
                         .value(options.get('filter_prepaid_product_price_point_product_price_point_id', None)))
            .query_param(Parameter()
                         .key('filter[use_site_exchange_rate]')
                         .value(options.get('filter_use_site_exchange_rate', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ProductResponse.from_dictionary)
        ).execute()
