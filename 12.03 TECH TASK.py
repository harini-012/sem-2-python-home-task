'''Write a Python program that takes an integer n as input and prints the following zig-zag 
number pattern: 
 
1       1   
  2   2   
    3   
  4   4   
5       5  '''


n=int(input("Enter the maximum maximum rows and coloumns"))
right=n-1
for i in range(n):
        for j in range(n):
            if i==j or j==right:
                print(i+1,end=" ")
            else:
                print(" ",end=" ")
        right-=1
        print()
            
            
