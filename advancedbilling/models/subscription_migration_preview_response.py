# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.subscription_migration_preview import SubscriptionMigrationPreview


class SubscriptionMigrationPreviewResponse(object):

    """Implementation of the 'Subscription Migration Preview Response' model.

    TODO: type model description here.

    Attributes:
        migration (SubscriptionMigrationPreview): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "migration": 'migration'
    }

    def __init__(self,
                 migration=None,
                 additional_properties={}):
        """Constructor for the SubscriptionMigrationPreviewResponse class"""

        # Initialize members of the class
        self.migration = migration 

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
        migration = SubscriptionMigrationPreview.from_dictionary(dictionary.get('migration')) if dictionary.get('migration') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(migration,
                   dictionary)
