# Inheritance - classes can inherite something, usually attributes and methods
# from another class, these classes can form parent-child relationships
# where a child will recieve everything that the parent class has.
# classes can have children and give whatever they won to their children
# and in today's video we'll be creating a parent class called animal and children
# children of the animal class will inherit the common attributes and methods that
# all animals can have. (example2.png/jpg/jpeg)
class Animal:
    alive = True

    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")

class Rabbit(Animal):
    pass

class Fish(Animal):
    pass

class Hawk(Animal):
    pass

# this is a shortcut instead of assigning same code to each of the classes

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
# .alive = inheritance, even though rabbit function doesn't have class variable in