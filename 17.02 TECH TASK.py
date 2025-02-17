'''1. Write a function that takes two dictionaries and merges them into one.'''

def merge_dictionary(d1,d2):
    new_d={}
    for i,j in d1.items():
        new_d[i]=j
    for i,j in d2.items():
        new_d[i]=j
    print(new_d)
n1=int(input("Enter the number of elements in dict1"))
d1={}
for i in range(n1):
    key=input("enter the key")
    value=input("Enter the value")
    d1[key]=value
n2=int(input("Enter the number of elements in dict2"))
d2={}
for i in range(n2):
    key=input("enter the key")
    value=input("Enter the value")
    d2[key]=value
merge_dictionary(d1,d2)


'''Write a function that takes two lists and returns a dictionary with common elements
as keys and their counts as values.'''

def dictionary():
    n1=int(input("Enter the number of elements in list1"))
    n2=int(input("Enter the number of elements in list2"))
    l1=[]
    l2=[]
    for i in range(n1):
        e=int(input())
        l1.append(e)
    for i in range(n2):
        e=int(input())
        l2.append(e)

    occ1={}
    occ2={}
    for i in l1:
        if i in occ1:
            occ1[i]+=1
        else:
            occ1[i]=1
    for i in l2:
        if i in occ2:
            occ2[i]+=1
        else:
            occ2[i]=1
    l1=set(l1)
    l2=set(l2)
    l3=l1.intersection(l2)
    new_d={}
    for i in l3:
        new_d[i]=min(occ1[i],occ2[i])
    print(new_d)
dictionary()


'''Write a function that takes a list of (key, value) tuples and converts it into a
dictionary'''


def tuple_c():
    n1=int(input("Enter the number of tuples in a list"))
    l1=[]
    for i in range(n1):
        v1=input("Enter the value1 of each tuple")
        v2=int(input("Enter the value2 of each tuple"))
        t1=(v1,v2)
        
        l1.append(t1)
    new_d={}
    for i in l1:
        new_d[i[0]]=i[1]
    print(new_d)

tuple_c()







            
