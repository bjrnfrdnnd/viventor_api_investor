# swagger_client.RegistrationControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_using_post**](RegistrationControllerApi.md#confirm_using_post) | **POST** /api/ia/clients/registration/confirmation | Registration confirmation
[**confirmation_resend_using_post**](RegistrationControllerApi.md#confirmation_resend_using_post) | **POST** /api/ia/clients/registration/confirmation-resend | confirmationResend
[**step1_using_post**](RegistrationControllerApi.md#step1_using_post) | **POST** /api/ia/clients/registration/step1 | Registration first step
[**step2_using_post**](RegistrationControllerApi.md#step2_using_post) | **POST** /api/ia/clients/registration/step2 | Registration second step
[**step3_using_post**](RegistrationControllerApi.md#step3_using_post) | **POST** /api/ia/clients/registration/step3 | Registration third step


# **confirm_using_post**
> Token confirm_using_post(code)

Registration confirmation

Returns token with authority STEP2

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
api_instance = swagger_client.RegistrationControllerApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | code

try:
    # Registration confirmation
    api_response = api_instance.confirm_using_post(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationControllerApi->confirm_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code | 

### Return type

[**Token**](Token.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirmation_resend_using_post**
> confirmation_resend_using_post()

confirmationResend

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
api_instance = swagger_client.RegistrationControllerApi(swagger_client.ApiClient(configuration))

try:
    # confirmationResend
    api_instance.confirmation_resend_using_post()
except ApiException as e:
    print("Exception when calling RegistrationControllerApi->confirmation_resend_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **step1_using_post**
> Token step1_using_post(step1)

Registration first step

Returns token with authority STEP1

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
api_instance = swagger_client.RegistrationControllerApi(swagger_client.ApiClient(configuration))
step1 = swagger_client.RegistrationStep1Model() # RegistrationStep1Model | step1

try:
    # Registration first step
    api_response = api_instance.step1_using_post(step1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationControllerApi->step1_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **step1** | [**RegistrationStep1Model**](RegistrationStep1Model.md)| step1 | 

### Return type

[**Token**](Token.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **step2_using_post**
> Token step2_using_post(step2)

Registration second step

Returns token with authority STEP3

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
api_instance = swagger_client.RegistrationControllerApi(swagger_client.ApiClient(configuration))
step2 = swagger_client.RegistrationStep2Model() # RegistrationStep2Model | step2

try:
    # Registration second step
    api_response = api_instance.step2_using_post(step2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationControllerApi->step2_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **step2** | [**RegistrationStep2Model**](RegistrationStep2Model.md)| step2 | 

### Return type

[**Token**](Token.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **step3_using_post**
> Token step3_using_post()

Registration third step

Returns token with authority STEP4

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
api_instance = swagger_client.RegistrationControllerApi(swagger_client.ApiClient(configuration))

try:
    # Registration third step
    api_response = api_instance.step3_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationControllerApi->step3_using_post: %s\n" % e)
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

