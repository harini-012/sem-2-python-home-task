
#Multiple Inheritance

#1)
'''1. Multiple inheritance example - Imagine a Smartphone that combines features of a Camera and a
Phone. Use multiple inheritance to implement the following.
The Camera class - variable resolution and method (Take photo)
The Phone class –Phone number as variable with methods such as making calls and sending
messages.
The Smartphone class inherits from both, combining the features of both a camera and a phone
with additional variables such as brand and model. Method in smart phone is : display device
information.'''
class Camera:
    def __init__(self):
        self.resolution=input("Enter the resolution")
        self.camera_name=input("Enter the camera name")
    def display_camera(self):
        print("Resolution:",self.resolution)
        print("Camera name:",self.camera_name)
class Phone:
    def __init__(self):
        self.phone_no=int(input("Enter the phone number:"))
    def display_phone(self):
        print("Phone Number:",self.phone_no)
class SmartPhone(Camera,Phone):
    def __init__(self):
        Camera.__init__(self)
        Phone.__init__(self)
        self.brand=input("Enter the brand")
        self.model=input("Enter the model")
    def displaydevice(self):
        print("Model:",self.model)
        print("Brand:",self.brand)
        self.display_camera()
        self.display_phone()
        print("Model:",self.model)
        print("Brand:",self.brand)
s=SmartPhone()
s.displaydevice()
print("**************************")        


#2)Single Inheritance

'''Single inheritance example - Student as the parent class, providing attributes and methods related
to education (e.g., studentInfo()).
StudentAthlete, which specializes the Student class, adds attributes for sports name, and provides
method (e.g., displayAtheletInfo() – which should include student name, course and the sport).'''
class Student:
    def __init__(self):
        self.name=input("Enter the student name")
        self.department=input("Enter the department of the student")
        self.section=input("Enter the section of the student")
    def studentInfo(self):
        print("Student Name:",self.name)
        print("Department:",self.department)
        print("Section:",self.section)
class StudentAthelete(Student):
    def __init__(self):
        Student.__init__(self)
        self.sports_name=input("Enter the sports that student want to participate")
    def studentathelete(self):
        self.studentInfo()
        print("Sports Name:",self.sports_name)
s=StudentAthelete()
s.studentathelete()
