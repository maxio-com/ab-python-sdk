# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CardType(object):

    """Implementation of the 'Card Type' enum.

    The type of card used.

    Attributes:
        BOGUS: TODO: type description here.
        VISA: TODO: type description here.
        MASTER: TODO: type description here.
        DISCOVER: TODO: type description here.
        AMERICAN_EXPRESS: TODO: type description here.
        DINERS_CLUB: TODO: type description here.
        JCB: TODO: type description here.
        SWITCH: TODO: type description here.
        SOLO: TODO: type description here.
        DANKORT: TODO: type description here.
        MAESTRO: TODO: type description here.
        LASER: TODO: type description here.
        FORBRUGSFORENINGEN: TODO: type description here.

    """
    _all_values = ['bogus', 'visa', 'master', 'discover', 'american_express', 'diners_club', 'jcb', 'switch', 'solo', 'dankort', 'maestro', 'laser', 'forbrugsforeningen']
    BOGUS = 'bogus'

    VISA = 'visa'

    MASTER = 'master'

    DISCOVER = 'discover'

    AMERICAN_EXPRESS = 'american_express'

    DINERS_CLUB = 'diners_club'

    JCB = 'jcb'

    SWITCH = 'switch'

    SOLO = 'solo'

    DANKORT = 'dankort'

    MAESTRO = 'maestro'

    LASER = 'laser'

    FORBRUGSFORENINGEN = 'forbrugsforeningen'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
