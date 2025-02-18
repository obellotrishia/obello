class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"Brand: {self.brand}, Model:{self.model}, Year:{self.year}"

# Example of creating a Car object
my_car = Car("Toyota", "corolla", 2020)
print(my_car.display_info())