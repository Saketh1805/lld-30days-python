class Rider:
    def __init__(self, name:str):
        self.name = name
        self.ride_history = []
    
    def add_ride(self, ride):
        self.ride_history.append(ride)
    
    def __str__(self):
        return f"Rider: {self.name}, Total Rides: {len(self.ride_history)}"

    