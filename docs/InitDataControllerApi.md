# swagger_client.InitDataControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_init_data_using_get**](InitDataControllerApi.md#get_init_data_using_get) | **GET** /api/ia/init-data | getInitData


# **get_init_data_using_get**
> InitDataModel get_init_data_using_get()

getInitData

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
api_instance = swagger_client.InitDataControllerApi(swagger_client.ApiClient(configuration))

try:
    # getInitData
    api_response = api_instance.get_init_data_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InitDataControllerApi->get_init_data_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InitDataModel**](InitDataModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

