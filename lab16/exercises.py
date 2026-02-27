from fileinput import filename
import json

# Lab Exercise 1: Converting a Python Dictionary to a JSON String (Serialization)
student_info = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

json_string = json.dumps(student_info, indent=4)
print("Serialized JSON string:")
print(json_string)


# Lab Exercise 2: Converting a JSON String Back to a Python Object (Deserialization)
json_string = '''
{
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}
'''

student_info = json.loads(json_string)

print("Deserialized Python object:")
print(student_info)


# Lab Exercise 3: Reading from and Writing to a JSON File
student_info = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

filename = 'student.json'

with open(filename, 'w') as file:
    json.dump(student_info, file, indent=4)
print (f"Data has been written to {filename}")

with open(filename, 'r') as file:
    data_loaded = json.load(file)

print("Data loaded from the JSON file:")
print(data_loaded)