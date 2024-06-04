# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RefundSuccess(object):

    """Implementation of the 'Refund Success' model.

    TODO: type model description here.

    Attributes:
        refund_id (int): TODO: type description here.
        gateway_transaction_id (int): TODO: type description here.
        product_id (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "refund_id": 'refund_id',
        "gateway_transaction_id": 'gateway_transaction_id',
        "product_id": 'product_id'
    }

    def __init__(self,
                 refund_id=None,
                 gateway_transaction_id=None,
                 product_id=None,
                 additional_properties={}):
        """Constructor for the RefundSuccess class"""

        # Initialize members of the class
        self.refund_id = refund_id 
        self.gateway_transaction_id = gateway_transaction_id 
        self.product_id = product_id 

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
        refund_id = dictionary.get("refund_id") if dictionary.get("refund_id") else None
        gateway_transaction_id = dictionary.get("gateway_transaction_id") if dictionary.get("gateway_transaction_id") else None
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(refund_id,
                   gateway_transaction_id,
                   product_id,
                   dictionary)

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
            return APIHelper.is_valid_type(value=dictionary.refund_id,
                                           type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.gateway_transaction_id,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.product_id,
                                            type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('refund_id'),
                                       type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('gateway_transaction_id'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('product_id'),
                                        type_callable=lambda value: isinstance(value, int))
