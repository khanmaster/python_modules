# importing requests to make an api call to www

import requests
from emoji import emojize

live_response = requests.get("http://api.postcodes.io/postcodes/e47le")
# it provides in integer as a response code

print(live_response.headers)


# print(type(live_response.content))
# first Iteration
try:
    if live_response.status_code == 200:
        print(" mission successful !!!! " + str(live_response.status_code))
        print(emojize((":thumbs_up:")))
except ConnectionRefusedError:
    #elif live_response.status_code == "400":
    print(" the site is unavailable until further notice please contact mobile: ")

else:
    print("OOPs something went wrong please try later ")

# Second Iteration
# def check_response_code():
#     if live_response.status_code == 200:
#         print(" mission successful !!!! " + str(live_response.status_code))
#         print(emojize(":thumbs_up:"))
#     elif live_response.status_code == 404:
#         print(" the site is unavailable until further notice please contact mobile: ")
#     else:
#         print("OOPs something went wrong please try later ")
#
# check_response_code()

# 3rd Iteration
# What does requests module bring to the table
#
# def check_response_code():
#     if live_response.status_code:
#         print(" mission successful !!!! " + str(live_response.status_code))
#         print(emojize(":thumbs_up:"))
#     elif live_response.status_code == 404:
#         print(" the site is unavailable until further notice please contact mobile: ")
#     else:
#         print("OOPs something went wrong please try later ")
#
#
# check_response_code()
#
# # It will evaluate to True if the status code was between 200-400, otherwise False
# #
