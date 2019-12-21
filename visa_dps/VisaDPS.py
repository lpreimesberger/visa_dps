# -*- coding: utf-8 -*-
"""
Visa DPS Library
:copyright: (c) 2019 by Lee Preimesberger / Caprica LLC
:license: MIT, see LICENSE for more details.
"""
import json
import logging
import base64
from visa_dps.VisaSession import VisaSession
from datetime import datetime
from typing import List


class Account:
    account_alias_id: str
    account_number: str
    account_type_code: str
    account_type_description: None
    institution_id: None
    account_indicator_code: None
    account_indicator_description: None
    balances: None
    is_funding: bool
    is_funding_computed: bool
    account_opened_date: datetime

    def __init__(self, account_alias_id: str, account_number: str, account_type_code: str, account_type_description: None, institution_id: None, account_indicator_code: None, account_indicator_description: None, balances: None, is_funding: bool, is_funding_computed: bool, account_opened_date: datetime) -> None:
        self.account_alias_id = account_alias_id
        self.account_number = account_number
        self.account_type_code = account_type_code
        self.account_type_description = account_type_description
        self.institution_id = institution_id
        self.account_indicator_code = account_indicator_code
        self.account_indicator_description = account_indicator_description
        self.balances = balances
        self.is_funding = is_funding
        self.is_funding_computed = is_funding_computed
        self.account_opened_date = account_opened_date


class Card:
    card_id: str
    pan: str
    accounts: List[Account]

    def __init__(self, card_id: str, pan: str, accounts: List[Account]) -> None:
        self.card_id = card_id
        self.pan = pan
        self.accounts = accounts


def dps_get_balances( session: VisaSession, card_id: str):
    """Get balances for given card_id

       Args:
            session: initialized VisaSession
            card_id: card_id to get info on, this is _NOT_ a card number (4242 4242 4242 4242)

        Returns:
            Account info or {}

        Raises:
            None    """
    output = session.get("/dcas/cardservices/v1/cards/%s/accounts?lookUpBalances=true" % card_id)
    if output.status_code is not 200:
        print("Failed to get balance info for %s" % card_id)
        return {}
    # this is a Card object above that is wrapped in another junk object
    account = json.loads(output.text)
    try:
        return account['resource']['accounts'][0]
    except KeyError:
        return {}


def dps_cardstatus(session: VisaSession, card_id: str):
    """Get status for given card_id

       Args:
            session: initialized VisaSession
            card_id: card_id to get info on, this is _NOT_ a card number (4242 4242 4242 4242)

        Returns:
            Object with some opaque info - the resource.cardStatus is 'optional' and is an int?   no idea what it means

        Raises:
            None    """
    output = session.get("/dcas/cardservices/v1/cards/%s/cardstatus" % card_id)
    return output


def dps_getcardid(session: VisaSession, card_number: str):
    """Get card_id for given card number

       Args:
            session: initialized VisaSession
            card_number: card number (4242 4242 4242 4242)

        Returns:
            Text card_id if available, "" else.  API allows multiple but that's weird.

        Raises:
            None    """
    pan = {"cardIdModel": [
        {
            "pan": card_number,
            "lookUpBalances": True
        },
    ]}
    output = session.post("/dcas/cardservices/v1/cards", pan)
    if output.status_code is not 200:
        print("Whoops")
        print(output)
        return ""
    # this is a Card object above that is wrapped in another junk object
    card = json.loads(output.text)
    try:
        return card['resource']['cards'][0]['cardId']
    except KeyError:
        return ""

