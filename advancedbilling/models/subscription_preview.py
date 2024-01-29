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

    TODO: type model description here.

    Attributes:
        current_billing_manifest (BillingManifest): TODO: type description
            here.
        next_billing_manifest (BillingManifest): TODO: type description here.

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
                 next_billing_manifest=APIHelper.SKIP):
        """Constructor for the SubscriptionPreview class"""

        # Initialize members of the class
        if current_billing_manifest is not APIHelper.SKIP:
            self.current_billing_manifest = current_billing_manifest 
        if next_billing_manifest is not APIHelper.SKIP:
            self.next_billing_manifest = next_billing_manifest 

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
        current_billing_manifest = BillingManifest.from_dictionary(dictionary.get('current_billing_manifest')) if 'current_billing_manifest' in dictionary.keys() else APIHelper.SKIP
        next_billing_manifest = BillingManifest.from_dictionary(dictionary.get('next_billing_manifest')) if 'next_billing_manifest' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(current_billing_manifest,
                   next_billing_manifest)
