# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ComponentAllocationChange(object):

    """Implementation of the 'Component Allocation Change' model.

    TODO: type model description here.

    Attributes:
        previous_allocation (int): TODO: type description here.
        new_allocation (int): TODO: type description here.
        component_id (int): TODO: type description here.
        component_handle (str): TODO: type description here.
        memo (str): TODO: type description here.
        allocation_id (int): TODO: type description here.
        allocated_quantity (int | str | None): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "previous_allocation": 'previous_allocation',
        "new_allocation": 'new_allocation',
        "component_id": 'component_id',
        "component_handle": 'component_handle',
        "memo": 'memo',
        "allocation_id": 'allocation_id',
        "allocated_quantity": 'allocated_quantity'
    }

    _optionals = [
        'allocated_quantity',
    ]

    def __init__(self,
                 previous_allocation=None,
                 new_allocation=None,
                 component_id=None,
                 component_handle=None,
                 memo=None,
                 allocation_id=None,
                 allocated_quantity=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ComponentAllocationChange class"""

        # Initialize members of the class
        self.previous_allocation = previous_allocation 
        self.new_allocation = new_allocation 
        self.component_id = component_id 
        self.component_handle = component_handle 
        self.memo = memo 
        self.allocation_id = allocation_id 
        if allocated_quantity is not APIHelper.SKIP:
            self.allocated_quantity = allocated_quantity 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        previous_allocation = dictionary.get("previous_allocation") if dictionary.get("previous_allocation") else None
        new_allocation = dictionary.get("new_allocation") if dictionary.get("new_allocation") else None
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else None
        component_handle = dictionary.get("component_handle") if dictionary.get("component_handle") else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        allocation_id = dictionary.get("allocation_id") if dictionary.get("allocation_id") else None
        allocated_quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('ComponentAllocationChangeAllocatedQuantity'), dictionary.get('allocated_quantity'), False) if dictionary.get('allocated_quantity') is not None else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(previous_allocation,
                   new_allocation,
                   component_id,
                   component_handle,
                   memo,
                   allocation_id,
                   allocated_quantity,
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
            return APIHelper.is_valid_type(value=dictionary.previous_allocation,
                                           type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.new_allocation,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.component_id,
                                            type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.component_handle,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.memo,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.allocation_id,
                                            type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('previous_allocation'),
                                       type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('new_allocation'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('component_id'),
                                        type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('component_handle'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('memo'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('allocation_id'),
                                        type_callable=lambda value: isinstance(value, int))
