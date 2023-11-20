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
from advancedbilling.models.subscription_group_signup_response import SubscriptionGroupSignupResponse
from advancedbilling.models.subscription_group_response import SubscriptionGroupResponse
from advancedbilling.models.list_subscription_groups_response import ListSubscriptionGroupsResponse
from advancedbilling.models.full_subscription_group_response import FullSubscriptionGroupResponse
from advancedbilling.models.delete_subscription_group_response import DeleteSubscriptionGroupResponse
from advancedbilling.exceptions.subscription_group_signup_error_response_exception import SubscriptionGroupSignupErrorResponseException
from advancedbilling.exceptions.single_string_error_response_exception import SingleStringErrorResponseException
from advancedbilling.exceptions.subscription_group_update_error_response_exception import SubscriptionGroupUpdateErrorResponseException
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException


class SubscriptionGroupsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(SubscriptionGroupsController, self).__init__(config)

    def signup_with_subscription_group(self,
                                       body=None):
        """Does a POST request to /subscription_groups/signup.json.

        Create multiple subscriptions at once under the same customer and
        consolidate them into a subscription group.
        You must provide one and only one of the
        `payer_id`/`payer_reference`/`payer_attributes` for the customer
        attached to the group.
        You must provide one and only one of the
        `payment_profile_id`/`credit_card_attributes`/`bank_account_attributes`
        for the payment profile attached to the group.
        Only one of the `subscriptions` can have `"primary": true` attribute
        set.
        When passing product to a subscription you can use either `product_id`
        or `product_handle` or `offer_id`. You can also use `custom_price`
        instead.

        Args:
            body (SubscriptionGroupSignupRequest, optional): TODO: type
                description here.

        Returns:
            SubscriptionGroupSignupResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscription_groups/signup.json')
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionGroupSignupResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', SubscriptionGroupSignupErrorResponseException)
        ).execute()

    def create_subscription_group(self,
                                  body=None):
        """Does a POST request to /subscription_groups.json.

        Creates a subscription group with given members.

        Args:
            body (CreateSubscriptionGroupRequest, optional): TODO: type
                description here.

        Returns:
            SubscriptionGroupResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscription_groups.json')
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionGroupResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', SingleStringErrorResponseException)
        ).execute()

    def list_subscription_groups(self,
                                 options=dict()):
        """Does a GET request to /subscription_groups.json.

        Returns an array of subscription groups for the site. The response is
        paginated and will return a `meta` key with pagination information.
        #### Account Balance Information
        Account balance information for the subscription groups is not
        returned by default. If this information is desired, the
        `include[]=account_balances` parameter must be provided with the
        request.

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
                    include -- str -- A list of additional information to
                        include in the response. The following values are
                        supported:  - `account_balances`: Account balance
                        information for the subscription groups. Use in query:
                        `include[]=account_balances`

        Returns:
            ListSubscriptionGroupsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscription_groups.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('include')
                         .value(options.get('include', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListSubscriptionGroupsResponse.from_dictionary)
        ).execute()

    def read_subscription_group(self,
                                uid):
        """Does a GET request to /subscription_groups/{uid}.json.

        Use this endpoint to find subscription group details.
        #### Current Billing Amount in Cents
        Current billing amount for the subscription group is not returned by
        default. If this information is desired, the
        `include[]=current_billing_amount_in_cents` parameter must be provided
        with the request.

        Args:
            uid (str): The uid of the subscription group

        Returns:
            FullSubscriptionGroupResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscription_groups/{uid}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FullSubscriptionGroupResponse.from_dictionary)
        ).execute()

    def update_subscription_group_members(self,
                                          uid,
                                          body=None):
        """Does a PUT request to /subscription_groups/{uid}.json.

        Use this endpoint to update subscription group members.
        `"member_ids": []` should contain an array of both subscription IDs to
        set as group members and subscription IDs already present in the
        groups. Not including them will result in removing them from
        subscription group. To clean up members, just leave the array empty.

        Args:
            uid (str): The uid of the subscription group
            body (UpdateSubscriptionGroupRequest, optional): TODO: type
                description here.

        Returns:
            SubscriptionGroupResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscription_groups/{uid}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
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
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionGroupResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', SubscriptionGroupUpdateErrorResponseException)
        ).execute()

    def delete_subscription_group(self,
                                  uid):
        """Does a DELETE request to /subscription_groups/{uid}.json.

        Use this endpoint to delete subscription group.
        Only groups without members can be deleted

        Args:
            uid (str): The uid of the subscription group

        Returns:
            DeleteSubscriptionGroupResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscription_groups/{uid}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeleteSubscriptionGroupResponse.from_dictionary)
            .local_error('404', 'Not Found', APIException)
        ).execute()

    def read_subscription_group_by_subscription_id(self,
                                                   subscription_id):
        """Does a GET request to /subscription_groups/lookup.json.

        Use this endpoint to find subscription group associated with
        subscription.
        If the subscription is not in a group endpoint will return 404 code.

        Args:
            subscription_id (str): The Chargify id of the subscription
                associated with the subscription group

        Returns:
            FullSubscriptionGroupResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscription_groups/lookup.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('subscription_id')
                         .value(subscription_id)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FullSubscriptionGroupResponse.from_dictionary)
            .local_error('404', 'Not Found', APIException)
        ).execute()

    def create_subscription_group_hierarchy(self,
                                            subscription_id,
                                            body=None):
        """Does a POST request to /subscriptions/{subscription_id}/group.json.

        For sites making use of the [Relationship
        Billing](https://chargify.zendesk.com/hc/en-us/articles/4407737494171)
        and [Customer
        Hierarchy](https://chargify.zendesk.com/hc/en-us/articles/4407746683291
        ) features, it is possible to add existing subscriptions to
        subscription groups.
        Passing `group` parameters with a `target` containing a `type` and
        optional `id` is all that's needed. When the `target` parameter
        specifies a `"customer"` or `"subscription"` that is already part of a
        hierarchy, the subscription will become a member of the customer's
        subscription group.  If the target customer or subscription is not
        part of a subscription group, a new group will be created and the
        subscription will become part of the group with the specified target
        customer set as the responsible payer for the group's subscriptions.
        **Please Note:** In order to add an existing subscription to a
        subscription group, it must belong to either the same customer record
        as the target, or be within the same customer hierarchy.
        Rather than specifying a customer, the `target` parameter could
        instead simply have a value of
        * `"self"` which indicates the subscription will be paid for not by
        some other customer, but by the subscribing customer,
        * `"parent"` which indicates the subscription will be paid for by the
        subscribing customer's parent within a customer hierarchy, or
        * `"eldest"` which indicates the subscription will be paid for by the
        root-level customer in the subscribing customer's hierarchy.
        To create a new subscription into a subscription group, please
        reference the following:
        [Create Subscription in a Subscription
        Group](https://developers.chargify.com/docs/api-docs/d571659cf0f24-crea
        te-subscription#subscription-in-a-subscription-group)

        Args:
            subscription_id (str): The Chargify id of the subscription
            body (AddSubscriptionToAGroup, optional): TODO: type description
                here.

        Returns:
            SubscriptionGroupResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/group.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
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
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionGroupResponse.from_dictionary)
        ).execute()

    def remove_subscription_from_group(self,
                                       subscription_id):
        """Does a DELETE request to /subscriptions/{subscription_id}/group.json.

        For sites making use of the [Relationship
        Billing](https://chargify.zendesk.com/hc/en-us/articles/4407737494171)
        and [Customer
        Hierarchy](https://chargify.zendesk.com/hc/en-us/articles/4407746683291
        ) features, it is possible to remove existing subscription from
        subscription group.

        Args:
            subscription_id (str): The Chargify id of the subscription

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/group.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .local_error('404', 'Not Found', APIException)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()
