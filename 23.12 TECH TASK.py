# EXTRA QUESTIONS
'''1.	You are building a program to track user login attempts. Write a function that:
•	Records a new login attempt.
•	Limits login attempts to 5.
•	Locks the account after 5 failed attempts'''


id=True
LOGIN="LIB1234"
for i in range(5):
    login=input("Enter the login id:")
    if login==LOGIN:
        id=True
        print("Login id is valid:")
        break
    else:
        id=False
        print("Your id is worng")
        print(f"you have {5-(i+1)} attempts")
if not id:
    print("Login id is invalid")




'''2.	You are asked to write a script that manipulates a list of integers to meet specific conditions:
•	Remove duplicates.
•	Sort the list in descending order.'''
n=int(input("Enter the no of  elements in the list"))
l=[]
for i in range(n):
    elements=int(input("Enter the elements"))
    l.append(elements)
print(l)
l=set(l)
print("The list without duplicates:",l)
l=list(l)
l.sort(reverse=True)
print("The list in descending order:",l)

'''3.	Write a program that takes a number as input and returns the sum of its digits'''
n=int(input("Enter the number to find its sum:"))
sum_of_digits=0
while n!=0:
    temp=n%10
    sum_of_digits+=temp
    n=n//10
print(sum_of_digits)


'''4Identify common elements between two lists'''

n1=int(input("Enter the number of elements in list1"))
n2=int(input("Enter the number of elements in list2"))
l1=[]
l2=[]
for i in range(n1):
    e=int(input("Enter the elements in list1"))
    l1.append(e)
for i in range(n2):
    e2=int(input("Enter the elements in list2"))
    l2.append(e2)
print(l1)
print(l2)
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)

'''5.Write a program that counts the number of words in a given string'''
sentence=input("Enter the sentence:")
word_count=print(len(sentence.split()))
'''
6.Sort a list of integers without using Python's sorted() function'''
n=int(input("Enter the number of elements in the array"))
elements=list(map(int,input().split())) 
for i in range(n):
    for j in range(0,n-i-1):
        if elements[j]>elements[j+1]:
            elements[j],elements[j+1]=elements[j+1],elements[j]
print(elements)


'''7)Create a BankAccount class to simulate a bank account with features:
Deposit money.
Withdraw money (ensure sufficient balance).
Check balance.'''

print("1.Deposit 2.Withdraw 3.View balance 4.Exit")
balance=10000
while True:
    choice=int(input("Enter the choice you wanted"))
    match choice:
            case 1:
                print("Deposit")
                deposit=int(input("Enter the deposit amount"))
                balance+=deposit
                print(f"You have successfully deposited {deposit}")
            case 2:
                print("Withdraw")
                withdraw=int(input("Enter the withdraw amount"))
                if balance>=withdraw:
                    print(f"You have successfully withdrawn {withdraw}")
                    balance-=withdraw
                else:
                    print("You have insyfficient balance")
            case 3:
                print("Check balance")
                print(balance)
            case 4:
                exit()


'''8)Check if a given string is a valid email address'''

import re
email=input("Enter the email id:")
ex= ex=r'^[a-z0-9._%+-]+@gmail\.com$'
if re.match(ex,email):
    print("Valid")
else:
    print("invalid")

'''9.Extract all phone numbers from a given text.'''
text=input("Enter the text")
phone=[]
for i in text:
    if i.isdigit()==True:
        phone.append(i)
for i in phone:
    print(i,end="")

'''10. Extract all hashtags from a given text'''
import re
text=input("Enter the text:")
ex=r'#\w+'
result=re.findall(ex,text)
print(result)
    

    

    
    





    



    

