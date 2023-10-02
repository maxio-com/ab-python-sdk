# -*- coding: utf-8 -*-

"""
maxioadvancedbillingformerlychargifyapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from maxioadvancedbillingformerlychargifyapi.api_helper import APIHelper
from maxioadvancedbillingformerlychargifyapi.models.create_subscription_request import CreateSubscriptionRequest


class ProformaInvoicesControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ProformaInvoicesControllerTests, cls).setUpClass()
        cls.controller = cls.client.proforma_invoices
        cls.response_catcher = cls.controller.http_call_back

    # This endpoint is only available for Relationship Invoicing sites. It cannot be used to create consolidated proforma invoices or preview prepaid subscriptions.
    #
    #Create a proforma invoice to preview costs before a subscription's signup. Like other proforma invoices, it can be emailed to the customer, voided, and publicly viewed on the chargifypay domain.
    #
    #Pass a payload that resembles a subscription create or signup preview request. For example, you can specify components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate a shipping or billing address.
    #
    #A product and customer first name, last name, and email are the minimum requirements. We recommend associating the proforma invoice with a customer_id to easily find their proforma invoices, since the subscription_id will always be blank.
    def test_create_signup_proforma_invoice(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"subscription":{"product_handle":"gold-product","customer_attribu'
            'tes":{"first_name":"Myra","last_name":"Maisel","email":"mmaisel@ex'
            'ample.com"}}}', CreateSubscriptionRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.create_signup_proforma_invoice(body)

        # Test response code
        assert self.response_catcher.response.status_code == 201

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # This endpoint is only available for Relationship Invoicing sites. It cannot be used to create consolidated proforma invoice previews or preview prepaid subscriptions.
    #
    #Create a signup preview in the format of a proforma invoice to preview costs before a subscription's signup. You have the option of optionally previewing the first renewal's costs as well. The proforma invoice preview will not be persisted.
    #
    #Pass a payload that resembles a subscription create or signup preview request. For example, you can specify components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate a shipping or billing address.
    #
    #A product and customer first name, last name, and email are the minimum requirements.
    def test_preview_signup_proforma_invoice(self):
        # Parameters for the API call
        include_next_proforma_invoice = None
        body = APIHelper.json_deserialize('{"subscription":{"product_handle":"gold-plan","customer_attributes'
            '":{"first_name":"first","last_name":"last","email":"flast@example.'
            'com"}}}', CreateSubscriptionRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.preview_signup_proforma_invoice(include_next_proforma_invoice, body)

        # Test response code
        assert self.response_catcher.response.status_code == 201

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


