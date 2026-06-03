# Question: Write a Python program for List Medium problem 8.

n = int(input())
arr = list(map(int,input().split()))
for i in arr:
    x = arr.count(i)
    if (x>1):
        arr.remove(i)
arr.sort(reverse = True)
print(arr[1])
