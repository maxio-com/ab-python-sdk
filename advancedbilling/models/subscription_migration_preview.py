# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SubscriptionMigrationPreview(object):

    """Implementation of the 'Subscription Migration Preview' model.

    TODO: type model description here.

    Attributes:
        prorated_adjustment_in_cents (long|int): The amount of the prorated
            adjustment that would be issued for the current subscription.
        charge_in_cents (long|int): The amount of the charge that would be
            created for the new product.
        payment_due_in_cents (long|int): The amount of the payment due in the
            case of an upgrade.
        credit_applied_in_cents (long|int): Represents a credit in cents that
            is applied to your subscription as part of a migration process for
            a specific product, which reduces the amount owed for the
            subscription.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prorated_adjustment_in_cents": 'prorated_adjustment_in_cents',
        "charge_in_cents": 'charge_in_cents',
        "payment_due_in_cents": 'payment_due_in_cents',
        "credit_applied_in_cents": 'credit_applied_in_cents'
    }

    _optionals = [
        'prorated_adjustment_in_cents',
        'charge_in_cents',
        'payment_due_in_cents',
        'credit_applied_in_cents',
    ]

    def __init__(self,
                 prorated_adjustment_in_cents=APIHelper.SKIP,
                 charge_in_cents=APIHelper.SKIP,
                 payment_due_in_cents=APIHelper.SKIP,
                 credit_applied_in_cents=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionMigrationPreview class"""

        # Initialize members of the class
        if prorated_adjustment_in_cents is not APIHelper.SKIP:
            self.prorated_adjustment_in_cents = prorated_adjustment_in_cents 
        if charge_in_cents is not APIHelper.SKIP:
            self.charge_in_cents = charge_in_cents 
        if payment_due_in_cents is not APIHelper.SKIP:
            self.payment_due_in_cents = payment_due_in_cents 
        if credit_applied_in_cents is not APIHelper.SKIP:
            self.credit_applied_in_cents = credit_applied_in_cents 

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
        prorated_adjustment_in_cents = dictionary.get("prorated_adjustment_in_cents") if dictionary.get("prorated_adjustment_in_cents") else APIHelper.SKIP
        charge_in_cents = dictionary.get("charge_in_cents") if dictionary.get("charge_in_cents") else APIHelper.SKIP
        payment_due_in_cents = dictionary.get("payment_due_in_cents") if dictionary.get("payment_due_in_cents") else APIHelper.SKIP
        credit_applied_in_cents = dictionary.get("credit_applied_in_cents") if dictionary.get("credit_applied_in_cents") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(prorated_adjustment_in_cents,
                   charge_in_cents,
                   payment_due_in_cents,
                   credit_applied_in_cents,
                   additional_properties)
