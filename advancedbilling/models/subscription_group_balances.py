# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.account_balance import AccountBalance


class SubscriptionGroupBalances(object):

    """Implementation of the 'Subscription Group Balances' model.

    TODO: type model description here.

    Attributes:
        prepayments (AccountBalance): TODO: type description here.
        service_credits (AccountBalance): TODO: type description here.
        open_invoices (AccountBalance): TODO: type description here.
        pending_discounts (AccountBalance): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prepayments": 'prepayments',
        "service_credits": 'service_credits',
        "open_invoices": 'open_invoices',
        "pending_discounts": 'pending_discounts'
    }

    _optionals = [
        'prepayments',
        'service_credits',
        'open_invoices',
        'pending_discounts',
    ]

    def __init__(self,
                 prepayments=APIHelper.SKIP,
                 service_credits=APIHelper.SKIP,
                 open_invoices=APIHelper.SKIP,
                 pending_discounts=APIHelper.SKIP):
        """Constructor for the SubscriptionGroupBalances class"""

        # Initialize members of the class
        if prepayments is not APIHelper.SKIP:
            self.prepayments = prepayments 
        if service_credits is not APIHelper.SKIP:
            self.service_credits = service_credits 
        if open_invoices is not APIHelper.SKIP:
            self.open_invoices = open_invoices 
        if pending_discounts is not APIHelper.SKIP:
            self.pending_discounts = pending_discounts 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        prepayments = AccountBalance.from_dictionary(dictionary.get('prepayments')) if 'prepayments' in dictionary.keys() else APIHelper.SKIP
        service_credits = AccountBalance.from_dictionary(dictionary.get('service_credits')) if 'service_credits' in dictionary.keys() else APIHelper.SKIP
        open_invoices = AccountBalance.from_dictionary(dictionary.get('open_invoices')) if 'open_invoices' in dictionary.keys() else APIHelper.SKIP
        pending_discounts = AccountBalance.from_dictionary(dictionary.get('pending_discounts')) if 'pending_discounts' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(prepayments,
                   service_credits,
                   open_invoices,
                   pending_discounts)
