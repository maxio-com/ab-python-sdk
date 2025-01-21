# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.batch_job import BatchJob


class BatchJobResponse(object):

    """Implementation of the 'Batch Job Response' model.

    Attributes:
        batchjob (BatchJob): The model property of type BatchJob.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "batchjob": 'batchjob'
    }

    def __init__(self,
                 batchjob=None,
                 additional_properties=None):
        """Constructor for the BatchJobResponse class"""

        # Initialize members of the class
        self.batchjob = batchjob 

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
        batchjob = BatchJob.from_dictionary(dictionary.get('batchjob')) if dictionary.get('batchjob') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(batchjob,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'batchjob={self.batchjob!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'batchjob={self.batchjob!s}, '
                f'additional_properties={self.additional_properties!s})')
