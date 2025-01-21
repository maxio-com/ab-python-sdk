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
        VISA: The enum member of type str.
        MASTER: The enum member of type str.
        ELO: The enum member of type str.
        CABAL: The enum member of type str.
        ALELO: The enum member of type str.
        DISCOVER: The enum member of type str.
        AMERICAN_EXPRESS: The enum member of type str.
        NARANJA: The enum member of type str.
        DINERS_CLUB: The enum member of type str.
        JCB: The enum member of type str.
        DANKORT: The enum member of type str.
        MAESTRO: The enum member of type str.
        MAESTRO_NO_LUHN: The enum member of type str.
        FORBRUGSFORENINGEN: The enum member of type str.
        SODEXO: The enum member of type str.
        ALIA: The enum member of type str.
        VR: The enum member of type str.
        UNIONPAY: The enum member of type str.
        CARNET: The enum member of type str.
        CARTES_BANCAIRES: The enum member of type str.
        OLIMPICA: The enum member of type str.
        CREDITEL: The enum member of type str.
        CONFIABLE: The enum member of type str.
        SYNCHRONY: The enum member of type str.
        ROUTEX: The enum member of type str.
        MADA: The enum member of type str.
        BP_PLUS: The enum member of type str.
        PASSCARD: The enum member of type str.
        EDENRED: The enum member of type str.
        ANDA: The enum member of type str.
        TARJETAD: The enum member of type str.
        HIPERCARD: The enum member of type str.
        BOGUS: The enum member of type str.
        SWITCH: The enum member of type str.
        SOLO: The enum member of type str.
        LASER: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['visa', 'master', 'elo', 'cabal', 'alelo', 'discover', 'american_express', 'naranja', 'diners_club', 'jcb', 'dankort', 'maestro', 'maestro_no_luhn', 'forbrugsforeningen', 'sodexo', 'alia', 'vr', 'unionpay', 'carnet', 'cartes_bancaires', 'olimpica', 'creditel', 'confiable', 'synchrony', 'routex', 'mada', 'bp_plus', 'passcard', 'edenred', 'anda', 'tarjeta-d', 'hipercard', 'bogus', 'switch', 'solo', 'laser']
    VISA = 'visa'

    MASTER = 'master'

    ELO = 'elo'

    CABAL = 'cabal'

    ALELO = 'alelo'

    DISCOVER = 'discover'

    AMERICAN_EXPRESS = 'american_express'

    NARANJA = 'naranja'

    DINERS_CLUB = 'diners_club'

    JCB = 'jcb'

    DANKORT = 'dankort'

    MAESTRO = 'maestro'

    MAESTRO_NO_LUHN = 'maestro_no_luhn'

    FORBRUGSFORENINGEN = 'forbrugsforeningen'

    SODEXO = 'sodexo'

    ALIA = 'alia'

    VR = 'vr'

    UNIONPAY = 'unionpay'

    CARNET = 'carnet'

    CARTES_BANCAIRES = 'cartes_bancaires'

    OLIMPICA = 'olimpica'

    CREDITEL = 'creditel'

    CONFIABLE = 'confiable'

    SYNCHRONY = 'synchrony'

    ROUTEX = 'routex'

    MADA = 'mada'

    BP_PLUS = 'bp_plus'

    PASSCARD = 'passcard'

    EDENRED = 'edenred'

    ANDA = 'anda'

    TARJETAD = 'tarjeta-d'

    HIPERCARD = 'hipercard'

    BOGUS = 'bogus'

    SWITCH = 'switch'

    SOLO = 'solo'

    LASER = 'laser'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   