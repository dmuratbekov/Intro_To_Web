import json
# Example 1: Converting Python Data to JSON (Serialization)

student_data = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

json_string = json.dumps(student_data, indent=4)
print("Serialized JSON string:")
print(json_string)


# Example 2: Converting JSON Back to Python Data (Deserialization)

json_string = '''
{
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}
'''
student_data = json.loads(json_string)
print("Deserialized Python object:")
print(student_data)


# Example 3: Reading from and Writing to a JSON File
# Writing JSON to a File
data = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

with open('student.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data has been written to student.json")


# Reading JSON from a File
with open('student.json', 'r') as file:
    data_loaded = json.load(file)

print("Data loaded from student.json:")
print(data_loaded)