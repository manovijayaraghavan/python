# Question: Write a Python program for List easy problem 7.

n = int(input())
arr = list(map(int,input().split()))
u = []
for i in arr:
    if i not in u:
        u.append(i)
u.sort()
print(u[len(u)-2])
