# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.address_change import AddressChange
from advancedbilling.models.customer_custom_fields_change import CustomerCustomFieldsChange
from advancedbilling.models.customer_payer_change import CustomerPayerChange


class CustomerChange(object):

    """Implementation of the 'Customer Change' model.

    TODO: type model description here.

    Attributes:
        payer (CustomerPayerChange): TODO: type description here.
        shipping_address (AddressChange): TODO: type description here.
        billing_address (AddressChange): TODO: type description here.
        custom_fields (CustomerCustomFieldsChange): TODO: type description
            here.

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
                 custom_fields=APIHelper.SKIP,
                 additional_properties={}):
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
        if 'payer' in dictionary.keys():
            payer = CustomerPayerChange.from_dictionary(dictionary.get('payer')) if dictionary.get('payer') else None
        else:
            payer = APIHelper.SKIP
        if 'shipping_address' in dictionary.keys():
            shipping_address = AddressChange.from_dictionary(dictionary.get('shipping_address')) if dictionary.get('shipping_address') else None
        else:
            shipping_address = APIHelper.SKIP
        if 'billing_address' in dictionary.keys():
            billing_address = AddressChange.from_dictionary(dictionary.get('billing_address')) if dictionary.get('billing_address') else None
        else:
            billing_address = APIHelper.SKIP
        if 'custom_fields' in dictionary.keys():
            custom_fields = CustomerCustomFieldsChange.from_dictionary(dictionary.get('custom_fields')) if dictionary.get('custom_fields') else None
        else:
            custom_fields = APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(payer,
                   shipping_address,
                   billing_address,
                   custom_fields,
                   dictionary)
