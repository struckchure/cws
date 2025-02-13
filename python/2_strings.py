"""
Strings: Anything within quotation mark (`'`, `"`)
"""

name_of_film = "007 James Bond"

print("Hello!")
print(name_of_film)
print(type(name_of_film))
print(name_of_film.upper())
print(name_of_film.lower())
print(name_of_film.isalpha())
print("james bond".isalpha())
print("jamesbond".isalpha())
print(name_of_film.isnumeric())
print("007".isnumeric())
print(name_of_film.isalnum())
print("007JamesBond".isalnum())
print(name_of_film.split())
print("10/12/2045".split("/"))
print(len(name_of_film))

# Indexing

print("James"[0])
print("James Bond"[4])
print("James Bond"[-1])
print("JAMES"[::-1])
