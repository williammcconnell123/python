from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'd1745fde28a14b70b1f200705232310'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
q = '30308' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.
dt = '2013-10-20' # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format

try:
    # Astronomy API
    api_response = api_instance.astronomy(q, dt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->astronomy: %s\n" % e)
