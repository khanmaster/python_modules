# Let's have a look at some built in function in Python

# import is the key word we used to call modules from Python library

# first Iteration
# from random import random
# import math
# # We have random method in python library which we use by importing
#
# print(random())
#
# # Second Iteration
# import random
#
# print(random.random())
#
# # It generates float number between 0-1
# #
# # num_float = 23.44
# print(" floor method rounds the figure to lower end")
# print(math.floor(num_float))
#
# print(" ceil() method rounds the figure to higher end of the value ")
# print(math.ceil(num_float))
# print(math.pi)

# Task
# get user input of a float number
# check if the number is lower than .50 then round the figure to lower end
# check if the number is greater than .51 then round the figure to higher end
# example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end
# tips - get help online - python library

import os
# To find out system configuration or system related information
# Based on the information provided we can handle the user request
import math, datetime, sys

working_dir = os.getcwd()

print(working_dir)

# Let's find out the name of our os
# only available in Linux
#print(os.uname())

# Let's count the number of CPUs

# How can we create a customised method and utilise the built in functionality at the same time
# When and why should we do that
def current_system_path():
    print(" this is your current directory ")
    return sys.path

print(current_system_path())