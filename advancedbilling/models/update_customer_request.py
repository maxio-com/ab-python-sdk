# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.update_customer import UpdateCustomer


class UpdateCustomerRequest(object):

    """Implementation of the 'Update Customer Request' model.

    TODO: type model description here.

    Attributes:
        customer (UpdateCustomer): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer": 'customer'
    }

    def __init__(self,
                 customer=None):
        """Constructor for the UpdateCustomerRequest class"""

        # Initialize members of the class
        self.customer = customer 

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
        customer = UpdateCustomer.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        # Return an object of this model
        return cls(customer)
