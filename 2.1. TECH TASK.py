'''Suppose you are creating a system for calculating payments for different types of employees, such as
salaried employees and hourly employees. Each employee type has a different way of calculating
their payment, but all employees should have a common interface.
Classes :
Abstract class : Employee
Abstract method : calculate pay
Concrete class :SalariedEmployee (Atrributes: Annual salary)
-CalculatePay() – should return the monthly pay of the employee
HourlyEmployee(Attributes – hoursworked and hourlyrate)
-CalculatePay() will return the pay based on the hours worked and rate.
Sample Input and Output:
For example, if you create a SalariedEmployee with an annual salary of $60,000 and an
HourlyEmployee with a rate of $20/hour who worked 120 hours, the program should calculate and
display their pay as follows:
Salaried Employee (John Doe) Pay: $5000.00
Hourly Employee (Jane Smith) Pay: $2400.00'''

from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass
class SalariedEmployee:
    def __init__(self,annualsalary,hours_w,hourly_r):
        self.annualsalary=annualsalary
        self.hours_w=hours_w
        self.hourly_r=hourly_r
    def calculate_pay(self):
        return annualsalary/12
    def hourly(self):
        return (hours_w)*hourly_r
annualsalary=int(input("Enter the annual salary"))
hours_w=int(input("Enter the number of hours worked"))
hourly_r=int(input("Enter the hourly rate"))
a=SalariedEmployee(annualsalary,hours_w,hourly_r)
print("Monthy salary:",a.calculate_pay())
print("Hourly employee:",a.hourly())

    
