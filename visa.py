from __future__ import print_function
import time
from src.apis.card_services_api import CardServicesApi
from src.configuration import Configuration

from card_services_api.src.rest import ApiException

config = Configuration()
# Uncomment this block to enable proxy
# config.proxy_url = 'PROXY_URL'

# Configure HTTP basic authorization: basicAuth
config.username = 'DMO62GRKXC2WH51HRJEB213s8uyurSp3vnvJzGwALxvGSLSLg'
config.password = 'r4Guxh565P2BIvyK5WZpuX'
config.cert_file = 'cert.pem'
config.key_file = 'rosarius.pem'
config.ssl_ca_cer = 'DigiCertGlobalRootCA.pem'

# Unblock this block to configure MLE credentials
# config.api_key['keyId'] = 'YOUR_KEY_ID'
# config.encryption_public_key_path = 'ABSOLUTE_PATH_TO_MLE_CERT_FILE'
# config.decryption_private_key_path = 'ABSOLUTE_PATH_TO_MLE_KEY_FILE'

# create an instance of the API class
api_instance = CardServicesApi()

# Set all the required parameters in the getcard_status. Look at the documentation for further clarification.
card_id = '4883836336860016'
pan = {"cardIdModel": [
    {
        "pan": "4883836336860016",
        "lookUpBalances": True
    },
    {
        "pan": "4169334953890037",
        "lookUpBalances": True
    }
    ]}


try:
    api_response = api_instance.postcreate_card_identifiers(pan)
    print(api_response)
except ApiException as e:
    print("Exception when calling postcreate_card_identifiers %s\n" % e)

print(api_response)
exit(1)
try:
    api_response = api_instance.getcard_status(card_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling CardServicesApi->getcard_status: %s\n" % e)
