# Example 1: Basic Text File Operations

filename = 'example.txt'
content_to_write = "Hello, world!\nwelcome to file handling in Python."

with open(filename, 'w') as file:
    file.write(content_to_write)

print(f"Content written to (filename)")

with open(filename, 'r') as file:
    content_read = file.read()

print("Content read from file:")
print(content_read)


# Example 2: Processing CSV Files
import csv

# Writing to a CSV File
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

csv_filename = 'people.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows (data)

print (f"Data written to {csv_filename}")

# Reading from a CSV File
with open('people.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


# Example 3: Appending Data to a File
filename = 'example.txt'
additional_content = "\nAppending new lines to the file."

with open(filename, 'a') as file:
    file.write(additional_content)

print(f"New content appended to {filename}")

with open (filename, 'r') as file:
    content_read = file.read()

print("Updated file content:")
print(content_read)

