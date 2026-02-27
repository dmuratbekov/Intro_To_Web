import mymodule

#1
mymodule.greeting("Jonathan")

#2
a = mymodule.person1["age"]
print(a)

#3
import mymodule as mx

a = mx.person1["age"]
print(a)

#4
import platform

x = platform.system()
print(x)

#5
x = dir(platform)
print(x)

#6
from mymodule import person1

print (person1["age"])


