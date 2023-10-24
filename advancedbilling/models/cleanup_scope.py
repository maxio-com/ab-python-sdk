# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CleanupScope(object):

    """Implementation of the 'Cleanup scope' enum.

    all: Will clear all products, customers, and related subscriptions from
    the site. customers: Will clear only customers and related subscriptions
    (leaving the products untouched) for the site. Revenue will also be reset
    to 0.

    Attributes:
        ALL: TODO: type description here.
        CUSTOMERS: TODO: type description here.

    """
    ALL = 'all'

    CUSTOMERS = 'customers'

