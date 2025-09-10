# There are two types of Modules :-
# - Built in Modules
# - External Modules
# list of all built-in Modules:- https://docs.python.org/3/library/functions.html

import math
import os
import my_module
import requests

print(math.sqrt(16))
my_module.hello()
r = requests.get("https://www.instagram.com")
print(r.text)