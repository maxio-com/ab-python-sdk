# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SendInvoiceRequest(object):

    """Implementation of the 'Send Invoice Request' model.

    TODO: type model description here.

    Attributes:
        recipient_emails (List[str]): TODO: type description here.
        cc_recipient_emails (List[str]): TODO: type description here.
        bcc_recipient_emails (List[str]): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "recipient_emails": 'recipient_emails',
        "cc_recipient_emails": 'cc_recipient_emails',
        "bcc_recipient_emails": 'bcc_recipient_emails'
    }

    _optionals = [
        'recipient_emails',
        'cc_recipient_emails',
        'bcc_recipient_emails',
    ]

    def __init__(self,
                 recipient_emails=APIHelper.SKIP,
                 cc_recipient_emails=APIHelper.SKIP,
                 bcc_recipient_emails=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SendInvoiceRequest class"""

        # Initialize members of the class
        if recipient_emails is not APIHelper.SKIP:
            self.recipient_emails = recipient_emails 
        if cc_recipient_emails is not APIHelper.SKIP:
            self.cc_recipient_emails = cc_recipient_emails 
        if bcc_recipient_emails is not APIHelper.SKIP:
            self.bcc_recipient_emails = bcc_recipient_emails 

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
        recipient_emails = dictionary.get("recipient_emails") if dictionary.get("recipient_emails") else APIHelper.SKIP
        cc_recipient_emails = dictionary.get("cc_recipient_emails") if dictionary.get("cc_recipient_emails") else APIHelper.SKIP
        bcc_recipient_emails = dictionary.get("bcc_recipient_emails") if dictionary.get("bcc_recipient_emails") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(recipient_emails,
                   cc_recipient_emails,
                   bcc_recipient_emails,
                   additional_properties)
