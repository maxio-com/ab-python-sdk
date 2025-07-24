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

    Attributes:
        payer (CustomerPayerChange): The model property of type
            CustomerPayerChange.
        shipping_address (AddressChange): The model property of type
            AddressChange.
        billing_address (AddressChange): The model property of type
            AddressChange.
        custom_fields (CustomerCustomFieldsChange): The model property of type
            CustomerCustomFieldsChange.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
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
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(payer,
                   shipping_address,
                   billing_address,
                   custom_fields,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'payer={(self.payer if hasattr(self, "payer") else None)!r}, '
                f'shipping_address={(self.shipping_address if hasattr(self, "shipping_address") else None)!r}, '
                f'billing_address={(self.billing_address if hasattr(self, "billing_address") else None)!r}, '
                f'custom_fields={(self.custom_fields if hasattr(self, "custom_fields") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'payer={(self.payer if hasattr(self, "payer") else None)!s}, '
                f'shipping_address={(self.shipping_address if hasattr(self, "shipping_address") else None)!s}, '
                f'billing_address={(self.billing_address if hasattr(self, "billing_address") else None)!s}, '
                f'custom_fields={(self.custom_fields if hasattr(self, "custom_fields") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
