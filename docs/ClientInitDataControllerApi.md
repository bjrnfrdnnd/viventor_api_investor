# swagger_client.ClientInitDataControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**init_using_get**](ClientInitDataControllerApi.md#init_using_get) | **GET** /api/ia/clients/init-data | init


# **init_using_get**
> ClientInitData init_using_get()

init

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
api_instance = swagger_client.ClientInitDataControllerApi(swagger_client.ApiClient(configuration))

try:
    # init
    api_response = api_instance.init_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientInitDataControllerApi->init_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientInitData**](ClientInitData.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

