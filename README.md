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
- 