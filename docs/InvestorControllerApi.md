# swagger_client.InvestorControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_using_get7**](InvestorControllerApi.md#get_using_get7) | **GET** /api/ia/investor | get


# **get_using_get7**
> InvestorInfo get_using_get7()

get

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
api_instance = swagger_client.InvestorControllerApi(swagger_client.ApiClient(configuration))

try:
    # get
    api_response = api_instance.get_using_get7()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestorControllerApi->get_using_get7: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InvestorInfo**](InvestorInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

