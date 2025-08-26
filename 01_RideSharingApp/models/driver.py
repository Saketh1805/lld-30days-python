from interfaces.driveable import Driveable
from models.car import Car

class Driver(Driveable):
    #Constructor
    def __init__(self, name: str, car: Car):
        self.name = name
        self.car = car

    def drive(self):
        print(f"{self.name} is driving {self.car}")

    def __str__(self):
        return f"Driver: {self.name} with {self.car} "