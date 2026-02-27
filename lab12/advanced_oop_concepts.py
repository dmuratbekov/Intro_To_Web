# Example: Using Encapsulation to Protect Data
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(300)

print(account.get_balance())


# Example: Inheritance in Python
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound (self):
        return "Some sound"

class Dog (Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, "says:", dog.make_sound())
print(cat.name, "says:", cat.make_sound())


# Example: Polymorphism in Python
class Bird:
    def fly(self):
        return "Flying high!"

class Airplane:
    def fly(self):
        return "Taking off into the sky!"

class Fish:
    def fly(self):
        return "I can't fly!"

for obj in [Bird(), Airplane(), Fish()]:
    print(obj.fly())


# Example: Abstraction in Python
from abc import ABC, abstractmethod

class Vehicle (ABC):
    @abstractmethod

    def start_engine (self):
        pass

class Car (Vehicle):
    def start_engine (self):
        print("Car engine started!")

class Bike (Vehicle):
    def start_engine(self):
        print("Bike engine started!")

car = Car()
bike = Bike()

car.start_engine()
bike.start_engine()

