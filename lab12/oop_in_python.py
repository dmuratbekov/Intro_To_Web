# Example 1: Defining a Simple Class and Creating an Object
class Car:
    def _init_(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        return f"{self.brand} {self.model} ({self.year})"

#Creating objects (instances)
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)

print(car1.display_info())
print(car2.display_info())


# Understanding the __init__ Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Toyota", 20)
print(p1.name)
print(p1.age)


# Example 2: Adding Methods to a Class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

dog1 = Dog("Bobby", "Golden retriever")
print(dog1.bark())


# Example 3: Changing Object Attributes
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

phone1 = Phone("Samsung", 500)
print(phone1.price)

phone1.price = 450
print(phone1.price)


# Example 4: Class vs. Instance Variables
class Employee:
    company = "TechCorp"

    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

print(e1.company)
print(e2.company)

Employee.company = "NewTechCorp"

print(e1.company)
print(e2.company)


# Example 5: The Role of self
class Calculator:
    def __init_(self, value):
        self.value = value

    def add(self, num):
        self.value += num

    def get_value(self):
        return self.value

calc = Calculator(10)
calc.add(5)
print(calc.get_value())


# Example 6: Deleting Attributes and Objects
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

user1 = User("Alice", "alica@gmail,com")
print(user1.email)

del user1.email

del user1


# Real-World Example: User Authentication System
class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password

    def login(self, password):
        if password == self._password:
            return f"Welcome, {self.username}!"
        else:
            return "Invalid credentials!"

user = User("admin", "secure123")

print(user.login("secure123"))
print(user.login ("wrongpass"))


#