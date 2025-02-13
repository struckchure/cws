"""
Functions are reusable pieces of code that can be called from other parts of your program to perform specified operations, e.g `sin()` function in mathematics.

Syntax

def <function-name>(<parameters>):
    <function-body>
"""

"""
None-returning function: are functions that do not return a value.
"""


def average(a, b):
    print((a + b) / 2)


average(1, 2)

"""
Returning function: are functions that return a value.
"""


def square_root(a):
    return a**0.5


print(square_root(144))


"""
Lambda functions: are anonymous functions that can be defined in a single line of code.
"""


# def square(a):
#     return a**2

square = lambda a: a**2

print(square(10))


"""
Function argments: Positional Argments
"""


def show_profile(name, age, gender):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")


# WRONG
# show_profile(30, "John", "Male")

# CORRECT
show_profile("John", 30, "Male")
show_profile(*("Jane", 25, "Female"))


"""
Function argments: Keyword Argments (**kwargs)
"""

show_profile(age=30, gender="Male", name="John")
show_profile(**{"name": "Jane", "age": 25, "gender": "Female"})

"""
Creating functions to use *args
"""

# LONG METHOD (or not recommended in some case)
# def sum(a, b, c):
#     return a + b + c


def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(sum(1, 2, 3, 4, 5))

"""
Creating functions to use **kwargs
"""


def show_profile_v2(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


show_profile_v2(name="John", age=30, gender="Male", username="j.doe")
