'''1. Keerthana wants to print the UserName and Department and Mobile
number and also print the same in the required format.
Conditions of Input:
Print your name Concatenate with First Name and Last Name
Print Concatenate with College name and Stream
Print the ASCII value of Your Name
Print the ASCII value of your Mobile Number
Print the ASCII value Addition Result of Your Name and Mobile
number with Alternate method.
Sample Output:
Your Name is : Face Prep
Your College Name : XXXXX College Department of CSE
ASCII value name is : W – 87, I-73, S-83. E-69
ASCII value of Mobile Number: 9-57, 8-58,9-57,4-52
Result of Addition: W+9 = 144, I+8= 131, S+9 = 147, E+4 = 122

first_name=input("Enter the first name:")
last_name=input("Enterr the last name:")
name=first_name+last_name
print("Your name is:",name)
college_name=input("Enter the college name:")
depart=input("Enter the department name:")
print("Your college name is :",college_name+depart)
mobile_no=input("Enter the mobile number:")
ascii_name=[]
for i in name:
    if i!="":
        ascii_name.append(ord(i))
        print(f"Your ASCII name is :{i}-{ord(i)}")
ascii_mobile=[]
for i in mobile_no:
    if i!="":
        ascii_no=ord(i)
        ascii_mobile.append(ascii_no)
        print(f"Your ascii mobile number is:{i}-{ascii_no}")
for i in range(len(ascii_name)):
    for j in range(len(ascii_mobile)):
        if i==j:
            print(ascii_name[i]+ascii_mobile[j])'''


'''2. Nithya wants to print the Operational Result with two user input
values.
1. Do the all Arithmetic operation and Print the result.
2. Swapping Three values using bitwise operator without third
variable .
Input:
First value of Input – 30
Second value of Input – 20
Third Value of Input - 10
Sample Output:
Addition – 50
Subtraction - 10
Before Swapping
First value – 30
Second value – 20
Third Value - 10
After Swapping
First value – 20
Second Value - 10
Third Value – 30


n1=int(input("Enter the value 1:"))
n2=int(input("Enter the value 2:"))
print("Addition:",n1+n2)
print("Subtraction:",n1-n2)
print("Multiplication:",n1*n2)
print("Division:",n1/n2)
print("Floor division:",n1//n2)
print("Power:",n1**n2)
print("Modulus:",n1%n2)
a=n1
b=n2
c=int(input("Enter the value 3"))
a=a^b
b=b^c
a=a^b
b=b^c
c=b^c
b=b^c
print(f"After swapping: a = {a}, b = {b}, c = {c}")'''

'''3. Scenario- Conditional Statements
Kathir has to design a method that will accept the UserName Input:
Print Username with Conditions
Requirements: Name with Special Characters
a. Print the string with special characters.
Input:
Enter First Name : face123@#$%^
Output:
Hi ! Your Entered Input is “face@#$%^”
b. Split Characters and Special Characters from the given string.
Enter Name : faceprep12345!@#$%^&
Your entered Characters are –faceprep
Your entered Special Characters are -!@#$%^&
SL – Self – Learning
a. Find the suitable method to print the String with a special Character'''

string=input("Enter the first name:")
char=[]
special=[]
dig=[]
for i in string:
    if i.isalpha():
        char.append(i)
    if not i.isalpha() and not i.isdigit():
        special.append(i)
    else:
        dig.append(i)
print(''.join(char)+''.join(special))
print("Your entered characters are:")
for i in char:
    print(i,end="")
print()
print("Your special characters are:")
for i in special:
    print(i,end="")
print()

    


        
