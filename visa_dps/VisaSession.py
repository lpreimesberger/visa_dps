# -*- coding: utf-8 -*-
"""
Visa DPS Library
:copyright: (c) 2019 by Lee Preimesberger / Caprica LLC
:license: MIT, see LICENSE for more details.
"""
import logging
import base64
import requests


class VisaSession:
    user_name = ""
    user_password = ""
    api_server = "https://sandbox.api.visa.com"
    noisy = False
    encoded_auth = ""
    client_cert = ""
    client_key = ""
    headers = {}

    def __init__(self, user_name, user_password, use_sandbox=False, be_noisy=False, client_cert="", client_key=""):
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
                        'Content-Type': 'application/json', 'User-Agent': 'VDP_SampleCode_Python'}

    def get(self, url):
        if self.noisy:
            print("<< %s%s" % (self.api_server, url))
            print("<< auth %s:%s" % (self.user_name, self.user_password))
        return_value = requests.get(self.api_server + url, headers=self.headers, cert=(self.client_cert, self.client_key))
        if self.noisy:
            print("<<", return_value.request.headers)
            print(">>", return_value.url)
            print(">>", return_value.content)
        return return_value
