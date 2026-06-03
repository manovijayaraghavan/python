# Question: Write a Python program for List easy problem 3.

n = int(input())
arr = list(map(int,input().split()))
h = 0
for i in arr:
    if (i>h):
        h=i
print(h)
arr.sort()
print(arr[len(arr)-1])
