# Question: Write a Python program for List easy problem 1.

arr = list(map(int,input().split()))
s = int(input())
for i in range(len(arr)-1,-1,-1):
    if (arr[i] == s):
        print(i)
        break
