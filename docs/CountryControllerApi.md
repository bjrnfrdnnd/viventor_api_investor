# swagger_client.CountryControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries_using_get**](CountryControllerApi.md#get_countries_using_get) | **GET** /api/ia/countries | getCountries
[**get_loan_countries_using_get**](CountryControllerApi.md#get_loan_countries_using_get) | **GET** /api/ia/loan-countries | getLoanCountries
[**get_originator_countries_using_get**](CountryControllerApi.md#get_originator_countries_using_get) | **GET** /api/ia/originator-countries | getOriginatorCountries


# **get_countries_using_get**
> list[CountryModel] get_countries_using_get()

getCountries

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
api_instance = swagger_client.CountryControllerApi(swagger_client.ApiClient(configuration))

try:
    # getCountries
    api_response = api_instance.get_countries_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryControllerApi->get_countries_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CountryModel]**](CountryModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_countries_using_get**
> list[CountryModel] get_loan_countries_using_get()

getLoanCountries

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
api_instance = swagger_client.CountryControllerApi(swagger_client.ApiClient(configuration))

try:
    # getLoanCountries
    api_response = api_instance.get_loan_countries_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryControllerApi->get_loan_countries_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CountryModel]**](CountryModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_originator_countries_using_get**
> list[CountryModel] get_originator_countries_using_get()

getOriginatorCountries

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
api_instance = swagger_client.CountryControllerApi(swagger_client.ApiClient(configuration))

try:
    # getOriginatorCountries
    api_response = api_instance.get_originator_countries_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryControllerApi->get_originator_countries_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CountryModel]**](CountryModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

