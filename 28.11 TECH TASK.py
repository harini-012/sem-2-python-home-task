'''1)Write a Python program that demonstrates single inheritance. Create a parent class called Person with
an attribute name and a method show_name to display the name. Create a child class called Student
that inherits from the Person class and adds a new attribute student_id with a method
show_student_id to display the student ID. Create an object of the Student class, and use it to display
both the name and student ID.'''

class Person:
    def getname(self):
        self.name=input("Enter the name of the perosn:")
class Student(Person):
    def getid(self):
        self.id=input("enter the student id:")
    def display(self):
        self.getname()
        print("The name is:",self.name)
        print("The id is ",self.id)
s=Student()
s.getid()
s.display()
print("***********************")

'''2)
Write a Python program to demonstrate single inheritance. Create a parent class Employee with
attributes name and salary, and a method display_details to show the employee's details. Create a
child class Manager that inherits from Employee and adds an attribute department, along with a
method display_department to show the department name. Create an object of the Manager class to
display all details.'''

class Employee:
    def getinfo(self):
        self.name=input("Enter the name of the employee")
        self.salary=int(input("Enter the salary of the employee"))
class Manager(Employee):
    def getdept(self):
        self.depart=input("Enter the department name:")
    def display(self):
        self.getinfo()
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.depart)
m=Manager()
m.getdept()
m.display()
