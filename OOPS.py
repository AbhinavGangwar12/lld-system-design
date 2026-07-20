class CAR:
    def __init__(self, model, year):
        self.model = model
        self.year = year

car = CAR("Toyota", 2020)
print(car.model)  # Output: Toyota
new_car = CAR("Honda", 2021)
print(new_car.year)  # Output: 2021