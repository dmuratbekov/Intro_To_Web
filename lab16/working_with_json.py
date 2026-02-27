import json

# 1. Converting Python Objects to JSON (Serialization)
data = {
    "name": "Alica",
    "age": 25,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)

# 2. Writing JSON to a File
with open("data.json", "w") as file:
    json.dump(data, file)

# 3. Reading JSON from a File
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)

# 4. Converting JSON to a Python Object (Deserialization)
json_string = {
    "name": "Alica",
    "age": 25,
    "city": "New York"
}

data = json.loads(json_string)

print(data["name"])
print(type[data])

# 5. Working with Lists in JSON
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22}
]

json_string = json.dumps(users, indent=4)
print(json_string)

# 6. Writing a List of Dictionaries to a File
with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

# 7. Handling JSON Errors
invalid_json = {
    "name": "Alica",
    "age": 25,
    "city": "New York"
}

try:
    data = json.loads(invalid_json)
except json.JS0NDecodeError as e:
    print(f"Error loading JSON: {e}")
