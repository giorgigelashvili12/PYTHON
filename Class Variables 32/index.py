class Car: 
    wheels = 4 # class variable
    # declared in a class but outside a constructor

    def __init__(self, make, model, year, color): 
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        # Instance variables - have values assigned