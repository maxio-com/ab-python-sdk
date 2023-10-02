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


class SitesControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites
        cls.response_catcher = cls.controller.http_call_back

    # This endpoint allows you to fetch some site data.
    #
    #Full documentation on Sites in the Chargify UI can be located [here](https://chargify.zendesk.com/hc/en-us/articles/4407870738587).
    #
    #Specifically, the [Clearing Site Data](https://maxio-chargify.zendesk.com/hc/en-us/articles/5405428327309) section is extremely relevant to this endpoint documentation.
    #
    ##### Relationship invoicing enabled
    #If site has RI enabled then you will see more settings like:
    #
    #    "customer_hierarchy_enabled": true,
    #    "whopays_enabled": true,
    #    "whopays_default_payer": "self"
    #You can read more about these settings here:
    # [Who Pays & Customer Hierarchy](https://chargify.zendesk.com/hc/en-us/articles/4407746683291)
    def test_read_site(self):

        # Perform the API call through the SDK function
        result = self.controller.read_site()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"site":{"id":0,"name":"string","subdomain":"string","currency":"s'
            'tring","seller_id":0,"non_primary_currencies":["string"],"relation'
            'ship_invoicing_enabled":true,"customer_hierarchy_enabled":true,"wh'
            'opays_enabled":true,"whopays_default_payer":"string","default_paym'
            'ent_collection_method":"string","organization_address":{"street":n'
            'ull,"line2":null,"city":null,"state":null,"zip":null,"country":nul'
            'l,"name":"string","phone":"string"},"tax_configuration":{"kind":"c'
            'ustom","fully_configured":true,"destination_address":"shipping_the'
            'n_billing"},"net_terms":{"default_net_terms":0,"automatic_net_term'
            's":0,"remittance_net_terms":0,"net_terms_on_remittance_signups_ena'
            'bled":false,"custom_net_terms_enabled":false},"test":true}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # This call is asynchronous and there may be a delay before the site data is fully deleted. If you are clearing site data for an automated test, you will need to build in a delay and/or check that there are no products, etc., in the site before proceeding.
    #
    #**This functionality will only work on sites in TEST mode. Attempts to perform this on sites in “live” mode will result in a response of 403 FORBIDDEN.**
    #
    def test_clear_site(self):
        # Parameters for the API call
        cleanup_scope = 'all'

        # Perform the API call through the SDK function
        self.controller.clear_site(cleanup_scope)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # This endpoint returns public keys used for Chargify.js.
    def test_list_chargify_js_public_keys(self):
        # Parameters for the API call
        page = 1
        per_page = 20

        # Perform the API call through the SDK function
        result = self.controller.list_chargify_js_public_keys(page, per_page)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"chargify_js_keys":[{"public_key":"chjs_ftrxt7c4fv6f74wchjs_5zyn7'
            'gnwv","requires_security_token":false,"created_at":"2021-01-01T05:'
            '00:00-04:00"}],"meta":{"total_count":1,"current_page":1,"total_pag'
            'es":1,"per_page":10}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

