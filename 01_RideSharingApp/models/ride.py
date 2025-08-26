from enums.ride_status import RideStatus

class Ride:
    def __init__(self, rider, driver, car_type):
        self.rider = rider
        self.driver = driver
        self.car_type = car_type
        self.status = RideStatus.REQUESTED
    
    def start_ride(self):
        self.status = RideStatus.ONGOING
    
    def complete_ride(self):
        self.status = RideStatus.COMPLETED
    
    def cancel_ride(self):
        self.status = RideStatus.CANCELLED

    def __str__(self):
        return f"Ride({self.car_type.value}) | {self.rider.name} with {self.driver.name} | Status: {self.status.name}"