from enum import Enum
from abc import ABC, abstractmethod

class VehicleType(Enum):
    CAR = "Car"
    TRUCK = "Truck"
    BIKE = "Bike"

class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"
    
class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"
    
class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> str:
        pass

class CarFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Car()

class BikeFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Bike()
    
class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Truck()
    

    