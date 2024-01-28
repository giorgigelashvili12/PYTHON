# slicing = create a substring by extracting elements from another string

# indexing[] or slice()
# [start:stop:step]
# index operator [] = gives access to a sequence's element
# (str, list, tuples, dicts). Can work and select 
# elements/values from lists, tuples and dicts.
# start - from what index to start
# stop - what index to stop at
# step - How much is index increased

name = "Giorgi Gelashvili"
first_name = name[0:6] # long way
# shorter way
first_name = name[:6] # shortcut
# every letter to 6

second_name = name[7:18] # long way
# shorter way
second_name = name[7:] # shortcut
# from 7 to the last letter
# [start:stop:step]

# step
test_name = name[0:18:2]
# from 0, to 18, include every second character
# shorter
test_name = name [::2]

# How to reverse a string
reverse = name[::-1]
# same like counting backwards
# creating a new substring based off my name!

# Slicing a variable step by step
some_guy = "Jack Bigol Lawson"
first = slice(0, 4)
# same thing! 0 = from where, 4 = where to
print(some_guy[first])

print(test_name)
print(first_name)
print(second_name)