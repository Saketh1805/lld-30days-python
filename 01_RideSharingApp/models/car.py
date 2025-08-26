from enums.car_type import CarType

class Car:
    #Constructor
    def __init__(self, number_plate: str, car_type: CarType):
        self.number_plate = number_plate
        self.car_type = car_type
    
    def __str__(self):
        return f"{self.car_type.value} Car, with Number Plate: {self.number_plate}"