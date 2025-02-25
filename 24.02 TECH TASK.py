

'''1. Checks for twin primes (pairs of prime numbers that differ by 2) within a given range.
Sample input”
1
50
Sample Output:
Twin Primes: [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)


'''
s=int(input("Enter the number of start range"))
e=int(input("Enter the end range "))
primes=[]
p=False
for n in range(s,e+1):
    if n==2:
        primes.append(n)
    else:
        for i in range(2,n):
            if n%i==0:
                p=False
                break
            else:
                p=True
        if p:
            primes.append(n)

twin_primes=[]
for i in range(len(primes)-1):
    if primes[i+1]-primes[i]==2:
        twin_primes.append((primes[i],primes[i+1]))
print(twin_primes)


'''
2. Write a program that:
Takes an input range (start and end).
Finds all prime numbers within the range.
Checks if they are palindromes.
Outputs all palindromic prime numbers in the given range.
Sample Input:
Enter start: 10
Enter end: 200
Sample Output:
Palindromic Primes: [11, 101, 131, 151, 181, 191]'''


s=int(input("Enter the number of start range"))
e=int(input("Enter the end range "))
primes=[]
p=False
for n in range(s,e+1):
    if n==2:
        primes.append(n)
    else:
        for i in range(2,n):
            if n%i==0:
                p=False
                break
            else:
                p=True
        if p:
            primes.append(n)
pali=[]
for i in primes:
    i=str(i)
    if len(i)>=2:
        i=int(i)
        num=i
        rev=0
        while i>0:
            temp=i%10
            rev=rev*10+temp
            i=i//10
        if num==rev:
            pali.append(num)
print(pali)
    
        
