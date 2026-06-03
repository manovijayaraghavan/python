# Question 19: Find Duplicate Elements Once
n=int(input())
a=list(map(int,input().split()))
s=set(); d=[]
for i in a:
    if i in s and i not in d:d.append(i)
    s.add(i)
print(*d if d else [-1])