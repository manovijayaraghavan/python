# Question: Write a Python program for List Medium problem 1.

n = int(input())
a = []
arr = list(map(int,input().split()))
for j in arr:
    if (a==[] or a[-1]!=j):
        a.append(j)
print(*a)
