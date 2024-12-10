'''Q-1) Vehicle – example hybrid inheritance
1. Vehicle (Base Class): Represents a general vehicle with basic attributes like
make, model, and year.
2. Car (Derived from Vehicle): Represents cars, which have additional
features like the number of doors and trunk capacity.
3. Truck (Derived from Vehicle): Represents trucks, which have attributes
like cargo capacity and number of axles.
4. PickupTruck (Derived from both Car and Truck): A specific type of vehicle
that combines features of both cars (passenger-friendly) and trucks (cargofriendly). Method – display all the features.'''


class Vehicle:
    def __init__(self):
        self.make=input("Enter the country name where the engine of the vehicle is made")
        self.model=input("Enter the model of the vehicle")
        self.year=int(input("Enter the year in which the vehicle is made"))
    def displayVehicle(self):
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)
class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.doors=int(input("Enter the number of doors in the car"))
        self.capacity=int(input("Enter the number of persons can sit in the car"))
    def displayCar(self):
        print("Doors:",self.doors)
        print("Capacity:",self.capacity)
class Truck(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.cargo=input("Enter the cargo capacity")
        self.pixels=int(input("Enter the number of pixels"))
    def displayTruck(self):
        print("Cargo:",self.cargo)
        print("Pixels:",self.pixels)
class PickTruck(Car,Truck):
    def __init__(self):
        Car.__init__(self)
        self.cargo=input("Enter the cargo capacity")
        self.pixels=int(input("Enter the number of pixels"))
        self.pickup=input("Enter the pick up location")
    def displayPickup(self):
        print("Pickup:",self.pickup)
t=PickTruck()
t.displayVehicle()
t.displayCar()
t.displayTruck()
t.displayPickup()

''''#2)
1. Product (Base Class): Defines common attributes like product ID, name,
and price. Method to display all the info.
2. Electronics (Derived Class): Inherits from Product and adds attributes
like warranty period and brand. Method to display all the info.
3. Clothing (Derived Class): Inherits from Product and adds attributes like
size and material. Method to display all the info'''


class Product:
    def __init__(self):
        self.p_id=input("Enter the product id")
        self.name=input("Enter the name")
        self.price=int(input("enter the price"))
    def displayProduct(self):
        print("Product ID:",self.p_id)
        print("Name:",self.name)
        print("Price:",self.price)
class Electronics(Product):
    def __init__(self):
        Product.__init__(self)
        self.waranty=int(input("Enter the waranty years"))
        self.brand=input("Enter the brand")
    def displayElectronics(self):
        self.displayProduct()               
        print("Waranty:",self.waranty)
        print("Brand:",self.brand)
class Clothing(Product):
     def __init__(self):
         Product.__init__(self)
         self.size=input("enter the size")
         self.material=input("Enter the material")

     def displayClothing(self):
        print("Size:",self.size)
        print("Material:",self.material)

e=Electronics()
e.displayElectronics()
c=Clothing()
c.displayClothing()

