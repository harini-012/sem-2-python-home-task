'''i. You are a developer at a school, and you have been given a dictionary containing students' names
and their marks in a test. [Use lambda function and methods for each task]
Your task is to:
1. Sort students by marks in ascending order.
2. Sort students by marks in descending order.
3. Find the top 3 students with the highest marks.
4. Sort students by name alphabetically.'''


n=int(input("Enter the number of students"))
d={}
for i in range(n):
    name=input("Enter the name of the student")
    mark=int(input("Enter the marks of the student"))
    d[name]=mark
print("Sorted by using ascending order of marks")
sort_a=dict(sorted(d.items(),key=lambda x:x[1]))
print(sort_a)
print("Sorted by using descending order")
sort_d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
print(sort_d)
print("The toppers are")
toppers = dict(list(sort_d.items())[:3])
print(toppers)
print("Sorting alphabetically")
sort_al=dict(sorted(d.items(),key=lambda x:x[0]))
print(sort_al)

'''Sorting a List of Tuples Using Lambda
Scenario
You are working as a data analyst for a sports organization. You have a list of tuples where each tuple
represents a player's name and their total number of goals scored in a football season.
Your task is to:
1. Sort the players by goals scored in ascending order.
2. Sort the players by goals scored in descending order.
3. Find the top 3 goal scorers.
4. Sort players by their names alphabetically.
5. Find employees earning more than $5000.'''

t=[]
n=int(input("Enter the number of players participated in the football tournament"))
for i in range(n):
    name=input("Enter the name of the player")
    goal=int(input("Enter teh goals by them"))
    t.append((name,goal))
print(t)
print("The players in the ascending order of goals")
sort_a=tuple(sorted(t,key=lambda x:x[1]))
print(sort_a)
print("The players in the descending order is")
sort_d=tuple(sorted(t,key=lambda x:x[1],reverse=True))
print(sort_d)
print("The top scorers")
toppers=tuple(list(sort_d)[:3])
print(toppers)
print("The alphabetical order:")
sort_al=tuple(sorted(t,key=lambda x:x[0]))
print(sort_al)

