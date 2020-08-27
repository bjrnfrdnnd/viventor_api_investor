# swagger_client.PublicInvestmentControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_loan_attachment_using_get1**](PublicInvestmentControllerApi.md#download_loan_attachment_using_get1) | **GET** /api/public/ia/investment/attachment/{id} | downloadLoanAttachment
[**get_primary_market_loan_info_using_get**](PublicInvestmentControllerApi.md#get_primary_market_loan_info_using_get) | **GET** /api/public/ia/investment/primary/{loanId} | getPrimaryMarketLoanInfo
[**list_loan_attachments_using_get**](PublicInvestmentControllerApi.md#list_loan_attachments_using_get) | **GET** /api/public/ia/investment/attachments/{loanId} | listLoanAttachments


# **download_loan_attachment_using_get1**
> download_loan_attachment_using_get1(id)

downloadLoanAttachment

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
api_instance = swagger_client.PublicInvestmentControllerApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # downloadLoanAttachment
    api_instance.download_loan_attachment_using_get1(id)
except ApiException as e:
    print("Exception when calling PublicInvestmentControllerApi->download_loan_attachment_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_primary_market_loan_info_using_get**
> LoanPrimaryMarketModel get_primary_market_loan_info_using_get(loan_id)

getPrimaryMarketLoanInfo

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
api_instance = swagger_client.PublicInvestmentControllerApi(swagger_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # getPrimaryMarketLoanInfo
    api_response = api_instance.get_primary_market_loan_info_using_get(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicInvestmentControllerApi->get_primary_market_loan_info_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**LoanPrimaryMarketModel**](LoanPrimaryMarketModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loan_attachments_using_get**
> list[LoanAttachment] list_loan_attachments_using_get(loan_id)

listLoanAttachments

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
api_instance = swagger_client.PublicInvestmentControllerApi(swagger_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # listLoanAttachments
    api_response = api_instance.list_loan_attachments_using_get(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicInvestmentControllerApi->list_loan_attachments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**list[LoanAttachment]**](LoanAttachment.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

