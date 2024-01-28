# if statement = a block of code that will execute if the conditing is true
# how it works
# if the condition is true, execute a code, if not and the other condition is true then execute that

age = int(input("How old are you?: "))

# if age >= 18: # if age is more or equal to 18,
#     print("You are an adult!") # then exeture this
# else: # if top is false, then execute this:
#     print("HAHA kiddo.")

# What if we need more than 2 conditions?
# we can't just do if, if, if and else.
# That is the biggest mistake as a python developer.
# you only use if and else ONCE in the if statement!
# so we do simply:
if age == 100:
    print("Bro.. Thats a lot...")
    print("'III'M STILL STANDIN...'")
elif age < 0:
    print("Still in mommas belly?")
    print("Blud's still in the tutorial")
elif age >= 18:
    print("You are an adult!")
else:
    print("HAHA kiddo.")
# yes we SHOULD use if and else only ONCE, but
# can use elif a BUNCH OF TIMES in an if statements
# as much as we want, should work though.
    
# Let's say for example: we need to make a same
# if statement code (up), and we need to assign 
# two different functions a same print code,
# an Looza programmer would write if and elif
# with same prints.
# A Genius one would write that in one line...
# How?!... This is how:
# Okay so we need to learn a bunch of types of operators..
# first one is
    
#--------- PYTHON LOGICAL OPERATORS --------------
# 1. and - Returns True, if both statements are true
# 2. or  - Returns True if one of the statements is true
# 3. not - Reverse the result, returns False even if 
#          the result is true
    
#--------- HOW TO USE THEM -----------------------
# 1. and operator
x = 5
y = 4
if x < 5 and x < 10:
# if x is greater than 5 and x is less than 10 print this below
# Since none of them are true, this print code will not be executed
    print("So x is less than 5 AND x is less than 10")
elif y == 5 or y > 2:
# if y equals to 5 or y is more than 2 print code down below
# y doesn't equal to 5, BUT is greater than 2,
# and SINCE one of these is TRUE, will be still output
    print("y is greater than 2 OR is equal to five")
elif not(x == 5) and not(y == 4):
# REMEMBER not() switches ture statements to false
# and flase to true
    print(False)

# You will learn ALL Operators in one of the lessons