# keyword arguments = arguments preceded by an identifier
# when we pass them to a function. The order of the arguments
# doesn't matter, unlike positional arguments. Python knows
# the names of the arguments that our function recieves

def greet(first, middle, last):
    print("Hello " + first + middle + last)

greet(last="brotha?", first="Name ", middle="wassup ")