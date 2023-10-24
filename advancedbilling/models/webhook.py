# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Webhook(object):

    """Implementation of the 'Webhook' model.

    TODO: type model description here.

    Attributes:
        event (str): A string describing which event type produced the given
            webhook
        id (int): The unique identifier for the webhooks (unique across all of
            Chargify). This is not changed on a retry/replay of the same
            webhook, so it may be used to avoid duplicate action for the same
            event.
        created_at (str): Timestamp indicating when the webhook was created
        last_error (str): Text describing the status code and/or error from
            the last failed attempt to send the Webhook. When a webhook is
            retried and accepted, this field will be cleared.
        last_error_at (str): Timestamp indicating when the last non-acceptance
            occurred. If a webhook is later resent and accepted, this field
            will be cleared.
        accepted_at (str): Timestamp indicating when the webhook was accepted
            by the merchant endpoint. When a webhook is explicitly replayed by
            the merchant, this value will be cleared until it is accepted
            again.
        last_sent_at (str): Timestamp indicating when the most recent attempt
            was made to send the webhook
        last_sent_url (str): The url that the endpoint was last sent to.
        successful (bool): A boolean flag describing whether the webhook was
            accepted by the webhook endpoint for the most recent attempt.
            (Acceptance is defined by receiving a “200 OK” HTTP response
            within a reasonable timeframe, i.e. 15 seconds)
        body (str): The data sent within the webhook post
        signature (str): The calculated webhook signature
        signature_hmac_sha_256 (str): The calculated HMAC-SHA-256 webhook
            signature

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "event": 'event',
        "id": 'id',
        "created_at": 'created_at',
        "last_error": 'last_error',
        "last_error_at": 'last_error_at',
        "accepted_at": 'accepted_at',
        "last_sent_at": 'last_sent_at',
        "last_sent_url": 'last_sent_url',
        "successful": 'successful',
        "body": 'body',
        "signature": 'signature',
        "signature_hmac_sha_256": 'signature_hmac_sha_256'
    }

    _optionals = [
        'event',
        'id',
        'created_at',
        'last_error',
        'last_error_at',
        'accepted_at',
        'last_sent_at',
        'last_sent_url',
        'successful',
        'body',
        'signature',
        'signature_hmac_sha_256',
    ]

    _nullables = [
        'accepted_at',
    ]

    def __init__(self,
                 event=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 last_error=APIHelper.SKIP,
                 last_error_at=APIHelper.SKIP,
                 accepted_at=APIHelper.SKIP,
                 last_sent_at=APIHelper.SKIP,
                 last_sent_url=APIHelper.SKIP,
                 successful=APIHelper.SKIP,
                 body=APIHelper.SKIP,
                 signature=APIHelper.SKIP,
                 signature_hmac_sha_256=APIHelper.SKIP):
        """Constructor for the Webhook class"""

        # Initialize members of the class
        if event is not APIHelper.SKIP:
            self.event = event 
        if id is not APIHelper.SKIP:
            self.id = id 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if last_error is not APIHelper.SKIP:
            self.last_error = last_error 
        if last_error_at is not APIHelper.SKIP:
            self.last_error_at = last_error_at 
        if accepted_at is not APIHelper.SKIP:
            self.accepted_at = accepted_at 
        if last_sent_at is not APIHelper.SKIP:
            self.last_sent_at = last_sent_at 
        if last_sent_url is not APIHelper.SKIP:
            self.last_sent_url = last_sent_url 
        if successful is not APIHelper.SKIP:
            self.successful = successful 
        if body is not APIHelper.SKIP:
            self.body = body 
        if signature is not APIHelper.SKIP:
            self.signature = signature 
        if signature_hmac_sha_256 is not APIHelper.SKIP:
            self.signature_hmac_sha_256 = signature_hmac_sha_256 

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
        event = dictionary.get("event") if dictionary.get("event") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        last_error = dictionary.get("last_error") if dictionary.get("last_error") else APIHelper.SKIP
        last_error_at = dictionary.get("last_error_at") if dictionary.get("last_error_at") else APIHelper.SKIP
        accepted_at = dictionary.get("accepted_at") if "accepted_at" in dictionary.keys() else APIHelper.SKIP
        last_sent_at = dictionary.get("last_sent_at") if dictionary.get("last_sent_at") else APIHelper.SKIP
        last_sent_url = dictionary.get("last_sent_url") if dictionary.get("last_sent_url") else APIHelper.SKIP
        successful = dictionary.get("successful") if "successful" in dictionary.keys() else APIHelper.SKIP
        body = dictionary.get("body") if dictionary.get("body") else APIHelper.SKIP
        signature = dictionary.get("signature") if dictionary.get("signature") else APIHelper.SKIP
        signature_hmac_sha_256 = dictionary.get("signature_hmac_sha_256") if dictionary.get("signature_hmac_sha_256") else APIHelper.SKIP
        # Return an object of this model
        return cls(event,
                   id,
                   created_at,
                   last_error,
                   last_error_at,
                   accepted_at,
                   last_sent_at,
                   last_sent_url,
                   successful,
                   body,
                   signature,
                   signature_hmac_sha_256)
