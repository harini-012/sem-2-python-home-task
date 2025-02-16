'''1.Imagine you are building an Employee Management System where you need to store employee
details and calculate their yearly salary.
• The __init__ method initializes attributes: name, emp_id, and salary.
• display_info() prints employee details.
• calculate_yearly_salary() computes the yearly salary.'''




class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    def display(self):
        print("Name:",self.name)
        print("Employee id:",self.emp_id)
        print("Salary:",self.salary)
    def calculate_salary(self):
        ann_sal=self.salary*12
        print(" Annual Salary:",ann_sal)
name=input("Enter the name of the employee")
emp_id=int(input("Enter the employee id"))
salary=int(input("Enter the monthly salary"))
e=Employee(name,emp_id,salary)
e.display()
e.calculate_salary()



'''2. You are developing an Employee Management System for a company where there are two types of
employees:
• Full-Time Employees who receive a fixed monthly salary.
• Part-Time Employees who are paid based on the hours they work.
Since all employees share common attributes (name, employee ID, and department), you decide to
use inheritance to create specialized classes for different types of employees.
Parent Class (Employee)
• Common attributes: name, emp_id, department.
• display_info() method prints basic employee details.
Child Class (FullTimeEmployee)
• Inherits from Employee and adds a salary attribute.
• calculate_annual_salary() calculates the yearly salary.
• display_full_time_info() shows all details for a full-time employee.
Child Class (PartTimeEmployee)
• Inherits from Employee and adds hourly_rate and hours_worked.
• calculate_salary() computes the total earnings.
• display_part_time_info() shows all details for a part-time employee'''



class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    def display_d(self):
        print("Name:",self.name)
        print("Employee id:",self.emp_id)
class FullEmployee(Employee):
    def __init__(self,name,emp_id,f_sal):
        Employee.__init__(self,name,emp_id)
        self.f_sal=f_sal
    def full_time_employee(self):
        self.display_d()
        ann_sal=f_sal*12
        print("Annual salary:",ann_sal)
class PartEmployee(Employee):
    def __init__(self,name,emp_id,p_sal,hours_w):
        Employee.__init__(self,name,emp_id)
        self.p_sal=p_sal
        self.hours_w=hours_w
    def display_part_sal(self):
        self.display_d()
        self.p_sal=p_sal
        print("Annual salary part:",(self.p_sal)*hours_w)
while True:
    choice=input("Enter p or f")
    if choice=="p":
        name=input("Enter the name of the employee")
        emp_id=int(input("Enter the employee id"))
        p_sal=int(input("Enter the monthly salary"))
        hours_w=int(input("Enter the number of hours worked"))
        part=PartEmployee(name,emp_id,p_sal,hours_w)
        part.display_part_sal()
    else:
         name=input("Enter the name of the employee")
         emp_id=int(input("Enter the employee id"))
         f_sal=int(input("Enter the monthly salary"))
         full=FullEmployee(name,emp_id,f_sal)
         full.full_time_employee()
                
    
