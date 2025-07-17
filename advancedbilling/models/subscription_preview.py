# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.billing_manifest import BillingManifest


class SubscriptionPreview(object):

    """Implementation of the 'Subscription Preview' model.

    Attributes:
        current_billing_manifest (BillingManifest): The model property of type
            BillingManifest.
        next_billing_manifest (BillingManifest): The model property of type
            BillingManifest.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_billing_manifest": 'current_billing_manifest',
        "next_billing_manifest": 'next_billing_manifest'
    }

    _optionals = [
        'current_billing_manifest',
        'next_billing_manifest',
    ]

    def __init__(self,
                 current_billing_manifest=APIHelper.SKIP,
                 next_billing_manifest=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionPreview class"""

        # Initialize members of the class
        if current_billing_manifest is not APIHelper.SKIP:
            self.current_billing_manifest = current_billing_manifest 
        if next_billing_manifest is not APIHelper.SKIP:
            self.next_billing_manifest = next_billing_manifest 

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
        current_billing_manifest = BillingManifest.from_dictionary(dictionary.get('current_billing_manifest')) if 'current_billing_manifest' in dictionary.keys() else APIHelper.SKIP
        next_billing_manifest = BillingManifest.from_dictionary(dictionary.get('next_billing_manifest')) if 'next_billing_manifest' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(current_billing_manifest,
                   next_billing_manifest,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'current_billing_manifest={(self.current_billing_manifest if hasattr(self, "current_billing_manifest") else None)!r}, '
                f'next_billing_manifest={(self.next_billing_manifest if hasattr(self, "next_billing_manifest") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'current_billing_manifest={(self.current_billing_manifest if hasattr(self, "current_billing_manifest") else None)!s}, '
                f'next_billing_manifest={(self.next_billing_manifest if hasattr(self, "next_billing_manifest") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
