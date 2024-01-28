# nested loops = The "inner loop" will finish all of it's iterations before
# finishing one iteration of the "outer loop". Simplified, nested loop is a
# loop inside another loop.
# let's make a symple or dumb programm as an example
first_num = int(input("Enter your first number "))
second_num = int(input("Enter your second number "))
symbol = input("Enter a symbol ")

for i in range(first_num):
    for j in range(second_num):
        print(symbol)
    print()
# as we see a loop is inside an another loop.
# what does this programm do?
# variable first_num displays "rows" but one by one,
# variable second_num displays lines of an symbol input.
# for exampl if we typed 2, 4 and a % sign it would display:
# %
# %
# %
# %

# %
# %
# %
# %