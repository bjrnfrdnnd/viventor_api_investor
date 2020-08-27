# swagger_client.AgreementControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_agreements_using_post**](AgreementControllerApi.md#update_agreements_using_post) | **POST** /api/ia/clients/agreements | updateAgreements


# **update_agreements_using_post**
> update_agreements_using_post(agreement_model)

updateAgreements

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AgreementControllerApi(swagger_client.ApiClient(configuration))
agreement_model = swagger_client.AgreementModel() # AgreementModel | agreementModel

try:
    # updateAgreements
    api_instance.update_agreements_using_post(agreement_model)
except ApiException as e:
    print("Exception when calling AgreementControllerApi->update_agreements_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agreement_model** | [**AgreementModel**](AgreementModel.md)| agreementModel | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

