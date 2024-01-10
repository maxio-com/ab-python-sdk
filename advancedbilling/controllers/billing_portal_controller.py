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
from advancedbilling.models.customer_response import CustomerResponse
from advancedbilling.models.portal_management_link import PortalManagementLink
from advancedbilling.models.resent_invitation import ResentInvitation
from advancedbilling.models.revoked_invitation import RevokedInvitation
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.exceptions.too_many_management_link_requests_error_exception import TooManyManagementLinkRequestsErrorException
from advancedbilling.exceptions.api_exception import APIException


class BillingPortalController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(BillingPortalController, self).__init__(config)

    def enable_billing_portal_for_customer(self,
                                           customer_id,
                                           auto_invite=None):
        """Does a POST request to /portal/customers/{customer_id}/enable.json.

        ## Billing Portal Documentation
        Full documentation on how the Billing Portal operates within the
        Chargify UI can be located
        [here](https://chargify.zendesk.com/hc/en-us/articles/4407648972443).
        This documentation is focused on how the to configure the Billing
        Portal Settings, as well as Subscriber Interaction and Merchant
        Management of the Billing Portal.
        You can use this endpoint to enable Billing Portal access for a
        Customer, with the option of sending the Customer an Invitation email
        at the same time.
        ## Billing Portal Security
        If your customer has been invited to the Billing Portal, then they
        will receive a link to manage their subscription (the “Management
        URL”) automatically at the bottom of their statements, invoices, and
        receipts. **This link changes periodically for security and is only
        valid for 65 days.**
        If you need to provide your customer their Management URL through
        other means, you can retrieve it via the API. Because the URL is
        cryptographically signed with a timestamp, it is not possible for
        merchants to generate the URL without requesting it from Chargify.
        In order to prevent abuse & overuse, we ask that you request a new URL
        only when absolutely necessary. Management URLs are good for 65 days,
        so you should re-use a previously generated one as much as possible.
        If you use the URL frequently (such as to display on your website),
        please **do not** make an API request to Chargify every time.

        Args:
            customer_id (int): The Chargify id of the customer
            auto_invite (AutoInvite, optional): When set to 1, an Invitation
                email will be sent to the Customer. When set to 0, or not
                sent, an email will not be sent. Use in query:
                `auto_invite=1`.

        Returns:
            CustomerResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/portal/customers/{customer_id}/enable.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('auto_invite')
                         .value(auto_invite))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CustomerResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()

    def read_billing_portal_link(self,
                                 customer_id):
        """Does a GET request to /portal/customers/{customer_id}/management_link.json.

        This method will provide to the API user the exact URL required for a
        subscriber to access the Billing Portal.
        ## Rules for Management Link API
        + When retrieving a management URL, multiple requests for the same
        customer in a short period will return the **same** URL
        + We will not generate a new URL for 15 days
        + You must cache and remember this URL if you are going to need it
        again within 15 days
        + Only request a new URL after the `new_link_available_at` date
        + You are limited to 15 requests for the same URL. If you make more
        than 15 requests before `new_link_available_at`, you will be blocked
        from further Management URL requests (with a response code `429`)

        Args:
            customer_id (int): The Chargify id of the customer

        Returns:
            PortalManagementLink: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/portal/customers/{customer_id}/management_link.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PortalManagementLink.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
            .local_error('429', 'Too Many Requests', TooManyManagementLinkRequestsErrorException)
        ).execute()

    def resend_billing_portal_invitation(self,
                                         customer_id):
        """Does a POST request to /portal/customers/{customer_id}/invitations/invite.json.

        You can resend a customer's Billing Portal invitation.
        If you attempt to resend an invitation 5 times within 30 minutes, you
        will receive a `422` response with `error` message in the body.
        If you attempt to resend an invitation when the Billing Portal is
        already disabled for a Customer, you will receive a `422` error
        response.
        If you attempt to resend an invitation when the Billing Portal is
        already disabled for a Customer, you will receive a `422` error
        response.
        If you attempt to resend an invitation when the Customer does not
        exist a Customer, you will receive a `404` error response.
        ## Limitations
        This endpoint will only return a JSON response.

        Args:
            customer_id (int): The Chargify id of the customer

        Returns:
            ResentInvitation: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/portal/customers/{customer_id}/invitations/invite.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ResentInvitation.from_dictionary)
            .local_error('404', 'Not Found', APIException)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()

    def revoke_billing_portal_access(self,
                                     customer_id):
        """Does a DELETE request to /portal/customers/{customer_id}/invitations/revoke.json.

        You can revoke a customer's Billing Portal invitation.
        If you attempt to revoke an invitation when the Billing Portal is
        already disabled for a Customer, you will receive a 422 error
        response.
        ## Limitations
        This endpoint will only return a JSON response.

        Args:
            customer_id (int): The Chargify id of the customer

        Returns:
            RevokedInvitation: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/portal/customers/{customer_id}/invitations/revoke.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RevokedInvitation.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', APIException)
        ).execute()
