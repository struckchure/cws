# Loops (for, while)

"""
For Loop

syntax

for <item> in <iterable>:
    <code>


An iterable is an object that can return it's value one by one when looped over.
e.g strings, lists, tuples, dictionaries, sets, etc.
"""

name = "clark kent"
for letter in name:
    print(letter)

# enumerate() - a generator function
# returns index and value of each item in the iterable
print(list(enumerate(name)))

for idx, letter in enumerate(name):
    # print(value[0], value[1])
    print(idx, letter)

# range() - a generator function
# returns a sequence of numbers with a given start, stop and step
print(list(range(10)))
print(list(range(1, 11)))
print(list(range(2, 11, 2)))

# print a diamond pattern
for i in range(1, 11, 2):
    print("*" * i)

# For...Else
empty_string = ""
for letter in empty_string:
    print(letter)
else:
    print("empty string")

"""
While Loop

syntax
while <condition>:
    <code>
"""

# RUNS INDEFINITELY
# while True:
#     print("hello, world!")

n = 1
while n <= 10:
    print(n)
    n += 1

x = 0
while x <= 10:
    if x > 0:
        print(x)
    x += 2

z = 0
while z <= 10:
    if z % 2 == 1:
        break
    print(z)
    z += 1

# a = 0
# while a <= 10:
#     if a % 2 == 1:
#         print("found an odd number")
#         continue  # skip the rest of the code and continue with the next iteration

#     print(a)
#     a += 1

# While...Else
while 10 > 90:
    print("hello")
else:
    print("world")
