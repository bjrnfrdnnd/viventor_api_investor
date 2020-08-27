# swagger_client.LoanConfigurationControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration_using_get**](LoanConfigurationControllerApi.md#get_configuration_using_get) | **GET** /api/ia/loan-configuration | getConfiguration


# **get_configuration_using_get**
> LoanConfigurationModel get_configuration_using_get(groups=groups)

getConfiguration

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
api_instance = swagger_client.LoanConfigurationControllerApi(swagger_client.ApiClient(configuration))
groups = ['groups_example'] # list[str] | groups (optional)

try:
    # getConfiguration
    api_response = api_instance.get_configuration_using_get(groups=groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanConfigurationControllerApi->get_configuration_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups** | [**list[str]**](str.md)| groups | [optional] 

### Return type

[**LoanConfigurationModel**](LoanConfigurationModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

