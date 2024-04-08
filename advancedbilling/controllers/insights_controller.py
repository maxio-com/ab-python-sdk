# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from deprecation import deprecated
from advancedbilling.api_helper import APIHelper
from advancedbilling.configuration import Server
from advancedbilling.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from advancedbilling.http.http_method_enum import HttpMethodEnum
from apimatic_core.types.array_serialization_format import SerializationFormats
from apimatic_core.authentication.multiple.single_auth import Single
from advancedbilling.models.site_summary import SiteSummary
from advancedbilling.models.mrr_response import MRRResponse
from advancedbilling.models.list_mrr_response import ListMRRResponse
from advancedbilling.models.subscription_mrr_response import SubscriptionMRRResponse
from advancedbilling.exceptions.subscriptions_mrr_error_response_exception import SubscriptionsMrrErrorResponseException


class InsightsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(InsightsController, self).__init__(config)

    def read_site_stats(self):
        """Does a GET request to /stats.json.

        The Stats API is a very basic view of some Site-level stats. This API
        call only answers with JSON responses. An XML version is not
        provided.
        ## Stats Documentation
        There currently is not a complimentary matching set of documentation
        that compliments this endpoint. However, each Site's dashboard will
        reflect the summary of information provided in the Stats reposnse.
        ```
        https://subdomain.chargify.com/dashboard
        ```

        Returns:
            SiteSummary: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/stats.json')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SiteSummary.from_dictionary)
        ).execute()

    @deprecated()
    def read_mrr(self,
                 at_time=None,
                 subscription_id=None):
        """Does a GET request to /mrr.json.

        This endpoint returns your site's current MRR, including plan and
        usage breakouts.

        Args:
            at_time (datetime, optional): submit a timestamp in ISO8601 format
                to request MRR for a historic time
            subscription_id (int, optional): submit the id of a subscription
                in order to limit results

        Returns:
            MRRResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/mrr.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('at_time')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, at_time)))
            .query_param(Parameter()
                         .key('subscription_id')
                         .value(subscription_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(MRRResponse.from_dictionary)
        ).execute()

    @deprecated()
    def list_mrr_movements(self,
                           options=dict()):
        """Does a GET request to /mrr_movements.json.

        This endpoint returns your site's MRR movements.
        ## Understanding MRR movements
        This endpoint will aid in accessing your site's [MRR
        Report](https://chargify.zendesk.com/hc/en-us/articles/4407838249627)
        data.
        Whenever a subscription event occurs that causes your site's MRR to
        change (such as a signup or upgrade), we record an MRR movement. These
        records are accessible via the MRR Movements endpoint.
        Each MRR Movement belongs to a subscription and contains a timestamp,
        category, and an amount. `line_items` represent the subscription's
        product configuration at the time of the movement.
        ### Plan & Usage Breakouts
        In the MRR Report UI, we support a setting to [include or
        exclude](https://chargify.zendesk.com/hc/en-us/articles/4407838249627#d
        isplaying-component-based-metered-usage-in-mrr) usage revenue. In the
        MRR APIs, responses include `plan` and `usage` breakouts.
        Plan includes revenue from:
        * Products
        * Quantity-Based Components
        * On/Off Components
        Usage includes revenue from:
        * Metered Components
        * Prepaid Usage Components

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    subscription_id -- int -- optionally filter results by
                        subscription
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
                        The maximum allowed values is 50; any per_page value
                        over 50 will be changed to 50. Use in query
                        `per_page=20`.
                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.

        Returns:
            ListMRRResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/mrr_movements.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('subscription_id')
                         .value(options.get('subscription_id', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListMRRResponse.from_dictionary)
        ).execute()

    @deprecated()
    def list_mrr_per_subscription(self,
                                  options=dict()):
        """Does a GET request to /subscriptions_mrr.json.

        This endpoint returns your site's current MRR, including plan and
        usage breakouts split per subscription.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    filter -- ListMrrFilter -- Filter to use for List MRR per
                        subscription operation
                    at_time -- str -- Submit a timestamp in ISO8601 format to
                        request MRR for a historic time. Use in query:
                        `at_time=2022-01-10T10:00:00-05:00`.
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
                    direction -- Direction -- Controls the order in which
                        results are returned. Records are ordered by
                        subscription_id in ascending order by default. Use in
                        query `direction=desc`.

        Returns:
            SubscriptionMRRResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions_mrr.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('filter')
                         .value(options.get('filter', None)))
            .query_param(Parameter()
                         .key('at_time')
                         .value(options.get('at_time', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionMRRResponse.from_dictionary)
            .local_error_template('400', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SubscriptionsMrrErrorResponseException)
        ).execute()
