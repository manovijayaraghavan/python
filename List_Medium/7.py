# Question: Write a Python program for List Medium problem 7.

n = int(input())
arr = list(map(int,input().split()))
t = int(input())
count = 0
for i in range(n):
    for j in range(i+1,n):
        if (arr[i]+arr[j] == t):
            count += 1
print(count)
    
