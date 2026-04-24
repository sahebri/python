from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class car (vehicle):
    def start (self):
        print("Starting")
    def stop (self):
        print("Stop")
my_car=car()
my_car.start()
my_car.stop()