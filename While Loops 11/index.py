# while loop = a statement that will execut it's block of code
# as long as it's condition remains true.

# Let's talk about meaning of the loops.
# word "loop" should be known to a lor of people.
# so loop is like a cycle that is that doesn't end.
# it regularly is repeated in the same order.

# in python we have two <u> primitive </u> loop commands:
# 1. while loops, this lesson
# 2. for loops.

# as we said, while loop can execute a statement, or a set of statements
# as long as a condition is true. This is how it works.
i = 1
# we made a variable i, there's no special meaning,
# it's just mostly used and "easier" to use.
while i < 6: # while i is less than 6
    print(i) # print i (1)
    i += 1 # and every time change variable to var-value + 1
# without i += 1, this would be an endless loop, that continues
# and goes on. (don't let your device catch on fire)
# so this loop would be like this in a sentence:
# while i is less than 6, output variable i, 1,
# but output evereytime and add 1, then end the programm
# when it reaches 5.
# 1, 2, 3, 4, 5.
# += can be called as an increment in while loops.

# WHILE LOOP BREAK STATEMENT ---------------------
# with the break statement we can stop the loop/cycle
# even if the while condition is true.
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
# since we learned if statement, this should be easier to understand.
# while i is less than 6 print i, and increase by 1, when output everytime
# but IF i (value) is equal to 3, then break/Stop/End the programm
  
# WHILE LOOP CONTINUE STATEMENT ------------------
# with continue statement we can stop the current iteration
# and continue with the next ones
while i < 6:
  print(i)
  if (i == 3):
    continue
  i += 1
# let's go to the if statement since we already know
# how while statement works. so it will output 1 and 2
# as normal, but if i is equal to 3 continue the loop
# till it reaches 5. Note that 3 is ignored and not output.
# why? because it says IF i = 3, then CONTINUE 
# this way sound confusing but when you'll leanr you'll get used to it

# WHILE LOOP ELSE STATEMENT ----------------------
# simmiliar right? yes we learned else statement in if statements.
# what about in while loops? does this make any difference?
# Nope! Nothing changes! Works just like in if statements:
# if condition is no longer true, then else statement activates.
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Now let's make a simple programm using while loop.
# Idea: Ask user their name (input()), if its blank
# don't stop spamming until user actually enter in their name.
# we also might learn something!
name = ''
while len(name) == 0:
  name = input("Enter Your Name: ")
print("Hello, " + name)
# len() function returns a number of items in an object
# when an object is a string, the len() function returns
# the number of characters in the string.
# in this part, if variable name <u>chars</u> are 0 (empty)
# ask user their name, ENDLESLY.

# WHILE LOOP PASS STATEMENT ----------------------
for i in range(1, 21):
  if i == 13:
    pass
  else:
    print(i)
# same as countinue statement, if i is equal to 13,
# pass/ignore 13 and continue