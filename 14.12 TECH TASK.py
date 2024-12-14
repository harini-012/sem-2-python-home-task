'''1. You are given two strings word1 and word2. Merge the strings by adding letters in alternating
order, starting with word1. If a string is longer than the other, append the additional letters
onto the end of the merged string.
Return the merged string.
Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1: a b c
word2: p q r
merged: a p b q c r'''


word1=input("Enter the word1")
word2=input("Enter the word2")
lw1=len(word1)
lw2=len(word2)
if lw1==lw2:
    for i in range(lw1):
        print(word1[i]+word2[i],end="")
elif lw1>lw2:
        for i in range(lw2):
            print(word1[i]+word2[i],end="")
        print(word1[lw2:])
elif lw2>lw1:
        for i in range(lw1):
            print(word1[i]+word2[i],end="")
        print(word2[lw1:])



'''2. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However,
flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means
not empty, and an integer n, return true if n new flowers can be planted in the flowerbed
without violating the no-adjacent-flowers rule and false otherwise.
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length'''
bed=list(map(int,input().split()))
n=int(input("Enter how many flowers you needed to plant:"))
count=0
for i in range(len(bed)):
    if bed[i]==0 :
        left=(i==0 or bed[i-1]==0)
        right=(i==len(bed)-1 or bed[i+1])==0
        if left and right:
            bed[i]=1
            count+=1
            if count>=n:
                print("True")
                break
else:
    print("False")
