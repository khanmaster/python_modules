# importing requests to make an api call to www

import requests
from emoji import emojize

live_response = requests.get("https://www.bbc.co.uk/")
# it provides in integer as a response code

if live_response.status_code == 200:
    print(" mission successful !!!! " + str(live_response.status_code))
    print(emojize((":thumbs_up:")))
else:
    print("OOPs something went wrong please try later ")
