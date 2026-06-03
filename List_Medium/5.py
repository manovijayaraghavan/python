# Question: Write a Python program for List Medium problem 5.

n = int(input())
arr = list(map(int,input().split()))
a = []
for i in range(n):
    a_is = True
    for j in range(i+1,n):
        if (arr[j]>arr[i]):
            a_is  = False
            break
    if (a_is == True):
        a.append(arr[i])
print(*a)
