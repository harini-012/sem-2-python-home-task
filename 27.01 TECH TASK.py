'''1.Keerthana has to design a method that will accept the UserName and
Password from the user and also print the same in the required format.
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
1. User Name Validation: Should not allow Numbers & any special characters
to be entered.
2. Password: Must contain at least one number and one Special character.
Should not be greater than 8 in length
3. User must be allowed to continue till he enters in the correct format'''
import re
def validate_details(name,depart,password):
   
    
    def validate_name(name):
        
        for i in name:
            if not i.isalpha():
               return False
            
        return True
    def validate_password(password):
        import re
        ex = r'^(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{1,8}$'
        return bool(re.match(ex, password))

       
    def display(name,depart,password):
        
            for i in range(len(name)):
                print("X",end="")
            print("fresher")
            print()
            print("Your encoded department is:",end=" ")
            for i in range(len(depart)):
                print("X",end="")
            print()
            print("Your encoded password is:",end=" ")
            print()
            for i in range(len(password)):
                print("X",end="")
            print()
            print("Your encoded retyped password is:",end=" ")
            for i in range(len(password)):
                print("X",end="")
            print()
    
    while True:
        if not validate_name(name):
            print("Invalid name")
            name=input("Retype your name")
            continue
        while True :
            if not validate_password(password):
                print("Invalid password:")
                password=input("Enter the password")
            else:
                re=input("REtype your password to confirm")
                if password != re:
                        print("Error: Passwords do not match. Please try again.")
                        password = input("Re-enter your Password: ")
                else:
                        break
        break
    display(name,depart,password)
name = input("Enter your Name: ")
depart = input("Enter your Department: ")
password = input("Enter your Password: ")
validate_details(name, depart, password)


'''2.Write a Python program to remove the first occurrence of a specified
element from an array.
Sample Output:
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Remove the first occurrence of 3 from the said array:
New array: array('i', [1, 5, 3, 7, 1, 9, 3])'''

n=int(input("Enter the number of items in the list"))
t=int(input("Enter the target"))
arr=[]
for i in range(n):
    e=int(input())
    arr.append(e)
for i in arr:
    if i==t:
        arr.remove(i)
        break
print("New array:",arr)

'''3.Create an array with limited Input size and Print Inverse and Non Inverse
Order.
The Array is - [Face, Prep, Campus, Tech, Solutions]
Sample Output Your Inverse order Array is - [Solutions ,Tech, Campus,
Prep, Face]
Your Non - Inverse Order Array is - [Face, Prep, Campus, Tech, Solutions]'''

n=int(input("Enter the number of elements in the array"))
arr=[]
for i in range(n):
    e=input()
    arr.append(e)
arr.reverse()
print("Your Inverse order Array is -",arr)
arr.reverse()

print("Your Non - Inverse Order Array is -",arr)



