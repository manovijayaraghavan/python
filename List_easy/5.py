# Question: Write a Python program for List easy problem 5.

n = int(input())
arr = list(map(int,input().split()))
a = (arr[::-1])
for i in a:
    print(i,end=" ")
