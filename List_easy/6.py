# Question: Write a Python program for List easy problem 6.

n = int(input())
arr = list(map(int,input().split()))
s = int(input())
if s in arr:
    print("FOUND")
else:
    print("NOT FOUND")
