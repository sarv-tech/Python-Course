# Q. Import the math module and use it to:
# Find the square root of 144
# Calculate sin(90°)

import math

a = math.sqrt(144)
b = math.sin(math.radians(90))

print(a, b)



# Q. Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".

import requests

response = requests.get("https://api.github.com")
print(response.json())