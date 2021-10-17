# goal of this is to to demonstrate making requests using python code instead of postman(a tool for making API requests and
# receiving responses)
# we will be using requests a py. library used to facilitate making api requests, you can also set rate limits so that
# we dont get an error with requests(read docs)
# in requests we need to set the path, set the query params like query string, formart etc
# for apis that need auth keys we also need to set the keys are global constants
# we can use the debugging tool and breakpoint to inspect our response
# this code specifically gets the lat and lon of the 7 wonders of the world 
# based on the first result through location IQ API
# dependencies are request library and time library 


import requests as r
import time

# https://us1.locationiq.com/v1/search.php?key=YOUR_ACCESS_TOKEN&q=SEARCH_STRING&format=json
# requests.get(url, params=None, **kwargs)



seven_wonders_of_the_world = ["Great Wall of China", "Petra", "Colosseum", "Chichen Itza", "Machu Picchu" , "Taj Mahal", "Christ the Redeemer"]


def get_query_params(query_string, LOCATION_IQ_ACCESS_KEY = ""):
    """
    returns query parmeters for requests 
    takes query string to be search assumes query is always a list
    specificies format for requests should send json response 
    requires location IQ access key
    """
    LOCATION_IQ_ACCESS_KEY = ""
    
    format = "json"
    LOCATION_IQ_ACCESS_KEY = LOCATION_IQ_ACCESS_KEY 

    query_params = {}
    query_params["key"] = LOCATION_IQ_ACCESS_KEY
    query_params["q"] = query_string
    query_params["format"] = format

    return query_params
    

def get_requests_json(query_params): 
    """
    takes query params and returns response from requests in a json
    base URL is location IQ, endpoint specified in params 
    """
    PATH = "https://us1.locationiq.com/v1/search.php"
    response = r.get(PATH, query_params)

    return response.json()

def retrieve_lon_lat_from_json_(request_json): 
    """
    takes response json and returns lon and lat in a dictionary
    returns lat and lon of first object in json response
    outputs dictionary of lat and lon

    """
    wonder_lon_lat = {}
    wonder_lon_lat["longitude"] = request_json[0]["lon"]
    wonder_lon_lat["laitude"] = request_json[0]["lat"]

    return wonder_lon_lat

def get_lon_and_lat_of_location(query_string_list): 
    """
    should take the string and propulate query params 
    returns dict with key being the query string
    output is a dictionary, key is query string and value is 
    lat and lon of the query string, expected to be a valid location
    uses time library to sleep between returns and avoid rate limits
    """
    request_dict = {}
    
    
    for i in query_string_list:
        query_params = get_query_params(i)
        query_json = get_requests_json(query_params)
        lon_and_lat = retrieve_lon_lat_from_json_(query_json)

        request_dict[i] = lon_and_lat
        time.sleep(.25)

    return request_dict



lon_lat_seven_wonders = get_lon_and_lat_of_location(seven_wonders_of_the_world)

print(lon_lat_seven_wonders)








