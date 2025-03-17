'''You are given a 0-indexed array of unique strings words.
A palindrome pair is a pair of integers (i, j) such that:
0 <= i, j < words.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a palindrome.
Return an array of all the palindrome pairs of words.
You must write an algorithm with O(sum of words[i].length) runtime complexity.
Example 1:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
Example 2:
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]'''

n=int(input("Enter the number of words"))
arr=[]
for i in range(n):
    e=input()
    arr.append(e)
    
pali=[]
for i in range(len(arr)):
    for j in range(len(arr)):
        if i!=j:
            concat=arr[i]+arr[j]
            if concat==concat[::-1]:
                pali.append([i,j])
print(pali)
