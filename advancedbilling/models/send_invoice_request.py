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
                 bcc_recipient_emails=APIHelper.SKIP):
        """Constructor for the SendInvoiceRequest class"""

        # Initialize members of the class
        if recipient_emails is not APIHelper.SKIP:
            self.recipient_emails = recipient_emails 
        if cc_recipient_emails is not APIHelper.SKIP:
            self.cc_recipient_emails = cc_recipient_emails 
        if bcc_recipient_emails is not APIHelper.SKIP:
            self.bcc_recipient_emails = bcc_recipient_emails 

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
        recipient_emails = dictionary.get("recipient_emails") if dictionary.get("recipient_emails") else APIHelper.SKIP
        cc_recipient_emails = dictionary.get("cc_recipient_emails") if dictionary.get("cc_recipient_emails") else APIHelper.SKIP
        bcc_recipient_emails = dictionary.get("bcc_recipient_emails") if dictionary.get("bcc_recipient_emails") else APIHelper.SKIP
        # Return an object of this model
        return cls(recipient_emails,
                   cc_recipient_emails,
                   bcc_recipient_emails)
