# type casting = convert the data types of a value intop another type
x = 1 # integer
y = 1.5 # float
z = "3" # string

# Let's turn these into strings. How? its done very easily
x_2 = str(x)
y_2 = str(y)
z_3 = str(z)
# They are now strings, if we add 1 to them:
# x_2 = 11
# y_2 = 11 - 1.5 is float so will change to the first index
# z_3 = 31

print(z * 3)
# Since z is a string, it will output 333

print(float(1))
# Will output 1.0 since float is same a full number

# Lets say that we want to output a sentence, for example:
# x equals 1, and y equals 1.5. Tehir sum is 2.5
# If this came first on your mind:
# print("x is "+ x +", and y is "+ y +". Their sum is: "+ x + y)
# This is wrong. as was mentioned: you can't combine strs and ints
# Why? Answer, whats the sum of burger and 2? 
# Exactly, this is the dumbest question ever.
# How to do it:
print("x is "+ str(x) +", y is "+ str(y) +". Their sum is: " + str(x + y))
# The output is: x is 1, y is 1.5. Their sum is: 2.5
