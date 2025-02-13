# Sets
"""
A set a unique collection of items
"""

numbers = {1, 2, 2, 2, 3, 4, 4, 5, 5}
print(numbers)

universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
x = {1, 2, 3, 4, 5}
y = {6, 7, 8, 9, 10}
z = {11, 12, 13, 14, 15}

print(x.intersection(y))
print(x.intersection(universal_set))
x.intersection_update(universal_set)  # x = {*x, *x.intersection(universal_set)}
print(x)

print(x.union(y))

print(x.difference(z))
print(z.difference(x))

print(x.pop())
print(x)

y.remove(6)
print(y)
