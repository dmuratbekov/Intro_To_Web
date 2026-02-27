import re

# Search and Replace Example:
text = "My phone number is 1234567890 and my office number is 9876543210"
pattern = r'\d'
replacement = "NUMBER"

result = re.sub(pattern, replacement, text)
print(result)


# The re Module: Basic Functions
# 1. re.search()
text = "The rain in Spain falls mainly on the plain."

pattern = r"Spain"

match = re.search(pattern, text)
if match:
    print("Found:", match.group())
else:
    print("Not found.")


# 2. re.match()
text = "Hello, world!"
pattern = r"Hello"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match.")

pattern = r"world"
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match with match().")


# 3. re.findall()
text = "John's number is 555-1234, and Mary's number is 555-5678."
pattern = r"\d{3}-\d{4}"

matches = re.findall(pattern, text)
print("Phone numbers found:", matches)


# Additional Tips
match = re.search(r"python", "I love Python", re.IGNORECASE)
if match:
    print("Match found:", match.group())
