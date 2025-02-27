'''1. Given a string containing multiple words, write a function to reverse every alternate
word in the sentence while keeping the others unchanged.
 Constraints:
• Words are separated by a single space.
• Punctuation should be preserved in its place.
• The first word remains unchanged, the second word is reversed, the third word
remains unchanged, and so on.
Sample Input and Output:
Hello world this is Python
Hello dlrow this si Python'''


string=input()
l=[]
split=""
for i in string:
    if i!=" ":
        split+=i
    else:
        l.append(split)
        split=""
if split:
    l.append(split)
odd=[]
even=[]
for i in range(len(l)):
    if i%2==0:
        even.append(l[i])
    else:
        odd.append(l[i])

rev=[]
rev_s=""
for i in odd:
    rev_s+=i[::-1]
    rev.append(rev_s)
    rev_s=""
ans=[]

if len(even)>len(rev):
    for i in range(len(rev)):
        ans.append(even[i])
        ans.append(rev[i])
    ans.extend(even[i+1:])
if len(rev)>len(even):
    for i in range(len(even)):
        ans.append(even[i])
        ans.append(rev[i])
    ans.extend(rev[i+1:])
if len(even)==len(rev):
    for i in range(len(rev)):
        ans.append(even[i])
        ans.append(rev[i])

ans_r=""
for i in ans:
    ans_r+=i
    ans_r+=" "
print(ans_r)

    
