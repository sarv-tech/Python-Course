# Converting Python to JSON
# We use dumps() to convert Python objects into JSON string.
import json

data = { 
    "name": "John",
    "age": 25,
    "marks": [85, 90, 92]
}

json_string = json.dumps(data) 
print(json_string)

print("\n")

# Converting JSON to python 
# We use loads() to convert JSON string to Python dictionary
json_data = '{"name": "John", "age": 25}' 
python_obj = json.loads(json_data) 
print(python_obj["name"])

print("\n")

# Writing JSON to a File (json.dump)
import json

data = {"name": "Aisha", "city": "Delhi"} 
with open("data.json", "w") as f: 
    json.dump(data, f, indent=4)