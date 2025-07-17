# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CalendarBilling(object):

    """Implementation of the 'Calendar Billing' model.

    (Optional). Cannot be used when also specifying next_billing_at

    Attributes:
        snap_day (int | str | None): A day of month that subscription will be
            processed on. Can be 1 up to 28 or 'end'.
        calendar_billing_first_charge (FirstChargeType): The model property of
            type FirstChargeType.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "snap_day": 'snap_day',
        "calendar_billing_first_charge": 'calendar_billing_first_charge'
    }

    _optionals = [
        'snap_day',
        'calendar_billing_first_charge',
    ]

    def __init__(self,
                 snap_day=APIHelper.SKIP,
                 calendar_billing_first_charge=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CalendarBilling class"""

        # Initialize members of the class
        if snap_day is not APIHelper.SKIP:
            self.snap_day = snap_day 
        if calendar_billing_first_charge is not APIHelper.SKIP:
            self.calendar_billing_first_charge = calendar_billing_first_charge 

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
        snap_day = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CalendarBillingSnapDay'), dictionary.get('snap_day'), False) if dictionary.get('snap_day') is not None else APIHelper.SKIP
        calendar_billing_first_charge = dictionary.get("calendar_billing_first_charge") if dictionary.get("calendar_billing_first_charge") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(snap_day,
                   calendar_billing_first_charge,
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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'snap_day={(self.snap_day if hasattr(self, "snap_day") else None)!r}, '
                f'calendar_billing_first_charge={(self.calendar_billing_first_charge if hasattr(self, "calendar_billing_first_charge") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'snap_day={(self.snap_day if hasattr(self, "snap_day") else None)!s}, '
                f'calendar_billing_first_charge={(self.calendar_billing_first_charge if hasattr(self, "calendar_billing_first_charge") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
