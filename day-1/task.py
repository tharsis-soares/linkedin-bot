# strings
print('hello world')

# numbers
print(1 + 2)

# booleans
print(True)

# lists
print([1, 2, 3])

# dictionaries
print({"name": "Alice", "age": 25})

# variables

name = "Alice"

print(name)

# functions
def say_hello():
    print("Hello!")

say_hello()

# loops
for i in range(5):
    print(i)

# conditionals

if 1 > 2:
    print("1 is greater than 2")
else:
    print("1 is not greater than 2")

# classes
class Greeter:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")

greeter = Greeter("Alice")
greeter.say_hello()

# imports
import math

print(math.sqrt(16))

# libraries

import requests

response = requests.get("https://www.google.com")

print(response.status_code)

# writing files
with open("hello.txt", "w") as file:
    file.write("Hello, world!")


# reading files
with open("hello.txt", "r") as file:
    print(file.read())

# command line arguments

import sys

print(sys.argv)

# environment variables

import os

print(os.environ["HOME"])