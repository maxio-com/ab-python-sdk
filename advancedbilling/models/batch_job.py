# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class BatchJob(object):

    """Implementation of the 'Batch-Job' model.

    Attributes:
        id (int): The model property of type int.
        finished_at (datetime): The model property of type datetime.
        row_count (int): The model property of type int.
        created_at (datetime): The model property of type datetime.
        completed (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 additional_properties=None):
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
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   finished_at,
                   row_count,
                   created_at,
                   completed,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'finished_at={self.finished_at!r}, '
                f'row_count={self.row_count!r}, '
                f'created_at={self.created_at!r}, '
                f'completed={self.completed!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'finished_at={self.finished_at!s}, '
                f'row_count={self.row_count!s}, '
                f'created_at={self.created_at!s}, '
                f'completed={self.completed!s}, '
                f'additional_properties={self.additional_properties!s})')
