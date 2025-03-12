'''
Print the following pattern:
Sample input: 5
Sample Output:
1
1 1
2 1
1 2 1 1
1 1 1 2 2 1
'''

n=int(input("Enter the number of rows"))#5
seq=["1"]
for i in range(n):
    print(" ".join(seq))
    new_seq=[]
    count=1
    for j in range(1,len(seq)):
        if seq[j]==seq[j-1]:
            count+=1
        else:wor
            new_seq.append(str(count))
            new_seq.append(seq[j-1])
            count=1
    new_seq.append(str(count))
    new_seq.append(seq[-1])
    seq=new_seq


'''
Iteration 1

Initial:
seq=[1]
new_seq=[]
1 will be printed
count=1
for j in range(1,1) No excecution
new_sequence.append("1")
new_seq.append("1")

Final:
seq=[1,1]
new_seq=[1,1]


Iteration 2
Initial:
seq=[1,1]
new_seq=[1,1]
1 1 will be printed
new_seq=[]
count=1
for j in range(1,2)
seq[1]==seq[0]---->yes
count=2
new_seq.append(str(2))
new_seq.append(1)

Final:
seq=[2,1]
new_seq=[2 1]

Iteration 3:
Initial:
seq=[2,1]
new_seq=[2 1]
2 1 will be printed
new_seq=[]
count=1
for j in range(1,2)
if i==1
seq[1]==seq[0]-->no

new_sequence.append(1)
new_seq.append(seq[0])-->2
new_seq.append(str(1))
new_seq.append(seq[-1])-->1

Iteration 4

Inital:
seq=[1 2 1 1]
new_seq=[1 2 1 1]




Final:
seq=[1 2 1 1]
new_seq=[1 2 1 1]


Iteration 4
Initial:
seq=[1 2 1 1]
new_seq=[1 2 1 1]
1 2 1 1 will be printed
new_seq=[]
count=1
for j in range(1,4)
if i==1
seq[1]==seq[0]-->No
new_sequence.append(str(1))
new_sequence.append(seq[j-1])-->1
count=1

if i==2
seq[2]==seq[1]-->no
new_sequence.append(str(1))
new_sequence.append(seq[1])-->2

if i==3
seq[2]==seq[1]-->yes
count=2
new_sequence.append(2)
new_sequence.append(1)

Final:
seq=[1 1 1 2 2 1]
new_seq=[1 1 1 2 2 1]

Iteration 5-->n==4
printed the new sequence



