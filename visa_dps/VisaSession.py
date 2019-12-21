# -*- coding: utf-8 -*-
"""
Visa DPS Library
:copyright: (c) 2019 by Lee Preimesberger / Caprica LLC
:license: MIT, see LICENSE for more details.
"""
import logging
import base64
import requests
import json


class VisaSession:
    """Low level wrapper for the REST calls.

    """
    user_name = ""
    user_password = ""
    api_server = "https://sandbox.api.visa.com"
    noisy = False
    encoded_auth = ""
    client_cert = ""
    client_key = ""
    headers = {}

    def __init__(self, user_name, user_password, use_sandbox=False, be_noisy=False, client_cert="", client_key=""):
        """Init the connection.

        Args:
            user_name: Project name from the dev portal
            user_password: Project password from the dev portal
            use_sandbox: Optional - True for sandbox, false for production.   Defaults sandbox.
            be_noisy: Optional - extremely verbose stdout, defaults False
            client_cert: cert.pem from your set up.   Make sure you don't check this in :)
            client_key: client PEM you create.   Also don't check it in.

        Returns:
            Object to use with helpers to call the API

        Raises:
            None
        """
        self.user_name = user_name
        self.user_password = user_password
        self.noisy = be_noisy
        self.client_cert = client_cert
        self.client_key = client_key
        if be_noisy:
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True
        if use_sandbox is False:
            print("Not implemented yet - switch to production")
        self.encoded_auth = base64.b64encode(bytes("%s:%s" % (user_name, user_password), "utf-8")).decode("utf-8")
        self.headers = {"Authorization": "Basic " + self.encoded_auth,
                        'Content-Type': 'application/json',
                        'User-Agent': 'https://github.com/lpreimesberger/visa_dps'
                        }

    def get(self, url):
        """Handles GET to Visa backend to the selected API endpoint (api_server).

        Args:
            url: URL to call - built up by helpers

        Returns:
            requests object with the full headers, data, etc.  handlers parse and handle

        Raises:
            None
        """
        if self.noisy:
            print("<< GET %s%s" % (self.api_server, url))
            print("<< auth %s:%s" % (self.user_name, self.user_password))
        return_value = requests.get(self.api_server + url, headers=self.headers,
                                    cert=(self.client_cert, self.client_key))
        if self.noisy:
            print("<<", return_value.request.headers)
            print(">>", return_value.url)
            print(">>", return_value.content)
        return return_value

    def post(self, url, payload):
        """Handles POST to Visa backend to the selected API endpoint (api_server).
        Note that the remote end isn't smart enough to really handle a json payload in spite of
        the headers - force to utf-8

        Args:
            url: URL to call - built up by helpers
            payload: POST payload in Object form

        Returns:
            requests object with the full headers, data, etc.  handlers parse and handle

        Raises:
            None
        """
        if self.noisy:
            print("<< POST %s%s" % (self.api_server, url))
            print("<< auth %s:%s" % (self.user_name, self.user_password))
        # the remote side is expecting a byte string json payload (?)
        return_value = requests.post(self.api_server + url,
                                     data=json.dumps(payload),
                                     headers=self.headers,
                                     cert=(self.client_cert, self.client_key))
        if self.noisy:
            print("<<", return_value.request.headers)
            print(">>", return_value.url)
            print(">>", return_value.content)
        return return_value
