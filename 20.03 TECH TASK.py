'''Given an unsorted array of integers, rearrange the array so that:
All even-indexed elements are greater than their adjacent odd-indexed elements.
All odd-indexed elements are less than their adjacent even-indexed elements.
Input: [5, 3, 1, 2, 3, 7, 6, 4]
Output: [5, 1, 3, 2, 7, 3, 6, 4]'''


arr=[]
n=int(input())
for i in range(n):
    e=int(input())
    arr.append(e)
for i in range(len(arr)-1):
    if i%2==0:
        if arr[i]<arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    else:
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
print(arr)
        
