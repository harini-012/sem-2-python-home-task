'''1. You are developing a vehicle management system for a transportation company. The system
should handle different types of vehicles, such as Cars and Bikes. Each vehicle has a method
called fuelType() that specifies the type of fuel it uses.
However, different vehicles use different fuels, so you need to
implement method overriding to ensure each vehicle class
provides its own fuel type.
Task:
• Create a base class Vehicle with a method fuelType() that
returns "General Fuel".
• Create two subclasses Car and Bike, both inheriting from
Vehicle.
• Override the fuelType() method in each subclass:
• The Car class should return "Petrol or Diesel".
• The Bike class should return "Petrol".
• Create objects of Car and Bike and call their fuelType()
methods to demonstrate method overriding.'''


class Vehicle:
    def fueltype(self):
        return "General fuel"
class Car(Vehicle):
    def fueltype(self):
        return "Petrol or Disel"
class Bike(Vehicle):
    def fueltype(self):
        return "Petrol"

v=Vehicle()
a=v.fueltype()
print("Vehicle:",a)
c=Car()
a=c.fueltype()
print("Car fuel type:",a)
b=Bike()
an=b.fueltype()
print("Bike fuel type:",an)

