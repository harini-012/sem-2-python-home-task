'''1. Benedict needs to write a simple code to ask the user his name and also the number of times
he wants his name to be printed. Use class and method to validate. The format to display has
been given below
INPUT:
Enter your Name:
Enter your Password:
Enter your Email Address:
How many times to want to Print?
OUTPUT:
<<Name>> Wants to Print <<N>> Times and send Mail to <<email-id>>.
Your password <<password>> will be encrypted and will be stored.
Condition:
Include Password to your program
Name Validation: Should allow only one Number & one special character
Password: Must not contain any Number and Special characters except (#, _ and @). Should not be
greater than 8 in length
Email Id: Should be valid format.
User must be allowed to continue till he enters in correct format'''
import re
class Details:
    def __init__(self,name,password,email):
        self.name=name
        self.password=password
        self.email=email
        
    def validate_name(self):
        while True:
            digit=0
            spec=0
            for i in name:
                if i.isdigit():
                    digit+=1
                if not i.isalpha() and not i.isdigit():
                    spec+=1
            if digit==1 and spec==1:
                break
                    
            
        
            else:
                self.name=input("RE-enter the name")
    def validate_password(self):
        while True:
            ex_p = r'^[a-zA-Z_@]{1,8}$'
            if  re.match(ex_p,self.password):
                break
            else:
                self.password=input("Re-enter the password")
    def validate_email(self):
        while True:
            ex_e= r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if re.match(ex_e,self.email):
                break
            else:
                email=input("Enter the email id")
    def display(self):
       
            times=input("How many times do you want to print your name")
            print(f"{self.name} wants to print {times} times and send mail to {self.email}")
            print(f"Your password {password} will be encrypted and will be stored")
        
name=input("Enter the name")
password=input("Enter the password")
email=input("Enter the email")

d=Details(name,password,email)
d.validate_name()
d.validate_password()
d.validate_email()
d.display()

'''
2. Banu has forgot her password. Please help her to get password again. Must Use Method and
Constructor.
Input:
Enter your Name:
Enter your Department:
Enter your Password:
Re-Type your Password:
Output:
Your Encoded Name is: XXXXX – Fresher
Your Department is: XXXX
Your Password is: XXXXX
Re-Type your Password: XXXXX
Condition:
1. If Password does not match with Entered Password allow to re-enter the password 3 times.
After limited time entry ask to Forgot Password or Know password
2. Allow again one time entered the password. If again wrong Direct go to forgot password.
3. Ask two security Questions for show password. If any one question is wrong ask again the
security questions.
4. Once both questions answers were correct then Show the password
5. Password: Must contain at least one number and one Special character. Should not be greater
than 8 in length
6. User must be allowed to continue till he enters in the correct format'''
import re
name=input("Enter the name")
dept=input("Enter the department")
password=input("Enter the password")
Re_pass=input("Enter the password again")
class Details:
    def __init__(self,name,dept,password,Re_pass):
        self.name=name
        self.dept=dept
        self.password=password
        self.Re_pass=Re_pass
    def print_pass(self):

        print("Your encode password is")
        for i in range(len(password)):
            print("X",end="")
        print()
    def recheck(self,Re_pass):
        
            for i in range(3):
                if password!=Re_pass:
                    re_pass=input("Retype your password")
                    Re_pass=re_pass
                    if password==Re_pass:
                       print("Your encoded password is")
                       for i in range(len(password)):
                           print("X",end="")
                       print()
                       break
               
                    
                      
            if password!=re_pass:
                print("1.Forgot password 2.Show password")
                Re_pass=input("Enter the password again for one time")
                if Re_pass!=password:
                    self.forget_password(name,dept)
                else:
                    for i in range(len(Re_pass)):
                        print("X",end="")
                    print()
    def forget_password(self,name,dept):
        ques1=input("Enter the name")
        ques2=input("Enter the department")
        if ques1==name and ques2==dept:
            p=False
           
            while True:
                    new_pass=input("Enter the new password")
                    ex= r'^(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{1,8}$'
                    if re.match(ex,new_pass):
                        self.show_new(new_pass)
                        break
                    else:
                        continue
        else:
            self.forget_password(name,dept)
            
    def  show_new(self,new_pass):
        print("Your password")
        for i in range(len(new_pass)):
            print("X",end="")
                            
    def display(self):
        print("Your encoded name is:")
        for i in range(len(name)):
            print("X",end="")
        print()
        print("your department is :")
        for i in range(len(dept)):
            print("X",end="")
        print()
        if password==Re_pass:
            self.print_pass()
        if password!=Re_pass:
            self.recheck(Re_pass)
          
    
          
d=Details(name,dept,password,Re_pass)
d.display()

        
        
