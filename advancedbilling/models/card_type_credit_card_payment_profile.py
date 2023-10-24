# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CardTypeCreditCardPaymentProfile(object):

    """Implementation of the 'CardType_Credit Card Payment Profile' enum.

    TODO: type enum description here.

    Attributes:
        VISA: TODO: type description here.
        MASTER: TODO: type description here.
        ELO: TODO: type description here.
        CABAL: TODO: type description here.
        ALELO: TODO: type description here.
        DISCOVER: TODO: type description here.
        AMERICAN_EXPRESS: TODO: type description here.
        NARANJA: TODO: type description here.
        DINERS_CLUB: TODO: type description here.
        JCB: TODO: type description here.
        DANKORT: TODO: type description here.
        MAESTRO: TODO: type description here.
        MAESTRO_NO_LUHN: TODO: type description here.
        FORBRUGSFORENINGEN: TODO: type description here.
        SODEXO: TODO: type description here.
        ALIA: TODO: type description here.
        VR: TODO: type description here.
        UNIONPAY: TODO: type description here.
        CARNET: TODO: type description here.
        CARTES_BANCAIRES: TODO: type description here.
        OLIMPICA: TODO: type description here.
        CREDITEL: TODO: type description here.
        CONFIABLE: TODO: type description here.
        SYNCHRONY: TODO: type description here.
        ROUTEX: TODO: type description here.
        MADA: TODO: type description here.
        BP_PLUS: TODO: type description here.
        PASSCARD: TODO: type description here.
        EDENRED: TODO: type description here.
        ANDA: TODO: type description here.
        TARJETAD: TODO: type description here.
        HIPERCARD: TODO: type description here.
        BOGUS: TODO: type description here.

    """
    _all_values = ['visa', 'master', 'elo', 'cabal', 'alelo', 'discover', 'american_express', 'naranja', 'diners_club', 'jcb', 'dankort', 'maestro', 'maestro_no_luhn', 'forbrugsforeningen', 'sodexo', 'alia', 'vr', 'unionpay', 'carnet', 'cartes_bancaires', 'olimpica', 'creditel', 'confiable', 'synchrony', 'routex', 'mada', 'bp_plus', 'passcard', 'edenred', 'anda', 'tarjeta-d', 'hipercard', 'bogus']
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

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
