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
from advancedbilling.models.offer_response import OfferResponse
from advancedbilling.models.list_offers_response import ListOffersResponse
from advancedbilling.exceptions.error_array_map_response_exception import ErrorArrayMapResponseException


class OffersController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(OffersController, self).__init__(config)

    def create_offer(self,
                     body=None):
        """Does a POST request to /offers.json.

        Create an offer within your Advanced Billing site by sending a POST
        request.
        ## Documentation
        Offers allow you to package complicated combinations of products,
        components and coupons into a convenient package which can then be
        subscribed to just like products.
        Once an offer is defined it can be used as an alternative to the
        product when creating subscriptions.
        Full documentation on how to use offers in the Advanced Billing UI can
        be located
        [here](https://maxio.zendesk.com/hc/en-us/articles/24261295098637-Offer
        s-Overview).
        ## Using a Product Price Point
        You can optionally pass in a `product_price_point_id` that corresponds
        with the `product_id` and the offer will use that price point. If a
        `product_price_point_id` is not passed in, the product's default price
        point will be used.

        Args:
            body (CreateOfferRequest, optional): TODO: type description here.

        Returns:
            OfferResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/offers.json')
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
            .deserialize_into(OfferResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorArrayMapResponseException)
        ).execute()

    def list_offers(self,
                    options=dict()):
        """Does a GET request to /offers.json.

        This endpoint will list offers for a site.

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
                    include_archived -- bool -- Include archived products. Use
                        in query: `include_archived=true`.

        Returns:
            ListOffersResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/offers.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('include_archived')
                         .value(options.get('include_archived', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListOffersResponse.from_dictionary)
        ).execute()

    def read_offer(self,
                   offer_id):
        """Does a GET request to /offers/{offer_id}.json.

        This method allows you to list a specific offer's attributes. This is
        different than list all offers for a site, as it requires an
        `offer_id`.

        Args:
            offer_id (int): The Chargify id of the offer

        Returns:
            OfferResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/offers/{offer_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('offer_id')
                            .value(offer_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(OfferResponse.from_dictionary)
        ).execute()

    def archive_offer(self,
                      offer_id):
        """Does a PUT request to /offers/{offer_id}/archive.json.

        Archive an existing offer. Please provide an `offer_id` in order to
        archive the correct item.

        Args:
            offer_id (int): The Chargify id of the offer

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/offers/{offer_id}/archive.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('offer_id')
                            .value(offer_id)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('BasicAuth'))
        ).execute()

    def unarchive_offer(self,
                        offer_id):
        """Does a PUT request to /offers/{offer_id}/unarchive.json.

        Unarchive a previously archived offer. Please provide an `offer_id` in
        order to un-archive the correct item.

        Args:
            offer_id (int): The Chargify id of the offer

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/offers/{offer_id}/unarchive.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('offer_id')
                            .value(offer_id)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('BasicAuth'))
        ).execute()
