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
from advancedbilling.models.site_response import SiteResponse
from advancedbilling.models.list_public_keys_response import ListPublicKeysResponse
from advancedbilling.exceptions.api_exception import APIException


class SitesController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(SitesController, self).__init__(config)

    def read_site(self):
        """Does a GET request to /site.json.

        This endpoint allows you to fetch some site data.
        Full documentation on Sites in the Chargify UI can be located
        [here](https://chargify.zendesk.com/hc/en-us/articles/4407870738587).
        Specifically, the [Clearing Site
        Data](https://maxio-chargify.zendesk.com/hc/en-us/articles/540542832730
        9) section is extremely relevant to this endpoint documentation.
        #### Relationship invoicing enabled
        If site has RI enabled then you will see more settings like:
            "customer_hierarchy_enabled": true,
            "whopays_enabled": true,
            "whopays_default_payer": "self"
        You can read more about these settings here:
         [Who Pays & Customer
         Hierarchy](https://chargify.zendesk.com/hc/en-us/articles/440774668329
         1)

        Returns:
            SiteResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/site.json')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SiteResponse.from_dictionary)
        ).execute()

    def clear_site(self,
                   cleanup_scope='all'):
        """Does a POST request to /sites/clear_data.json.

        This call is asynchronous and there may be a delay before the site
        data is fully deleted. If you are clearing site data for an automated
        test, you will need to build in a delay and/or check that there are no
        products, etc., in the site before proceeding.
        **This functionality will only work on sites in TEST mode. Attempts to
        perform this on sites in “live” mode will result in a response of 403
        FORBIDDEN.**

        Args:
            cleanup_scope (CleanupScope, optional): `all`: Will clear all
                products, customers, and related subscriptions from the site. 
                `customers`: Will clear only customers and related
                subscriptions (leaving the products untouched) for the site. 
                Revenue will also be reset to 0. Use in query
                `cleanup_scope=all`.

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
            .path('/sites/clear_data.json')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('cleanup_scope')
                         .value(cleanup_scope))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .local_error('403', 'Forbidden', APIException)
        ).execute()

    def list_chargify_js_public_keys(self,
                                     options=dict()):
        """Does a GET request to /chargify_js_keys.json.

        This endpoint returns public keys used for Chargify.js.

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

        Returns:
            ListPublicKeysResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/chargify_js_keys.json')
            .http_method(HttpMethodEnum.GET)
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
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListPublicKeysResponse.from_dictionary)
        ).execute()
