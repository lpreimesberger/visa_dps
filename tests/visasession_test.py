# -*- coding: utf-8 -*-
"""
Visa DPS Library
:copyright: (c) 2019 by Lee Preimesberger / Caprica LLC
:license: MIT, see LICENSE for more details.
"""
import unittest
from visa_dps.VisaDPS import *
from visa_dps.VisaSession import VisaSession
from config import Config


class MyTestCase(unittest.TestCase):
    def test_cardstatus_404(self):
        print("Expect a 404")
        my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                 client_cert="../cert.pem", client_key="../rosarius.pem")
        output = dps_cardstatus(my_session, "not_a_key")
        print(output)
        self.assertTrue(output.status_code, 404)

    def test_cardstatus_(self):
        print("Expect a 200")
        my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                 client_cert="../cert.pem", client_key="../rosarius.pem")
        output = dps_cardstatus(my_session, "7a353971-l4uo-9877-algd-lz1fe25349i9")
        print(output)
        self.assertTrue(output.status_code, 200)


    def test_dps_get_card_details_(self):
        print("Expect a 200")
        my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                 client_cert="../cert.pem", client_key="../rosarius.pem")
        output = dps_get_card_details(my_session, "7a353971-l4uo-9877-algd-lz1fe25349i9")
        print(output)
        self.assertIsNot(output, {})

    def test_getbalance_XXXXXXXXXXXX0022(self):
        print("Expect a 200")
        my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                 client_cert="../cert.pem", client_key="../rosarius.pem")
        output = dps_get_balances(my_session, "7a353971-l4uo-9877-algd-bp0df3321ly2")
        print(output)
        self.assertIsNot(output, {})


    def test_gettransactions(self):
        print("Expect a 200")
        my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                 client_cert="../cert.pem", client_key="../rosarius.pem")
        output = dps_get_transactions(my_session, "7a353971-l4uo-9877-algd-bp0df3321ly2")
        print(output)
        self.assertIsNot(output, [])

    """
        def test_getbalance_XXXXXXXXXXXX0037(self):
            print("Expect a 200")
            my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                     client_cert="../cert.pem", client_key="../rosarius.pem")
            output = dps_get_balances(my_session, "7a353971-l4uo-9877-algd-lz1fe25349i9")
            print(output)
            self.assertIsNot(output, {})


        def test_getbalance_XXXXXXXXXXXX0046(self):
            print("Expect a 200")
            my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                     client_cert="../cert.pem", client_key="../rosarius.pem")
            output = dps_get_balances(my_session, "7a353971-l4uo-9877-algd-bd3zl43218j9")
            print(output)
            self.assertIsNot(output, {})


        def test_getbalance_XXXXXXXXXXXX0016(self):
            print("Expect a 200")
            my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                     client_cert="../cert.pem", client_key="../rosarius.pem")
            output = dps_get_balances(my_session, "8d212293-c6bc-4738-afaf-bc0ae5456df5")
            print(output)
            self.assertIsNot(output, {})
    """

    def test_getcardid_4883836336860016(self):
        print("Expect a 200 and a valid string of some sort")
        my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                 client_cert="../cert.pem", client_key="../rosarius.pem")
        output = dps_getcardid(my_session, "4883836336860016")
        print(output)
        self.assertIsNot(output, "")


    """
        def test_getcardid_4169334953890037(self):
            print("Expect a 200 and a valid string of some sort")
            my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                     client_cert="../cert.pem", client_key="../rosarius.pem")
            output = dps_getcardid(my_session, "4169334953890037")
            print(output)
            self.assertIsNot(output, "")


        def test_getcardid_4105837613490022(self):
            print("Expect a 200 and a valid string of some sort")
            my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                     client_cert="../cert.pem", client_key="../rosarius.pem")
            output = dps_getcardid(my_session, "4105837613490022")
            print(output)
            self.assertIsNot(output, "")


        def test_getcardid_4386624808860046(self):
            print("Expect a 200 and a valid string of some sort")
            my_session = VisaSession(Config.username, Config.password, be_noisy=True, use_sandbox=True,
                                     client_cert="../cert.pem", client_key="../rosarius.pem")
            output = dps_getcardid(my_session, "4386624808860046")
            print(output)
            self.assertIsNot(output, "")
    """

if __name__ == '__main__':
    unittest.main()
