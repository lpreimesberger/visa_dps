# -*- coding: utf-8 -*-
"""
Visa DPS Library
:copyright: (c) 2019 by Lee Preimesberger / Caprica LLC
:license: MIT, see LICENSE for more details.
"""
import json
import logging
import base64
from requests import Response
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


def _unpack_account(output: Response):
    """Internal function to unpack the struct returned by most GET calls for accounts

       Args:
            output: Response from VisaSession

        Returns:
            Account info or {}

        Raises:
            None    """
    if output.status_code is not 200:
        print("Failed %s" % output.url)
        return {}
    # this is a Card object above that is wrapped in another junk object
    account = json.loads(output.text)
    try:
        return account['resource']['accounts'][0]
    except KeyError:
        return {}


def dps_get_balances(session: VisaSession, card_id: str):
    """Get balances for given card_id

       Args:
            session: initialized VisaSession
            card_id: card_id to get info on, this is _NOT_ a card number (4242 4242 4242 4242)

        Returns:
            Account info or {}

        Raises:
            None    """
    return _unpack_account(session.get("/dcas/cardservices/v1/cards/%s/accounts?lookUpBalances=true" % card_id))


def dps_get_card_details(session: VisaSession, card_id: str):
    """Get details for given card_id

       Args:
            session: initialized VisaSession
            card_id: card_id to get info on, this is _NOT_ a card number (4242 4242 4242 4242)

        Returns:
            Account info or {}

        Raises:
            None    """
    url_packed = "/dcas/cardservices/v1/cards/%s" % card_id
    return _unpack_account(session.get(url_packed))


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


def dps_set_status(session: VisaSession, card_id: str, active_state: bool):
    """Documentation is crummy for this - Active to enable, Inactive to not?

       Args:
            session: initialized VisaSession
            card_id: card id from mapping
            active_state: turn off or on

        Returns:
            Text card_id if available, "" else.  API allows multiple but that's weird.

        Raises:
            None    """
    mode = "Active"
    if active_state is not True:
        mode = "Inactive"
    pan = {
            "cardStatus": mode
        }

    output = session.post("/dcas/cardservices/v1/cards/%s/cardstatus" % card_id, pan)
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


def dps_get_transactions(session: VisaSession, card_id: str, page=None, rows_on_page=10, alias_id=None):
    """Get transactions for the card (slow, talky)

       Args:
            session: initialized VisaSession
            card_id: card id from mapping function
            page: page of results
            rows_on_page: results per page (default 10)
            alias_id: card alias for subquery only

        Returns:
            array of Transactions or []

        Raises:
            None    """
    url_text = "/dcas/cardservices/v1/cards/%s/transactions?rowsOnPage=%s" % (card_id, rows_on_page)
    if page is not None:
        url_text = url_text + "&indexRow=" + page
    if alias_id is not None:
        url_text = url_text + "&accountAliasId=" + alias_id
    output = session.get(url_text)
    if output.status_code is not 200:
        print("Whoops")
        print(output)
        return []
    # this is a Card object above that is wrapped in another junk object
    card = json.loads(output.text)
    try:
        return card['resource']['transactions']
    except KeyError:
        return []


# i dont need these - if anyone else really wants we can do.  mobile already know who they are
# not implementing https://sandbox.api.visa.com/dcas/cardservices/v1/cards/{cardId}/cardverification
# not implementing https://sandbox.api.visa.com/dcas/cardservices/v1/cards/{cardId}/cardholderdetails
# doesnt seem useful (dont understand use case - issuers?)
# https://sandbox.api.visa.com/dcas/cardservices/v1/cards/{cardId}/cardholderdetails
# https://sandbox.api.visa.com/dcas/cardservices/v1/cards/{cardId}/notifications/otpverification
