# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ListInvoiceEventsResponse(object):

    """Implementation of the 'List Invoice Events Response' model.

    Attributes:
        events (List[ApplyCreditNoteEvent | ApplyDebitNoteEvent |
            ApplyPaymentEvent | BackportInvoiceEvent |
            ChangeChargebackStatusEvent | ChangeInvoiceCollectionMethodEvent |
            ChangeInvoiceStatusEvent | CreateCreditNoteEvent |
            CreateDebitNoteEvent | FailedPaymentEvent | IssueInvoiceEvent |
            RefundInvoiceEvent | RemovePaymentEvent | VoidInvoiceEvent |
            VoidRemainderEvent] | None): The model property of type
            List[ApplyCreditNoteEvent | ApplyDebitNoteEvent |
            ApplyPaymentEvent | BackportInvoiceEvent |
            ChangeChargebackStatusEvent | ChangeInvoiceCollectionMethodEvent |
            ChangeInvoiceStatusEvent | CreateCreditNoteEvent |
            CreateDebitNoteEvent | FailedPaymentEvent | IssueInvoiceEvent |
            RefundInvoiceEvent | RemovePaymentEvent | VoidInvoiceEvent |
            VoidRemainderEvent] | None.
        page (int): The model property of type int.
        per_page (int): The model property of type int.
        total_pages (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "events": 'events',
        "page": 'page',
        "per_page": 'per_page',
        "total_pages": 'total_pages'
    }

    _optionals = [
        'events',
        'page',
        'per_page',
        'total_pages',
    ]

    def __init__(self,
                 events=APIHelper.SKIP,
                 page=APIHelper.SKIP,
                 per_page=APIHelper.SKIP,
                 total_pages=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ListInvoiceEventsResponse class"""

        # Initialize members of the class
        if events is not APIHelper.SKIP:
            self.events = events 
        if page is not APIHelper.SKIP:
            self.page = page 
        if per_page is not APIHelper.SKIP:
            self.per_page = per_page 
        if total_pages is not APIHelper.SKIP:
            self.total_pages = total_pages 

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
        events = APIHelper.deserialize_union_type(UnionTypeLookUp.get('Invoice-Event'), dictionary.get('events'), False) if dictionary.get('events') is not None else APIHelper.SKIP
        page = dictionary.get("page") if dictionary.get("page") else APIHelper.SKIP
        per_page = dictionary.get("per_page") if dictionary.get("per_page") else APIHelper.SKIP
        total_pages = dictionary.get("total_pages") if dictionary.get("total_pages") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(events,
                   page,
                   per_page,
                   total_pages,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'events={(self.events if hasattr(self, "events") else None)!r}, '
                f'page={(self.page if hasattr(self, "page") else None)!r}, '
                f'per_page={(self.per_page if hasattr(self, "per_page") else None)!r}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'events={(self.events if hasattr(self, "events") else None)!s}, '
                f'page={(self.page if hasattr(self, "page") else None)!s}, '
                f'per_page={(self.per_page if hasattr(self, "per_page") else None)!s}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
