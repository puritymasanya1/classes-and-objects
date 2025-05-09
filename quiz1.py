'''
create a car class that uses __init__ to set the brand, model and year
and uses __str__ to print something like 'Toyota made in 2021'
'''


class Vehicle:

    def __init__(self, car, model, year):
        self.car = car
        self.model = model
        self.year = year

    def __str__(self):
        return f" The {self.car} {self.model} was made in {self.year}."


my_car = Vehicle("Toyota", "Corolla", 2000)

print(my_car)
