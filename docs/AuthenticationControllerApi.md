# swagger_client.AuthenticationControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_using_post**](AuthenticationControllerApi.md#authenticate_using_post) | **POST** /api/ia/clients/authentication | authenticate
[**refresh_using_post**](AuthenticationControllerApi.md#refresh_using_post) | **POST** /api/ia/clients/authentication/refresh | refresh


# **authenticate_using_post**
> Token authenticate_using_post(credentials)

authenticate

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
api_instance = swagger_client.AuthenticationControllerApi(swagger_client.ApiClient(configuration))
credentials = swagger_client.Credentials() # Credentials | credentials

try:
    # authenticate
    api_response = api_instance.authenticate_using_post(credentials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationControllerApi->authenticate_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**Credentials**](Credentials.md)| credentials | 

### Return type

[**Token**](Token.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_using_post**
> Token refresh_using_post()

refresh

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
api_instance = swagger_client.AuthenticationControllerApi(swagger_client.ApiClient(configuration))

try:
    # refresh
    api_response = api_instance.refresh_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationControllerApi->refresh_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Token**](Token.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

