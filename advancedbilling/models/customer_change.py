# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CustomerChange(object):

    """Implementation of the 'Customer Change' model.

    TODO: type model description here.

    Attributes:
        payer (CustomerPayerChange | None): TODO: type description here.
        shipping_address (AddressChange | None): TODO: type description here.
        billing_address (AddressChange | None): TODO: type description here.
        custom_fields (CustomerCustomFieldsChange | None): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payer": 'payer',
        "shipping_address": 'shipping_address',
        "billing_address": 'billing_address',
        "custom_fields": 'custom_fields'
    }

    _optionals = [
        'payer',
        'shipping_address',
        'billing_address',
        'custom_fields',
    ]

    _nullables = [
        'payer',
        'shipping_address',
        'billing_address',
        'custom_fields',
    ]

    def __init__(self,
                 payer=APIHelper.SKIP,
                 shipping_address=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP):
        """Constructor for the CustomerChange class"""

        # Initialize members of the class
        if payer is not APIHelper.SKIP:
            self.payer = payer 
        if shipping_address is not APIHelper.SKIP:
            self.shipping_address = shipping_address 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        if 'payer' in dictionary.keys():
            payer = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomerChangePayer'), dictionary.get('payer'), False) if dictionary.get('payer') is not None else None
        else:
            payer = APIHelper.SKIP
        if 'shipping_address' in dictionary.keys():
            shipping_address = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomerChangeShippingAddress'), dictionary.get('shipping_address'), False) if dictionary.get('shipping_address') is not None else None
        else:
            shipping_address = APIHelper.SKIP
        if 'billing_address' in dictionary.keys():
            billing_address = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomerChangeBillingAddress'), dictionary.get('billing_address'), False) if dictionary.get('billing_address') is not None else None
        else:
            billing_address = APIHelper.SKIP
        if 'custom_fields' in dictionary.keys():
            custom_fields = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CustomerChangeCustomFields'), dictionary.get('custom_fields'), False) if dictionary.get('custom_fields') is not None else None
        else:
            custom_fields = APIHelper.SKIP
        # Return an object of this model
        return cls(payer,
                   shipping_address,
                   billing_address,
                   custom_fields)
