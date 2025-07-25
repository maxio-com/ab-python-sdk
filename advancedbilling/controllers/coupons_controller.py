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
from advancedbilling.models.coupon_response import CouponResponse
from advancedbilling.models.coupon_usage import CouponUsage
from advancedbilling.models.coupon_currency_response import CouponCurrencyResponse
from advancedbilling.models.coupon_subcodes_response import CouponSubcodesResponse
from advancedbilling.models.coupon_subcodes import CouponSubcodes
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.exceptions.single_string_error_response_exception import SingleStringErrorResponseException
from advancedbilling.exceptions.error_string_map_response_exception import ErrorStringMapResponseException
from advancedbilling.exceptions.api_exception import APIException


class CouponsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(CouponsController, self).__init__(config)

    def create_coupon(self,
                      product_family_id,
                      body=None):
        """Does a POST request to /product_families/{product_family_id}/coupons.json.

        ## Coupons Documentation
        Coupons can be administered in the Advanced Billing application or
        created via API. Please view our section on [creating
        coupons](https://maxio.zendesk.com/hc/en-us/articles/24261212433165-Cre
        ating-Editing-Deleting-Coupons) for more information.
        Additionally, for documentation on how to apply a coupon to a
        subscription within the Advanced Billing UI, please see our
        documentation
        [here](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupo
        ns-and-Subscriptions).
        ## Create Coupon
        This request will create a coupon, based on the provided information.
        You can create either a flat amount coupon, by specyfing
        `amount_in_cents`, or percentage coupon by specyfing `percentage`.
        You can restrict a coupon to only apply to specific products /
        components by optionally passing in `restricted_products` and/or
        `restricted_components` objects in the format:
        `{ "<product_id/component_id>": boolean_value }`

        Args:
            product_family_id (int): The Advanced Billing id of the product
                family to which the coupon belongs
            body (CouponRequest, optional): The request body parameter.

        Returns:
            CouponResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/product_families/{product_family_id}/coupons.json')
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
            .deserialize_into(CouponResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def list_coupons_for_product_family(self,
                                        options=dict()):
        """Does a GET request to /product_families/{product_family_id}/coupons.json.

        List coupons for a specific Product Family in a Site.
        If the coupon is set to `use_site_exchange_rate: true`, it will return
        pricing based on the current exchange rate. If the flag is set to
        false, it will return all of the defined prices for each currency.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    product_family_id -- int -- The Advanced Billing id of the
                        product family to which the coupon belongs
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
                        records to fetch in each request. Default value is 30.
                        The maximum allowed values is 200; any per_page value
                        over 200 will be changed to 200. Use in query
                        `per_page=200`.
                    filter -- ListCouponsFilter -- Filter to use for List
                        Coupons operations
                    currency_prices -- bool -- When fetching coupons, if you
                        have defined multiple currencies at the site level,
                        you can optionally pass the `?currency_prices=true`
                        query param to include an array of currency price data
                        in the response. Use in query `currency_prices=true`.

        Returns:
            List[CouponResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/product_families/{product_family_id}/coupons.json')
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
                         .key('filter')
                         .value(options.get('filter', None)))
            .query_param(Parameter()
                         .key('currency_prices')
                         .value(options.get('currency_prices', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CouponResponse.from_dictionary)
        ).execute()

    def find_coupon(self,
                    product_family_id=None,
                    code=None,
                    currency_prices=None):
        """Does a GET request to /coupons/find.json.

        You can search for a coupon via the API with the find method. By
        passing a code parameter, the find will attempt to locate a coupon
        that matches that code. If no coupon is found, a 404 is returned.
        If you have more than one product family and if the coupon you are
        trying to find does not belong to the default product family in your
        site, then you will need to specify (either in the url or as a query
        string param) the product family id.

        Args:
            product_family_id (int, optional): The Advanced Billing id of the
                product family to which the coupon belongs
            code (str, optional): The code of the coupon
            currency_prices (bool, optional): When fetching coupons, if you
                have defined multiple currencies at the site level, you can
                optionally pass the `?currency_prices=true` query param to
                include an array of currency price data in the response.

        Returns:
            CouponResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/coupons/find.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('product_family_id')
                         .value(product_family_id))
            .query_param(Parameter()
                         .key('code')
                         .value(code))
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
            .deserialize_into(CouponResponse.from_dictionary)
        ).execute()

    def read_coupon(self,
                    product_family_id,
                    coupon_id,
                    currency_prices=None):
        """Does a GET request to /product_families/{product_family_id}/coupons/{coupon_id}.json.

        You can retrieve the Coupon via the API with the Show method. You must
        identify the Coupon in this call by the ID parameter that Advanced
        Billing assigns.
        If instead you would like to find a Coupon using a Coupon code, see
        the Coupon Find method.
        When fetching a coupon, if you have defined multiple currencies at the
        site level, you can optionally pass the `?currency_prices=true` query
        param to include an array of currency price data in the response.
        If the coupon is set to `use_site_exchange_rate: true`, it will return
        pricing based on the current exchange rate. If the flag is set to
        false, it will return all of the defined prices for each currency.

        Args:
            product_family_id (int): The Advanced Billing id of the product
                family to which the coupon belongs
            coupon_id (int): The Advanced Billing id of the coupon
            currency_prices (bool, optional): When fetching coupons, if you
                have defined multiple currencies at the site level, you can
                optionally pass the `?currency_prices=true` query param to
                include an array of currency price data in the response.

        Returns:
            CouponResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/product_families/{product_family_id}/coupons/{coupon_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('coupon_id')
                            .value(coupon_id)
                            .is_required(True)
                            .should_encode(True))
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
            .deserialize_into(CouponResponse.from_dictionary)
        ).execute()

    def update_coupon(self,
                      product_family_id,
                      coupon_id,
                      body=None):
        """Does a PUT request to /product_families/{product_family_id}/coupons/{coupon_id}.json.

        ## Update Coupon
        You can update a Coupon via the API with a PUT request to the resource
        endpoint.
        You can restrict a coupon to only apply to specific products /
        components by optionally passing in hashes of `restricted_products`
        and/or `restricted_components` in the format:
        `{ "<product/component_id>": boolean_value }`

        Args:
            product_family_id (int): The Advanced Billing id of the product
                family to which the coupon belongs
            coupon_id (int): The Advanced Billing id of the coupon
            body (CouponRequest, optional): The request body parameter.

        Returns:
            CouponResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/product_families/{product_family_id}/coupons/{coupon_id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('coupon_id')
                            .value(coupon_id)
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
            .deserialize_into(CouponResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def archive_coupon(self,
                       product_family_id,
                       coupon_id):
        """Does a DELETE request to /product_families/{product_family_id}/coupons/{coupon_id}.json.

        You can archive a Coupon via the API with the archive method.
        Archiving makes that Coupon unavailable for future use, but allows it
        to remain attached and functional on existing Subscriptions that are
        using it.
        The `archived_at` date and time will be assigned.

        Args:
            product_family_id (int): The Advanced Billing id of the product
                family to which the coupon belongs
            coupon_id (int): The Advanced Billing id of the coupon

        Returns:
            CouponResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/product_families/{product_family_id}/coupons/{coupon_id}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('coupon_id')
                            .value(coupon_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CouponResponse.from_dictionary)
        ).execute()

    def list_coupons(self,
                     options=dict()):
        """Does a GET request to /coupons.json.

        You can retrieve a list of coupons.
        If the coupon is set to `use_site_exchange_rate: true`, it will return
        pricing based on the current exchange rate. If the flag is set to
        false, it will return all of the defined prices for each currency.

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
                        records to fetch in each request. Default value is 30.
                        The maximum allowed values is 200; any per_page value
                        over 200 will be changed to 200. Use in query
                        `per_page=200`.
                    filter -- ListCouponsFilter -- Filter to use for List
                        Coupons operations
                    currency_prices -- bool -- When fetching coupons, if you
                        have defined multiple currencies at the site level,
                        you can optionally pass the `?currency_prices=true`
                        query param to include an array of currency price data
                        in the response. Use in query `currency_prices=true`.

        Returns:
            List[CouponResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/coupons.json')
            .http_method(HttpMethodEnum.GET)
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
                         .key('currency_prices')
                         .value(options.get('currency_prices', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CouponResponse.from_dictionary)
        ).execute()

    def read_coupon_usage(self,
                          product_family_id,
                          coupon_id):
        """Does a GET request to /product_families/{product_family_id}/coupons/{coupon_id}/usage.json.

        This request will provide details about the coupon usage as an array
        of data hashes, one per product.

        Args:
            product_family_id (int): The Advanced Billing id of the product
                family to which the coupon belongs
            coupon_id (int): The Advanced Billing id of the coupon

        Returns:
            List[CouponUsage]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/product_families/{product_family_id}/coupons/{coupon_id}/usage.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('product_family_id')
                            .value(product_family_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('coupon_id')
                            .value(coupon_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CouponUsage.from_dictionary)
        ).execute()

    def validate_coupon(self,
                        code,
                        product_family_id=None):
        """Does a GET request to /coupons/validate.json.

        You can verify if a specific coupon code is valid using the `validate`
        method. This method is useful for validating coupon codes that are
        entered by a customer. If the coupon is found and is valid, the coupon
        will be returned with a 200 status code.
        If the coupon is invalid, the status code will be 404 and the response
        will say why it is invalid. If the coupon is valid, the status code
        will be 200 and the coupon will be returned. The following reasons for
        invalidity are supported:
        + Coupon not found
        + Coupon is invalid
        + Coupon expired
        If you have more than one product family and if the coupon you are
        validating does not belong to the first product family in your site,
        then you will need to specify the product family, either in the url or
        as a query string param. This can be done by supplying the id or the
        handle in the `handle:my-family` format.
        Eg.
        ```
        https://<subdomain>.chargify.com/product_families/handle:<product_famil
        y_handle>/coupons/validate.<format>?code=<coupon_code>
        ```
        Or:
        ```
        https://<subdomain>.chargify.com/coupons/validate.<format>?code=<coupon
        _code>&product_family_id=<id>
        ```

        Args:
            code (str): The code of the coupon
            product_family_id (int, optional): The Advanced Billing id of the
                product family to which the coupon belongs

        Returns:
            CouponResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/coupons/validate.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('code')
                         .value(code)
                         .is_required(True))
            .query_param(Parameter()
                         .key('product_family_id')
                         .value(product_family_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CouponResponse.from_dictionary)
            .local_error_template('404', 'Not Found: \'{$response.body}\'', SingleStringErrorResponseException)
        ).execute()

    def create_or_update_coupon_currency_prices(self,
                                                coupon_id,
                                                body=None):
        """Does a PUT request to /coupons/{coupon_id}/currency_prices.json.

        This endpoint allows you to create and/or update currency prices for
        an existing coupon. Multiple prices can be created or updated in a
        single request but each of the currencies must be defined on the site
        level already and the coupon must be an amount-based coupon, not
        percentage.
        Currency pricing for coupons must mirror the setup of the primary
        coupon pricing - if the primary coupon is percentage based, you will
        not be able to define pricing in non-primary currencies.

        Args:
            coupon_id (int): The Advanced Billing id of the coupon
            body (CouponCurrencyRequest, optional): The request body parameter.

        Returns:
            CouponCurrencyResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/coupons/{coupon_id}/currency_prices.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('coupon_id')
                            .value(coupon_id)
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
            .deserialize_into(CouponCurrencyResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorStringMapResponseException)
        ).execute()

    def create_coupon_subcodes(self,
                               coupon_id,
                               body=None):
        """Does a POST request to /coupons/{coupon_id}/codes.json.

        ## Coupon Subcodes Intro
        Coupon Subcodes allow you to create a set of unique codes that allow
        you to expand the use of one coupon.
        For example:
        Master Coupon Code:
        + SPRING2020
        Coupon Subcodes:
        + SPRING90210
        + DP80302
        + SPRINGBALTIMORE
        Coupon subcodes can be administered in the Admin Interface or via the
        API.
        When creating a coupon subcode, you must specify a coupon to attach it
        to using the coupon_id. Valid coupon subcodes are all capital letters,
        contain only letters and numbers, and do not have any spaces.
        Lowercase letters will be capitalized before the subcode is created.
        ## Coupon Subcodes Documentation
        Full documentation on how to create coupon subcodes in the Advanced
        Billing UI can be located
        [here](https://maxio.zendesk.com/hc/en-us/articles/24261208729229-Coupo
        n-Codes).
        Additionally, for documentation on how to apply a coupon to a
        Subscription within the Advanced Billing UI, please see our
        documentation
        [here](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupo
        ns-and-Subscriptions).
        ## Create Coupon Subcode
        This request allows you to create specific subcodes underneath an
        existing coupon code.
        *Note*: If you are using any of the allowed special characters ("%",
        "@", "+", "-", "_", and "."), you must encode them for use in the URL.
            % to %25
            @ to %40
            + to %2B
            - to %2D
            _ to %5F
            . to %2E
        So, if the coupon subcode is `20%OFF`, the URL to delete this coupon
        subcode would be:
        `https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>`

        Args:
            coupon_id (int): The Advanced Billing id of the coupon
            body (CouponSubcodes, optional): The request body parameter.

        Returns:
            CouponSubcodesResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/coupons/{coupon_id}/codes.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('coupon_id')
                            .value(coupon_id)
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
            .deserialize_into(CouponSubcodesResponse.from_dictionary)
        ).execute()

    def list_coupon_subcodes(self,
                             options=dict()):
        """Does a GET request to /coupons/{coupon_id}/codes.json.

        This request allows you to request the subcodes that are attached to a
        coupon.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    coupon_id -- int -- The Advanced Billing id of the coupon
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
            CouponSubcodes: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/coupons/{coupon_id}/codes.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('coupon_id')
                            .value(options.get('coupon_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CouponSubcodes.from_dictionary)
        ).execute()

    def update_coupon_subcodes(self,
                               coupon_id,
                               body=None):
        """Does a PUT request to /coupons/{coupon_id}/codes.json.

        You can update the subcodes for the given Coupon via the API with a
        PUT request to the resource endpoint.
        Send an array of new coupon subcodes.
        **Note**: All current subcodes for that Coupon will be deleted first,
        and replaced with the list of subcodes sent to this endpoint.
        The response will contain:
        + The created subcodes,
        + Subcodes that were not created because they already exist,
        + Any subcodes not created because they are invalid.

        Args:
            coupon_id (int): The Advanced Billing id of the coupon
            body (CouponSubcodes, optional): The request body parameter.

        Returns:
            CouponSubcodesResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/coupons/{coupon_id}/codes.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('coupon_id')
                            .value(coupon_id)
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
            .deserialize_into(CouponSubcodesResponse.from_dictionary)
        ).execute()

    def delete_coupon_subcode(self,
                              coupon_id,
                              subcode):
        """Does a DELETE request to /coupons/{coupon_id}/codes/{subcode}.json.

        ## Example
        Given a coupon with an ID of 567, and a coupon subcode of 20OFF, the
        URL to `DELETE` this coupon subcode would be:
        ```
        http://subdomain.chargify.com/coupons/567/codes/20OFF.<format>
        ```
        Note: If you are using any of the allowed special characters (“%”,
        “@”, “+”, “-”, “_”, and “.”), you must encode them for use in the URL.
        | Special character | Encoding |
        |-------------------|----------|
        | %                 | %25      |
        | @                 | %40      |
        | +                 | %2B      |
        | –                 | %2D      |
        | _                 | %5F      |
        | .                 | %2E      |
        ## Percent Encoding Example
        Or if the coupon subcode is 20%OFF, the URL to delete this coupon
        subcode would be:
        @https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>

        Args:
            coupon_id (int): The Advanced Billing id of the coupon to which
                the subcode belongs
            subcode (str): The subcode of the coupon

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/coupons/{coupon_id}/codes/{subcode}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('coupon_id')
                            .value(coupon_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('subcode')
                            .value(subcode)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('BasicAuth'))
        ).execute()
