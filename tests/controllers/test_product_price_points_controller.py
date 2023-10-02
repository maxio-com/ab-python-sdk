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
from maxioadvancedbillingformerlychargifyapi.utilities.union_type_lookup import UnionTypeLookUp
from maxioadvancedbillingformerlychargifyapi.api_helper import APIHelper


class ProductPricePointsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ProductPricePointsControllerTests, cls).setUpClass()
        cls.controller = cls.client.product_price_points
        cls.response_catcher = cls.controller.http_call_back

    # This method allows retrieval of a list of Products Price Points belonging to a Site.
    def test_list_all_product_price_points(self):
        # Parameters for the API call
        direction = None
        filter_archived_at = 'not_null'
        filter_date_field = 'updated_at'
        filter_end_date = None
        filter_end_datetime = None
        filter_ids = APIHelper.json_deserialize('[1,2,3]')
        filter_start_date = None
        filter_start_datetime = None
        filter_type = APIHelper.json_deserialize('["catalog","default"]')
        include = 'currency_prices'
        page = 1
        per_page = 20

        # Perform the API call through the SDK function
        result = self.controller.list_all_product_price_points(direction, filter_archived_at, filter_date_field, filter_end_date, filter_end_datetime, filter_ids, filter_start_date, filter_start_datetime, filter_type, include, page, per_page)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"price_points":[{"id":0,"name":"My pricepoint","handle":"handle",'
            '"price_in_cents":10,"interval":5,"interval_unit":"month","trial_pr'
            'ice_in_cents":10,"trial_interval":1,"trial_interval_unit":"month",'
            '"trial_type":"payment_expected","introductory_offer":true,"initial'
            '_charge_in_cents":0,"initial_charge_after_trial":true,"expiration_'
            'interval":0,"expiration_interval_unit":"month","product_id":1230,"'
            'created_at":"2021-04-02T17:52:09-04:00","updated_at":"2021-04-02T1'
            '7:52:09-04:00","use_site_exchange_rate":true}]}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

