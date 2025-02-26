'''1. Print the following pattern using python
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9 
'''

n=int(input())
matrix=[[0]* n for i in range(n)]
l,r,t,b=0,n-1,0,n-1
num=1
while l<=r and t<=b:
    for i in range(l,r+1):
        matrix[t][i]=num
        num+=1
    t+=1
    for i in range(t,b+1):
        matrix[i][r]=num
        num+=1
    r-=1
    for i in range(r,l-1,-1):
        matrix[b][i]=num
        num+=1
    b-=1
    for i in range(b,t-1,-1):
        matrix[i][l]=num
        num+=1
    l+=1
for i in matrix:
    for j in i:
        print(f"{j:2}",end="  ")
    print()

'''2. The Collatz Conjecture
For any positive integer n:
1. If n is even, divide it by 2 → n = n / 2.
2. If n is odd, multiply it by 3 and add 1 → n = 3n + 1.
3. Repeat until n becomes 1.
Input: 12
Output: 12 steps to reach 1.'''

n=int(input())
steps=0
while n>1:
    if n%2==0:
        n=n//2
        
    else:
        n=(3*n)+1
    steps+=1
print(steps)
    
