# use json module to do json encoding and decoding

import json

car_data = {"name": "tesla", "engine": "electric"}
# creating a dictionary and storing it into a variable
#print(type(car_data))

# json.dumps() - serialises json to a formatted sting
car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))

# this how we can encode from a dictionary and write to a file
with open("new_json_file.json", "w") as jsonfile: # w is to give write permission
#
    json.dump(car_data, jsonfile)

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile) # load() copies the data and stores into a variable
    print(type(car))
    print(car['name'])
    print(car['engine'])
# getting the value by keys

# Json is used heavily in the industry so reading, writing, parsing and converting data are the most commonly utilised options








# json.dump() creates a stream object and except a file object to write to