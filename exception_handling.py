# We will have a look at the practical use cases and implementation of try, except, raise and finally

we will create a variable to store a file data using open()
Iteration 1
try: # let's use try block for a 1 line of code where we know this will throw an error
    file = open("orders.text")
except:
    print(" Panic Alert!!!! ")

# Iteration 2
try:
    file = open("orders.text")
except FileNotFoundError as errmsg: # creating an alais for FileNotFound Error in except block
    print("Alert something sent wrong" + str(errmsg))
# if we still wanted them to see the actual exception together with our customised message
    raise # raise will send back the actual exception

finally: # finally will execute regardless of the above conditions
    print(" Hope you had a good Customer experience, please visit again")















# import json
#
# car_data = {"name": "tesla", "engine": "electric"} # dic
#
# print(type(car_data))
#
#
# car_data_json_string = json.dumps(car_data) #
# print(type(car_data_json_string))
#
# with open("new_json_file.json", "w") as jsonfile:
#     json.dump(car_data, jsonfile)
#
# with open("new_json_file.json") as jsonfile:
#     car = json.load(jsonfile)
#     print(car['name'])
#     print(car['engine'])
