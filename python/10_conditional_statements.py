# Conditional Statements
"""
Conditional statements allow you to execute different blocks of code based on certain conditions.
"""

"""
if statatements

syntax

if <condition>:
    <block of code>
"""

# input() is used to recieve a value from the user via the terminal
# number = input("Enter a number: ")
# print(type(number))

# convert the input to an integer with type casting
number = int(input("Enter a number: "))
if (number % 2) == 0:
    print("Even")

"""
else statements

syntax
if <condition>:
    <block of code>
else:
    <block of code>
"""

if (number % 2) == 0:
    print("Even")
else:
    print("Odd")


"""
elif statements (else if)

syntax
if <condition>:
    <block of code>
elif <condition>:
    <block of code>
else: # optional
    <block of code>
"""

# Get angle measurement from user
angle = float(input("Enter angle in degrees: "))

if angle == 0:
    print("This is a zero angle")
elif angle < 90:
    print("This is an acute angle")
elif angle == 90:
    print("This is a right angle")
elif angle < 180:
    print("This is an obtuse angle")
elif angle == 180:
    print("This is a straight angle")
elif angle < 360:
    print("This is a reflex angle")
elif angle == 360:
    print("This is a complete angle")
else:
    print("Angle is greater than 360 degrees")
