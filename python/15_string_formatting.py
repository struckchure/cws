"""
String Formatting: is the process of inserting values into a string.
The values can be variables, expressions, or constants.
The values are inserted into the string at the points where the placeholders are.
"""

name = "John"
age = 20

# f-string
print(f"My name is {name} and i am {age} years old.")

# .format()
print("My name is {} and i am {} years old.".format(name, age))

# % operator
print("My name is %s and i am %d years old." % (name, age))

# concatenation
print("My name is " + name + " and i am " + str(age) + " years old.")
