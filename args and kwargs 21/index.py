# *args = If you do not know many arguments that will be passed
# into your function, add a * before a parameter name in the function
# definition. This way function will recieve a tuple of arguments,
# and can access the items accorfingly. If the number of arguments is unknown
# add a * before the parameter name.
# arg stands for asterisk

# simplified: this parameter will pack all arguments into a tuple
# it is useful so that a function can accept a varying amount of arguments
# def add(num1, num2):
#     sum = num1 + num2
#     return sum

# print(add(1, 2, 3)) 
# since we have 3 values given, it will be an error, so we do this:
def add(*nums): # can be called anything
    sum = 0
# tuple does not support value assigment,
# so you can't change the values: stuff[0] = 0
    stuff = list(stuff)
    stuff[0] = 0
# we turn stuff into a list since a list is changable
    for i in nums: 
        sum += i
    return sum
# we need to iterate, so will use tuples, since it's iterable

print(add(1, 2, 3, 4, 5)) 

# **kwargs = If you do not know how many keyword arguments
# will be passed into your function, add two asterisks: **
# before the parameter name in the function definition.
# two asterisks now are kwargs.
# This way the function will recieve a dictionary of arguments
# and can access the items accordingly

# simplified: parameter that will pack all arguments into a dict
# this is useful so that a function can accept a varying amount of
# keyword arguments.