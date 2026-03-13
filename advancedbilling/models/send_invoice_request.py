"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class SendInvoiceRequest(object):
    """Implementation of the 'Send Invoice Request' model.

    Attributes:
        recipient_emails (List[str]): The model property of type List[str].
        cc_recipient_emails (List[str]): The model property of type List[str].
        bcc_recipient_emails (List[str]): The model property of type List[str].
        attachment_urls (List[str]): Array of URLs to files to attach to the invoice
            email. Max 10 files, 10MB each.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "recipient_emails": "recipient_emails",
        "cc_recipient_emails": "cc_recipient_emails",
        "bcc_recipient_emails": "bcc_recipient_emails",
        "attachment_urls": "attachment_urls",
    }

    _optionals = [
        "recipient_emails",
        "cc_recipient_emails",
        "bcc_recipient_emails",
        "attachment_urls",
    ]

    def __init__(
        self,
        recipient_emails=APIHelper.SKIP,
        cc_recipient_emails=APIHelper.SKIP,
        bcc_recipient_emails=APIHelper.SKIP,
        attachment_urls=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SendInvoiceRequest instance."""
        # Initialize members of the class
        if recipient_emails is not APIHelper.SKIP:
            self.recipient_emails = recipient_emails
        if cc_recipient_emails is not APIHelper.SKIP:
            self.cc_recipient_emails = cc_recipient_emails
        if bcc_recipient_emails is not APIHelper.SKIP:
            self.bcc_recipient_emails = bcc_recipient_emails
        if attachment_urls is not APIHelper.SKIP:
            self.attachment_urls = attachment_urls

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

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
        recipient_emails =\
            dictionary.get("recipient_emails")\
            if dictionary.get("recipient_emails")\
                else APIHelper.SKIP
        cc_recipient_emails =\
            dictionary.get("cc_recipient_emails")\
            if dictionary.get("cc_recipient_emails")\
                else APIHelper.SKIP
        bcc_recipient_emails =\
            dictionary.get("bcc_recipient_emails")\
            if dictionary.get("bcc_recipient_emails")\
                else APIHelper.SKIP
        attachment_urls =\
            dictionary.get("attachment_urls")\
            if dictionary.get("attachment_urls")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(recipient_emails,
                   cc_recipient_emails,
                   bcc_recipient_emails,
                   attachment_urls,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _recipient_emails=(
            self.recipient_emails
            if hasattr(self, "recipient_emails")
            else None
        )
        _cc_recipient_emails=(
            self.cc_recipient_emails
            if hasattr(self, "cc_recipient_emails")
            else None
        )
        _bcc_recipient_emails=(
            self.bcc_recipient_emails
            if hasattr(self, "bcc_recipient_emails")
            else None
        )
        _attachment_urls=(
            self.attachment_urls
            if hasattr(self, "attachment_urls")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"recipient_emails={_recipient_emails!r}, "
            f"cc_recipient_emails={_cc_recipient_emails!r}, "
            f"bcc_recipient_emails={_bcc_recipient_emails!r}, "
            f"attachment_urls={_attachment_urls!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _recipient_emails=(
            self.recipient_emails
            if hasattr(self, "recipient_emails")
            else None
        )
        _cc_recipient_emails=(
            self.cc_recipient_emails
            if hasattr(self, "cc_recipient_emails")
            else None
        )
        _bcc_recipient_emails=(
            self.bcc_recipient_emails
            if hasattr(self, "bcc_recipient_emails")
            else None
        )
        _attachment_urls=(
            self.attachment_urls
            if hasattr(self, "attachment_urls")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"recipient_emails={_recipient_emails!s}, "
            f"cc_recipient_emails={_cc_recipient_emails!s}, "
            f"bcc_recipient_emails={_bcc_recipient_emails!s}, "
            f"attachment_urls={_attachment_urls!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
