'''1. Count how many trailing zeros are in n! (n factorial).
Input: 10
Output: 2 (since 10! = 3,628,800)'''


n=int(input("Enter the number to find its factorial"))
fact=1
while n>1:
    fact*=n*(n-1)
    n=n-2
print(fact)
fact_l=list(str(fact))
count=0
length=len(fact_l)

for i in range(length-1,-1,-1):
    if fact_l[i]=="0":
        count+=1
    else:
        break
print(count)



'''1. To convert an integer to English words, we need to break it down into groups of thousands
and handle each group separately.
Sample Input: 45
Sample Output : "Forty Five"
Sample Input: 12345
Sample Output : Twelve Thousand Three Hundred Forty Five'''

n=int(input("Enter the number"))
first=["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen","Seventeen", "Eighteen", "Nineteen"]
tens=["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
if n==0:
    print("Zero")
elif n<20:
    print(first[n])
elif n<100:
    print(tens[n//10]+(" "+first[n%10] if n%10!=0 else " "))
else:
    if n % 100 < 20:  
        print(first[n//100] +"Hundred" + (" " +first[n % 100] if n % 100 != 0 else ""))
    else:
        print(first[n // 100] + " Hundred" + (" " + tens[(n % 100) // 10] if (n % 100) // 10 > 1 else "") +  (" " +first[(n % 100)%10] if n%10!=0 else ""))
