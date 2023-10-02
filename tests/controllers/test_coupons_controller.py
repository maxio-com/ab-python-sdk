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


class CouponsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(CouponsControllerTests, cls).setUpClass()
        cls.controller = cls.client.coupons
        cls.response_catcher = cls.controller.http_call_back

    # You can search for a coupon via the API with the find method. By passing a code parameter, the find will attempt to locate a coupon that matches that code. If no coupon is found, a 404 is returned.
    #
    #If you have more than one product family and if the coupon you are trying to find does not belong to the default product family in your site, then you will need to specify (either in the url or as a query string param) the product family id.
    def test_read_coupon_by_code(self):
        # Parameters for the API call
        product_family_id = None
        code = None

        # Perform the API call through the SDK function
        result = self.controller.read_coupon_by_code(product_family_id, code)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # You can retrieve a list of coupons.
    #
    #If the coupon is set to `use_site_exchange_rate: true`, it will return pricing based on the current exchange rate. If the flag is set to false, it will return all of the defined prices for each currency.
    def test_list_coupons(self):
        # Parameters for the API call
        page = 1
        per_page = 30
        date_field = 'updated_at'
        start_date = None
        end_date = None
        start_datetime = None
        end_datetime = None
        filter_ids = APIHelper.json_deserialize('[1,2,3]')
        filter_codes = APIHelper.json_deserialize('["free","free_trial"]')
        currency_prices = True
        filter_end_date = None
        filter_end_datetime = None
        filter_start_date = None
        filter_start_datetime = None
        filter_date_field = 'updated_at'
        filter_use_site_exchange_rate = True

        # Perform the API call through the SDK function
        result = self.controller.list_coupons(page, per_page, date_field, start_date, end_date, start_datetime, end_datetime, filter_ids, filter_codes, currency_prices, filter_end_date, filter_end_datetime, filter_start_date, filter_start_datetime, filter_date_field, filter_use_site_exchange_rate)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"coupon":{"id":0,"name":"string","code":"string","description":"'
            'string","amount":0,"amount_in_cents":0,"product_family_id":0,"prod'
            'uct_family_name":"string","start_date":"string","end_date":"string'
            '","percentage":0,"recurring":true,"recurring_scheme":"do_not_recur'
            '","duration_period_count":0,"duration_interval":0,"duration_interv'
            'al_unit":"string","duration_interval_span":"string","allow_negativ'
            'e_balance":true,"archived_at":"string","conversion_limit":"string"'
            ',"stackable":true,"compounding_strategy":"compound","use_site_exch'
            'ange_rate":true,"created_at":"string","updated_at":"string","disco'
            'unt_type":"amount","exclude_mid_period_allocations":true,"apply_on'
            '_cancel_at_end_of_period ":true,"coupon_restrictions":[{"id":"stri'
            'ng","item_type":"Component","item_id":0,"name":"string","handle":"'
            'string"}]}}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

