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
from advancedbilling.models.reactivate_subscription_group_response import ReactivateSubscriptionGroupResponse
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException


class SubscriptionGroupStatusController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(SubscriptionGroupStatusController, self).__init__(config)

    def cancel_subscriptions_in_group(self,
                                      uid,
                                      body=None):
        """Does a POST request to /subscription_groups/{uid}/cancel.json.

        This endpoint will immediately cancel all subscriptions within the
        specified group. The group is identified by it's `uid` passed in the
        URL. To successfully cancel the group, the primary subscription must
        be on automatic billing. The group members as well must be on
        automatic billing or they must be prepaid.
        In order to cancel a subscription group while also charging for any
        unbilled usage on metered or prepaid components, the
        `charge_unbilled_usage=true` parameter must be included in the
        request.

        Args:
            uid (str): The uid of the subscription group
            body (CancelGroupedSubscriptionsRequest, optional): TODO: type
                description here.

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
            .path('/subscription_groups/{uid}/cancel.json')
            .http_method(HttpMethodEnum.POST)
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
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).execute()

    def initiate_delayed_cancellation_for_group(self,
                                                uid):
        """Does a POST request to /subscription_groups/{uid}/delayed_cancel.json.

        This endpoint will schedule all subscriptions within the specified
        group to be canceled at the end of their billing period. The group is
        identified by it's uid passed in the URL.
        All subscriptions in the group must be on automatic billing in order
        to successfully cancel them, and the group must not be in a "past_due"
        state.

        Args:
            uid (str): The uid of the subscription group

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
            .path('/subscription_groups/{uid}/delayed_cancel.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('global'))
        ).execute()

    def cancel_delayed_cancellation_for_group(self,
                                              uid):
        """Does a DELETE request to /subscription_groups/{uid}/delayed_cancel.json.

        Removing the delayed cancellation on a subscription group will ensure
        that the subscriptions do not get canceled at the end of the period.
        The request will reset the `cancel_at_end_of_period` flag to false on
        each member in the group.

        Args:
            uid (str): The uid of the subscription group

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
            .path('/subscription_groups/{uid}/delayed_cancel.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('global'))
        ).execute()

    def reactivate_subscription_group(self,
                                      uid,
                                      body=None):
        """Does a POST request to /subscription_groups/{uid}/reactivate.json.

        This endpoint will attempt to reactivate or resume a cancelled
        subscription group. Upon reactivation, any canceled invoices created
        after the beginning of the primary subscription's billing period will
        be reopened and payment will be attempted on them. If the subscription
        group is being reactivated (as opposed to resumed), new charges will
        also be assessed for the new billing period.
        Whether a subscription group is reactivated (a new billing period is
        created) or resumed (the current billing period is respected) will
        depend on the parameters that are sent with the request as well as the
        date of the request relative to the primary subscription's period.
        ## Reactivating within the current period
        If a subscription group is cancelled and reactivated within the
        primary subscription's current period, we can choose to either start a
        new billing period or maintain the existing one. If we want to
        maintain the existing billing period the `resume=true` option must be
        passed in request parameters.
        An exception to the above are subscriptions that are on calendar
        billing. These subscriptions cannot be reactivated within the current
        period. If the `resume=true` option is not passed the request will
        return an error.
        The `resume_members` option is ignored in this case. All eligible
        group members will be automatically resumed.
        ## Reactivating beyond the current period
        In this case, a subscription group can only be reactivated with a new
        billing period. If the `resume=true` option is passed it will be
        ignored.
        Member subscriptions can have billing periods that are longer than the
        primary (e.g. a monthly primary with annual group members). If the
        primary subscription in a group cannot be reactivated within the
        current period, but other group members can be, passing
        `resume_members=true` will resume the existing billing period for
        eligible group members. The primary subscription will begin a new
        billing period.
        For calendar billing subscriptions, the new billing period created
        will be a partial one, spanning from the date of reactivation to the
        next corresponding calendar renewal date.

        Args:
            uid (str): The uid of the subscription group
            body (ReactivateSubscriptionGroupRequest, optional): TODO: type
                description here.

        Returns:
            ReactivateSubscriptionGroupResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscription_groups/{uid}/reactivate.json')
            .http_method(HttpMethodEnum.POST)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ReactivateSubscriptionGroupResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()
