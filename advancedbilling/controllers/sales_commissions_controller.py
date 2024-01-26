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
from advancedbilling.models.list_sale_rep_item import ListSaleRepItem
from advancedbilling.models.sale_rep_settings import SaleRepSettings
from advancedbilling.models.sale_rep import SaleRep


class SalesCommissionsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(SalesCommissionsController, self).__init__(config)

    def list_sales_reps(self,
                        options=dict()):
        """Does a GET request to /sellers/{seller_id}/sales_reps.json.

        Endpoint returns sales rep list with details
        ## Modified Authentication Process
        The Sales Commission API differs from other Chargify API endpoints.
        This resource is associated with the seller itself. Up to now all
        available resources were at the level of the site, therefore creating
        the API Key per site was a sufficient solution. To share resources at
        the seller level, a new authentication method was introduced, which is
        user authentication. Creating an API Key for a user is a required step
        to correctly use the Sales Commission API, more details
        [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5
        NTg0-2020-04-20-new-api-authentication).
        Access to the Sales Commission API endpoints is available to users
        with financial access, where the seller has the Advanced Analytics
        component enabled. For further information on getting access to
        Advanced Analytics please contact Chargify support.
        > Note: The request is at seller level, it means `<<subdomain>>`
        variable will be replaced by `app`

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    seller_id -- str -- The Chargify id of your seller
                        account
                    authorization -- str -- For authorization use user API
                        key. See details
                        [here](https://developers.chargify.com/docs/developer-d
                        ocs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication)
                        .
                    live_mode -- bool -- This parameter indicates if records
                        should be fetched from live mode sites. Default value
                        is true.
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
                        records to fetch in each request. Default value is
                        100.

        Returns:
            List[ListSaleRepItem]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/sellers/{seller_id}/sales_reps.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('seller_id')
                            .value(options.get('seller_id', None))
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(options.get('authorization', None)))
            .query_param(Parameter()
                         .key('live_mode')
                         .value(options.get('live_mode', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListSaleRepItem.from_dictionary)
        ).execute()

    def list_sales_commission_settings(self,
                                       options=dict()):
        """Does a GET request to /sellers/{seller_id}/sales_commission_settings.json.

        Endpoint returns subscriptions with associated sales reps
        ## Modified Authentication Process
        The Sales Commission API differs from other Chargify API endpoints.
        This resource is associated with the seller itself. Up to now all
        available resources were at the level of the site, therefore creating
        the API Key per site was a sufficient solution. To share resources at
        the seller level, a new authentication method was introduced, which is
        user authentication. Creating an API Key for a user is a required step
        to correctly use the Sales Commission API, more details
        [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5
        NTg0-2020-04-20-new-api-authentication).
        Access to the Sales Commission API endpoints is available to users
        with financial access, where the seller has the Advanced Analytics
        component enabled. For further information on getting access to
        Advanced Analytics please contact Chargify support.
        > Note: The request is at seller level, it means `<<subdomain>>`
        variable will be replaced by `app`

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    seller_id -- str -- The Chargify id of your seller
                        account
                    authorization -- str -- For authorization use user API
                        key. See details
                        [here](https://developers.chargify.com/docs/developer-d
                        ocs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication)
                        .
                    live_mode -- bool -- This parameter indicates if records
                        should be fetched from live mode sites. Default value
                        is true.
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
                        records to fetch in each request. Default value is
                        100.

        Returns:
            List[SaleRepSettings]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/sellers/{seller_id}/sales_commission_settings.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('seller_id')
                            .value(options.get('seller_id', None))
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(options.get('authorization', None)))
            .query_param(Parameter()
                         .key('live_mode')
                         .value(options.get('live_mode', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SaleRepSettings.from_dictionary)
        ).execute()

    def read_sales_rep(self,
                       seller_id,
                       sales_rep_id,
                       authorization='Bearer <<apiKey>>',
                       live_mode=None,
                       page=1,
                       per_page=100):
        """Does a GET request to /sellers/{seller_id}/sales_reps/{sales_rep_id}.json.

        Endpoint returns sales rep and attached subscriptions details.
        ## Modified Authentication Process
        The Sales Commission API differs from other Chargify API endpoints.
        This resource is associated with the seller itself. Up to now all
        available resources were at the level of the site, therefore creating
        the API Key per site was a sufficient solution. To share resources at
        the seller level, a new authentication method was introduced, which is
        user authentication. Creating an API Key for a user is a required step
        to correctly use the Sales Commission API, more details
        [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5
        NTg0-2020-04-20-new-api-authentication).
        Access to the Sales Commission API endpoints is available to users
        with financial access, where the seller has the Advanced Analytics
        component enabled. For further information on getting access to
        Advanced Analytics please contact Chargify support.
        > Note: The request is at seller level, it means `<<subdomain>>`
        variable will be replaced by `app`

        Args:
            seller_id (str): The Chargify id of your seller account
            sales_rep_id (str): The Chargify id of sales rep.
            authorization (str, optional): For authorization use user API key.
                See details
                [here](https://developers.chargify.com/docs/developer-docs/ZG9j
                OjMyNzk5NTg0-2020-04-20-new-api-authentication).
            live_mode (bool, optional): This parameter indicates if records
                should be fetched from live mode sites. Default value is
                true.
            page (int, optional): Result records are organized in pages. By
                default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can
                start navigating through the pages to consume the results. You
                do this by passing in a page parameter. Retrieve the next page
                by adding ?page=2 to the query string. If there are no results
                to return, then an empty result set will be returned. Use in
                query `page=1`.
            per_page (int, optional): This parameter indicates how many
                records to fetch in each request. Default value is 100.

        Returns:
            SaleRep: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/sellers/{seller_id}/sales_reps/{sales_rep_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('seller_id')
                            .value(seller_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('sales_rep_id')
                            .value(sales_rep_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(authorization))
            .query_param(Parameter()
                         .key('live_mode')
                         .value(live_mode))
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .query_param(Parameter()
                         .key('per_page')
                         .value(per_page))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SaleRep.from_dictionary)
        ).execute()
