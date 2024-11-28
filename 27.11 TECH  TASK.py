#1)Given students details, marks in 3 subjects and we have to find student's grade.In this program, you have to take student name, roll number and marks in 3 subjects and calculatingstudent's grade based on the percentage and printing the all details.
# SELF IS CURRENT INSTANCE OF A CLASS
class Student:
    def __init__(self,name,rollno,mark1,mark2,mark3):
        self.name=name
        self.rollno=rollno
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def calculate_per(self):
        total=self.mark1+self.mark2+self.mark3
        percentage=(total/300)*100
        return percentage
    def display_percentage(self):
        percentage=self.calculate_per()
        print(f"your percentage is {percentage}")
    def grade(self):
        percentage=self.calculate_per()
        if percentage>=85:
            print("your grade is S")
        elif percentage>=75 and percentage <=85:
            print("your grade is A")
        
        elif percentage>=65 and percentage <=75:
            print("your grade is B")
        elif percentage>=55 and percentage <=65:
                print("your grade is C")
        elif percentage>=50 and percentage <=55:
            print("your grade is D")
s=Student("Harini","E24AI012",90,91,86)
s.calculate_per()
s.display_percentage()
s.grade()



#2). Implement destructor and constructors using __del__() and __init__() to display student information.Student information – name, age, course and grade

class Student:
    def __init__(self,name,age,course,grade):
        self.name=name
        self.age=age
        self.course=course
        self.grade=grade
    def display(self):
        print(f"Your name is {self.name}")
        print(f"your age is {self.age}")
        print(f"Your course is {self.course}")
        print(f"Your grade is {self.grade}")
    def __del__(self):
        print("All the databases are deleted")
s=Student("Harini",18,"Bsc computer science with ai","A")
s.display()
del s
