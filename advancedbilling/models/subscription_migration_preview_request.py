# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.subscription_migration_preview_options import SubscriptionMigrationPreviewOptions


class SubscriptionMigrationPreviewRequest(object):

    """Implementation of the 'Subscription Migration Preview Request' model.

    TODO: type model description here.

    Attributes:
        migration (SubscriptionMigrationPreviewOptions): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "migration": 'migration'
    }

    def __init__(self,
                 migration=None):
        """Constructor for the SubscriptionMigrationPreviewRequest class"""

        # Initialize members of the class
        self.migration = migration 

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
        migration = SubscriptionMigrationPreviewOptions.from_dictionary(dictionary.get('migration')) if dictionary.get('migration') else None
        # Return an object of this model
        return cls(migration)
