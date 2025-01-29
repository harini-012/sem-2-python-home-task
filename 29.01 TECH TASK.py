'''1. You are given an integer array nums. A "good subarray" is a subarray (continuous part of
nums) that contains an equal number of 0s and 1s. Find the length of the longest good
subarray.
Sample Input 1:
nums = [0, 1, 0, 1, 1, 0, 1, 0]
Sample Output 1:
8 (The entire array is a "good subarray" because it has equal 0s and 1s.)
Sample Input 2:
nums = [0, 1, 1, 1, 0, 0, 1, 0]
Sample Output 2:
6 (The longest good subarray is [1, 1, 1, 0, 0])
Sample Input 3:
nums = [0, 0, 1, 1, 0]
Sample Output 3:
nums = [0, 0, 1, 1]
'''

array=list(input().split())
subarr=[]
zero=0
one=0
for i in array:
    if i=="0":
        zero+=1
    else:
        one+=1

if zero==one:
    c=True
    for i in range(0,len(array)-1,2):
        if array[i]!=array[i+1]:
            c=False
        else:
            c=True
            break
    if not c:
        print(len(array))
        print("The entire array is a good subarray because it has equal 0s and 1s",array)
    else:
          for i in range(len(array)-1):
              if array[i+1]==array[i]:
                  subarr.append(array[i])
                  subarr.append(array[i+1])
          print(len(subarr))
          print("The longest good subarray is",subarr)

        
if  zero!=one:
      for i in range(len(array)-1):
        if array[i+1]==array[i]:
            subarr.append(array[i])
            subarr.append(array[i+1])
      print(len(subarr))
      print("The longest good subarray is",subarr)

  
