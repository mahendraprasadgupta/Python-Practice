# # Python JSON

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Python has a built-in package called json, which can be used to work with JSON data.

# Convert from JSON to Python:
# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

import json

# a Python object (dict):
x = {
  "name": "Mahendra",
  "age": 27,
  "city": "India"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)