# python object oriented programming = POOP
# What is object-oriented programming?
# Object-oriented programming (OOP) is a computer programming model 
# that organizes software design around data, or objects, rather 
# than functions and logic. An object can be defined as a data 
# field that has unique attributes and behavior.
# OOP focuses on the objects that developers want to manipulate rather
# than the logic required to manipulate them. This approach to programming
# is well-suited for programs that are large, complex and actively updated
# or maintained. This includes programs for manufacturing and design, as
# well as mobile applications; for example, OOP can be used for manufacturing
# system simulation software.
# The first step of OOP is to collect every object that programmer wants to work on.
# this is known as data modeling. Once the object is known, it is labeled
# as a class of objects that defines data it contains, can be any logical sequences
# that can manipulate it. Every logic sequence is known simply as a method.
# The structure/building blocks of OOP includes:
# Classes, they are used data-types which work on objects attributes and methods.
# Objects are instances of a class created with specifically defined data.
# Methods are functions which are defined inside a class that describr the object
# If we had a human given it would be like this:
# class - human; object - name; properties - email, adress; methods - verify, send email.

# class Car:
#     make = None
#     model = None
#     year = None
#     color = None

#     def drive(self):
#         print("Driving")

#     def stop(self):
#         print("Stopped")
# The self parameter is a reference to the current instance of the class, and is
# used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has
# to be the first parameter of any function in the class:

# special method is needed which is known as a init method (__init__), that will construct
# methods and create objects for us, so we need to define this method
class Car:
    def __init__(self, make, model, year, color): # self as an argument
        self.make = make
        self.model = model
        self.year = year
        self.color = color # self. is referring to the object we're currenly working on
# need to pass them in as an argument in our init method so we need to set up some parameters
    def drive(self):
         print(self.make + " is driving")

    def stop(self):
        print(self.make + " has stopped")
    # two methods.