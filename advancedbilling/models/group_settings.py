# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.group_billing import GroupBilling
from advancedbilling.models.group_target import GroupTarget


class GroupSettings(object):

    """Implementation of the 'Group Settings' model.

    TODO: type model description here.

    Attributes:
        target (GroupTarget): Attributes of the target customer who will be
            the responsible payer of the created subscription. Required.
        billing (GroupBilling): Optional attributes related to billing date
            and accrual. Note: Only applicable for new subscriptions.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "target": 'target',
        "billing": 'billing'
    }

    _optionals = [
        'billing',
    ]

    def __init__(self,
                 target=None,
                 billing=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the GroupSettings class"""

        # Initialize members of the class
        self.target = target 
        if billing is not APIHelper.SKIP:
            self.billing = billing 

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
        target = GroupTarget.from_dictionary(dictionary.get('target')) if dictionary.get('target') else None
        billing = GroupBilling.from_dictionary(dictionary.get('billing')) if 'billing' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(target,
                   billing,
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
            return APIHelper.is_valid_type(value=dictionary.target,
                                           type_callable=lambda value: GroupTarget.validate(value),
                                           is_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('target'),
                                       type_callable=lambda value: GroupTarget.validate(value),
                                       is_model_dict=True)
