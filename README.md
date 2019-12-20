# Card Services API
Manage cardholder’s card and account information, notification settings, and balance information.

- API version: 1.0
- Package version: 1.0.0

For more information, please visit [https://developer.visa.com/](https://developer.visa.com/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

To install by pip, execute the below command.

```sh
pip install -r requirements.txt
```
(you may need to run `pip` with root permission: `sudo pip install -r requirements.txt`)

Then import the package:
```python
from src.apis.card_services_api import CardServicesApi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
from src.apis.card_services_api import CardServicesApi
```
## Tests
- Edit the file **globlaConfig.py** to set the fields shown below. Please refer the [Getting Started Guide](https://developer.visa.com/vdpguide#get-started-overview) to get the credentials.

```python
# For mutual auth
userName = 'your_username'
password = 'your_password'
certificatePath = '/absolute/path/to/cert.pem'
privateKeyPath = '/absolute/path/to/key_xxxx.pem'
caCertPath = '/absolute/path/to/cacert.pem'

# For MLE also set the following fields
mleKeyId = 'your_keyId'
encryptionPublicKeyPath = 'your_encryption_public_key_path'
self.decryptionPrivateKeyPath = 'your_decryption_private_key_path'

# For x-pay token
apiKey = 'your_apiKey'
sharedSecret = 'your_shared_secret'

# For Proxy
proxyUrl = 'proxy_url'

```
To run the unit tests:
- Note: The data in the unit tests are just placeholders. Please refer the [Create Project Guide](https://developer.visa.com/pages/working-with-visa-apis/create-project) to get the test data
```
nosetests --nocapture
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
from src.apis.card_services_api import CardServicesApi
from src.configuration import Configuration

config = Configuration()
# Uncomment this block to enable proxy
# config.proxy_url = 'PROXY_URL'

# Configure HTTP basic authorization: basicAuth
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'
config.cert_file = 'ABSOLUTE_PATH_TO_CERT_FILE'
config.key_file = 'ABSOLUTE_PATH_TO_KEY_FILE'
config.ssl_ca_cert = 'ABSOLUTE_PATH_TO_CA_CERT_FILE'

# Unblock this block to configure MLE credentials
# config.api_key['keyId'] = 'YOUR_KEY_ID'
# config.encryption_public_key_path = 'ABSOLUTE_PATH_TO_MLE_CERT_FILE'
# config.decryption_private_key_path = 'ABSOLUTE_PATH_TO_MLE_KEY_FILE'

# create an instance of the API class
api_instance = CardServicesApi()

# Set all the required parameters in the getcard_status. Look at the documentation for further clarification.
card_id = 'card_id_example' # str | CardId unique Indentifier

try:
    api_response = api_instance.getcard_status(card_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardServicesApi->getcard_status: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://sandbox.api.visa.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CardServicesApi* | [**getcard_status**](docs/CardServicesApi.md#getcard_status) | **GET** /dcas/cardservices/v1/cards/{cardId}/cardstatus | 
*CardServicesApi* | [**getget_account_details**](docs/CardServicesApi.md#getget_account_details) | **GET** /dcas/cardservices/v1/cards/{cardId}/accounts?lookUpBalances&#x3D;{lookUpBalances} | 
*CardServicesApi* | [**getget_card_by_alias**](docs/CardServicesApi.md#getget_card_by_alias) | **GET** /dcas/cardservices/v1/cards/{cardId} | 
*CardServicesApi* | [**getget_cardholder_details**](docs/CardServicesApi.md#getget_cardholder_details) | **GET** /dcas/cardservices/v1/cards/{cardId}/cardholderdetails | 
*CardServicesApi* | [**getget_notification_settings**](docs/CardServicesApi.md#getget_notification_settings) | **GET** /dcas/cardservices/v1/cards/{cardId}/notifications | 
*CardServicesApi* | [**getget_single_account_details**](docs/CardServicesApi.md#getget_single_account_details) | **GET** /dcas/cardservices/v1/accounts/{accountAliasId}?lookUpBalances&#x3D;{lookUpBalances} | 
*CardServicesApi* | [**getget_transaction_history**](docs/CardServicesApi.md#getget_transaction_history) | **GET** /dcas/cardservices/v1/cards/{cardId}/transactions | 
*CardServicesApi* | [**getnotification_details**](docs/CardServicesApi.md#getnotification_details) | **GET** /dcas/cardservices/v1/cards/{cardId}/notifications/settings | 
*CardServicesApi* | [**getnotification_subscriptions**](docs/CardServicesApi.md#getnotification_subscriptions) | **GET** /dcas/cardservices/v1/cards/{cardId}/notifications/subscriptions | 
*CardServicesApi* | [**postcard_activation**](docs/CardServicesApi.md#postcard_activation) | **POST** /dcas/cardservices/v1/cardservices/v1/cards/{cardId}/cardactivation | 
*CardServicesApi* | [**postcard_verification**](docs/CardServicesApi.md#postcard_verification) | **POST** /dcas/cardservices/v1/cards/{cardId}/cardverification | 
*CardServicesApi* | [**postcreate_card_identifiers**](docs/CardServicesApi.md#postcreate_card_identifiers) | **POST** /dcas/cardservices/v1/cards | 
*CardServicesApi* | [**postget_list_of_fund_transfer_accounts**](docs/CardServicesApi.md#postget_list_of_fund_transfer_accounts) | **POST** /dcas/cardservices/v1/cards/{cardId}/fundstransfers/requirementsinquiry | 
*CardServicesApi* | [**postload_funds_to_card**](docs/CardServicesApi.md#postload_funds_to_card) | **POST** /dcas/cardservices/v1/cards/{cardId}/cardloads | 
*CardServicesApi* | [**postretrieve_requirements_to_load_funds**](docs/CardServicesApi.md#postretrieve_requirements_to_load_funds) | **POST** /dcas/cardservices/v1/cards/{cardId}/cardloads/requirementsinquiry | 
*CardServicesApi* | [**posttransfer_funds_to_account**](docs/CardServicesApi.md#posttransfer_funds_to_account) | **POST** /dcas/cardservices/v1/cards/{cardId}/fundstransfers | 
*CardServicesApi* | [**postverify_one_time_passcode**](docs/CardServicesApi.md#postverify_one_time_passcode) | **POST** /dcas/cardservices/v1/cards/{cardId}/notifications/otpverification | 
*CardServicesApi* | [**putcard_status**](docs/CardServicesApi.md#putcard_status) | **PUT** /dcas/cardservices/v1/cards/{cardId}/cardstatus | 
*CardServicesApi* | [**putnotification_details**](docs/CardServicesApi.md#putnotification_details) | **PUT** /dcas/cardservices/v1/cards/{cardId}/notifications/settings | 
*CardServicesApi* | [**putnotification_subscriptions**](docs/CardServicesApi.md#putnotification_subscriptions) | **PUT** /dcas/cardservices/v1/cards/{cardId}/notifications/subscriptions | 


## Documentation For Models

 - [Accounts](docs/Accounts.md)
 - [Address](docs/Address.md)
 - [AmountDue](docs/AmountDue.md)
 - [AmountOwing](docs/AmountOwing.md)
 - [Available](docs/Available.md)
 - [AvailableCredit](docs/AvailableCredit.md)
 - [Balances](docs/Balances.md)
 - [BirthDateToken](docs/BirthDateToken.md)
 - [CardActivationpostPayload](docs/CardActivationpostPayload.md)
 - [CardActivationpostResponse](docs/CardActivationpostResponse.md)
 - [CardIdModel](docs/CardIdModel.md)
 - [CardStatusgetResponse](docs/CardStatusgetResponse.md)
 - [CardStatusputPayload](docs/CardStatusputPayload.md)
 - [CardStatusputResponse](docs/CardStatusputResponse.md)
 - [CardVerificationpostPayload](docs/CardVerificationpostPayload.md)
 - [CardVerificationpostResponse](docs/CardVerificationpostResponse.md)
 - [CardholderLowBalanceAmount](docs/CardholderLowBalanceAmount.md)
 - [Cards](docs/Cards.md)
 - [CreateCardIdentifierspostPayload](docs/CreateCardIdentifierspostPayload.md)
 - [CreateCardIdentifierspostResponse](docs/CreateCardIdentifierspostResponse.md)
 - [CreditLine](docs/CreditLine.md)
 - [DriversLicenseToken](docs/DriversLicenseToken.md)
 - [ExpirationDate](docs/ExpirationDate.md)
 - [FeeAmount](docs/FeeAmount.md)
 - [GetAccountDetailsgetResponse](docs/GetAccountDetailsgetResponse.md)
 - [GetCardByAliasgetResponse](docs/GetCardByAliasgetResponse.md)
 - [GetCardholderDetailsgetResponse](docs/GetCardholderDetailsgetResponse.md)
 - [GetListOfFundTransferAccountspostPayload](docs/GetListOfFundTransferAccountspostPayload.md)
 - [GetListOfFundTransferAccountspostResponse](docs/GetListOfFundTransferAccountspostResponse.md)
 - [GetNotificationSettingsgetResponse](docs/GetNotificationSettingsgetResponse.md)
 - [GetSingleAccountDetailsgetResponse](docs/GetSingleAccountDetailsgetResponse.md)
 - [GetTransactionHistorygetResponse](docs/GetTransactionHistorygetResponse.md)
 - [ImmediateLoad](docs/ImmediateLoad.md)
 - [Ledger](docs/Ledger.md)
 - [LoadAmount](docs/LoadAmount.md)
 - [LoadFundsToCardpostPayload](docs/LoadFundsToCardpostPayload.md)
 - [LoadFundsToCardpostResponse](docs/LoadFundsToCardpostResponse.md)
 - [MothersMaidenNameToken](docs/MothersMaidenNameToken.md)
 - [NotificationDetailsgetResponse](docs/NotificationDetailsgetResponse.md)
 - [NotificationDetailsputPayload](docs/NotificationDetailsputPayload.md)
 - [NotificationDetailsputResponse](docs/NotificationDetailsputResponse.md)
 - [NotificationSubscriptionsgetResponse](docs/NotificationSubscriptionsgetResponse.md)
 - [NotificationSubscriptionsputPayload](docs/NotificationSubscriptionsputPayload.md)
 - [NotificationSubscriptionsputResponse](docs/NotificationSubscriptionsputResponse.md)
 - [PhoneNumberToken](docs/PhoneNumberToken.md)
 - [Resource](docs/Resource.md)
 - [RetrieveRequirementsToLoadFundspostPayload](docs/RetrieveRequirementsToLoadFundspostPayload.md)
 - [RetrieveRequirementsToLoadFundspostResponse](docs/RetrieveRequirementsToLoadFundspostResponse.md)
 - [SsnToken](docs/SsnToken.md)
 - [Subscriptions](docs/Subscriptions.md)
 - [TransferAmount](docs/TransferAmount.md)
 - [TransferFundsToAccountpostPayload](docs/TransferFundsToAccountpostPayload.md)
 - [TransferFundsToAccountpostResponse](docs/TransferFundsToAccountpostResponse.md)
 - [VerifyOneTimePasscodepostPayload](docs/VerifyOneTimePasscodepostPayload.md)
 - [VerifyOneTimePasscodepostResponse](docs/VerifyOneTimePasscodepostResponse.md)



##Authors
**Visa Developer Platform**
See also the list of [contributors](https://github.com/visa/java-sample-code/graphs/contributors) who participated in this project.

##License
**© Copyright 2018 Visa. All Rights Reserved.**

*NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of
and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property
rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.*

*By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy (developer.visa.com/privacy).
In addition, all permissible uses of the Software must be in support of Visa products, programs and services provided
through the Visa Developer Program (VDP) platform only (developer.visa.com). **THE SOFTWARE AND ANY ASSOCIATED
INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL FAULTS” BASIS WITHOUT WARRANTY OR
CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.** All brand names are the property of their respective owners, used for identification purposes only, and do not imply
product endorsement or affiliation with Visa. Any links to third party sites are for your information only and equally
do not constitute a Visa endorsement. Visa has no insight into and control over third party content and code and disclaims
all liability for any such components, including continued availability and functionality. Benefits depend on implementation
details and business factors and coding steps shown are exemplary only and do not reflect all necessary elements for the
described capabilities. Capabilities and features are subject to Visa’s terms and conditions and may require development,
implementation and resources by you based on your business and operational details. Please refer to the specific
API documentation for details on the requirements, eligibility and geographic availability.*

*This Software includes programs, concepts and details under continuing development by Visa. Any Visa features,
functionality, implementation, branding, and schedules may be amended, updated or canceled at Visa’s discretion.
The timing of widespread availability of programs and functionality is also subject to a number of factors outside Visa’s control,
including but not limited to deployment of necessary infrastructure by issuers, acquirers, merchants and mobile device manufacturers.*