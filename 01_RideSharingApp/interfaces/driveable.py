from abc import ABC, abstractmethod

class Driveable(ABC):
    @abstractmethod
    def drive(self):
        pass
    