'''1. find the Kth largest element in an unsorted list
Input:
Space separated input
K value
Sample Input:
6 2 4 5 7
3
Sampel Output:
5'''

l=list(map(int,input().split()))
k=int(input("Enter the k to find kth largest"))
for i in range(k):
    maxi=float('-inf')
    for i in l:
        if i>maxi:
            maxi=i
    l.remove(maxi)
print(maxi)


'''2. Check if a Number is a Disarium Number
A Disarium number is a number where the sum of its digits raised to their respective positions is
equal to the number itself.
Example: 135 is a Disarium number because 1^1 + 3^2 + 5^3 = 135'''

n=int(input())
n=str(n)
l=[]
s=0
for i in n:
    l.append(i)
for i,j in enumerate(l):
    i=int(i)
    j=int(j)
    s+=j**(i+1)
print("The sum of the number raised to the power of the position is",s)
if s==int(n):
    print("Disarium number")
else:
    print("Not a disarium number")



    
    

    
