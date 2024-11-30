'''1. Scenario: Library Management System
Creating a simple library management system where:
• Library handles book details.
• Member handles member details.
• LibraryManagement combines the features of both Library and Member
and allows borrowing books'''


class Library:
    def __init__(self,bookname,price):
        self.bookname=bookname
        self.price=price
    def display_book(self):
        print("Book name:",self.bookname)
        print("Price:",self.price)
class Member:
    def __init__(self,member_name,member_age):
        self.member_name=member_name
        self.member_age=member_age
    def display_mem(self):
         print("Member name:",self.member_name)
         print("Age:",self.member_age)
class LibraryManagement(Library,Member):
    def __init__(self,bookname,price,member_name,member_age):
        super().__init__(bookname,price)
        Member.__init__(self,member_name,member_age)
    def display(self):
        self.display_book()
        self.display_mem()
lib=LibraryManagement("Ponniyin selvan", 2000,"Harini",18)
lib.display()

print("****************************")



'''22. Scenario: Food Delivery System
Create a system where:
• Restaurant handles the menu and food preparation.
• Delivery manages the delivery details and rider information.
• Order combines both Restaurant and Delivery to process food orders
and manage delivery logistics.'''



class Restaurant:
    def __init__(self,menu,food_preparation):
        self.menu=menu
        self.food_preparation=food_preparation
    def display_res(self):
        print("Menu:",self.menu)
        print("Food preparation:",self.food_preparation)
class Delivery:
    def __init__(self,location,rider_name):
        self.location=location
        self.rider_name=rider_name
    def display_del(self):
        print("Location:",self.location)
        print("Rider Name:",self.rider_name)
class Order(Restaurant,Delivery):
    def __init__(self,menu,food_preparation,location,rider_name):
        super().__init__(menu,food_preparation)
        Delivery.__init__(self,location,rider_name)
    def display_ord(self):
        self.display_res()
        self.display_del()
res=Order("Poori","frying","west mambalam", "Rio")
res.display_ord()
