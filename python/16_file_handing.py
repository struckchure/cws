"""
File handling: read/write files in python
"""

# Read file
file = open("info.txt", "r")
print(file.read())

# Write file
file = open("extra-info.txt", "w")
file.write("Fizz Buzz")

# Update file content
file = open("info.txt", "a")
file.write("\nBrainiac 5")


# Using `with` keyword

with open("info.txt", "r") as file:
    print(file.read())

with open("info.txt", "w+") as file:
    file.write("\nBrainiac 6")
    print(file.read())

with open("extra-info.txt", "a+") as file:
    file.write("\nBrainiac 6")
    print(file.read())
