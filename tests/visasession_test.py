import unittest
import visa_dps
from visa_dps.VisaSession import VisaSession

username = 'DMO62GRKXC2WH51HRJEB213s8uyurSp3vnvJzGwALxvGSLSLg'
password = 'r4Guxh565P2BIvyK5WZpuX'
cert_file = 'cert.pem'
key_file = 'rosarius.pem'
ssl_ca_cer = 'DigiCertGlobalRootCA.pem'


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_session = VisaSession(username, password, be_noisy=True, use_sandbox=True,
                                 client_cert="../cert.pem", client_key="../rosarius.pem")
        output = my_session.get("/dcas/cardservices/v1/cards/xxxx/cardstatus")
        print(output)


if __name__ == '__main__':
    unittest.main()
