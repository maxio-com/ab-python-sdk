# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class PaymentRelatedEvents(object):

    """Implementation of the 'Payment Related Events' model.

    TODO: type model description here.

    Attributes:
        product_id (int): TODO: type description here.
        account_transaction_id (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_id": 'product_id',
        "account_transaction_id": 'account_transaction_id'
    }

    def __init__(self,
                 product_id=None,
                 account_transaction_id=None):
        """Constructor for the PaymentRelatedEvents class"""

        # Initialize members of the class
        self.product_id = product_id 
        self.account_transaction_id = account_transaction_id 

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
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else None
        account_transaction_id = dictionary.get("account_transaction_id") if dictionary.get("account_transaction_id") else None
        # Return an object of this model
        return cls(product_id,
                   account_transaction_id)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.product_id, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.account_transaction_id, type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('product_id'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('account_transaction_id'), type_callable=lambda value: isinstance(value, int))
