# This lesson covers Python Modules

- Python Library and Built in functions
- What is pip and how do we use it
- APIs with Python 

- Built in functions help us accelerate our development of software 












- How can we create a customised method and utilise the built in functionality at the same time
- When and why should we do that

- Creating a customised method to add required information and use the functionality provided by sys module 
```
def current_system_path():
    print(" this is your current directory ")
    return sys.path

print(current_system_path())
```


**What is pip?**

- Package manager for Python and helps us install external packages such as requests

- syntax: pip install name_of_the_package
 ``` pip install requests ```
 
 - 3rd Iteration
- What does requests module bring to the table
```python
import requests

from emoji import emojize

live_response = requests.get("https://www.bbc.co.uk/")

def check_response_code():
    if live_response.status_code:
        print(" mission successful !!!! " + str(live_response.status_code))
        print(emojize(":thumbs_up:"))
    elif live_response.status_code == 404:
        print(" the site is unavailable until further notice please contact mobile: ")
    else:
        print("OOPs something went wrong please try later ")


check_response_code()
```
**NOTE**
 - It will evaluate to True if the status code was between 200-400, otherwise False
# API testing 
- Postman

```python
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
```

# Json basics
- Java script object notation
- use cases - browser data 
- data is in key value pairs
- Json encoding from a Dictionary
- Jason decoding into a dictionary
- handling/creating files with python
- writing to a file
- reading from a file

## Handling files and permissions


`open(file, mode)`

| Mode	 |Description|
| :----: |:----                                                    |
|'r'	 |This is the default mode. It Opens file for reading.       |
|'w'	 |This Mode Opens file for writing.  If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x'	 |Creates a new file. If file already exists, the operation fails.|
|'a'	 |Open file in append mode. If file does not exist, it creates a new file.|
|'t'	 |This is the default mode. It opens in text mode.|
|'b'	 |This opens in binary mode.
|'+'	 |This will open a file for reading and writing (updating)|


**Exception handling**
- ```try``` & ```except``` blocks
- ```rasie``` & ```finally```

**Use cases**
- we use these blocks when we expect an error or an exception from python interpreter 
- why - this helps us handle the ```errors``` or ```exception``` and add customised message as well as make a decision based on the customer needs 

- we will create a variable to store a file data using ```open()```
**Iteration 1**
```
try: # let's use try block for a 1 line of code where we know this will throw an error
    file = open("orders.text")
except:
    print(" Panic Alert!!!! ")
```
**Iteration 2 using ```raise``` and ```finally```**
```
try:
    file = open("orders.text")
except FileNotFoundError as errmsg: # creating an alais for FileNotFound Error in except block
    print("Alert something sent wrong" + str(errmsg))
# if we still wanted them to see the actual exception together with our customised message
    raise # raise will send back the actual exception

finally: # finally will execute regardless of the above conditions
    print(" Hope you had a good Customer experience, please visit again")
```