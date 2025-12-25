#two types of modules in python:
# build in modules , external modules
import math
import os
import mymodule
import requests
mymodule.hello() #own module
print(math.sqrt(25))
r = requests.get("https://www.google.com")
print(r.text)