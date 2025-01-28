'''● For all the programs given below use Classes and Object.
● Use minimum two classes and one method
● Data has to be got from the user
● Do not have any static values in your program
Scenario – 14
Abstract Class and Method
1. Define a method Welcome which prints “Welcome To WTS!
WewishyoutheBest!!”
2. Define a method TestData which accepts Name and prints the belowgivenmessage
Please input a name : John
Expected Output :
Welcome John!
Have a nice day!
3. Define a method that accepts Name and counts the number of vowels in the names.
Please input a name : John
Expected Output :
Count of Vowels are : 2
a : 1
u : 1
4. Define a method that accepts Name, Mark1, Mark2 and returns the Grade of students
as mentioned below:
Total Marks Grade
>95 E
>=80 and <75 A+
>=75 and <=60 A
>60 and <=50 B
<50 F'''

from abc import ABC,abstractmethod
class Student_details(ABC):
    @abstractmethod
    def welcome(self):
        pass
    def TestData(self):
        pass
    def countvowels(self):
        pass
    def grade(self):
        pass
class Student(Student_details):
    def __init__(self,name,mark1,mark2):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
    def welcome(self):
        print("Welcome To WTS! WewishyoutheBest!!")
    def TestData(self):
        print("Welcome",self.name,"!")
        print("Have a nice day!")
    def countvowels(self):
        v_c=0
        app={}
        for i in self.name:
            if i in ["a","A","e","E","i","I","o","O","u","U"] and i not in app:
                app[i]=1
                v_c+=1
            elif i in ["a","A","e","E","i","I","o","O","u","U"] and i in app:
                app[i]+=1
                v_c+=1
        
                
        print("count of vowels:",v_c)
        for i,j in app.items():
            print(f"{i}:{j}")
    def grade(self):
        tot=self.mark1+self.mark2
        per=(tot/200)*100
        if per>=95:
            print("Grade A++")
        elif per>75:
            print("Grade A+")
        elif per>=60:
            print("Grade A")
        elif per>=50:
            print("Grade B")
        else:
            print("Grade C")
name=input("Enter the name:")
mark1=int(input("Enter the mark in subject 1"))
mark2=int(input("Enter the mark in subject 2"))
s=Student(name,mark1,mark2)
s.welcome()
s.TestData()
s.countvowels()
s.grade()
'''b2. Poorna wants to print the Data with skip
Understanding the Looping and Conditional Statements
Print the Password with Loop with Condition
b. Requirements : String without Numerical Value'''

class Break:
    def __init__(self,string):
        self.string=string
    def loopbreak(self):
        for i in range(len(string)):
            if string[i].isdigit():
                print(string[0:i])
                break
class Continue:
    def __init__(self,string):
        self.string=string
    def loopcontinue(self):
        for i in range(len(string)):
            if string[i].isdigit():
                
                continue
            else:
                print(string[i],end="")
        
    
string=input("Enter the string")
b=Break(string)
b.loopbreak()
c=Continue(string)
c.loopcontinue()

            
