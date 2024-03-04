# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.batch_job import BatchJob


class BatchJobResponse(object):

    """Implementation of the 'Batch Job Response' model.

    TODO: type model description here.

    Attributes:
        batchjob (BatchJob): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "batchjob": 'batchjob'
    }

    def __init__(self,
                 batchjob=None,
                 additional_properties={}):
        """Constructor for the BatchJobResponse class"""

        # Initialize members of the class
        self.batchjob = batchjob 

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
        batchjob = BatchJob.from_dictionary(dictionary.get('batchjob')) if dictionary.get('batchjob') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(batchjob,
                   dictionary)
