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

    Attributes:
        prepayments (AccountBalance): The model property of type
            AccountBalance.
        service_credits (AccountBalance): The model property of type
            AccountBalance.
        open_invoices (AccountBalance): The model property of type
            AccountBalance.
        pending_discounts (AccountBalance): The model property of type
            AccountBalance.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 pending_discounts=APIHelper.SKIP,
                 additional_properties=None):
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

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        prepayments = AccountBalance.from_dictionary(dictionary.get('prepayments')) if 'prepayments' in dictionary.keys() else APIHelper.SKIP
        service_credits = AccountBalance.from_dictionary(dictionary.get('service_credits')) if 'service_credits' in dictionary.keys() else APIHelper.SKIP
        open_invoices = AccountBalance.from_dictionary(dictionary.get('open_invoices')) if 'open_invoices' in dictionary.keys() else APIHelper.SKIP
        pending_discounts = AccountBalance.from_dictionary(dictionary.get('pending_discounts')) if 'pending_discounts' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(prepayments,
                   service_credits,
                   open_invoices,
                   pending_discounts,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'prepayments={(self.prepayments if hasattr(self, "prepayments") else None)!r}, '
                f'service_credits={(self.service_credits if hasattr(self, "service_credits") else None)!r}, '
                f'open_invoices={(self.open_invoices if hasattr(self, "open_invoices") else None)!r}, '
                f'pending_discounts={(self.pending_discounts if hasattr(self, "pending_discounts") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'prepayments={(self.prepayments if hasattr(self, "prepayments") else None)!s}, '
                f'service_credits={(self.service_credits if hasattr(self, "service_credits") else None)!s}, '
                f'open_invoices={(self.open_invoices if hasattr(self, "open_invoices") else None)!s}, '
                f'pending_discounts={(self.pending_discounts if hasattr(self, "pending_discounts") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
