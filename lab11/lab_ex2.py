#3
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A",
}
student["subject"] = "Math"
student["grade"] = "A+"
student.pop("age")
print(student.keys())
print(student.values())
print(student.items())