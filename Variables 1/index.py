# variable = a container which holds a value. Behaves as a value that it contacins

name = "YourName"
# variable 'name' holds a string value "YourName"
# Strings are like texts, if string is surrounded by
# double qutoes (""), it is a string.
# We can also create string usin single quotes ('')

print(name)
# print outputs anything that is put in it's parentheses/brackets/braces\
# Output is in console, to see it click play icon on top left corner
# In your programme that you are using.

print("Hello " + name)
# Console: Hello YourName
# Just like that!

print(type(name))
# This line of code will output the data type of this variable.
# As we know, variable 'name' is a string, which means,
# Console: <class 'str'>


# Can combine variables if they are the same type
# You are given 2 examples, true and false

# 1. True example (working):
first_name = "1stName"
second_name = "2ndName"
print(first_name + " " + second_name)
# 1stName + space + 2ndName -> 1stName 2ndName
# SHORTER VERSION AND BETTER TOO
full_name = first_name + " " + second_name
print("Hello " + full_name)
# Console: Hello 1stName 2ndName

# 2. False example (not working):
#In this part you will also learn integerts (int)
age = 21
# variable age holds an integer value.
# integer is same as a number
# Combining and shortcuts
age = age + 1
# Console: 22, updates variable 
# Shorter way
age += 1
# Now Combining strings and numbers
print(age + full_name)
# This is the biggest mistake, like in math, 
# You cant combine text and a number together
# A typeError

# to combine them together you shoudl convert age into a str
# one way: type casting
# str(age) is now a string
# int(age) is now an integer

# Float datatype, same as a whole number
height = 250.5 # A float

# Booleans: True and False
human = False
# variable human is a boolean