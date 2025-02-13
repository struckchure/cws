# Dictionary
"""
Just like the standard dictionary, you have a word and the meaning, in python you a key (word) and a value (meaning).

Syntax: {<key-1>:<value-1>, <key-2>:<value-2>, ..., <key-n>:<value-n>}
Key should be a string and value can be anything.
"""

profile = {
    "name": "John",
    "age": 25,
    "hobbies": ["reading", "coding", "gaming"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345",
    },
}

print(profile)
print(profile["name"])
print(profile["address"]["state"])

print(profile.keys())
print(profile.values())
print(profile.items())
# print(profile["not-a-key"]) # value that does not exist
print(profile.get("not-a-key"))  # use this if the key does not exist
print(profile.get("name"))
print(profile.pop("address"))
print(profile)
del profile["hobbies"]
print(profile)

# Merge 2 or more dictionaries

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {**d1, **d2, "e": 5}
print(d3)

# Extending a dictionary

d1.update(d2)
print(d1)
