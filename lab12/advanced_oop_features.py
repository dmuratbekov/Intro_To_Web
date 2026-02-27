# Method Overriding
class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    def show(self):
        print("This is the child class")

obj = Child()
obj.show()


# Multiple Inheritance
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    pass

obj = C()
obj.method_a()
obj.method_b()


# Real-World Example: OOP in a Library Management System
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self. year = year

    def display_info(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books (self):
        for book in self.books:
            print(book.display_info())

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
#Managing a library
library = Library()
library.add_book(book1)
library.add_book(book2)
library.list_books()


#