# many parameter functions exist in python, with them
# you can work in lists, strings and much more.
# First function:
# len()
# len stands shortly for length. it has two functions.
# 1. it counts elements on lists 
# 2. counts any character, symbols, numbers, letters and spaces in a string.
# yes we learned this but let's view examples and use it in lists.
# let's create an array/list
num = [1, 2, 3, 4, 5]
# Num holds 5 values, 1, 2, ..., 5
print(len(num))
# with len() parameter, we can count how many values it holds,
# easy peasy, the answer is 5.

# can count characters in strings too:
word = "shambalamba ding-dong"
print(len(word))
# the word "shambalamba ding-dong" contains 21 characters,
# REMEMBER! spaces and symbols count too!

# Now let's work with lists.
# let's say, we created a list, and want to add another element
# without changing any code/list.
# for this we use .append() function
# append adds an element in the back of the list.
# let's view and example and see how it works:
grocery_list = ["apple", "milk", "flour", "bread"]
# - oops! I forgot some cookies!
# - Don't worry, I'll help
grocery_list.append("Cookies")
# Now, we wanted to add cookies in the list without changing it,
# so we used append function. when we write .append, 
# we write anything we want in () to add in the back of the list.
# Very easy...
print(grocery_list)
# - Done!
# - You're my hero!

# Let's see another one.
# We've got... .insert() function!
# What does it do?
# In english, insert means to push something into something else.
# and tha's right! usign insert function we can add 
# anything in the list. You can think, "whats the difference bettwen append and insert?"
# append function adds list in the back of the list
# and with insert we can add anything on any index we want.

word_pack = ["Python" "fun!"]
word_pack.insert(1, "is")
# And the output is: "Python is fun!"
# let's explain what happened.
# what does 1 in insert do?
# 1 defines an index. You can put in any number you want!
# in this example, we put string "is" on the first index, after "Pyhton"
# REMEMBER! counting in python and some countries start
# from 0, 1, 3, 4, and etc.

# I've also got another one!
# .count() - TADAA!!! now what does it do?
# count function counts how many times something is repeated.
# to find that "something" we put that "something" in ()
# i.count("Something")
i = ["Something", "That", "Is", "Crazy", "Is", "Something"]
print(i.count("Something"))
# The output is 2, count function finds
# how many times string "Something" is repeated in the list.
# this one is pretty easy too.

# You think im finished? YOU WISH, ive got 3 more
# .remove(), I think it's pretty easy to understand what it does.
# ill still explain though...
# with remove method, we can remove an element from the list:
x = [2, 4, 6, 2, 7, 2, 9]
x.remove(2)# as usual, you put something you want to remove
# from the3 list in the ()
# don't just print x.remove(2) bro, it won't work..
print(x)
# Note this: it only removes the first 2 in the list, not all of them.

# Two more, knowing more is true power!!
# .reverse(), this is easy to understand too.
# reverse means moving in backwards,
# but here, it means ALIGNING elements backwards.
list = ["Mi", "Yu", "Her", "Him"]
list.reverse() # done! the list is now backwards.
print(list)
# print to see the proof!
# EASY!!!

# LAST ONE, 
# the .format() function.
# Format method formats specified values and inserts them inside the strings placeholder.
# placeolder is defined with curly brackets {}. returns a formatted string
# can be used with a list
family = ["Mom", "Dad", "Me"]
txt1 = "I love my {}".format(family[0])
txt2 = "I love my {}".format(family[1])
txt3 = "I love {}".format(family[2])
# REMEMBER! {} are placeholders, where the value should be put.
print(txt1)
print(txt2)
print(txt3)

# Can be used like this too:
# named indexes
msg1 = "My name is {name}, I'm {age}".format(name = "name", age = 20)
# created "variables" in format and output using placeholder
print(msg1)

# numbered indexes
msg2 = "My name is {0}, I'm {1}".format("name", 20)
# 1. put in what's on index 0 (in format)
# 2. put in what's on index 1 (in format)
print(msg2)

# empty placeholders
msg3 = "My name is {}, I'm {}".format("name", 20)
# aligns one by one, no indexes
print(msg3)

# fine I lied, a little more 
# set() function,
# set() function is a mathematical function, For example:
# if we put list in set, every repeated element will dissapear
x = [2, 4, 6, 2, 4, 7, 2, 9]
y = set(x)
print(y)
# as you can see, theres one two left, instead of 3
# one four, instead of 3
# and else was not repeated

# .join() function
# join allows to add something in list.
x = ", ".join(["spam", "eggs", "ham"])
print(x)
# in alist, adds , after every element, since we put in so..
# join() result is a string.

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5))
# defined a lambda function that takes one argument
# a and returns the result of the expression a + 10.
# Then, you call the lambda function with the argument 5,
# and it prints the result, which is 15.
# lambda a : (a is an expression)
# a + 10, this is a calculation
# x(5) = a is now equal to 5
# Add 10 to argument a, and return the result:
# here, a = 5, so a calculation happens this way:
# 5 + 10 = 15

# .pop() method
# pop method allows us to remove an element from the list.
#       .pop              (   )
# function name     index of element which has to get removed
# leaving parentheses blank, will remove the first element in the list
manufacturers = [  "Honda", "Volvo", "Mercedes"  ]
manufacturers.pop(1)  #0      #1      #2
print(manufacturers)

# clear function
# clear function is much easier
# clear function deletes every element from the list
fruits = ["apple", "banana", "cherry"]
fruits.clear() # shlis siashi mocemul yvela elements
print(fruits)

# clear function
# if we assign another variable a copy of a list, they will both have the same values
# var2 = var1.copy() 
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

# extend function
# extend function allows us to expand a list with another list just like this:
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars) 
print(fruits)

# sort function 
# sort function allows us to align list's elements alphabetically
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)