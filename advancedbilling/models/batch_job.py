# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class BatchJob(object):

    """Implementation of the 'Batch-Job' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        finished_at (datetime): TODO: type description here.
        row_count (int): TODO: type description here.
        created_at (datetime): TODO: type description here.
        completed (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "finished_at": 'finished_at',
        "row_count": 'row_count',
        "created_at": 'created_at',
        "completed": 'completed'
    }

    _optionals = [
        'id',
        'finished_at',
        'row_count',
        'created_at',
        'completed',
    ]

    _nullables = [
        'finished_at',
        'row_count',
        'created_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 finished_at=APIHelper.SKIP,
                 row_count=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 completed=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the BatchJob class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if finished_at is not APIHelper.SKIP:
            self.finished_at = APIHelper.apply_datetime_converter(finished_at, APIHelper.RFC3339DateTime) if finished_at else None 
        if row_count is not APIHelper.SKIP:
            self.row_count = row_count 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if completed is not APIHelper.SKIP:
            self.completed = completed 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        if 'finished_at' in dictionary.keys():
            finished_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("finished_at")).datetime if dictionary.get("finished_at") else None
        else:
            finished_at = APIHelper.SKIP
        row_count = dictionary.get("row_count") if "row_count" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        completed = dictionary.get("completed") if dictionary.get("completed") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   finished_at,
                   row_count,
                   created_at,
                   completed,
                   dictionary)
