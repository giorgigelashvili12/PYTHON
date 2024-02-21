# scope =  the region that a variable is recognized.
# a variable is only available from inside the region
# it is created. a global and localy scoped versions of
# a variable can be created.
# local - is only declared in a function and can be ONLY accessed in THIS function
# global - declared ouside a function, so it can be accessed both in outside and inside function
name = "name" # Global Scope (available inisde & outside functions)

def display():
    name = "name" # local scope (available only in this function)
    print(name) # can call both blobal and local scope
    #(if name in func would be nested)
    # python will follow this rule called legb
    # l = local; e = enclosing; g = global; b = built-in

# local scope = can't use outside a function, can't just print it
# if it's outside a function
display()
print(name)