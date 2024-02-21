from index import Car
# importing class from file

car_1 = Car("Honda", "Fit", 2011, "silver")
car_2 = Car("Mustang", "NaN", "NaN", "NaN")
# given 4 arguments
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_2.stop()