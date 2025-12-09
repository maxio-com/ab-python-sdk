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
from advancedbilling.models.subscription_response import SubscriptionResponse
from advancedbilling.models.prepaid_configuration_response import PrepaidConfigurationResponse
from advancedbilling.models.subscription_preview_response import SubscriptionPreviewResponse
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.exceptions.single_error_response_exception import SingleErrorResponseException
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.subscription_response_error_exception import SubscriptionResponseErrorException
from advancedbilling.exceptions.subscription_add_coupon_error_exception import SubscriptionAddCouponErrorException
from advancedbilling.exceptions.subscription_remove_coupon_errors_exception import SubscriptionRemoveCouponErrorsException
from advancedbilling.exceptions.error_array_map_response_exception import ErrorArrayMapResponseException


class SubscriptionsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(SubscriptionsController, self).__init__(config)

    def create_subscription(self,
                            body=None):
        """Does a POST request to /subscriptions.json.

        Creates a Subscription for a customer and product
        Specify the product with `product_id` or `product_handle`. To set a
        specific product pricepPoint, use `product_price_point_handle` or
        `product_price_point_id`.
        Identify an existing customer with `customer_id` or
        `customer_reference`. Optionally, include an existing payment profile
        using `payment_profile_id`. To create a new customer, pass
        customer_attributes. 
        Select an option from the **Request Examples** drop-down on the right
        side of the portal to see examples of common scenarios for creating
        subscriptions. 
        Payment information may be required to create a subscription,
        depending on the options for the Product being subscribed. See
        [product
        options](https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-P
        roducts) for more information. See the [Payments
        Profile]($e/Payment%20Profiles/createPaymentProfile) endpoint for
        details on payment parameters.
        Do not use real card information for testing. See the Sites articles
        that cover [testing your site
        setup](https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-
        Overview#testing-overview-0-0) for more details on testing in your
        sandbox.
        Note that collecting and sending raw card details in production
        requires [PCI
        compliance](https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI
        -Compliance#pci-compliance-0-0) on your end. If your business is not
        PCI compliant, use
        [Chargify.js](https://docs.maxio.com/hc/en-us/articles/38163190843789-C
        hargify-js-Overview#chargify-js-overview-0-0) to collect credit card
        or bank account information.
        See the [Subscription
        Signups](page:introduction/basic-concepts/subscription-signup) article
        for more information on working with subscriptions in Advanced Billing.

        Args:
            body (CreateSubscriptionRequest, optional): The request body
                parameter.

        Returns:
            SubscriptionResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions.json')
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
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def list_subscriptions(self,
                           options=dict()):
        """Does a GET request to /subscriptions.json.

        This method will return an array of subscriptions from a Site. Pay
        close attention to query string filters and pagination in order to
        control responses from the server.
        ## Search for a subscription
        Use the query strings below to search for a subscription using the
        criteria available. The return value will be an array.
        ## Self-Service Page token
        Self-Service Page token for the subscriptions is not returned by
        default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the
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
                    state -- SubscriptionStateFilter -- The current state of
                        the subscription
                    product -- int -- The product id of the subscription.
                        (Note that the product handle cannot be used.)
                    product_price_point_id -- int -- The ID of the product
                        price point. If supplied, product is required
                    coupon -- int -- The numeric id of the coupon currently
                        applied to the subscription. (This can be found in the
                        URL when editing a coupon. Note that the coupon code
                        cannot be used.)
                    coupon_code -- str -- The coupon code currently applied to
                        the subscription
                    date_field -- SubscriptionDateField -- The type of filter
                        you'd like to apply to your search.  Allowed Values: ,
                        current_period_ends_at, current_period_starts_at,
                        created_at, activated_at, canceled_at, expires_at,
                        trial_started_at, trial_ended_at, updated_at
                    start_date -- date -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns
                        subscriptions with a timestamp at or after midnight
                        (12:00:00 AM) in your site’s time zone on the date
                        specified. Use in query `start_date=2022-07-01`.
                    end_date -- date -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns subscriptions
                        with a timestamp up to and including 11:59:59PM in
                        your site’s time zone on the date specified. Use in
                        query `end_date=2022-08-01`.
                    start_datetime -- datetime -- The start date and time
                        (format YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns subscriptions with a timestamp at
                        or after exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date. Use in query
                        `start_datetime=2022-07-01 09:00:05`.
                    end_datetime -- datetime -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns subscriptions with a timestamp at
                        or before exact time provided in query. You can
                        specify timezone in query - otherwise your site's time
                        zone will be used. If provided, this parameter will be
                        used instead of end_date. Use in query
                        `end_datetime=2022-08-01 10:00:05`.
                    metadata -- Dict[str, str] -- The value of the metadata
                        field specified in the parameter. Use in query
                        `metadata[my-field]=value&metadata[other-field]=another
                        _value`.
                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.
                    sort -- SubscriptionSort -- The attribute by which to sort
                    include -- List[SubscriptionListInclude] -- Allows
                        including additional data in the response. Use in
                        query: `include[]=self_service_page_token`.

        Returns:
            List[SubscriptionResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('state')
                         .value(options.get('state', None)))
            .query_param(Parameter()
                         .key('product')
                         .value(options.get('product', None)))
            .query_param(Parameter()
                         .key('product_price_point_id')
                         .value(options.get('product_price_point_id', None)))
            .query_param(Parameter()
                         .key('coupon')
                         .value(options.get('coupon', None)))
            .query_param(Parameter()
                         .key('coupon_code')
                         .value(options.get('coupon_code', None)))
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
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('start_datetime', None))))
            .query_param(Parameter()
                         .key('end_datetime')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('end_datetime', None))))
            .query_param(Parameter()
                         .key('metadata')
                         .value(options.get('metadata', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .query_param(Parameter()
                         .key('sort')
                         .value(options.get('sort', None)))
            .query_param(Parameter()
                         .key('include')
                         .value(options.get('include', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
        ).execute()

    def update_subscription(self,
                            subscription_id,
                            body=None):
        """Does a PUT request to /subscriptions/{subscription_id}.json.

        Updates one or more attributes of a subscription.
        ## Update Subscription Payment Method
        Change the card that your subscriber uses for their subscription. You
        can also use this method to change the expiration date of the card
        **if your gateway allows**.
        Do not use real card information for testing. See the Sites articles
        that cover [testing your site
        setup](https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-
        Overview#testing-overview-0-0) for more details on testing in your
        sandbox.
        Note that collecting and sending raw card details in production
        requires [PCI
        compliance](https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI
        -Compliance#pci-compliance-0-0) on your end. If your business is not
        PCI compliant, use
        [Chargify.js](https://docs.maxio.com/hc/en-us/articles/38163190843789-C
        hargify-js-Overview#chargify-js-overview-0-0) to collect credit card
        or bank account information.
        > Note: Partial card updates for **Authorize.Net** are not allowed via
        this endpoint. The existing Payment Profile must be directly updated
        instead.
        ## Update Product
        You also use this method to change the subscription to a different
        product by setting a new value for product_handle. A product change
        can be done in two different ways, **product change** or **delayed
        product change**.
        ### Product Change
        You can change a subscription's product. The new payment amount is
        calculated and charged at the normal start of the next period. If you
        require complex product changes or prorated upgrades and downgrades
        instead, please see the documentation on [Migrating Subscription
        Products](https://docs.maxio.com/hc/en-us/articles/24252069837581-Produ
        ct-Changes-and-Migrations#product-changes-and-migrations-0-0).
        To perform a product change, set either the `product_handle` or
        `product_id` attribute to that of a different product from the same
        site as the subscription. You can also change the price point by
        passing in either `product_price_point_id` or
        `product_price_point_handle` - otherwise the new product's default
        price point is used.
        ### Delayed Product Change
        This method also changes the product and/or price point, and the new
        payment amount is calculated and charged at the normal start of the
        next period.
        This method schedules the product change to happen automatically at
        the subscription’s next renewal date. To perform a delayed product
        change, set the `product_handle` attribute as you would in a regular
        product change, but also set the `product_change_delayed` attribute to
        `true`. No proration applies in this case.
        You can also perform a delayed change to the price point by passing in
        either `product_price_point_id` or `product_price_point_handle`
        > **Note:** To cancel a delayed product change, set `next_product_id`
        to an empty string.
        ## Billing Date Changes
        You can update dates for a subscrption. 
        ### Regular Billing Date Changes
        Send the `next_billing_at` to set the next billing date for the
        subscription. After that date passes and the subscription is
        processed, the following billing date will be set according to the
        subscription's product period.
        > Note: If you pass an invalid date, the correct date is automatically
        set to he correct date. For example, if February 30 is passed, the
        next billing would be set to March 2nd in a non-leap year.
        The server response will not return data under the key/value pair of
        `next_billing_at`. View the key/value pair of `current_period_ends_at`
        to verify that the `next_billing_at` date has been changed
        successfully.
        ### Calendar Billing  and Snap Day Changes
        For a subscription using Calendar Billing, setting the next billing
        date is a bit different. Send the `snap_day` attribute to change the
        calendar billing date for **a subscription using a product eligible
        for calendar billing**.
        > Note: If you change the product associated with a subscription that
        contains a `snap_day` and immediately `READ/GET` the subscription
        data, it will still contain original `snap_day`. The `snap_day`will
        will reset to 'null on the next billing cycle. This is because  a
        product change is instantanous and only affects the product associated
        with a subscription.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (UpdateSubscriptionRequest, optional): The request body
                parameter.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}.json')
            .http_method(HttpMethodEnum.PUT)
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def read_subscription(self,
                          subscription_id,
                          include=None):
        """Does a GET request to /subscriptions/{subscription_id}.json.

        Use this endpoint to find subscription details.
        ## Self-Service Page token
        Self-Service Page token for the subscription is not returned by
        default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the
        request.

        Args:
            subscription_id (int): The Chargify id of the subscription
            include (List[SubscriptionInclude], optional): Allows including
                additional data in the response. Use in query:
                `include[]=coupons&include[]=self_service_page_token`.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('include')
                         .value(include))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
        ).execute()

    def override_subscription(self,
                              subscription_id,
                              body=None):
        """Does a PUT request to /subscriptions/{subscription_id}/override.json.

        This API endpoint allows you to set certain subscription fields that
        are usually managed for you automatically. Some of the fields can be
        set via the normal Subscriptions Update API, but others can only be
        set using this endpoint.
        This endpoint is provided for cases where you need to “align” Advanced
        Billing data with data that happened in your system, perhaps before
        you started using Advanced Billing. For example, you may choose to
        import your historical subscription data, and would like the
        activation and cancellation dates in Advanced Billing to match your
        existing historical dates. Advanced Billing does not backfill
        historical events (i.e. from the Events API), but some static data can
        be changed via this API.
        Why are some fields only settable from this endpoint, and not the
        normal subscription create and update endpoints? Because we want users
        of this endpoint to be aware that these fields are usually managed by
        Advanced Billing, and using this API means **you are stepping out on
        your own.**
        Changing these fields will not affect any other attributes. For
        example, adding an expiration date will not affect the next assessment
        date on the subscription.
        If you regularly need to override the current_period_starts_at for new
        subscriptions, this can also be accomplished by setting both
        `previous_billing_at` and `next_billing_at` at subscription creation.
        See the documentation on [Importing
        Subscriptions](./b3A6MTQxMDgzODg-create-subscription#subscriptions-impo
        rt) for more information.
        ## Limitations
        When passing `current_period_starts_at` some validations are made:
        1. The subscription needs to be unbilled (no statements or invoices).
        2. The value passed must be a valid date/time. We recommend using the
        iso 8601 format.
        3. The value passed must be before the current date/time.
        If unpermitted parameters are sent, a 400 HTTP response is sent along
        with a string giving the reason for the problem.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (OverrideSubscriptionRequest, optional): Only these fields
                are available to be set.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/override.json')
            .http_method(HttpMethodEnum.PUT)
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
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).execute()

    def find_subscription(self,
                          reference=None):
        """Does a GET request to /subscriptions/lookup.json.

        Use this endpoint to find a subscription by its reference.

        Args:
            reference (str, optional): Subscription reference

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/lookup.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('reference')
                         .value(reference))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
        ).execute()

    def purge_subscription(self,
                           subscription_id,
                           ack,
                           cascade=None):
        """Does a POST request to /subscriptions/{subscription_id}/purge.json.

        For sites in test mode, you may purge individual subscriptions.
        Provide the subscription ID in the url.  To confirm, supply the
        customer ID in the query string `ack` parameter. You may also delete
        the customer record and/or payment profiles by passing `cascade`
        parameters. For example, to delete just the customer record, the query
        params would be: `?ack={customer_id}&cascade[]=customer`
        If you need to remove subscriptions from a live site, contact support
        to discuss your use case.
        ### Delete customer and payment profile
        The query params will be:
        `?ack={customer_id}&cascade[]=customer&cascade[]=payment_profile`

        Args:
            subscription_id (int): The Chargify id of the subscription
            ack (int): id of the customer.
            cascade (List[SubscriptionPurgeType], optional): Options are
                "customer" or "payment_profile". Use in query:
                `cascade[]=customer&cascade[]=payment_profile`.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/purge.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('ack')
                         .value(ack)
                         .is_required(True))
            .query_param(Parameter()
                         .key('cascade')
                         .value(cascade))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('400', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SubscriptionResponseErrorException)
        ).execute()

    def update_prepaid_subscription_configuration(self,
                                                  subscription_id,
                                                  body=None):
        """Does a POST request to /subscriptions/{subscription_id}/prepaid_configurations.json.

        Use this endpoint to update a subscription's prepaid configuration.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (UpsertPrepaidConfigurationRequest, optional): The request
                body parameter.

        Returns:
            PrepaidConfigurationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/prepaid_configurations.json')
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PrepaidConfigurationResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', APIException)
        ).execute()

    def preview_subscription(self,
                             body=None):
        """Does a POST request to /subscriptions/preview.json.

        The Chargify API allows you to preview a subscription by POSTing the
        same JSON or XML as for a subscription creation.
        The "Next Billing" amount and "Next Billing" date are represented in
        each Subscriber's Summary.
        A subscription will not be created by utilizing this endpoint; it is
        meant to serve as a prediction.
        For more information, see our documentation
        [here](https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subsc
        riber-Interface-Overview).
        ## Taxable Subscriptions
        This endpoint will preview taxes applicable to a purchase. In order
        for taxes to be previewed, the following conditions must be met:
        + Taxes must be configured on the subscription
        + The preview must be for the purchase of a taxable product or
        component, or combination of the two.
        + The subscription payload must contain a full billing or shipping
        address in order to calculate tax
        For more information about creating taxable previews, see our
        documentation guide on how to create [taxable
        subscriptions.](https://maxio.zendesk.com/hc/en-us/sections/24287012349
        325-Taxes)
        You do **not** need to include a card number to generate tax
        information when you are previewing a subscription. However, when you
        actually want to create the subscription, you must include the credit
        card information if you want the billing address to be stored in
        Advanced Billing. The billing address and the credit card information
        are stored together within the payment profile object. Also, you may
        not send a billing address to Advanced Billing without payment profile
        information, as the address is stored on the card.
        You can pass shipping and billing addresses and still decide not to
        calculate taxes. To do that, pass `skip_billing_manifest_taxes: true`
        attribute.
        ## Non-taxable Subscriptions
        If you'd like to calculate subscriptions that do not include tax you
        may leave off the billing information.

        Args:
            body (CreateSubscriptionRequest, optional): The request body
                parameter.

        Returns:
            SubscriptionPreviewResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/preview.json')
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
            .deserialize_into(SubscriptionPreviewResponse.from_dictionary)
        ).execute()

    def apply_coupons_to_subscription(self,
                                      subscription_id,
                                      code=None,
                                      body=None):
        """Does a POST request to /subscriptions/{subscription_id}/add_coupon.json.

        An existing subscription can accommodate multiple discounts/coupon
        codes. This is only applicable if each coupon is stackable. For more
        information on stackable coupons, we recommend reviewing our [coupon
        documentation.](https://maxio.zendesk.com/hc/en-us/articles/24261259337
        101-Coupons-and-Subscriptions#stackability-rules)
        ## Query Parameters vs Request Body Parameters
        Passing in a coupon code as a query parameter will add the code to the
        subscription, completely replacing all existing coupon codes on the
        subscription.
        For this reason, using this query parameter on this endpoint has been
        deprecated in favor of using the request body parameters as described
        below. When passing in request body parameters, the list of coupon
        codes will simply be added to any existing list of codes on the
        subscription.

        Args:
            subscription_id (int): The Chargify id of the subscription
            code (str, optional): A code for the coupon that would be applied
                to a subscription
            body (AddCouponsRequest, optional): The request body parameter.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/add_coupon.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .query_param(Parameter()
                         .key('code')
                         .value(code))
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
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SubscriptionAddCouponErrorException)
        ).execute()

    def remove_coupon_from_subscription(self,
                                        subscription_id,
                                        coupon_code=None):
        """Does a DELETE request to /subscriptions/{subscription_id}/remove_coupon.json.

        Use this endpoint to remove a coupon from an existing subscription.
        For more information on the expected behaviour of removing a coupon
        from a subscription, See our documentation
        [here.](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coup
        ons-and-Subscriptions#removing-a-coupon)

        Args:
            subscription_id (int): The Chargify id of the subscription
            coupon_code (str, optional): The coupon code

        Returns:
            str: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/remove_coupon.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('coupon_code')
                         .value(coupon_code))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SubscriptionRemoveCouponErrorsException)
        ).execute()

    def activate_subscription(self,
                              subscription_id,
                              body=None):
        """Does a PUT request to /subscriptions/{subscription_id}/activate.json.

        Advanced Billing offers the ability to activate awaiting signup and
        trialing subscriptions. This feature is only available on the
        Relationship Invoicing architecture. Subscriptions in a group may not
        be activated immediately.
        For details on how the activation works, and how to activate
        subscriptions through the application, see [activation](#).
        The `revert_on_failure` parameter controls the behavior upon
        activation failure.
        - If set to `true` and something goes wrong i.e. payment fails, then
        Advanced Billing will not change the subscription's state. The
        subscription’s billing period will also remain the same.
        - If set to `false` and something goes wrong i.e. payment fails, then
        Advanced Billing will continue through with the activation and enter
        an end of life state. For trialing subscriptions, that will either be
        trial ended (if the trial is no obligation), past due (if the trial
        has an obligation), or canceled (if the site has no dunning strategy,
        or has a strategy that says to cancel immediately). For awaiting
        signup subscriptions, that will always be canceled.
        The default activation failure behavior can be configured per
        activation attempt, or you may set a default value under Config >
        Settings > Subscription Activation Settings.
        ## Activation Scenarios
        ### Activate Awaiting Signup subscription
        - Given you have a product without trial
        - Given you have a site without dunning strategy
        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Active
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| Canceled
        ```
        - Given you have a product with trial
        - Given you have a site with dunning strategy
        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Trialing
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| PD[Past Due]
        ```
        ### Activate Trialing subscription
        You can read more about the behavior of trialing subscriptions
        [here](https://maxio.zendesk.com/hc/en-us/articles/24252155721869-Trial
        ing-Subscriptions).
        When the `revert_on_failure` parameter is set to `true`, the
        subscription's state will remain as Trialing, we will void the invoice
        from activation and return any prepayments and credits applied to the
        invoice back to the subscription.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (ActivateSubscriptionRequest, optional): The request body
                parameter.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/activate.json')
            .http_method(HttpMethodEnum.PUT)
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('400', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorArrayMapResponseException)
        ).execute()
