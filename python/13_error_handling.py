"""
Error Handling

syntax

try:
    # code that might cause an error
except <ErrorType>:
    # code to handle the error
finally:
    # code that will run regardless of an error
"""

# throws ZeroDivisionError: division by zero
# print(1 / 0)

try:
    print(1 / 0)
except:
    print("an error occurred")

try:
    print(1 / 0)
except ZeroDivisionError:
    print("cannot divide number by 0")
finally:
    print("i just skipped over the exception")


try:
    print(1 / 4)
    x = [1, 2, 3, 4, 5]
    print(x[10])  # IndexError: list index out of range
except ZeroDivisionError:
    print("cannot divide number by 0")
except IndexError:
    print("index does not exist")


try:
    print(1 / 4)
    x = [1, 2, 3, 4, 5]
    print(x[3])

    # throwing an exception
    raise Exception("just felt like raising an exception")
except ZeroDivisionError:
    print("cannot divide number by 0")
except IndexError:
    print("index does not exist")
except Exception as e:
    print(e)
