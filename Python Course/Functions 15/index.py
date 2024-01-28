# function = a block of code which is executed only when it is called.
# you can pass data into a function. Function can return data as a result.
# In python a function is defined using the def keyword
# For Example:
def greeting():
  print("Hello There!")
# this is how to define a function.
greeting()
# writing this, allows you to output a function without using print

# this is pretty simple, we can make some programms using functions.
# Let's start with the basics.
# I've got an idea: let's make a programm, creating an account
# to make it more complex let's ouput hello and user input.
user = input("Enter Your User: ") 
def creating_account():
  print("Hello, @" + user + ".")

creating_account()

# We can pass Information in functions as an argument.
# Arguments are specified after the function name, 
# inside parentheses. You can add as many arguments
# You want, just seperate them with a coma.
# It's like that information is nested in a function.
# When the function is called, we pass along an argument,
# which is used inside an argument to print the argument

def name(firstname, lastname, fullname):
  print("Hello", fullname)
  print("Your first name is " + firstname)
  print("And Your lastname is " + lastname)

name("Yourname", "Yourlastname", "Yourfullname")
# it's pretty easy, now three arguments are nested in a function,
# firstname, lastname and fullname.

# The return statement
# Functions to send python values/objects back to the caller
# These values/objects are known as the function's return value
def multiply(number1, number2):
  result = number1 * number2
  return result
  