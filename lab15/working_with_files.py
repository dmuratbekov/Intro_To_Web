# file = open("filename", "mode")

# Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python makes file handling easy.")

# Reading from a File
with open("example.txt", "r") as file:
    content =file.read()
    print(content)

#  Reading Files Line by Line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Appending Data to a File
with open("example.txt", "a") as file:
    file.write("\nThis line was added later.")

# Checking if a File Exists Before Writing
try:
    with open("example.txt", "x") as file:
        file.write("This is a new file.")
except FileExistsError:
    print("File already exists.")


 # Reading a Text File and Processing Each Line
with open("data.txt", "r") as file:
    for line in file:
        print(f"Processed line: {line.strip()}")


# Writing Data to a CSV File
import csv

data = [
    ["Name", "Age", "City"],
    ["Alica", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 22, "Chicago"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


# Reading Data from a CSV File
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Reading CSV Files with Column Headers
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}.")


# Appending Data to a CSV File
new_data = [["David", 28, "San Francisco"]]

with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows (new_data)
