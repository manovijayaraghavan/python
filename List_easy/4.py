# Question: Write a Python program for List easy problem 4.

n = int(input())
arr = list(map(int,input().split()))
a = 0
for i in arr:
    if (i%2==0):
        a+=1
print(a)
