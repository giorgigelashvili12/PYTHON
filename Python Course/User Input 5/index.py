# input usually means something that is detected and goes in
# to get and execute user input in python we use:
# input()
# this is black input, we SHOULD tell user what to put in.
# So we do this very simply:
# input("What's Your Name? ")
# to submit the input you just press enter on your keyboard

# input function can be assigned to a variable, so we can do
# some things and functions with it, for example:
# name = input("What's Your Name? ")
# heres one thing we can do:
# we can display a mesage saying, hello {name>value}
# print("Hello, " + name)

# let's say we want to run a program asking your name and age
# now REMEMBER! we can't combine ints and strs together!
name = input("What's Your Name? ")
# input's value is defined as a string data type
# To change data type we use type casting:
age = int(input("And What's Your Age: "))
# Only integer should be put in, else = error

print("Hello, " + name)
print("You are " + str(age) + " years old.")
# now don't forget this!