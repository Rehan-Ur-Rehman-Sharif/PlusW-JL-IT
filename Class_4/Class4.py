# Functions as first class objects

# assigning function to some variable


def say_hello():
    print("Helloo, I learning python")


greet = say_hello

say_hello()


# Passing functions as an arguments
def add(x, y):
    return x + y


def operate_numbers(f, a, b):
    return f(a, b)


result = operate_numbers(add, 2, 3)

print(result)

# Retruning functions from other function


def multiplier(factor):
    def multiply(num):
        return num * factor

    return multiply


double = multiplier(2)  # Set factor = 2

print(double(5))  # double is basically multiply function (inner function)


# rescursive function


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # 120

# Doc strings


def calculator(values):
    """This function is basically used for the calculation"""
    pass


help(calculator)


# local variable can use only inside the fucntion
# global variable can use both outside and inside the function

# local variable


def calculator():
    a = 10
    b = 20
    print(f"Addition of 2 numbers are: {a+b}")


calculator()


# Global variable
a = 10
b = 20


def calculator():

    print(f"Addition of 2 numbers are: {a+b}")


calculator()

a = 10
b = 20


def calculator():
    global a
    a = 20
    print(f"Addition of 2 numbers are: {a+b}")


calculator()


def outer():
    x = 5

    def inner():
        nonlocal x
        x = 10

    inner()
    print("Outer function x value is:", x)


outer()

# pip install numpy

import numpy as np


# python list and Numpy Array
py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

print(type(py_list))
print(type(np_array))


# 1D array

arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)

# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3 matrix
print(arr_2d)

print(arr_2d.ndim)


# arrays filled with zeros
zeros_array = np.zeros((2, 3))
print(zeros_array)

# arrays filled with ones
zeros_array = np.ones((2, 3))
print(zeros_array)

# arrays filled with nine
zeros_array = np.full((2, 3), 8)
print(zeros_array)


# def array_function()
# array filled with evenly spaced value

linspace_array = np.linspace(1, 10, 5)
print(linspace_array)

# array filled with range of numbers

range_array = np.arange(1, 10, 5)
print(range_array)


# Create a random arrays

# array between 0 & 1

random_array = np.random.rand(3, 3)
print(random_array)

# array between 1 & 99

random_array = np.random.randint(1, 100, (3, 3))
print(random_array.ndim)


# Shape, Size and Dimension of array

arr = np.array([[1, 2, 3], [3, 4, 5]])

print(arr.shape)

print(arr.size)


# reshaping the arrays

arr = np.array([1, 2, 3, 5, 6])

arr_reshaped = arr.reshape((2, 3))
print(arr_reshaped)

arr2 = np.array([4, 5, 6])

print(arr + arr2)


# min, max, sum

arr = np.array([[1, 2, 3], [3, 4, 5]])

print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))


# array indexing

arr = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])


print(arr[-1, -1])


# slicing concept
arr1 = np.array([1, 2, 3])

arr1[::-1]

arr = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

arr[:, 1:3]


# conditonal filtering
arr1 = np.array([1, 2, 3])
result = np.where(arr1 > 10)

print(result)


# np.take()

arr1 = np.array([1, 2, 3])

np.put(arr1, [0, 1], [10, 20])

print(arr1)
