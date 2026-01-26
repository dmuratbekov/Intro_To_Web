#1
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print(f"Hello {name}! You are {age} years old.")

#2
num1, num2, num3 = map(int, input("Please enter three numbers: ").split())
total = num1 + num2 + num3
average = total / 3
product = num1 * num2 * num3
print(f"Sum: {total}, Average: {average}, Product: {product}")