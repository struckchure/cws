"""
Modules and Packages

A module is a collection of code snippets, so parts can be reusable and some just perform specific actions. In python a module can be a single python file.

A package is a collection of modules.

syntax:
import <module_name>
from <module_name> import <function_name>
import <package_name>

<package_name>.<module_name>.<function_name>

from <package> import <module>
"""

import math

print(math.sqrt(16))
print(math.pi)
print(math.factorial(5))
print(math.sin(90))

from random import choices, randint

print(choices([1, 2, 3, 4, 5]))
print(randint(1000, 9999))

from datetime import date, datetime

# from datetime import * # DON'T USE THIS

print(date.today())
print(datetime.now())

from my_module import greetings

greetings("ade")

from my_module import greetings as say_hello

say_hello("ade")
