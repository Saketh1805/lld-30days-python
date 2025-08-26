from models.car import Car
from models.driver import Driver
from models.rider import Rider
from models.ride import Ride
from enums.car_type import CarType

#setup: 3 Driver
drivers = [
    Driver("Alice", Car("TX123", CarType.MINI)),
    Driver("Bob", Car("MA456", CarType.SEDAN)),
    Driver("Carol", Car("NY789", CarType.SUV))
]

#setup: 1 rider
rider = Rider("Alex")

#Rider requests a sedan
request_type = CarType.SEDAN
available_driver = next((d for d in drivers if d.car.car_type == request_type), None)

if available_driver:
    ride = Ride(rider, available_driver, request_type)
    rider.add_ride(ride)

    print("Ride Created:", ride)
    ride.start_ride()
    print("Ride Started:", ride)
    ride.complete_ride()
    print("Ride Completed:", ride)

else:
    print(f"No {requested_type.value} available right now.")