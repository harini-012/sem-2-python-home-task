'''A company has different types of employees: Full-Time Employees and Part-Time Employees. Each
employee has common details like name, employee ID, and department. However, the salary
calculation differs for each type:
• Full-Time Employee: Salary is calculated as a fixed monthly salary.
• Part-Time Employee: Salary is calculated based on hourly wages and hours worked.
You are tasked with designing an object-oriented solution using an abstract class to represent the
common behavior and structure of all employees while allowing specific implementations for each
type.
Hint:-
1. Create an abstract class Employee with the following:
o Fields: name, employee_id, department.
o An abstract method calculate_salary().
o A concrete method display_details() to display employee details.
2. Create two subclasses:
o FullTimeEmployee: Implements calculate_salary() for a fixed monthly salary.
o PartTimeEmployee: Implements calculate_salary() based on hourly wage and hours
worked.
3. Write a program to create objects of both types, calculate their salaries, and display their
details.'''

from abc import ABC,abstractmethod
class Salary(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    @abstractmethod
    def display_details(self):
        pass
class FullEmployee:
    def __init__(self,name,emp_id,depart,f_sal):
        self.name=name
        self.emp_id=emp_id
        self.depart=depart
        self.f_sal=f_sal
    def display_details(self):
         print("Name:",self.name)
         print("Employee id:",self.emp_id)
         print("Department:",self.depart)
    def calculate_salary(self):
        return self.f_sal*12
class Parttime:
     def __init__(self,name,emp_id,depart,p_sal,hours):
        self.name=name
        self.emp_id=emp_id
        self.depart=depart
        self.p_sal=p_sal
        self.hours=hours
     def display_details(self):
        print("Name:",self.name)
        print("Employee id:",self.emp_id)
        print("Department:",self.depart)
    
     
     def calculate_salary(self):
        return self.p_sal*hours

name=input("enter  the name:")
emp_id=input("Enter the employee id:")
depart=input("Enter the department:")
while True:
    choice=input("enter f or p for denoting full time or part time employee:")
    if choice=="f":
        f_sal=int(input("Enter the salary for the month:"))
        f=FullEmployee(name,emp_id,depart,f_sal)
        f.display_details()
        sal=f.calculate_salary()
        print("The salary is:",sal)
    if choice=="p":
        p_sal=int(input("Enter the part time salary:"))
        hours=int(input("Enter the number of hours worked:"))
        p=Parttime(name,emp_id,depart,p_sal,hours)
        
        p.display_details()
        sal=p.calculate_salary()
       
        print("The salary is:",sal)
    else:
        print("Invalid choice")
