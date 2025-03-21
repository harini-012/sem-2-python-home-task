'''2. Python program to find the following pattern:


            1 2 3 4
          8 7 6 5
     9 10 11 12
 16 15 14 13'''


n = 4  # Number of rows
num = 1  # Starting number

for i in range(1,n+1):
    print(" "*(n-i)*6,end="")
    temp=[num+j for j in range(4)]
    num+=4
    if i%2==0:
        temp.reverse()
    print("  ".join(f"{x:2}" for x in temp))




