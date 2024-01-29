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
        finished_at (str): TODO: type description here.
        row_count (int): TODO: type description here.
        created_at (str): TODO: type description here.
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
                 completed=APIHelper.SKIP):
        """Constructor for the BatchJob class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if finished_at is not APIHelper.SKIP:
            self.finished_at = finished_at 
        if row_count is not APIHelper.SKIP:
            self.row_count = row_count 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if completed is not APIHelper.SKIP:
            self.completed = completed 

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
        finished_at = dictionary.get("finished_at") if "finished_at" in dictionary.keys() else APIHelper.SKIP
        row_count = dictionary.get("row_count") if "row_count" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if "created_at" in dictionary.keys() else APIHelper.SKIP
        completed = dictionary.get("completed") if dictionary.get("completed") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   finished_at,
                   row_count,
                   created_at,
                   completed)
