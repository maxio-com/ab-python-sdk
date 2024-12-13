# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceAvataxDetails(object):

    """Implementation of the 'Invoice Avatax Details' model.

    TODO: type model description here.

    Attributes:
        id (long|int): TODO: type description here.
        status (str): TODO: type description here.
        document_code (str): TODO: type description here.
        commit_date (datetime): TODO: type description here.
        modify_date (datetime): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "status": 'status',
        "document_code": 'document_code',
        "commit_date": 'commit_date',
        "modify_date": 'modify_date'
    }

    _optionals = [
        'id',
        'status',
        'document_code',
        'commit_date',
        'modify_date',
    ]

    _nullables = [
        'id',
        'status',
        'document_code',
        'commit_date',
        'modify_date',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 document_code=APIHelper.SKIP,
                 commit_date=APIHelper.SKIP,
                 modify_date=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceAvataxDetails class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if document_code is not APIHelper.SKIP:
            self.document_code = document_code 
        if commit_date is not APIHelper.SKIP:
            self.commit_date = APIHelper.apply_datetime_converter(commit_date, APIHelper.RFC3339DateTime) if commit_date else None 
        if modify_date is not APIHelper.SKIP:
            self.modify_date = APIHelper.apply_datetime_converter(modify_date, APIHelper.RFC3339DateTime) if modify_date else None 

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
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        document_code = dictionary.get("document_code") if "document_code" in dictionary.keys() else APIHelper.SKIP
        if 'commit_date' in dictionary.keys():
            commit_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("commit_date")).datetime if dictionary.get("commit_date") else None
        else:
            commit_date = APIHelper.SKIP
        if 'modify_date' in dictionary.keys():
            modify_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("modify_date")).datetime if dictionary.get("modify_date") else None
        else:
            modify_date = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   status,
                   document_code,
                   commit_date,
                   modify_date,
                   additional_properties)

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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
