#1Print the following pattern and use method to call the pattern logic

'''
  1
 1 2
 1 2 3
1 2 3 4
1 2 3 4 5'''
def print_pattern():

    n=int(input("Enter the number of rows"))
    for i in range(1,n+1):
        space=" "*(n-i)
        if i==1:
            print(" "+space+"1")
            
        else:
            
            for j in range(1,i+1):
                
                print(space+str(j)+" "*2*(i-35),end="")
            print()

print_pattern()


'''2. A bank's IT department is working on a security feature that involves prime number
verification. They need a program that can check whether a given number is prime using a
method (function).'''

def check_prime(n):
    f=True
    if n<2:
        f=False
    elif n==2:
        f=True
    else:
        for i in range(2,n):
            if n%i==0:
                f=False
                break
            else:
                f=True
    if f:
        print("The given number is prime")
    else:
        print("The given number is not prime")
n=int(input("Enter a number to find it whether prime or not"))
check_prime(n)
