#1
print("task 1: ")
int_input = int(input("Enter an integer: "))
float_input = float(input("Enter a floating point number: "))
str_input = str(input("Enter a string: "))

print(type(int_input))
print(type(float_input))
print(type(str_input))

#2
print("\ntask 2: ")
str_ = 123
str_int = int(str_)
str_float = float(str_)

print(type(str_int))
print(type(str_float))

person = {
    "name": "Dan",
    "age": 20,
}

print(f"Hello, {person['name']}, your age is {person['age']}")

#3
print("\ntask 3: ")
my_set = {1, 2 , 1, 3, 3, 5, 5, 4, 6, 7, 7}
my_set.add(9)
my_set.remove(7)
print(my_set)