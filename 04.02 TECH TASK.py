'''1. Given a string s consisting of words and spaces, return the length of the last word in the
string.A word is a maximal substring consisting of non-space characters only.
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:
Input: s = " fly me to the moon "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.'''


string=input()
l=[]
split=""
for i in range(len(string)):
    split+=string[i]
    if string[i]==" ":
        l.append(split.strip())
        split=""
if split:
    l.append(split)
    
last=""
for i in l:
    if l.index(i)==len(l)-1:
        last+=i
print(f"The last word is {last} with {len(last)}")
        
