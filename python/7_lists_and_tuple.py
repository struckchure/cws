# List and Tuples
"""
A list is a collection of items (any python object), can be changed (mutable).
A tuple is a collection of items (any python object), but cannot be changed once create (immutable).
"""

# List

colors = ["red", "blue", "green", "alpha"]
print(type(colors))
print(colors[0])
print(colors[2])
print(colors[-1])

colors.append("black")
print(colors)

colors.insert(0, "white")
print(colors)

colors.remove("alpha")
print(colors)

popped_value = colors.pop()  # defaults to index -1
popped_value = colors.pop(0)
print(popped_value)
print(colors)

print(colors.index("red"))

colors.append("black")
print(colors)
print(colors.count("black"))

letters = ["x", "z", "y", "c", "a", "b"]
letters.sort()
print(letters)

letters.reverse()
print(letters)

print(letters[::-1])

numbers = [1, 2, 3, 4, 5]
numbers.extend(letters)
print(numbers)

letters_and_numbers = [*letters, *numbers]
print(letters_and_numbers)

numbers.clear()
print(numbers)

print(len(letters))

# Tuple
white = 255, 255, 255
print(type(white))

ages = (90,)
ages = (90,)
print(type(ages))

color = (255, 0, 0)
print(color[-1])
print(color[0])

# Value Unpacking
red = color[0]
green = color[1]
blue = color[2]
print(red, green, blue)

red, green, blue = color
print(red, green, blue)

# Throw away values

red, green, _ = color
print(red, green)
