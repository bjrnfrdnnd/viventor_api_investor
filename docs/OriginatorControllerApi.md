# swagger_client.OriginatorControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_originators_credentials_using_get**](OriginatorControllerApi.md#get_originators_credentials_using_get) | **GET** /api/ia/originators/credentials | getOriginatorsCredentials
[**get_originators_using_get**](OriginatorControllerApi.md#get_originators_using_get) | **GET** /api/ia/originators | getOriginators
[**investor_using_get**](OriginatorControllerApi.md#investor_using_get) | **GET** /api/ia/originators/validate-account | investor


# **get_originators_credentials_using_get**
> list[OriginatorCredentialsModel] get_originators_credentials_using_get()

getOriginatorsCredentials

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
api_instance = swagger_client.OriginatorControllerApi(swagger_client.ApiClient(configuration))

try:
    # getOriginatorsCredentials
    api_response = api_instance.get_originators_credentials_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OriginatorControllerApi->get_originators_credentials_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OriginatorCredentialsModel]**](OriginatorCredentialsModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_originators_using_get**
> list[OriginatorModel] get_originators_using_get()

getOriginators

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
api_instance = swagger_client.OriginatorControllerApi(swagger_client.ApiClient(configuration))

try:
    # getOriginators
    api_response = api_instance.get_originators_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OriginatorControllerApi->get_originators_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OriginatorModel]**](OriginatorModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **investor_using_get**
> ResponseEntity investor_using_get()

investor

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
api_instance = swagger_client.OriginatorControllerApi(swagger_client.ApiClient(configuration))

try:
    # investor
    api_response = api_instance.investor_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OriginatorControllerApi->investor_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

