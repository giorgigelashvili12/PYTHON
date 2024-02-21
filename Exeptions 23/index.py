#exeption = events detected during an execution that interrupts a flow of a programm

# num1 = int(input("Enter a number to divide: "))
# num2 = int(input("Enter a number to divide by: "))
# result = num1 / num2
# print(result)
# for example, if we divide something by 0,
# since it's not possible in maths, it will output error
# and stop the programm. to fix this, we simply do this:
try:
    num1 = int(input("Enter a number to divide: "))
    num2 = int(input("Enter a number to divide by: "))
    result = num1 / num2
    # if this code is dangerous, try it out
    # and continue with...
except ZeroDivisionError:
    print("Can't divide by 0.")
    # ZeroDivisionError - if there is an error for example:
    # 5 / 0, if so, print that
except ValueError:
    print("Enter only numbers.")
    # ValueError - in this, if str is put in int input,
    # then handle it by doing so. (this code)
except Exception:
    print("Mathematical Error.")
    # if try code does not work, then do not outpout error
    # and do this
else:
    print(result)
    # if there are no errors, output result 
finally:
    print("Process Finished. End Of Program.")
    # this will always execute