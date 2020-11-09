import requests

live_response = requests.get("http://api.postcodes.io/postcodes/e147le")

#argument = str(input(" please enter you postcode "))

#url_target = live_response + argument
print(live_response.content)

# research how to convert this data into dictionary
# HINT - python json library/module/method can be used to resolve this

# iterate through the data and print RESULTS
# print longitude and latitude (locations)
# Create a function that returns the longitude and latitude of the given postcode


#print(live_response.status_code)

# def check_response_code():
#     pass