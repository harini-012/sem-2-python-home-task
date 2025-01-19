#printing the specified pattern
n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#counting the sum of the elements in the dictionary
d={"a":1,"b":23 ,"c":40}
l=[]
tot=0
for i in d.values():
    l.append(i)
for i in l:
    tot+=i
print(tot)
    
