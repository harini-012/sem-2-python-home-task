''' Given a nested list like:
arr = [1, [2, [3, [4, 5]], 6], 7]
Write a function to flatten it into a single list:
[1, 2, 3, 4, 5, 6, 7]
(Without using built-in libraries like itertools!)'''

arr = [1, [2, [3, [4, 5]], 6], 7]
f=[]
def flatten(arr):
    for i in arr:
        if isinstance(i,list):
            flatten(i)
        else:
            f.append(i)
flatten(arr)
        
print(f)
