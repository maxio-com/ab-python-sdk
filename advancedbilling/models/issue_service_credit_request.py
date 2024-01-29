# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.issue_service_credit import IssueServiceCredit


class IssueServiceCreditRequest(object):

    """Implementation of the 'Issue Service Credit Request' model.

    TODO: type model description here.

    Attributes:
        service_credit (IssueServiceCredit): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "service_credit": 'service_credit'
    }

    def __init__(self,
                 service_credit=None):
        """Constructor for the IssueServiceCreditRequest class"""

        # Initialize members of the class
        self.service_credit = service_credit 

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
        service_credit = IssueServiceCredit.from_dictionary(dictionary.get('service_credit')) if dictionary.get('service_credit') else None
        # Return an object of this model
        return cls(service_credit)
