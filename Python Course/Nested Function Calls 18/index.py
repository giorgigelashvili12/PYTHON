# nested function calls = function calls inside other function calls.
# innermost function calls are resolved first. returned value is used
# as argument for the next outer function

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)
# not so cool way..
# the second way is easier and shorterL
print(round(abs(float(input("Enter a whole positive number: ")))))
# first we start rith the inner function, input
# and resolve that first whatever value is returned
# we use as an argument to the next outermost function
# and in this case it would be float, then we resolve that
# then we move on absolute value, then round and then print.
# this is just a way of writing a code which doesn't takes
# more than a 1 line of code.