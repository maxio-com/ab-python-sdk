# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.account_balance import AccountBalance


class AccountBalances(object):

    """Implementation of the 'Account Balances' model.

    TODO: type model description here.

    Attributes:
        open_invoices (AccountBalance): The balance, in cents, of the sum of
            the subscription's  open, payable invoices.
        pending_discounts (AccountBalance): The balance, in cents, of the
            subscription's Pending Discount account.
        service_credits (AccountBalance): The balance, in cents, of the
            subscription's Service Credit account.
        prepayments (AccountBalance): The balance, in cents, of the
            subscription's Prepayment account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "open_invoices": 'open_invoices',
        "pending_discounts": 'pending_discounts',
        "service_credits": 'service_credits',
        "prepayments": 'prepayments'
    }

    _optionals = [
        'open_invoices',
        'pending_discounts',
        'service_credits',
        'prepayments',
    ]

    def __init__(self,
                 open_invoices=APIHelper.SKIP,
                 pending_discounts=APIHelper.SKIP,
                 service_credits=APIHelper.SKIP,
                 prepayments=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the AccountBalances class"""

        # Initialize members of the class
        if open_invoices is not APIHelper.SKIP:
            self.open_invoices = open_invoices 
        if pending_discounts is not APIHelper.SKIP:
            self.pending_discounts = pending_discounts 
        if service_credits is not APIHelper.SKIP:
            self.service_credits = service_credits 
        if prepayments is not APIHelper.SKIP:
            self.prepayments = prepayments 

        # Add additional model properties to the instance
        self.additional_properties = additional_properties

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
        open_invoices = AccountBalance.from_dictionary(dictionary.get('open_invoices')) if 'open_invoices' in dictionary.keys() else APIHelper.SKIP
        pending_discounts = AccountBalance.from_dictionary(dictionary.get('pending_discounts')) if 'pending_discounts' in dictionary.keys() else APIHelper.SKIP
        service_credits = AccountBalance.from_dictionary(dictionary.get('service_credits')) if 'service_credits' in dictionary.keys() else APIHelper.SKIP
        prepayments = AccountBalance.from_dictionary(dictionary.get('prepayments')) if 'prepayments' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(open_invoices,
                   pending_discounts,
                   service_credits,
                   prepayments,
                   dictionary)
