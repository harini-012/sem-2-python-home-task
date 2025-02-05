'''1. Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Constraints:
• 1 <= strs.length <= 200
• 0 <= strs[i].length <= 200
• strs[i] consists of only lowercase English letters if it is non-empty'''

l=[]
n=int(input("Enter the number of words in the array"))
for i in range(n):
    e=input()
    l.append(e)
occ={}
for i in l:
    word=i
    for i in word:
        if i not in occ:
            occ[i]=1
        else:
            occ[i]+=1

maxi=0
pre=""
for i,j in occ.items():
    if j>=maxi:
        pre+=i
        maxi=j


for i in l:
    if i.startswith(pre):
        p=True
    else:
        p=False
if p:
    print(pre)
if not p:
    print("There is no common  prefix among the input strings")


'''2. Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can
be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false'''

string=input("Enter the string to find whether subseqence or not")#abc
subsequence=input("Enter the subsequence string")#ahbdgc
index=0
for i in subsequence:#a#h#b#g#d#c-True
    if index<len(string) and string[index]==i:#0<3 and string[0]==a #1<3 anf string[1]!=h string[1]==b string[2]!=g string[2]!=d string[2]==c
        index+=1#1#2#3
    if index==len(string):
        print("True")
        break
else:
    print("False")



    

    
    
