class Student:
    def __init__(self):
        self.id=input("Enter the id")
        self.name=input("enter the name")
        self.grade=input("enter the grade")
    def validate_id(self):
        
        id_len=len(self.id)
        if id_len==7:
            if self.id[0]=="S" and self.id[1]=="T" and self.id[2]=="U" :
                if self.id[3] and self.id[4] and self.id[5] and self.id[6].isdigit()  ==True:
                    print("Valid")
                else:
                    print("last 4 cases not valid")
            else:
                print("first 4 cases not valid")
        else:
            print("length not valid")
    def validate_name(self):
        if len(self.name)>=2 and all(char.isalpha() or char.isspace() for char in self.name):
            print("Valid name")
        else:
            print("Not valid")
    def validate_grade(self):
        if self.grade[0].isdigit==False:
            print("Invalid")
        number=int(self.grade.split(' ')[0])
        
        if number<1 and number> 12:
                print("Invalid")
        else:
                print("Valid")

    def display(self):
        print(self.id)
        print(self.name)
        print(f"{self.grade}TH")
s=Student()
s.validate_id()
s.validate_name()
s.validate_grade()
s.display()
