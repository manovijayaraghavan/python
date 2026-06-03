# Question: Write a Python program for List Medium problem 2.

n = int(input())
arr = list(map(int,input().split()))
p = 0
for i in range(n):
    for j in range(i+1,n):
        if(arr[j]>arr[i]):
            a = arr[j]-arr[i]
            if p<a:
                p=a
print(p)


