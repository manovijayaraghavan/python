# Question: Write a Python program for List Medium problem 9.

n = int(input())
arr = list(map(int,input().split()))
p = int(input())
b = []
a = []
e = []
for i in arr:
    if i<p:
        b.append(i)
    elif i>p:
        a.append(i)
    else:
        e.append(i)
print(*b+e+a)
