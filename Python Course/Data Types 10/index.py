# Integer (int):
x = 5
y = -10

# Floating-point (float):
pi = 3.14159
price = 19.99

# String (str):
name = "Alice"
message = 'Hello, world!'

# Boolean (bool):
is_true = True
is_false = False

# List (list):
numbers = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie']
# List = Litteraly a script. Can hold limited variables

# Tuple (tuple):
coordinates = (3.0, 4.0)
colors = ('red', 'green', 'blue')
# working on it
# Tuple = collection which is ordered and unchangeable, 
# used to group together related data.
# it is same as a list, but instead of square brackets []
# we use (). Tuple is a variable which holds limited amount
# of variables.
person = ("Guy", 17, "Male")

person.count("Guy")
# counts how many "Guy" is in the tuple
person.index("Male")
# finds the index of "Male"

# Dictionary (dict):
person = {'name': 'Alice', 'age': 30}
car = {'make': 'Toyota', 'model': 'Camry', 'year': 2022}
# working on it
# Dictionary = a changable unordered collection of unique
# key:value pairs fast because they use hashing, allows
# us to access a value quickly

# Set (set):
unique_numbers = {1, 2, 3, 4, 5}
vowels = {'a', 'e', 'i', 'o', 'u'}
# set = collection which is unordered, unindexed. No duplicate values.
# if a set has duplicated values, it will only display 1. 

# NoneType (None):
empty_variable = None

# Bytes (bytes) and Byte Arrays (bytearray):
binary_data = b'\x00\x01\x02\x03'
mutable_binary_data = bytearray(b'\x00\x01\x02\x03')