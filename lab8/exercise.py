#1
print("ex 1:")
def square(num):
    return num ** 2

print(square(5))

#2
print("\nex 2:")
def sum_list(nums):
    return sum(nums)

print(sum_list([1, 2, 3]))

#3
print("\nex 3:")
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

#4
print("\nex 4:")
def is_primme(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_primme(10))
print(is_primme(23))
