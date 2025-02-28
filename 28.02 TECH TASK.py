'''Write a Python program that takes an integer input N and prints N rows of a pattern where:
1. Each row starts with an increasing character from 'a' onward.
2. The row consists of two alternating characters repeated twice (e.g., "abab", "bcbc").
3. The number of rows printed should be equal to the given input N.
Sample Input:
Enter a number: 3
Sample Output:
abab
bcbc
cdcd
'''

n=int(input("Enter the number of rows"))
c=97
while n>=1:
    for i in range(2):
        print(chr(c),end="")
        print(chr(c+1),end="")
    print()
    n=n-1
    c=c+1
        

'''Write a Python program that takes an integer input N and prints N rows of a pattern where:
1. Each row starts with an increasing character from 'a' onward.
2. The row consists of the first character repeated twice, followed by the next character
repeated twice (e.g., "aabb", "bbcc").
3. The number of rows printed should be equal to the given input N.
Sample Input:
Enter a number: 3
Sample Output:
aabb
bbcc
ccdd'''

n=int(input("Enter the number of rows"))
c=97
while n>=1:
    for i in range(1):
        print(chr(c)*2,end="")
        print(chr(c+1)*2,end="")
    print()
    n=n-1
    c=c+1
